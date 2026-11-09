from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from agent_call import AgentConfig, create_agent_thread, run_json_agent
from contracts import validate_schema
from paired_pipeline import (
    PROMPTS, SCHEMAS, ArtifactBundle, PaperInput, SolverBatchError, SolverSpec,
    _add_usage, anonymous_assignment, apply_audit_replacements, audit_quality_summary,
    initialize_artifacts, load_json, run_all_solvers, run_paired_evaluator,
    run_paired_reviewer, run_task_audit,
)
from support import atomic_write_json, sha256_file


REPAIR_STATUSES = {
    "formalization_error_fixed", "scoring_error_fixed", "source_minor_issue_fixed",
}
MAX_CHECKER_FEEDBACK = 2


def artifact_hashes(bundle: ArtifactBundle) -> dict[str, str]:
    return {
        path.name: sha256_file(path)
        for path in (bundle.task, bundle.proof_ground_truth, bundle.rubric,
                     bundle.provenance, bundle.thread_b_view)
        if path.is_file()
    }


def checker_input(bundle: ArtifactBundle) -> str:
    return "\n\n".join([
        "# Public Task", bundle.task.read_text(encoding="utf-8").rstrip(),
        "# Private Reference Proof",
        bundle.proof_ground_truth.read_text(encoding="utf-8").rstrip(),
    ]) + "\n"


def validate_checker(result: dict[str, Any]) -> None:
    validate_schema(result, load_json(SCHEMAS / "task_checker.schema.json"))
    findings = result["findings"]
    if bool(findings) != (result["status"] == "issues_found"):
        raise ValueError("checker issues_found must have findings; other statuses must not")
    ids = [item["finding_id"] for item in findings]
    if len(ids) != len(set(ids)) or any(not item.strip() for item in ids):
        raise ValueError("checker finding IDs must be nonempty and unique")
    for finding in findings:
        for field in ("location", "reason", "counterexample_or_evidence"):
            if not finding[field].strip():
                raise ValueError(f"checker finding requires {field}")


def run_checker(
    bundle: ArtifactBundle, output: Path, agent: AgentConfig,
) -> tuple[dict[str, Any], dict[str, int] | None]:
    output.mkdir(parents=True, exist_ok=False)
    inputs = checker_input(bundle)
    (output / "checker_input.md").write_text(inputs, encoding="utf-8")
    atomic_write_json(output / "exposure.json", {
        "stage": "task_checker_not_solver", "task_revision": bundle.revision,
        "exposed_files": [
            {"path": str(path), "sha256": sha256_file(path)}
            for path in (bundle.task, bundle.proof_ground_truth,
                         PROMPTS / "task_checker.md", SCHEMAS / "task_checker.schema.json")
        ],
        "original_source_visible": False, "rubric_visible": False,
        "previous_audit_visible": False, "previous_checker_visible": False,
        "fresh_thread": True, "tools": [],
    })
    result, usage, call = run_json_agent(
        instructions=(PROMPTS / "task_checker.md").read_text(encoding="utf-8"),
        inputs=inputs, schema_path=SCHEMAS / "task_checker.schema.json",
        config=agent, output_label="isolated_task_checker",
    )
    atomic_write_json(output / "call_audit.json", {**call, "stage": "task_checker"})
    atomic_write_json(output / "checker.json", result)
    validate_checker(result)
    return result, usage


def run_calibrated_paper(
    paper: PaperInput, run_id: str, output_dir: Path, specs: list[SolverSpec],
    judge_agent: AgentConfig, audit_agent: AgentConfig,
) -> dict[str, Any]:
    """Check every repair in isolation; freeze only after the latest check passes."""
    started = time.monotonic()
    output_dir.mkdir(parents=True, exist_ok=False)
    bundle = initialize_artifacts(paper, output_dir)
    original_hashes = artifact_hashes(bundle)
    usage: dict[str, dict[str, int]] = {
        stage: {} for stage in ("task_audit", "task_checker", "solver", "reviewer", "evaluator")
    }
    model_usage: dict[str, dict[str, int]] = {spec.label: {} for spec in specs}
    state: dict[str, Any] = {
        "paper_id": paper.paper_id, "cohort": paper.cohort,
        "status": "running", "stop_reason": None, "scores": {},
        "calibration_feedback_count": 0, "validation_feedback_count": 0,
        "checker_count": 0, "checker_history": [],
        "max_checker_feedback": MAX_CHECKER_FEEDBACK,
        "formal_feedback_enabled": False, "round_count": 0,
        "calibration_quality": None,
    }

    def finish(status: str, reason: str | None = None) -> dict[str, Any]:
        state.update(
            status=status, stop_reason=reason, task_revision=bundle.revision,
            usage=usage, solver_usage_by_model=model_usage,
            wall_time_seconds=round(time.monotonic() - started, 3),
        )
        atomic_write_json(output_dir / "result.json", state)
        return state

    audit_thread = create_agent_thread(audit_agent, f"calibration-{paper.paper_id}")
    try:
        audit, returned = run_task_audit(
            paper, bundle, [], output_dir / "calibration/source_audit",
            audit_agent, audit_thread, include_full_source=True, audit_mode="pre_solver",
        )
        _add_usage(usage["task_audit"], returned)
        state["pre_solver_audit_status"] = audit["status"]
        state["calibration_quality"] = audit_quality_summary(audit)
        if audit["status"] == "paper_issue_confirmed":
            return finish("stopped", "paper_issue")
        if audit["status"] in REPAIR_STATUSES:
            bundle = apply_audit_replacements(bundle, audit, output_dir, paper)
        elif audit["status"] != "artifacts_verified":
            raise ValueError("unexpected proactive audit status")

        for check_index in range(1, MAX_CHECKER_FEEDBACK + 2):
            checked_revision = bundle.revision
            checked_hashes = artifact_hashes(bundle)
            checker_name = "checker" if check_index == 1 else f"checker_{check_index}"
            checker_dir = output_dir / "calibration" / checker_name
            report, returned = run_checker(bundle, checker_dir, audit_agent)
            _add_usage(usage["task_checker"], returned)
            state.update(checker_status=report["status"], checker_count=check_index)
            state["checker_history"].append({
                "check_index": check_index, "task_revision": checked_revision,
                "status": report["status"], "sha256": checked_hashes,
                "report_path": str((checker_dir / "checker.json").relative_to(output_dir)),
            })
            if report["status"] == "no_issue_found":
                break
            if state["calibration_feedback_count"] == MAX_CHECKER_FEEDBACK:
                state["calibration_quality"]["status"] = "not_passed"
                return finish("stopped", "max_checker_feedback")

            # Send the entire report, not just an extracted first objection.
            objections = [{
                "stage": "task_checker", "report": report,
                "reason": "Adjudicate every finding together; some concerns may overlap.",
            }]
            feedback_index = state["calibration_feedback_count"] + 1
            feedback_name = "checker_feedback" if feedback_index == 1 else f"checker_feedback_{feedback_index}"
            audit, returned = run_task_audit(
                paper, bundle, objections, output_dir / "calibration" / feedback_name,
                audit_agent, audit_thread, include_full_source=False, audit_mode="conditional",
            )
            _add_usage(usage["task_audit"], returned)
            state["calibration_feedback_count"] = feedback_index
            state["calibration_resolution"] = audit["status"]
            state["calibration_quality"] = audit_quality_summary(audit)
            if audit["status"] == "paper_issue_confirmed":
                return finish("stopped", "paper_issue")
            if audit["status"] in REPAIR_STATUSES:
                bundle = apply_audit_replacements(bundle, audit, output_dir, paper)
            elif audit["status"] != "invalid_objection":
                raise ValueError("unexpected checker-feedback audit status")
    finally:
        audit_thread.close()

    frozen = artifact_hashes(bundle)
    if state["checker_status"] != "no_issue_found" or frozen != checked_hashes:
        raise ValueError("only the unchanged, checker-approved artifacts may be frozen")
    atomic_write_json(output_dir / "frozen_artifacts.json", {
        "original_revision": 0, "original_sha256": original_hashes,
        "task_revision": bundle.revision, "sha256": frozen,
        "checker_revision": checked_revision,
        "checker_status": state["checker_status"],
        "checker_count": state["checker_count"],
        "checker_report_path": state["checker_history"][-1]["report_path"],
        "post_feedback_checker_rerun": state["calibration_feedback_count"] > 0,
        "formal_feedback_enabled": False,
        "calibration_quality": state["calibration_quality"],
        "exposure_policy": {
            "solver": ["task.md", "frozen_solver_system_prompt.md", "frozen_solver_answer_template.md"],
            "reviewer": ["task.md", "anonymized_proofs_without_self_assessment"],
            "evaluator": ["task.md", "anonymized_proofs_without_self_assessment",
                          "validity_reports", "proof_ground_truth.md", "rubric.md", "provenance.json"],
        },
    })
    round_dir = output_dir / "rounds/round_0"
    round_dir.mkdir(parents=True, exist_ok=False)
    state["round_count"] = 1
    try:
        results = run_all_solvers(specs, bundle, round_dir, frozen_task=True)
    except SolverBatchError as error:
        for label, result in error.results.items():
            _add_usage(usage["solver"], result.get("usage"))
            _add_usage(model_usage[label], result.get("usage"))
        state.update(error=str(error), failed_models=error.errors,
                     completed_solver_models=sorted(error.results),
                     unreported_failed_request_usage=True)
        return finish("failed")
    for label, result in results.items():
        _add_usage(usage["solver"], result.get("usage"))
        _add_usage(model_usage[label], result.get("usage"))
    active = [spec.label for spec in specs if results[spec.label]["solver_outcome"] != "no_final_answer"]
    assignment = anonymous_assignment(paper.paper_id, run_id, 0, active)
    atomic_write_json(round_dir / "anonymous_assignment.json", assignment)
    terminal_scores = {label: 0 for label in results if label not in active}
    state["scores"] = terminal_scores
    if assignment:
        reviews, returned = run_paired_reviewer(bundle, assignment, results, round_dir, judge_agent)
        _add_usage(usage["reviewer"], returned)
        # Even a target finding goes to final evaluation, never to task repair.
        evaluations, returned = run_paired_evaluator(
            bundle, assignment, results, reviews, round_dir, judge_agent,
        )
        _add_usage(usage["evaluator"], returned)
        unscorable = [assignment[key] for key, value in evaluations.items()
                      if value["evaluation_status"] == "unscorable"]
        per_model_scores = {
            **terminal_scores,
            **{assignment[key]: value["score"] for key, value in evaluations.items()},
        }
        if unscorable:
            state.update(unscorable_models=unscorable, per_model_scores=per_model_scores, scores={})
            if artifact_hashes(bundle) != frozen:
                raise ValueError("frozen artifacts changed during formal evaluation")
            return finish("stopped", "evaluator_unscorable")
        state["scores"] = per_model_scores
    if artifact_hashes(bundle) != frozen:
        raise ValueError("frozen artifacts changed during formal evaluation")
    return finish("completed")
