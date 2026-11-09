#!/usr/bin/env python3
"""Validate PaperProof audits, including v8 resource rejection and frozen legacy schemas."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

import jsonschema
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT_SCHEMA = ROOT / "schemas" / "result_node_audit.schema.json"
DEFAULT_PAPER_SCHEMA = ROOT / "schemas" / "paper_audit.schema.json"
DEFAULT_PROPAGATION_SCHEMA = ROOT / "schemas" / "propagation_audit.schema.json"

FINDING_ARRAYS = (
    ("statement_object", "theorem_failure", "statement_object_findings"),
    ("proof_obligation", "findings", "proof_obligation"),
    ("inference", "findings", "inference"),
    ("calculation", "findings", "calculation"),
)
REMOVED_KEYS = {
    "root_cause",
    "root_cause_group",
    "severity",
    "repairability",
    "confidence",
    "independence_status",
    "evidence_paths",
    "notes",
    "assessment_notes",
    "aggregate_status",
    "propagation_records",
    "input_issue_leads",
    "input_issue_lead_adjudication",
    "source_representation_fidelity",
    "oracle_policy_applied",
    "conclusion_gap_kinds",
    "oracle_completed_attempts",
    "failure_reason",
    "step_id",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=Path, help="Private paper/result audit JSON to validate")
    parser.add_argument("--result-schema", type=Path, default=DEFAULT_RESULT_SCHEMA)
    parser.add_argument("--paper-schema", type=Path, default=DEFAULT_PAPER_SCHEMA)
    parser.add_argument(
        "--propagation-schema", type=Path, default=DEFAULT_PROPAGATION_SCHEMA
    )
    return parser.parse_args()


def load_json_records(path: Path) -> list[dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list) and value and all(isinstance(item, dict) for item in value):
        return value
    raise ValueError(f"{path}: expected one JSON object or a non-empty JSON array")


def walk_items(value: Any, path: str = "$") -> Iterable[tuple[str, str, Any]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from walk_items(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_items(child, f"{path}[{index}]")


def result_findings(row: dict[str, Any]) -> dict[str, tuple[str, dict[str, Any]]]:
    output: dict[str, tuple[str, dict[str, Any]]] = {}
    for dimension, container, array_key in FINDING_ARRAYS:
        for finding in row[container][array_key]:
            output[finding["finding_id"]] = (dimension, finding)
    return output


def rejected_missing_proof_source(row: dict[str, Any]) -> bool:
    """Missing on legacy records means this new gate was not recorded."""
    return row.get("audit_status") == "rejected_missing_proof_source"


def semantic_errors(
    row: dict[str, Any],
    *,
    expected_lead_ids: set[str] | None = None,
    allowed_source_ids: set[str] | None = None,
    allowed_upstream_error_ids: set[str] | None = None,
) -> list[str]:
    """Check cross-field semantics that JSON Schema cannot express cleanly."""

    errors: list[str] = []

    if rejected_missing_proof_source(row):
        if result_findings(row) or row["theorem_failure"]["other_global_counterexamples"]:
            errors.append("missing-proof-source rejection must have no findings or failure witnesses")
        if row["dependencies"] or row["result_impact_assessment"] is not None:
            errors.append("missing-proof-source rejection must have empty dependencies and null impact")
        if not any(q.strip() for q in row["open_questions"]):
            errors.append("missing-proof-source rejection must identify the unavailable resource in open_questions")

    for key_path, key, child in walk_items(row):
        if key in REMOVED_KEYS:
            errors.append(f"{key_path}: removed v5 key {key!r}")
        if key == "locations" and allowed_source_ids is not None and isinstance(child, list):
            for index, location in enumerate(child):
                if isinstance(location, dict) and location.get("source_id") not in allowed_source_ids:
                    errors.append(
                        f"{key_path}.locations[{index}]: unknown source_id "
                        f"{location.get('source_id')!r}"
                    )

    adjudication_ids = [item["lead_id"] for item in row["lead_adjudications"]]
    duplicate_leads = {lead_id for lead_id in adjudication_ids if adjudication_ids.count(lead_id) > 1}
    for lead_id in sorted(duplicate_leads):
        errors.append(f"duplicate lead adjudication {lead_id!r}")
    if expected_lead_ids is not None:
        actual = set(adjudication_ids)
        for lead_id in sorted(expected_lead_ids - actual):
            errors.append(f"missing lead adjudication {lead_id!r}")
        for lead_id in sorted(actual - expected_lead_ids):
            errors.append(f"adjudication references a lead outside the current result: {lead_id!r}")

    findings: dict[str, tuple[str, dict[str, Any]]] = {}
    duplicate_ids: set[str] = set()
    error_statements: dict[str, list[str]] = {}
    for dimension, container, array_key in FINDING_ARRAYS:
        for finding in row[container][array_key]:
            finding_id = finding["finding_id"]
            if finding_id in findings:
                duplicate_ids.add(finding_id)
            findings[finding_id] = (dimension, finding)
            normalized = " ".join(finding["error_statement"].split()).casefold()
            error_statements.setdefault(normalized, []).append(finding_id)
    for finding_id in sorted(duplicate_ids):
        errors.append(f"duplicate finding_id {finding_id!r}")
    for ids in error_statements.values():
        if len(ids) > 1:
            errors.append(
                "one root error may belong to only one finding; duplicate error_statement at "
                + ", ".join(sorted(ids))
            )

    current_finding_ids = set(findings)
    for finding_id, (_, finding) in findings.items():
        for lead_id in finding["related_lead_ids"]:
            if expected_lead_ids is not None and lead_id not in expected_lead_ids:
                errors.append(f"{finding_id}: related_lead_id {lead_id!r} is not a current-result lead")
        for repaired_id in finding["assessed_after_repairing"]:
            if repaired_id == finding_id:
                errors.append(f"{finding_id}: cannot be assessed after repairing itself")
            elif repaired_id not in current_finding_ids:
                errors.append(f"{finding_id}: unknown repaired finding {repaired_id!r}")

    # Detect cycles in the counterfactual repair-order graph.
    repair_graph = {
        finding_id: set(finding["assessed_after_repairing"])
        for finding_id, (_, finding) in findings.items()
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(finding_id: str) -> None:
        if finding_id in visiting:
            errors.append(f"cyclic assessed_after_repairing relation involving {finding_id!r}")
            return
        if finding_id in visited:
            return
        visiting.add(finding_id)
        for prior_id in repair_graph.get(finding_id, set()):
            if prior_id in repair_graph:
                visit(prior_id)
        visiting.remove(finding_id)
        visited.add(finding_id)

    for finding_id in repair_graph:
        visit(finding_id)

    failure = row["theorem_failure"]
    expected_failure_status = (
        "proven_erroneous"
        if failure["statement_object_findings"] or failure["other_global_counterexamples"]
        else "undetermined"
    )
    if failure["status"] != expected_failure_status:
        errors.append(
            f"theorem_failure.status {failure['status']!r}; witness arrays imply "
            f"{expected_failure_status!r}"
        )
    counterexample_ids = [
        item["counterexample_id"] for item in failure["other_global_counterexamples"]
    ]
    if len(counterexample_ids) != len(set(counterexample_ids)):
        errors.append("duplicate counterexample_id in other_global_counterexamples")

    for dependency in row["dependencies"]:
        status = dependency["use_status"]
        local_ids = dependency["local_finding_ids"]
        upstream_ids = dependency["upstream_finding_ids"]
        for finding_id in local_ids:
            if finding_id not in current_finding_ids:
                errors.append(
                    f"dependency on {dependency['upstream_result_id']}: unknown local_finding_id "
                    f"{finding_id!r}"
                )
        if allowed_upstream_error_ids is not None:
            for finding_id in upstream_ids:
                if finding_id not in allowed_upstream_error_ids:
                    errors.append(
                        f"dependency on {dependency['upstream_result_id']}: upstream_finding_id "
                        f"{finding_id!r} is not in the established-prior-findings ledger"
                    )
        if status == "valid_use" and (local_ids or upstream_ids):
            errors.append("valid_use dependency cannot cite local or upstream error IDs")
        elif status == "invalid_use" and (not local_ids or upstream_ids):
            errors.append("invalid_use dependency requires local IDs and no upstream error IDs")
        elif status == "inherited_blocker" and (not upstream_ids or local_ids):
            errors.append("inherited_blocker requires upstream IDs and no local error IDs")
        elif status == "mixed" and (not upstream_ids or not local_ids):
            errors.append("mixed dependency requires both upstream and local error IDs")

    inherited_ids = {
        finding_id
        for dependency in row["dependencies"]
        if dependency["use_status"] in {"inherited_blocker", "mixed"}
        for finding_id in dependency["upstream_finding_ids"]
    }
    affected = bool(current_finding_ids or inherited_ids)
    impact = row["result_impact_assessment"]
    if not affected and impact is not None:
        errors.append(
            "result_impact_assessment must be null when there is no local finding or inherited blocker"
        )
    if affected and impact is None:
        errors.append(
            "affected result requires a result_impact_assessment object; use a null level if indeterminate"
        )
    if impact is not None:
        level = impact["result_impact_level"]
        driver = impact["primary_driver_finding_id"]
        allowed_drivers = current_finding_ids | inherited_ids
        if level is not None and driver is None:
            errors.append("non-null result impact level requires primary_driver_finding_id")
        if level is None and driver is not None:
            errors.append("indeterminate result impact must use a null primary driver")
        if driver is not None and driver not in allowed_drivers:
            errors.append(
                f"result impact primary driver {driver!r} is neither a local finding nor an inherited blocker"
            )

    return errors


def paper_impact_semantic_errors(
    assessment: dict[str, Any] | None,
    *,
    result_outputs: list[dict[str, Any]],
    allowed_source_ids: set[str],
    additional_affected_result_ids: set[str] | None = None,
) -> list[str]:
    """Validate paper-impact null semantics, references, and evidence locations."""

    errors: list[str] = []
    affected_result_ids = {
        result["result_id"]
        for result in result_outputs
        if not rejected_missing_proof_source(result)
        and result["result_impact_assessment"] is not None
    }
    if additional_affected_result_ids:
        affected_result_ids.update(additional_affected_result_ids)
    if not affected_result_ids and assessment is not None:
        errors.append(
            "paper_impact_assessment must be null when no audited or propagated result is affected"
        )
    if affected_result_ids and assessment is None:
        errors.append(
            "affected paper requires a paper_impact_assessment object; use a null level if indeterminate"
        )
    if assessment is None:
        return errors

    level = assessment["paper_impact_level"]
    driver = assessment["primary_driver_result_id"]
    if level is not None and driver is None:
        errors.append("non-null paper impact level requires primary_driver_result_id")
    if level is not None and not assessment["evidence_locations"]:
        errors.append("non-null paper impact level requires at least one evidence location")
    if level is None and driver is not None:
        errors.append("indeterminate paper impact must use a null primary driver")
    if driver is not None and driver not in affected_result_ids:
        errors.append(
            f"paper impact primary driver {driver!r} is not an affected audited or propagated result"
        )
    for index, location in enumerate(assessment["evidence_locations"]):
        if location["source_id"] not in allowed_source_ids:
            errors.append(
                f"paper impact evidence_locations[{index}] uses unknown source_id "
                f"{location['source_id']!r}"
            )
    return errors


def paper_semantic_errors(paper: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    sources = paper["paper_context"]["sources"]
    source_ids = [source["source_id"] for source in sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source_id in paper_context.sources")

    inventory_ids = [item["result_id"] for item in paper["result_inventory"]]
    inventory_set = set(inventory_ids)
    if len(inventory_ids) != len(inventory_set):
        errors.append("duplicate result_id in result_inventory")
    for item in paper["result_inventory"]:
        for upstream_id in item["depends_on"]:
            if upstream_id not in inventory_set:
                errors.append(
                    f"result_inventory item {item['result_id']!r} depends on absent result "
                    f"{upstream_id!r}"
                )

    target_ids = paper["target_result_ids"]
    for result_id in target_ids:
        if result_id not in inventory_set:
            errors.append(f"target_result_id {result_id!r} is absent from result_inventory")
    target_position = {result_id: index for index, result_id in enumerate(target_ids)}
    inventory_by_id = {item["result_id"]: item for item in paper["result_inventory"]}
    for result_id in target_ids:
        for upstream_id in inventory_by_id.get(result_id, {}).get("depends_on", []):
            if upstream_id in target_position and target_position[upstream_id] > target_position[result_id]:
                errors.append(
                    f"target_result_ids is not dependency-first: {result_id!r} precedes "
                    f"selected upstream {upstream_id!r}"
                )

    leads = paper["issue_leads"]
    lead_ids = [lead["lead_id"] for lead in leads]
    if len(lead_ids) != len(set(lead_ids)):
        errors.append("duplicate lead_id in issue_leads")
    for lead in leads:
        if lead["result_id"] not in inventory_set:
            errors.append(
                f"issue lead {lead['lead_id']!r} refers to absent result {lead['result_id']!r}"
            )

    audits = paper["result_audits"]
    if any(rejected_missing_proof_source(audit) for audit in audits) and not any(
        question.strip() for question in paper["paper_open_questions"]
    ):
        errors.append("paper with rejected proof resources must record its coverage limitation in paper_open_questions")
    audit_ids = [audit["result_id"] for audit in audits]
    if audit_ids != target_ids:
        errors.append(
            "result_audits must appear exactly once in target_result_ids order; got "
            f"{audit_ids!r}, expected {target_ids!r}"
        )

    source_id_set = set(source_ids)
    established_prior_ids: set[str] = set()
    lead_ids_by_result = {
        result_id: {lead["lead_id"] for lead in leads if lead["result_id"] == result_id}
        for result_id in inventory_set
    }
    for audit in audits:
        prefix = audit["result_id"]
        for message in semantic_errors(
            audit,
            expected_lead_ids=lead_ids_by_result[prefix],
            allowed_source_ids=source_id_set,
            allowed_upstream_error_ids=established_prior_ids,
        ):
            errors.append(f"{prefix}: {message}")
        for dependency in audit["dependencies"]:
            if dependency["upstream_result_id"] not in inventory_set:
                errors.append(
                    f"{prefix}: dependency refers to absent upstream result "
                    f"{dependency['upstream_result_id']!r}"
                )
        established_prior_ids.update(result_findings(audit))

    propagation = paper.get("propagation_audit")
    propagated_affected_result_ids = {
        assessment["downstream_result_id"]
        for assessment in (
            propagation["downstream_assessments"] if propagation is not None else []
        )
        if assessment.get("propagated_result_impact_assessment") is not None
    }
    if propagation is not None:
        propagation_ids = [
            assessment["downstream_result_id"]
            for assessment in propagation["downstream_assessments"]
        ]
        if len(propagation_ids) != len(set(propagation_ids)):
            errors.append("duplicate downstream_result_id in propagation_audit")
        known_finding_ids = {
            finding_id
            for audit in audits
            for finding_id in result_findings(audit)
        }
        finding_source_result = {
            finding_id: audit["result_id"]
            for audit in audits
            for finding_id in result_findings(audit)
        }

        def is_declared_descendant(
            downstream_result_id: str, upstream_result_id: str
        ) -> bool:
            pending = [downstream_result_id]
            visited: set[str] = set()
            while pending:
                current = pending.pop()
                if current in visited:
                    continue
                visited.add(current)
                for dependency_id in inventory_by_id.get(current, {}).get(
                    "depends_on", []
                ):
                    if dependency_id == upstream_result_id:
                        return True
                    pending.append(dependency_id)
            return False

        for assessment in propagation["downstream_assessments"]:
            result_id = assessment["downstream_result_id"]
            if result_id not in inventory_set:
                errors.append(
                    f"propagation assessment refers to absent result {result_id!r}"
                )
            elif inventory_by_id[result_id]["inventory_role"] != "theory_candidate":
                errors.append(
                    f"propagation assessment target {result_id!r} is not a theory_candidate"
                )
            if result_id in target_ids:
                errors.append(
                    f"propagation assessment duplicates fully audited target {result_id!r}"
                )
            unknown_finding_ids = (
                set(assessment["upstream_finding_ids"]) - known_finding_ids
            )
            if unknown_finding_ids:
                errors.append(
                    f"propagation assessment for {result_id!r} cites unknown finding IDs "
                    f"{sorted(unknown_finding_ids)!r}"
                )
            for finding_id in assessment["upstream_finding_ids"]:
                upstream_result_id = finding_source_result.get(finding_id)
                if (
                    upstream_result_id is not None
                    and result_id in inventory_set
                    and not is_declared_descendant(result_id, upstream_result_id)
                ):
                    errors.append(
                        f"propagation assessment for {result_id!r} cites finding "
                        f"{finding_id!r} from non-ancestor result {upstream_result_id!r}"
                    )
            for index, location in enumerate(assessment["use_locations"]):
                if location["source_id"] not in source_id_set:
                    errors.append(
                        f"propagation assessment for {result_id!r} use_locations[{index}] "
                        f"uses unknown source_id {location['source_id']!r}"
                    )

            status = assessment["propagation_status"]
            impact = assessment["propagated_result_impact_assessment"]
            if status == "unaffected_interface_not_used" and impact is not None:
                errors.append(
                    f"propagation assessment for {result_id!r}: unaffected status requires null impact"
                )
            if status != "unaffected_interface_not_used" and impact is None:
                errors.append(
                    f"propagation assessment for {result_id!r}: non-unaffected status requires impact"
                )
            if impact is not None:
                level = impact["result_impact_level"]
                driver = impact["primary_driver_finding_id"]
                if status == "indeterminate":
                    if level is not None or driver is not None:
                        errors.append(
                            f"propagation assessment for {result_id!r}: indeterminate status "
                            "requires null level and driver"
                        )
                else:
                    if status == "survives_under_selected_repair" and level != 1:
                        errors.append(
                            f"propagation assessment for {result_id!r}: surviving original "
                            "contract requires Level 1"
                        )
                    if level is None or driver is None:
                        errors.append(
                            f"propagation assessment for {result_id!r}: determinate affected "
                            "status requires level and driver"
                        )
                    elif driver not in assessment["upstream_finding_ids"]:
                        errors.append(
                            f"propagation assessment for {result_id!r}: impact driver is not "
                            "one of its upstream finding IDs"
                        )
    errors.extend(
        paper_impact_semantic_errors(
            paper["paper_impact_assessment"],
            result_outputs=audits,
            allowed_source_ids=source_id_set,
            additional_affected_result_ids=propagated_affected_result_ids,
        )
    )

    return errors


def make_paper_validator(
    paper_schema: dict[str, Any],
    result_schema: dict[str, Any],
    propagation_schema: dict[str, Any] | None = None,
) -> jsonschema.Draft202012Validator:
    registry = Registry().with_resource(
        "result_node_audit.schema.json",
        Resource.from_contents(result_schema),
    )
    if propagation_schema is not None:
        registry = registry.with_resource(
            "propagation_audit.schema.json",
            Resource.from_contents(propagation_schema),
        )
    return jsonschema.Draft202012Validator(paper_schema, registry=registry)


def main() -> int:
    args = parse_args()
    try:
        papers = load_json_records(args.data)
        result_schema = json.loads(args.result_schema.read_text(encoding="utf-8"))
        paper_schema = json.loads(args.paper_schema.read_text(encoding="utf-8"))
        propagation_schema = json.loads(
            args.propagation_schema.read_text(encoding="utf-8")
        )
        jsonschema.Draft202012Validator.check_schema(result_schema)
        jsonschema.Draft202012Validator.check_schema(paper_schema)
        jsonschema.Draft202012Validator.check_schema(propagation_schema)
    except (OSError, ValueError, json.JSONDecodeError, jsonschema.SchemaError) as exc:
        print(exc, file=sys.stderr)
        return 1

    validator = make_paper_validator(
        paper_schema, result_schema, propagation_schema
    )
    all_errors: list[str] = []
    paper_ids: set[str] = set()
    dimension_counts: Counter[str] = Counter()
    subtype_counts: Counter[str] = Counter()
    failure_counts: Counter[str] = Counter()
    verdict_counts: Counter[str] = Counter()
    repair_counts: Counter[str] = Counter()
    result_impact_counts: Counter[str] = Counter()
    paper_impact_counts: Counter[str] = Counter()
    propagation_counts: Counter[str] = Counter()

    for index, paper in enumerate(papers, 1):
        prefix = f"{args.data}:{index}"
        paper_id = paper.get("paper_id", "<missing>")
        if paper_id in paper_ids:
            all_errors.append(f"{prefix}: duplicate paper_id {paper_id!r}")
        paper_ids.add(paper_id)

        structural_errors = list(validator.iter_errors(paper))
        for error in sorted(structural_errors, key=lambda item: list(item.absolute_path)):
            json_path = "$" + "".join(
                f"[{part}]" if isinstance(part, int) else f".{part}"
                for part in error.absolute_path
            )
            all_errors.append(f"{prefix}:{json_path}: {error.message}")
        if structural_errors:
            continue

        for message in paper_semantic_errors(paper):
            all_errors.append(f"{prefix}: {message}")

        for audit in paper["result_audits"]:
            failure = audit["theorem_failure"]
            failure_counts[failure["status"]] += 1
            failure_counts["statement_object_witness"] += len(
                failure["statement_object_findings"]
            )
            failure_counts["other_global_counterexample"] += len(
                failure["other_global_counterexamples"]
            )
            for adjudication in audit["lead_adjudications"]:
                verdict_counts[adjudication["verdict"]] += 1
            for dimension, container, array_key in FINDING_ARRAYS:
                for finding in audit[container][array_key]:
                    dimension_counts[dimension] += 1
                    subtype_counts[finding["subtype"]] += 1
                    repair_level = finding["repair_assessment"]["repair_difficulty_level"]
                    repair_counts["null" if repair_level is None else str(repair_level)] += 1
            impact = audit["result_impact_assessment"]
            result_impact_counts[
                "clean"
                if impact is None
                else (
                    "null"
                    if impact["result_impact_level"] is None
                    else str(impact["result_impact_level"])
                )
            ] += 1
        paper_impact = paper["paper_impact_assessment"]
        paper_impact_counts[
            "clean"
            if paper_impact is None
            else (
                "null"
                if paper_impact["paper_impact_level"] is None
                else str(paper_impact["paper_impact_level"])
            )
        ] += 1
        propagation = paper.get("propagation_audit")
        if propagation is not None:
            propagation_counts["downstream_results"] += len(
                propagation["downstream_assessments"]
            )
            for assessment in propagation["downstream_assessments"]:
                propagation_counts[
                    f"status:{assessment['propagation_status']}"
                ] += 1
                propagation_counts["open_questions"] += len(
                    assessment["open_questions"]
                )
                impact = assessment["propagated_result_impact_assessment"]
                propagation_counts[
                    "impact:clean"
                    if impact is None
                    else (
                        "impact:null"
                        if impact["result_impact_level"] is None
                        else f"impact:{impact['result_impact_level']}"
                    )
                ] += 1

    if all_errors:
        print("Validation failed:", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(papers)} paper audit record(s) from {args.data}")
    print(f"Audited result nodes: {sum(len(paper['result_audits']) for paper in papers)}")
    print(f"Atomic findings/root errors: {sum(dimension_counts.values())}")
    print("Findings by dimension:")
    for name, count in sorted(dimension_counts.items()):
        print(f"  {name}: {count}")
    print("Findings by subtype:")
    for name, count in sorted(subtype_counts.items()):
        print(f"  {name}: {count}")
    print("Theorem-failure evidence:")
    for name, count in sorted(failure_counts.items()):
        print(f"  {name}: {count}")
    print("Input-lead adjudications:")
    for name, count in sorted(verdict_counts.items()):
        print(f"  {name}: {count}")
    print("Finding repair difficulty:")
    for name, count in sorted(repair_counts.items()):
        print(f"  {name}: {count}")
    print("Result impact:")
    for name, count in sorted(result_impact_counts.items()):
        print(f"  {name}: {count}")
    print("Paper impact:")
    for name, count in sorted(paper_impact_counts.items()):
        print(f"  {name}: {count}")
    if propagation_counts:
        print("Downstream propagation:")
        for name, count in sorted(propagation_counts.items()):
            print(f"  {name}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
