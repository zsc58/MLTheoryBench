#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from agent_call import AgentConfig
from bare_model import ProviderConfig, public_config
from calibrated_pipeline import MAX_CHECKER_FEEDBACK
from model_profiles import DEFAULT_PROFILES_DIR, load_suite, solver_profiles
from paired_pipeline import SolverSpec, load_json, run_paper, selected_inputs
from support import atomic_write_json, merged_environment, sha256_file


ROOT = Path(__file__).resolve().parents[1]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def solver_spec(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("solver must be LABEL=/path/to/config.env")
    label, path = value.split("=", 1)
    if not label or not label.replace("_", "").replace("-", "").isalnum():
        raise argparse.ArgumentTypeError("solver label must be alphanumeric")
    return label, Path(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a controlled paired comparison of two to eight bare solvers."
    )
    parser.add_argument("--selection", required=True, type=Path)
    parser.add_argument("--run-root", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--mode", choices=["formal", "test"], help="Default: test (two solvers).")
    parser.add_argument("--profiles-dir", type=Path, default=DEFAULT_PROFILES_DIR)
    parser.add_argument("--exclude-solver", action="append", default=[],
                        help="Exclude an explicit model label from this run only.")
    parser.add_argument("--calibrate-once", action="store_true",
                        help="Source audit, fresh task+GT checks with up to two feedbacks, then frozen scoring.")
    modes.add_argument(
        "--solver",
        action="append",
        type=solver_spec,
        help="Repeat as LABEL=/absolute/path/to/solver.env.",
    )
    parser.add_argument("--judge-api-profile", type=Path)
    parser.add_argument("--judge-model", default=load_suite()["agent"]["model"])
    parser.add_argument("--judge-reasoning-effort", default="high")
    parser.add_argument("--judge-timeout-seconds", type=int, default=3600)
    parser.add_argument("--audit-api-profile", type=Path)
    parser.add_argument("--audit-model", default=load_suite()["agent"]["model"])
    parser.add_argument("--audit-reasoning-effort", default="high")
    parser.add_argument("--audit-timeout-seconds", type=int, default=3600)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--paper-workers", type=int, default=1)
    parser.add_argument("--paper-id", action="append", default=[])
    parser.add_argument(
        "--solver-audit-only",
        action="store_true",
        help=(
            "Run bare solvers and conditional task audit/revision only; "
            "defer reviewer and evaluator calls."
        ),
    )
    parser.add_argument(
        "--pre-solver-audit",
        action="store_true",
        help=(
            "Run one comprehensive source-aware artifact audit before the first "
            "solver round. This does not consume downstream feedback quota."
        ),
    )
    args = parser.parse_args()
    if args.solver is None:
        args.mode = args.mode or "test"
        args.solver = solver_profiles(args.mode, args.profiles_dir)
    else:
        args.mode = "custom"
    missing = set(args.exclude_solver) - {label for label, _ in args.solver}
    if missing:
        parser.error("excluded solver labels are not active: " + ", ".join(sorted(missing)))
    args.solver = [(label, path) for label, path in args.solver if label not in args.exclude_solver]
    if args.calibrate_once and (args.solver_audit_only or args.pre_solver_audit):
        parser.error("calibrate-once includes its own audit and requires formal scoring")
    args.judge_api_profile = args.judge_api_profile or args.profiles_dir / "get-api"
    return args


def aggregate_usage(results: list[dict[str, Any]]) -> dict[str, Any]:
    totals: dict[str, dict[str, int]] = {}
    for result in results:
        for stage, usage in result.get("usage", {}).items():
            bucket = totals.setdefault(stage, {})
            for key, value in usage.items():
                bucket[key] = bucket.get(key, 0) + int(value or 0)
    return totals


def aggregate_solver_usage(results: list[dict[str, Any]]) -> dict[str, Any]:
    totals: dict[str, dict[str, int]] = {}
    for result in results:
        for label, usage in result.get("solver_usage_by_model", {}).items():
            bucket = totals.setdefault(label, {})
            for key, value in usage.items():
                bucket[key] = bucket.get(key, 0) + int(value or 0)
    return totals


def recover_recorded_usage(paper_output: Path) -> dict[str, Any]:
    """Keep returned usage when a later transport or contract check fails."""
    from usage_accounting import aggregate_agent_records

    stages: dict[str, dict[str, int]] = {}
    models: dict[str, dict[str, int]] = {}
    def add(bucket: dict[str, int], usage: dict[str, int] | None) -> None:
        for key, value in (usage or {}).items():
            bucket[key] = bucket.get(key, 0) + int(value or 0)
    for path in paper_output.rglob("call_usage.json"):
        record = load_json(path)
        add(stages.setdefault("solver", {}), record.get("usage"))
        parts = path.relative_to(paper_output).parts
        if "models" in parts:
            label = parts[parts.index("models") + 1]
            add(models.setdefault(label, {}), record.get("usage"))
    agent_records = []
    for path in paper_output.rglob("call_audit.json"):
        record = load_json(path)
        agent_records.append((str(path), record.get("stage", "task_audit"), record))
    for stage in ("reviewer", "evaluator"):
        for path in paper_output.rglob(f"paired_{stage}_audit.json"):
            for index, attempt in enumerate(load_json(path).get("attempts", [])):
                agent_records.append((f"{path}:{index}", stage, attempt))
    agent_stages, issues = aggregate_agent_records(agent_records)
    for stage, usage in agent_stages.items():
        add(stages.setdefault(stage, {}), usage)
    return {"usage": stages, "solver_usage_by_model": models,
            "usage_accounting_issues": issues,
            "usage_coverage": "returned_records_only_failed_requests_may_be_unreported"}


def build_summary(run_root: Path, results: list[dict[str, Any]]) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    stop_reasons: dict[str, int] = {}
    calibration_quality_counts: dict[str, int] = {}
    score_values: dict[str, list[int]] = {}
    for result in results:
        status = result["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
        quality = result.get("calibration_quality")
        if quality is not None:
            quality_status = quality["status"]
            calibration_quality_counts[quality_status] = calibration_quality_counts.get(quality_status, 0) + 1
        if result.get("stop_reason"):
            reason = result["stop_reason"]
            stop_reasons[reason] = stop_reasons.get(reason, 0) + 1
        for label, score in result.get("scores", {}).items():
            score_values.setdefault(label, []).append(int(score))
    score_summary = {
        label: {
            "count": len(values),
            "mean": round(sum(values) / len(values), 4) if values else None,
            "distribution": {
                str(score): values.count(score) for score in range(11)
            },
        }
        for label, values in score_values.items()
    }
    summary = {
        "paper_count": len(results),
        "status_counts": status_counts,
        "stop_reasons": stop_reasons,
        "calibration_quality_counts": calibration_quality_counts,
        "scores": score_summary,
        "usage": aggregate_usage(results),
        "solver_usage_by_model": aggregate_solver_usage(results),
    }
    atomic_write_json(run_root / "summary.json", summary)
    return summary


def main() -> int:
    args = parse_args()
    if not 2 <= len(args.solver) <= 8:
        raise ValueError("paired comparison requires two to eight solver models")
    labels = [label for label, _ in args.solver]
    if len(labels) != len(set(labels)):
        raise ValueError("solver labels must be unique")
    if args.paper_workers < 1:
        raise ValueError("paper-workers must be positive")
    selection, papers = selected_inputs(args.selection, args.paper_id)
    source_root = Path(selection["source_run_root"]).resolve()
    specs = [
        SolverSpec(
            label=label,
            config=ProviderConfig.from_environment(
                merged_environment(env_path.resolve()),
                require_credentials=True,
                base_dir=env_path.resolve().parent,
            ),
        )
        for label, env_path in args.solver
    ]
    judge_agent = AgentConfig(
        api_profile=args.judge_api_profile.resolve(),
        codex_bin=args.codex_bin,
        model=args.judge_model,
        reasoning_effort=args.judge_reasoning_effort,
        timeout_seconds=args.judge_timeout_seconds,
    )
    audit_agent = AgentConfig(
        api_profile=(args.audit_api_profile or args.judge_api_profile).resolve(),
        codex_bin=args.codex_bin,
        model=args.audit_model,
        reasoning_effort=args.audit_reasoning_effort,
        timeout_seconds=args.audit_timeout_seconds,
    )
    run_root = args.run_root.resolve()
    if (
        run_root == source_root
        or run_root in source_root.parents
        or source_root in run_root.parents
    ):
        raise ValueError(
            "run-root must be disjoint from the frozen source run; comparison "
            "outputs may not be written into or above the formal dataset"
        )
    if run_root.exists():
        raise FileExistsError(run_root)
    run_root.mkdir(parents=True)
    shutil.copy2(args.selection.resolve(), run_root / "selection.json")
    prompt_prefix = "frozen_" if args.calibrate_once else ""
    run_record = {
        "schema_version": "1.0",
        "run_id": args.run_id,
        "model_mode": args.mode,
        "protocol": "bounded_calibration_then_frozen_scoring" if args.calibrate_once else (
            "paired_bare_solvers_conditional_audit_only"
            if args.solver_audit_only
            else "paired_bare_solvers_shared_reviewer_evaluator_conditional_audit"
        ),
        "status": "running",
        "created_at": utc_now(),
        "selection_sha256": sha256_file(args.selection.resolve()),
        "paper_count": len(papers),
        "paper_ids": [paper.paper_id for paper in papers],
        "solvers": {
            spec.label: {
                **public_config(spec.config),
                "system_prompt_sha256": sha256_file(
                    ROOT / f"prompts/{prompt_prefix}solver_system_prompt.md"
                ),
                "answer_template_sha256": sha256_file(
                    ROOT / f"prompts/{prompt_prefix}solver_answer_template.md"
                ),
            }
            for spec in specs
        },
        "judge": {
            "model": judge_agent.model,
            "reasoning_effort": judge_agent.reasoning_effort,
            "reviewer_prompt_sha256": sha256_file(
                ROOT / "prompts/reviewer_system_prompt.md"
            ),
            "reviewer_schema_sha256": sha256_file(
                ROOT / "schemas/reviewer.schema.json"
            ),
            "evaluator_prompt_sha256": sha256_file(
                ROOT / "prompts/evaluator_system_prompt.md"
            ),
            "evaluator_schema_sha256": sha256_file(
                ROOT / "schemas/evaluator.schema.json"
            ),
        },
        "audit": {
            "model": audit_agent.model,
            "reasoning_effort": audit_agent.reasoning_effort,
            "conditional": not args.calibrate_once,
            "max_solver_reviewer_feedback": 0 if args.calibrate_once else 2,
            "max_checker_feedback": MAX_CHECKER_FEEDBACK if args.calibrate_once else 0,
            "fresh_checker_after_feedback": args.calibrate_once,
            "prompt_sha256": sha256_file(ROOT / "prompts/task_audit.md"),
            "checker_prompt_sha256": sha256_file(ROOT / "prompts/task_checker.md") if args.calibrate_once else None,
        },
        "paper_workers": args.paper_workers,
        "solver_audit_only": args.solver_audit_only,
        "pre_solver_audit": args.pre_solver_audit,
        "calibrate_once": args.calibrate_once,
        "excluded_solvers": args.exclude_solver,
    }
    atomic_write_json(run_root / "run.json", run_record)
    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=args.paper_workers
    ) as executor:
        if args.calibrate_once:
            from calibrated_pipeline import run_calibrated_paper
            run_function = run_calibrated_paper
            extra_args = ()
        else:
            run_function = run_paper
            extra_args = (args.solver_audit_only, args.pre_solver_audit)
        futures = {
            executor.submit(
                run_function,
                paper,
                args.run_id,
                run_root / "papers" / paper.paper_id,
                specs,
                judge_agent,
                audit_agent,
                *extra_args,
            ): paper.paper_id
            for paper in papers
        }
        for future in concurrent.futures.as_completed(futures):
            paper_id = futures[future]
            try:
                result = future.result()
            except Exception as error:
                paper_output = run_root / "papers" / paper_id
                result = {
                    "paper_id": paper_id,
                    "status": "failed",
                    "error": str(error),
                    **recover_recorded_usage(paper_output),
                }
                paper_output.mkdir(parents=True, exist_ok=True)
                atomic_write_json(paper_output / "result.json", result)
            results.append(result)
            print(
                json.dumps(
                    {**result, "progress": f"{len(results)}/{len(papers)}"},
                    ensure_ascii=False,
                ),
                flush=True,
            )
    summary = build_summary(run_root, results)
    run_record = load_json(run_root / "run.json")
    run_record["status"] = (
        "completed" if not summary["status_counts"].get("failed") else "completed_with_failures"
    )
    run_record["completed_at"] = utc_now()
    run_record["summary"] = summary
    atomic_write_json(run_root / "run.json", run_record)
    print(run_root / "summary.json")
    return 0 if run_record["status"] == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
