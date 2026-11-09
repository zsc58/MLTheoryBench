from __future__ import annotations

from typing import Any

from jsonschema import Draft202012Validator


VALIDITY_STATUSES = {
    "valid_complete",
    "valid_with_minor_issue",
    "incomplete_major_gap",
}
SEVERITY_RANK = {"none": 0, "minor": 1, "major": 2}


def validate_schema(value: Any, schema: dict[str, Any]) -> None:
    errors = sorted(
        Draft202012Validator(schema).iter_errors(value),
        key=lambda error: list(error.absolute_path),
    )
    if errors:
        error = errors[0]
        location = ".".join(str(item) for item in error.absolute_path) or "<root>"
        raise ValueError(f"schema validation failed at {location}: {error.message}")


def _unique_ids(items: list[Any], key: str, label: str) -> set[str]:
    identifiers: list[str] = []
    for item in items:
        if not isinstance(item, dict):
            raise ValueError(f"each {label} must be an object")
        identifier = item.get(key)
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError(f"each {label} requires a non-empty {key}")
        identifiers.append(identifier)
    if len(identifiers) != len(set(identifiers)):
        raise ValueError(f"{label} IDs must be unique")
    return set(identifiers)


def _validate_dag(items: list[dict[str, Any]], key: str = "step_id") -> dict[str, list[str]]:
    identifiers = _unique_ids(items, key, "step")
    graph: dict[str, list[str]] = {}
    for item in items:
        identifier = str(item[key])
        dependencies = item.get("depends_on")
        if not isinstance(dependencies, list) or not all(
            isinstance(dependency, str) for dependency in dependencies
        ):
            raise ValueError("step dependencies must be string lists")
        if identifier in dependencies:
            raise ValueError("a step cannot depend on itself")
        unknown = set(dependencies) - identifiers
        if unknown:
            raise ValueError(
                f"{identifier} has unknown dependencies: " + ", ".join(sorted(unknown))
            )
        graph[identifier] = dependencies

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(identifier: str) -> None:
        if identifier in visiting:
            raise ValueError("step dependencies must be acyclic")
        if identifier in visited:
            return
        visiting.add(identifier)
        for predecessor in graph[identifier]:
            visit(predecessor)
        visiting.remove(identifier)
        visited.add(identifier)

    for identifier in graph:
        visit(identifier)
    return graph


def validate_reviewer_report(
    value: Any, schema: dict[str, Any]
) -> dict[str, Any]:
    validate_schema(value, schema)
    if not isinstance(value, dict):
        raise ValueError("reviewer report must be an object")

    proof_steps = value["proof_steps"]
    findings = value["findings"]
    checks = value["adversarial_checks"]
    _validate_dag(proof_steps)
    finding_ids = _unique_ids(findings, "finding_id", "finding")

    active_severities: list[str] = []
    for finding in findings:
        status = finding["status"]
        severity = finding["severity"]
        if status == "resolved_nonissue":
            if severity != "none":
                raise ValueError("a resolved nonissue must have severity none")
        elif severity == "none":
            raise ValueError("an active finding cannot have severity none")
        if status in {"verified", "candidate"}:
            active_severities.append(severity)

    for check in checks:
        related = check["related_finding_ids"]
        unknown = set(related) - finding_ids
        if unknown:
            raise ValueError(
                "adversarial check references unknown findings: "
                + ", ".join(sorted(unknown))
            )
        if check["result"] == "break_found":
            linked = any(
                finding["finding_id"] in related
                and finding["status"] == "verified"
                and finding["severity"] == "major"
                for finding in findings
            )
            if not linked:
                raise ValueError(
                    "break_found requires a linked verified major finding"
                )

    support_statuses = {step["support_status"] for step in proof_steps}
    has_major = "major" in active_severities
    has_minor = "minor" in active_severities
    has_incomplete = bool(support_statuses & {"partial", "unsupported", "incorrect"})
    status = value["validity_status"]
    if status == "valid_complete" and (active_severities or has_incomplete):
        raise ValueError("valid_complete conflicts with findings or incomplete steps")
    if status == "valid_with_minor_issue":
        if not has_minor or has_major:
            raise ValueError(
                "valid_with_minor_issue requires a minor issue and no major issue"
            )
        if support_statuses & {"unsupported", "incorrect"}:
            raise ValueError("minor status cannot contain a broken proof step")
    if status == "incomplete_major_gap" and not (has_major or has_incomplete):
        raise ValueError("incomplete_major_gap requires a substantive proof gap")
    return value


def _expected_verdict(score: int) -> str:
    if score == 10:
        return "fully_correct"
    if score >= 8:
        return "minor_repair"
    if score >= 3:
        return "substantial_partial_progress"
    if score >= 1:
        return "minimal_progress"
    return "incorrect"


def validate_evaluation(
    value: Any,
    schema: dict[str, Any],
    reviewer_report: dict[str, Any],
) -> dict[str, Any]:
    validate_schema(value, schema)
    if not isinstance(value, dict):
        raise ValueError("evaluation must be an object")

    score = value["score"]
    if value["verdict"] != _expected_verdict(score):
        raise ValueError("score and verdict are inconsistent")

    steps = value["core_step_evaluations"]
    graph = _validate_dag(steps)
    step_by_id = {step["step_id"]: step for step in steps}
    if sum(step["points_available"] for step in steps) != 10:
        raise ValueError("core-step weights must total 10")
    if sum(step["points_awarded"] for step in steps) != score:
        raise ValueError("awarded core-step points must equal the score")
    for step in steps:
        available = step["points_available"]
        awarded = step["points_awarded"]
        if awarded > available:
            raise ValueError("points_awarded cannot exceed points_available")
        credit = step["credit"]
        if credit == "none" and awarded != 0:
            raise ValueError("none credit requires zero points")
        if credit == "full" and awarded != available:
            raise ValueError("full credit requires all available points")
        if credit == "partial" and not 0 < awarded < available:
            raise ValueError("partial credit must be strictly between zero and full")
        invalid_predecessors = [
            predecessor
            for predecessor in graph[step["step_id"]]
            if step_by_id[predecessor]["conclusion_status"]
            in {"incorrect", "not_applicable"}
        ]
        if invalid_predecessors and awarded > 0:
            raise ValueError(
                f"{step['step_id']} receives credit through an invalid predecessor: "
                + ", ".join(invalid_predecessors)
            )

    added_ids = set(value["added_core_steps"])
    evaluator_added_ids = {
        step["step_id"] for step in steps if step["origin"] == "evaluator_added"
    }
    if added_ids != evaluator_added_ids:
        raise ValueError(
            "added_core_steps must exactly match evaluator-added step IDs"
        )

    resolution = value["validity_review_resolution"]
    initial_status = reviewer_report["validity_status"]
    if resolution["initial_status"] != initial_status:
        raise ValueError("initial validity status does not match reviewer report")
    final_status = resolution["final_status"]
    if final_status == "valid_complete" and score != 10:
        raise ValueError("valid_complete requires score 10")
    if final_status == "valid_with_minor_issue" and score not in {8, 9}:
        raise ValueError("valid_with_minor_issue requires score 8 or 9")
    if final_status == "incomplete_major_gap" and score > 7:
        raise ValueError("incomplete_major_gap is capped at 7")

    findings = reviewer_report["findings"]
    finding_by_id = {finding["finding_id"]: finding for finding in findings}
    resolutions = resolution["finding_resolutions"]
    resolution_ids = [item["finding_id"] for item in resolutions]
    if len(resolution_ids) != len(set(resolution_ids)):
        raise ValueError("each reviewer finding must be resolved exactly once")
    if set(resolution_ids) != set(finding_by_id):
        raise ValueError("finding resolutions must match all reviewer findings")

    final_severities: set[str] = set()
    for item in resolutions:
        original = finding_by_id[item["finding_id"]]
        original_severity = original["severity"]
        final_severity = item["final_severity"]
        kind = item["resolution"]
        if kind == "confirmed" and final_severity != original_severity:
            raise ValueError("a confirmed finding must preserve severity")
        if kind == "dismissed" and final_severity != "none":
            raise ValueError("a dismissed finding must have severity none")
        if kind == "downgraded" and not (
            SEVERITY_RANK[final_severity] < SEVERITY_RANK[original_severity]
        ):
            raise ValueError("a downgraded finding must have lower severity")
        if (
            original["status"] == "verified"
            and original_severity == "major"
            and kind != "confirmed"
        ):
            raise ValueError("a verified major finding cannot be overridden")
        if kind != "dismissed":
            final_severities.add(final_severity)

    if final_status in {"valid_complete", "valid_with_minor_issue"}:
        if "major" in final_severities:
            raise ValueError("a valid final status cannot retain a major finding")
    if final_status == "valid_complete" and "minor" in final_severities:
        raise ValueError("valid_complete cannot retain a minor finding")

    if final_status == "valid_complete" and any(
        step["conclusion_status"] != "correct" or step["proof_status"] != "correct"
        for step in steps
    ):
        raise ValueError("score 10 requires every core conclusion and proof to be correct")
    if final_status == "valid_with_minor_issue" and any(
        step["conclusion_status"] in {"incorrect", "uncertain", "not_applicable"}
        or step["proof_status"] in {"incorrect", "missing", "not_applicable"}
        for step in steps
    ):
        raise ValueError("an 8-9 proof cannot contain a broken core step")
    return value
