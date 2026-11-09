#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import json
import shutil
import time
from pathlib import Path
from typing import Any

from agent_call import AgentConfig
from bare_model import ProviderConfig, public_config
from calibrated_pipeline import artifact_hashes
from model_profiles import DEFAULT_PROFILES_DIR, load_suite
from paired_pipeline import (
    PROMPTS, SCHEMAS, ArtifactBundle, SolverSpec, _add_usage, load_json,
    run_paired_evaluator, run_paired_reviewer, run_solver,
)
from run_comparison import build_summary, recover_recorded_usage, utc_now
from support import atomic_write_json, merged_environment, sha256_file


ARTIFACT_NAMES = {
    "task.md", "proof_ground_truth.md", "rubric.md", "provenance.json",
    "thread_b_view.json",
}
REQUIRED_ARTIFACTS = ARTIFACT_NAMES - {"thread_b_view.json"}
TERMINAL_UPSTREAM_STATUSES = {
    "completed", "completed_with_failures", "failed", "stopped", "cancelled",
}


def completed_papers(upstream: Path) -> list[str]:
    run = load_json(upstream / "run.json")
    ready = []
    for paper_id in run["paper_ids"]:
        if Path(paper_id).name != paper_id or not paper_id.startswith("paper_"):
            raise ValueError("invalid upstream paper ID")
        path = upstream / "papers" / paper_id / "result.json"
        if path.is_file() and load_json(path).get("status") == "completed":
            ready.append(paper_id)
    return ready


def prompt_fingerprints() -> dict[str, str]:
    names = (
        "frozen_solver_system_prompt.md", "frozen_solver_answer_template.md",
        "reviewer_system_prompt.md", "evaluator_system_prompt.md",
        "paired_reviewer_protocol.md", "paired_evaluator_protocol.md",
    )
    return {name: sha256_file(PROMPTS / name) for name in names} | {
        name: sha256_file(SCHEMAS / name)
        for name in ("reviewer.schema.json", "evaluator.schema.json",
                     "paired_reviewer.schema.json", "paired_evaluator.schema.json")
    }


def validate_upstream_protocol(run: dict[str, Any]) -> None:
    if run.get("protocol") != "bounded_calibration_then_frozen_scoring":
        raise ValueError("upstream must contain calibrated, frozen scoring tasks")
    fingerprints = prompt_fingerprints()
    for config in run["solvers"].values():
        for field, name in (("system_prompt_sha256", "frozen_solver_system_prompt.md"),
                            ("answer_template_sha256", "frozen_solver_answer_template.md")):
            if config[field] != fingerprints[name]:
                raise ValueError(f"solver prompt differs from upstream: {name}")
    for field, name in (("reviewer_prompt_sha256", "reviewer_system_prompt.md"),
                        ("evaluator_prompt_sha256", "evaluator_system_prompt.md"),
                        ("reviewer_schema_sha256", "reviewer.schema.json"),
                        ("evaluator_schema_sha256", "evaluator.schema.json")):
        if run["judge"][field] != fingerprints[name]:
            raise ValueError(f"judge contract differs from upstream: {name}")


def copy_frozen_bundle(source: Path, output: Path) -> tuple[ArtifactBundle, dict[str, Any]]:
    result = load_json(source / "result.json")
    frozen = load_json(source / "frozen_artifacts.json")
    revision = frozen["task_revision"]
    if (result["status"] != "completed" or not isinstance(revision, int)
            or isinstance(revision, bool) or revision < 0
            or result["task_revision"] != revision
            or frozen["checker_status"] != "no_issue_found"
            or frozen["checker_revision"] != revision):
        raise ValueError("only completed, checker-approved frozen versions are eligible")
    hashes = frozen["sha256"]
    if not REQUIRED_ARTIFACTS <= hashes.keys() <= ARTIFACT_NAMES:
        raise ValueError("incomplete or unexpected frozen artifact manifest")
    original = ArtifactBundle(revision, source / f"task_versions/revision_{revision}")
    for name, digest in hashes.items():
        path = original.root / name
        if (path.is_symlink() or not path.is_file()
                or not path.resolve().is_relative_to(source.resolve())
                or sha256_file(path) != digest):
            raise ValueError(f"frozen source changed or escaped its paper: {name}")
    bundle = ArtifactBundle(revision, output / f"task_versions/revision_{revision}")
    bundle.root.mkdir(parents=True, exist_ok=False)
    for name in hashes:
        shutil.copy2(original.root / name, bundle.root / name)
    if artifact_hashes(bundle) != hashes:
        raise ValueError("frozen artifact copy hash mismatch")
    shutil.copy2(source / "frozen_artifacts.json", output / "frozen_artifacts.json")
    reference = {
        "source_paper": str(source.resolve()), "task_revision": revision,
        "source_result_sha256": sha256_file(source / "result.json"),
        "source_frozen_manifest_sha256": sha256_file(source / "frozen_artifacts.json"),
        "sha256": hashes, "cohort": result.get("cohort"),
        "calibration_quality": frozen.get("calibration_quality"),
        "source_answers_or_scores_exposed_to_judges": False,
    }
    atomic_write_json(output / "source_reference.json", reference)
    return bundle, reference


def run_supplement(
    source: Path, output: Path, spec: SolverSpec, judge: AgentConfig,
) -> dict[str, Any]:
    started = time.monotonic()
    output.mkdir(parents=True, exist_ok=False)
    state: dict[str, Any] = {
        "paper_id": source.name, "status": "running", "stop_reason": None,
        "scores": {}, "formal_feedback_enabled": False,
        "validation_feedback_count": 0, "judging_scope": "single_answer_supplement",
    }
    usage: dict[str, dict[str, int]] = {stage: {} for stage in ("solver", "reviewer", "evaluator")}
    try:
        bundle, reference = copy_frozen_bundle(source, output)
        state.update(task_revision=bundle.revision, cohort=reference["cohort"],
                     calibration_quality=reference["calibration_quality"])
        round_dir = output / "rounds/round_0"
        answer = run_solver(spec, bundle, round_dir / "models" / spec.label, frozen_task=True)
        _add_usage(usage["solver"], answer.get("usage"))
        state["solver_outcome"] = answer["solver_outcome"]
        state["status"] = "completed"
        if answer["solver_outcome"] == "no_final_answer":
            state.update(scores={spec.label: 0}, scoring_method="automatic_zero_no_final_answer")
        else:
            assignment = {"answer_a": spec.label}
            answers = {spec.label: answer}
            atomic_write_json(round_dir / "anonymous_assignment.json", assignment)
            reviews, returned = run_paired_reviewer(bundle, assignment, answers, round_dir, judge)
            _add_usage(usage["reviewer"], returned)
            evaluations, returned = run_paired_evaluator(
                bundle, assignment, answers, reviews, round_dir, judge,
            )
            _add_usage(usage["evaluator"], returned)
            evaluation = evaluations["answer_a"]
            if evaluation["evaluation_status"] == "unscorable":
                state.update(status="stopped", stop_reason="evaluator_unscorable",
                             unscorable_models=[spec.label])
            else:
                state["scores"] = {spec.label: evaluation["score"]}
            state["scoring_method"] = "reviewer_then_evaluator"
        if artifact_hashes(bundle) != reference["sha256"]:
            raise ValueError("frozen supplement artifacts changed during evaluation")
        state.update(usage=usage, solver_usage_by_model={spec.label: usage["solver"]})
    except Exception as error:
        # Transport/schema failures remain failures, never empty-answer zero scores.
        state.update(status="failed", stop_reason=None, scores={},
                     error=str(error), **recover_recorded_usage(output))
    state["wall_time_seconds"] = round(time.monotonic() - started, 3)
    atomic_write_json(output / "result.json", state)
    return state


def follow_completed(
    upstream: Path, output: Path, spec: SolverSpec, judge: AgentConfig,
    *, workers: int, follow: bool, poll_seconds: float,
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    handled: set[str] = set()
    active: dict[concurrent.futures.Future, str] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        while True:
            ready = completed_papers(upstream)
            pending = [paper_id for paper_id in ready if paper_id not in handled]
            for paper_id in pending[:max(0, workers - len(active))]:
                active[pool.submit(
                    run_supplement, upstream / "papers" / paper_id,
                    output / "papers" / paper_id, spec, judge,
                )] = paper_id
                handled.add(paper_id)
            source_status = load_json(upstream / "run.json")["status"]
            progress = {
                "updated_at": utc_now(), "upstream_status": source_status,
                "eligible_completed": len(ready), "submitted": len(handled),
                "finished": len(results), "active_papers": sorted(active.values()),
                "waiting_for_upstream": follow and not active and source_status not in TERMINAL_UPSTREAM_STATUSES,
            }
            atomic_write_json(output / "progress.json", progress)
            if not active:
                if not follow or source_status in TERMINAL_UPSTREAM_STATUSES:
                    break
                time.sleep(poll_seconds)
                continue
            done, _ = concurrent.futures.wait(
                active, timeout=poll_seconds, return_when=concurrent.futures.FIRST_COMPLETED,
            )
            for future in done:
                paper_id = active.pop(future)
                result = future.result()
                results.append(result)
                print(json.dumps({"paper_id": paper_id, "status": result["status"],
                                  "scores": result["scores"], "finished": len(results)},
                                 ensure_ascii=False), flush=True)
            if done:
                build_summary(output, results)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one solver on completed frozen tasks; optionally follow new completions.")
    parser.add_argument("--upstream-run", type=Path, required=True)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--solver-label", default="glm53")
    parser.add_argument("--profiles-dir", type=Path, default=DEFAULT_PROFILES_DIR)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--paper-workers", type=int, default=5)
    parser.add_argument("--follow", action="store_true")
    parser.add_argument("--poll-seconds", type=float, default=30)
    args = parser.parse_args()
    if args.paper_workers < 1 or args.poll_seconds <= 0:
        parser.error("workers and poll interval must be positive")
    upstream, output = args.upstream_run.resolve(), args.run_root.resolve()
    if output == upstream or output in upstream.parents or upstream in output.parents:
        raise ValueError("supplement and upstream run directories must be disjoint")
    source_run = load_json(upstream / "run.json")
    validate_upstream_protocol(source_run)
    if args.solver_label not in load_suite()["solvers"]:
        parser.error("unknown solver label")
    profile = args.profiles_dir.resolve() / f"{args.solver_label}.env"
    config = ProviderConfig.from_environment(merged_environment(profile), base_dir=profile.parent)
    spec = SolverSpec(args.solver_label, config)
    judge = AgentConfig(args.profiles_dir.resolve() / "get-api", args.codex_bin,
                        source_run["judge"]["model"], source_run["judge"]["reasoning_effort"], 3600)
    output.mkdir(parents=True, exist_ok=False)
    record = {
        "schema_version": "1.0", "run_id": args.run_id, "status": "running",
        "created_at": utc_now(), "protocol": "single_solver_frozen_supplement",
        "upstream_run": str(upstream), "upstream_run_id": source_run["run_id"],
        "eligible_policy": "completed_only_latest_checker_approved_frozen_revision",
        "follow_upstream": args.follow, "paper_workers": args.paper_workers,
        "solvers": {spec.label: public_config(config)},
        "judge": {"model": judge.model, "reasoning_effort": judge.reasoning_effort},
        "prompt_and_schema_sha256": prompt_fingerprints(),
        "audit_enabled": False, "formal_feedback_enabled": False,
        "empty_answer_policy": "zero_without_reviewer_or_evaluator",
    }
    atomic_write_json(output / "run.json", record)
    results = follow_completed(upstream, output, spec, judge, workers=args.paper_workers,
                               follow=args.follow, poll_seconds=args.poll_seconds)
    record.update(status="completed_with_failures" if any(r["status"] == "failed" for r in results) else "completed",
                  completed_at=utc_now(), summary=build_summary(output, results))
    atomic_write_json(output / "run.json", record)
    return 1 if record["status"] == "completed_with_failures" else 0


if __name__ == "__main__":
    raise SystemExit(main())
