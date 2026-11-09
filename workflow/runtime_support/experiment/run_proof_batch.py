#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from runtime_support.experiment.run_utils import (  # noqa: E402
    atomic_write_json,
    merged_environment,
    split_self_assessment,
    update_run_record,
    validate_identifier,
)
from runtime_support.experiment.summary_builder import (  # noqa: E402
    build_all_paper_summaries,
)
from proof_experiment.llm_solver.run_llm_baseline import (  # noqa: E402
    DEFAULT_ENV_FILE,
    ProviderConfig,
    public_config,
)


DEFAULT_DATA_ROOT = WORKSPACE_ROOT / "data"
DEFAULT_RUNS_ROOT = WORKSPACE_ROOT / ".runtime/runs"
DEFAULT_API_PROFILE = WORKSPACE_ROOT.parent / ".venv/paperproof-config/model-suite/get-api"


@dataclass(frozen=True)
class ProofTask:
    paper_id: str
    theorem_id: str
    task_path: Path


@dataclass(frozen=True)
class StageLimits:
    solver: threading.Semaphore
    validity_reviewer: threading.Semaphore
    evaluator: threading.Semaphore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run theorem-level solver and evaluator jobs with global concurrency."
    )
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--paper-id", action="append", required=True)
    parser.add_argument("--data-root", type=Path, default=DEFAULT_DATA_ROOT)
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS_ROOT)
    parser.add_argument("--solver-env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--evaluator-api-profile", type=Path, default=DEFAULT_API_PROFILE)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--evaluator-model", default="gpt-6-astra")
    parser.add_argument(
        "--evaluator-reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="high",
    )
    parser.add_argument("--evaluator-timeout-seconds", type=int, default=1800)
    parser.add_argument("--max-workers", type=int, default=20)
    parser.add_argument("--max-solver-concurrency", type=int, default=10)
    parser.add_argument("--max-validity-concurrency", type=int, default=10)
    parser.add_argument("--max-evaluator-concurrency", type=int, default=10)
    parser.add_argument("--max-attempts", type=int, default=5)
    parser.add_argument("--retry-base-seconds", type=float, default=5.0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--extend",
        action="store_true",
        help=(
            "With --resume, allow new papers to be appended while requiring every "
            "existing paper and theorem selection to remain unchanged."
        ),
    )
    return parser.parse_args()


def discover_tasks(data_root: Path, paper_ids: list[str]) -> list[ProofTask]:
    tasks: list[ProofTask] = []
    seen_papers: set[str] = set()
    for raw_paper_id in paper_ids:
        paper_id = validate_identifier(raw_paper_id, "paper ID")
        if paper_id in seen_papers:
            raise ValueError(f"duplicate paper ID: {paper_id}")
        seen_papers.add(paper_id)
        paper_dir = data_root.resolve() / paper_id
        paths = sorted(
            paper_dir.glob(
                "selected_theorems/theorem_*/public_tasks/task_prove_theorem.md"
            )
        )
        if not paths:
            raise FileNotFoundError(f"paper has no proof tasks: {paper_dir}")
        for path in paths:
            tasks.append(
                ProofTask(
                    paper_id=paper_id,
                    theorem_id=path.parent.parent.name,
                    task_path=path.resolve(),
                )
            )
    return tasks


def recover_solver_outputs(answer: Path, evaluator_answer: Path) -> None:
    """Repair the only safe partial-write case before a retry."""
    if answer.is_file() and not evaluator_answer.exists():
        proof, _ = split_self_assessment(answer.read_text(encoding="utf-8"))
        evaluator_answer.write_text(proof, encoding="utf-8")
    elif evaluator_answer.exists() and not answer.is_file():
        raise RuntimeError(
            f"solver output is inconsistent: {evaluator_answer} exists without {answer}"
        )


def validate_resume_selection(
    existing_papers: dict[str, list[str]],
    requested_papers: dict[str, list[str]],
    *,
    extend: bool,
) -> None:
    if not extend:
        if existing_papers != requested_papers:
            raise ValueError("resume selection does not match the existing run")
        return

    missing = sorted(set(existing_papers) - set(requested_papers))
    if missing:
        raise ValueError(
            "extended selection omits existing papers: " + ", ".join(missing)
        )
    changed = sorted(
        paper_id
        for paper_id, theorem_ids in existing_papers.items()
        if theorem_ids != requested_papers.get(paper_id)
    )
    if changed:
        raise ValueError(
            "extended selection changes existing theorem lists: "
            + ", ".join(changed)
        )


def run_command(command: list[str]) -> None:
    process = subprocess.run(
        command,
        cwd=WORKSPACE_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if process.returncode != 0:
        raise RuntimeError(
            f"command failed ({process.returncode}): {' '.join(command)}\n"
            f"{process.stderr[-4000:]}"
        )


def run_one_task(
    task: ProofTask,
    args: argparse.Namespace,
    run_dir: Path,
    limits: StageLimits,
) -> dict[str, Any]:
    theorem_dir = run_dir / task.paper_id / task.theorem_id
    answer = theorem_dir / "answer.md"
    evaluator_answer = theorem_dir / "answer_for_evaluator.md"
    validity_report = theorem_dir / "validity_report.json"
    evaluation = theorem_dir / "evaluation.json"
    started = time.monotonic()
    last_error: Exception | None = None

    for attempt in range(1, args.max_attempts + 1):
        try:
            if evaluation.is_file():
                return {
                    "paper_id": task.paper_id,
                    "theorem_id": task.theorem_id,
                    "status": "already_completed",
                    "attempts": attempt - 1,
                    "wall_time_seconds": round(time.monotonic() - started, 3),
                }
            recover_solver_outputs(answer, evaluator_answer)
            if not (answer.is_file() and evaluator_answer.is_file()):
                with limits.solver:
                    run_command(
                        [
                            sys.executable,
                            str(
                                WORKSPACE_ROOT
                                / "proof_experiment/llm_solver/run_llm_baseline.py"
                            ),
                            "--task",
                            str(task.task_path),
                            "--run-id",
                            args.run_id,
                            "--runs-root",
                            str(args.runs_root.resolve()),
                            "--env-file",
                            str(args.solver_env_file.resolve()),
                        ]
                    )
            if not validity_report.is_file():
                with limits.validity_reviewer:
                    run_command(
                        [
                            sys.executable,
                            str(
                                WORKSPACE_ROOT
                                / "reviewer_and_evaluator/reviewer/run_reviewer.py"
                            ),
                            "--task",
                            str(task.task_path),
                            "--answer",
                            str(evaluator_answer),
                            "--run-id",
                            args.run_id,
                            "--runs-root",
                            str(args.runs_root.resolve()),
                            "--api-profile",
                            str(args.evaluator_api_profile.resolve()),
                            "--codex-bin",
                            args.codex_bin,
                            "--model",
                            args.evaluator_model,
                            "--reasoning-effort",
                            args.evaluator_reasoning_effort,
                            "--timeout-seconds",
                            str(args.evaluator_timeout_seconds),
                        ]
                    )
            with limits.evaluator:
                run_command(
                    [
                        sys.executable,
                        str(
                            WORKSPACE_ROOT
                            / "reviewer_and_evaluator/evaluator/run_evaluator.py"
                        ),
                        "--task",
                        str(task.task_path),
                        "--answer",
                        str(evaluator_answer),
                        "--validity-report",
                        str(validity_report),
                        "--run-id",
                        args.run_id,
                        "--runs-root",
                        str(args.runs_root.resolve()),
                        "--api-profile",
                        str(args.evaluator_api_profile.resolve()),
                        "--codex-bin",
                        args.codex_bin,
                        "--model",
                        args.evaluator_model,
                        "--reasoning-effort",
                        args.evaluator_reasoning_effort,
                        "--timeout-seconds",
                        str(args.evaluator_timeout_seconds),
                    ]
                )
            return {
                "paper_id": task.paper_id,
                "theorem_id": task.theorem_id,
                "status": "completed",
                "attempts": attempt,
                "wall_time_seconds": round(time.monotonic() - started, 3),
            }
        except Exception as error:
            last_error = error
            if attempt < args.max_attempts:
                time.sleep(
                    min(60.0, args.retry_base_seconds * (2 ** (attempt - 1)))
                )

    return {
        "paper_id": task.paper_id,
        "theorem_id": task.theorem_id,
        "status": "failed",
        "attempts": args.max_attempts,
        "wall_time_seconds": round(time.monotonic() - started, 3),
        "error": str(last_error),
    }


def main() -> int:
    args = parse_args()
    if args.extend and not args.resume:
        raise ValueError("--extend requires --resume")
    positive_values = {
        "max-workers": args.max_workers,
        "max-solver-concurrency": args.max_solver_concurrency,
        "max-validity-concurrency": args.max_validity_concurrency,
        "max-evaluator-concurrency": args.max_evaluator_concurrency,
        "max-attempts": args.max_attempts,
        "retry-base-seconds": args.retry_base_seconds,
    }
    if any(value <= 0 for value in positive_values.values()):
        raise ValueError(
            "all concurrency, retry-count, and retry-delay values must be positive"
        )
    args.run_id = validate_identifier(args.run_id, "run ID")
    tasks = discover_tasks(args.data_root, args.paper_id)
    run_dir = args.runs_root.resolve() / args.run_id
    if run_dir.exists() and not args.resume:
        raise FileExistsError(f"run already exists: {run_dir}")

    solver_config = ProviderConfig.from_environment(
        merged_environment(args.solver_env_file.resolve()),
        require_credentials=True,
    )
    if not run_dir.exists():
        run_command(
            [
                sys.executable,
                str(WORKSPACE_ROOT / "runtime_support/experiment/init_run.py"),
                "--run-id",
                args.run_id,
                "--runs-root",
                str(args.runs_root.resolve()),
            ]
        )
    record_path = run_dir / "run.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    papers: dict[str, dict[str, list[str]]] = {}
    for task in tasks:
        papers.setdefault(task.paper_id, {"theorem_ids": []})["theorem_ids"].append(
            task.theorem_id
        )
    if args.resume:
        existing_papers = {
            paper_id: sorted(value.get("theorem_ids", []))
            for paper_id, value in record.get("papers", {}).items()
            if isinstance(value, dict)
        }
        requested_papers = {
            paper_id: sorted(value["theorem_ids"])
            for paper_id, value in papers.items()
        }
        validate_resume_selection(
            existing_papers,
            requested_papers,
            extend=args.extend,
        )

    record.update(
        {
            "status": "running",
            "protocol": "closed_book_llm_then_two_stage_codex_evaluation",
            "dataset": {
                "root": str(args.data_root.resolve()),
                "split": "formal",
                "task_type": "task_prove_theorem",
                "selection": sorted(papers),
                "expected_task_count": len(tasks),
            },
            "papers": papers,
            "solver": {
                "kind": "llm_single_request",
                **public_config(solver_config),
                "system_prompt": "proof_experiment/llm_solver/prompts/proof_system_prompt.md",
                "answer_template": "proof_experiment/llm_solver/prompts/proof_answer_template.md",
                "tools_enabled": False,
                "retrieval_enabled": False,
                "requests_per_task": 1,
            },
            "evaluator": {
                "kind": "two_independent_codex_agents",
                "provider": args.evaluator_api_profile.name,
                "client": "codex_cli",
                "model": args.evaluator_model,
                "reasoning_effort": args.evaluator_reasoning_effort,
                "stages": [
                    {
                        "name": "validity_reviewer",
                        "prompt": (
                            "reviewer_and_evaluator/reviewer/system_prompt.md"
                        ),
                        "private_reference_access": False,
                        "assigns_score": False,
                    },
                    {
                        "name": "reference_scorer",
                        "prompt": (
                            "reviewer_and_evaluator/evaluator/system_prompt.md"
                        ),
                        "private_reference_access": True,
                        "assigns_score": True,
                    },
                ],
                "score_scale": "integer_0_to_10",
                "evaluators_per_answer": 2,
                "network_tools": "disabled",
            },
            "concurrency": {
                "unit": "theorem_job",
                "max_workers": args.max_workers,
                "max_solver_concurrency": args.max_solver_concurrency,
                "max_validity_concurrency": args.max_validity_concurrency,
                "max_evaluator_concurrency": args.max_evaluator_concurrency,
                "max_attempts": args.max_attempts,
                "retry_base_seconds": args.retry_base_seconds,
            },
        }
    )
    if args.resume:
        record["resume_count"] = int(record.get("resume_count", 0) or 0) + 1
        record["last_resumed_at"] = datetime.now(timezone.utc).isoformat()
        if args.extend:
            record["extension_count"] = int(record.get("extension_count", 0) or 0) + 1
    previous_wall_time = float(record.get("wall_time_seconds", 0) or 0)
    atomic_write_json(record_path, record)

    started = time.monotonic()
    outcomes: list[dict[str, Any]] = []
    limits = StageLimits(
        solver=threading.Semaphore(args.max_solver_concurrency),
        validity_reviewer=threading.Semaphore(args.max_validity_concurrency),
        evaluator=threading.Semaphore(args.max_evaluator_concurrency),
    )
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = {
            executor.submit(run_one_task, task, args, run_dir, limits): task
            for task in tasks
        }
        for future in as_completed(futures):
            outcome = future.result()
            outcomes.append(outcome)
            print(json.dumps(outcome, ensure_ascii=False), flush=True)

    summaries = build_all_paper_summaries(run_dir)
    failed = [item for item in outcomes if item["status"] == "failed"]
    completed_at = datetime.now(timezone.utc).isoformat()

    def finish(value: dict[str, Any]) -> None:
        value["status"] = "completed" if not failed else "completed_with_failures"
        value["completed_at"] = completed_at
        segment_wall_time = round(time.monotonic() - started, 3)
        value["wall_time_seconds"] = round(previous_wall_time + segment_wall_time, 3)
        value["last_segment_wall_time_seconds"] = segment_wall_time
        value["outcome_summary"] = {
            "expected_task_count": len(tasks),
            "completed_task_count": len(tasks) - len(failed),
            "failed_task_count": len(failed),
            "completed_paper_count": sum(
                summary["status"] == "completed" for summary in summaries.values()
            ),
            "failed_tasks": [
                f"{item['paper_id']}/{item['theorem_id']}" for item in failed
            ],
        }

    update_run_record(run_dir, finish)
    print(run_dir)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
