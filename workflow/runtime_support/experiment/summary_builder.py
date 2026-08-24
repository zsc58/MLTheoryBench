from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from runtime_support.experiment.run_utils import atomic_write_json
from reviewer_and_evaluator.evaluator.run_evaluator import validate_evaluation
from reviewer_and_evaluator.reviewer.run_reviewer import validate_validity_report


def expected_papers(run_record: dict[str, Any]) -> dict[str, list[str]]:
    declared = run_record.get("papers")
    if isinstance(declared, dict):
        result: dict[str, list[str]] = {}
        for paper_id, value in declared.items():
            theorem_ids = value.get("theorem_ids") if isinstance(value, dict) else None
            if isinstance(theorem_ids, list):
                result[str(paper_id)] = sorted(str(item) for item in theorem_ids)
        if result:
            return result

    result: dict[str, list[str]] = {}
    for value in run_record.get("tasks", {}).values():
        if not isinstance(value, dict):
            continue
        paper_id = value.get("paper_id")
        theorem_id = value.get("theorem_id")
        if isinstance(paper_id, str) and isinstance(theorem_id, str):
            result.setdefault(paper_id, []).append(theorem_id)
    return {paper_id: sorted(set(theorems)) for paper_id, theorems in result.items()}


def build_paper_summary(
    run_dir: Path,
    run_record: dict[str, Any],
    paper_id: str,
    theorem_ids: list[str],
) -> dict[str, Any]:
    paper_dir = run_dir / paper_id
    evaluations: list[tuple[str, dict[str, Any]]] = []
    for theorem_id in theorem_ids:
        path = paper_dir / theorem_id / "evaluation.json"
        if path.is_file():
            validity_path = paper_dir / theorem_id / "validity_report.json"
            validity_report = None
            if validity_path.is_file():
                validity_report = validate_validity_report(
                    json.loads(validity_path.read_text(encoding="utf-8"))
                )
            value = validate_evaluation(
                json.loads(path.read_text(encoding="utf-8")),
                validity_report,
                allow_legacy=validity_report is None,
            )
            evaluations.append((theorem_id, value))

    evaluated_ids = {theorem_id for theorem_id, _ in evaluations}
    missing = [item for item in theorem_ids if item not in evaluated_ids]
    failed: list[str] = []
    for theorem_id in missing:
        task = run_record.get("tasks", {}).get(f"{paper_id}/{theorem_id}", {})
        if not isinstance(task, dict):
            continue
        stages = [
            task.get("solver"),
            task.get("validity_reviewer"),
            task.get("evaluator"),
        ]
        if any(
            isinstance(stage, dict) and stage.get("status") == "failed"
            for stage in stages
        ):
            failed.append(theorem_id)

    scored = [
        (theorem_id, value)
        for theorem_id, value in evaluations
        if value["evaluation_status"] == "scored"
    ]
    scores = [int(value["score"]) for _, value in scored]
    unscorable = [
        theorem_id
        for theorem_id, value in evaluations
        if value["evaluation_status"] == "unscorable"
    ]
    needs_review = [
        theorem_id
        for theorem_id, value in evaluations
        if value["needs_human_review"]
    ]
    summary: dict[str, Any] = {
        "schema_version": "1.0",
        "paper_id": paper_id,
        "status": "completed" if not missing else "partial",
        "expected_theorem_count": len(theorem_ids),
        "evaluated_theorem_count": len(evaluations),
        "failed_theorem_count": len(failed),
        "missing_theorems": missing,
        "failed_theorems": failed,
        "scored_theorem_count": len(scored),
        "unscorable_theorem_count": len(unscorable),
        "theorems": [
            {
                "theorem_id": theorem_id,
                "evaluation_status": value["evaluation_status"],
                "score": value["score"],
                "verdict": value["verdict"],
                "validity_status": value.get(
                    "validity_review_resolution", {}
                ).get("final_status"),
                "needs_human_review": value["needs_human_review"],
            }
            for theorem_id, value in evaluations
        ],
        "mean_score": (sum(scores) / len(scores)) if scores else None,
        "score_range": [min(scores), max(scores)] if scores else None,
        "needs_human_review": bool(needs_review),
        "theorems_needing_human_review": needs_review,
        "unscorable_theorems": unscorable,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    atomic_write_json(paper_dir / "summary.json", summary)
    return summary


def build_all_paper_summaries(run_dir: Path) -> dict[str, dict[str, Any]]:
    run_dir = run_dir.resolve()
    run_record = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    return {
        paper_id: build_paper_summary(
            run_dir, run_record, paper_id, theorem_ids
        )
        for paper_id, theorem_ids in expected_papers(run_record).items()
    }
