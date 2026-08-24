from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"

SCHEMA_FILES = {
    "triage": "triage.schema.json",
    "triage_audit": "triage_audit.schema.json",
    "target_selection": "target_selection.schema.json",
    "source_audit": "source_audit.schema.json",
    "source_check": "source_check.schema.json",
    "paper_analysis": "paper_analysis.schema.json",
    "compile": "compile.schema.json",
    "artifact_audit": "artifact_audit.schema.json",
    "complexity": "prc_assessment.schema.json",
    "revision": "revision.schema.json",
}

RESULT_ROLES = {"theory_candidate", "internal_support"}


class Stage3ContractError(ValueError):
    pass


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMA_DIR / SCHEMA_FILES[name]).read_text(encoding="utf-8"))


def validate_schema(name: str, value: dict[str, Any]) -> None:
    errors = sorted(
        Draft202012Validator(load_schema(name)).iter_errors(value),
        key=lambda error: list(error.absolute_path),
    )
    if not errors:
        return
    rendered = []
    for error in errors[:10]:
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        rendered.append(f"{location}: {error.message}")
    raise Stage3ContractError(f"invalid {name}: " + "; ".join(rendered))


def _index_unique(items: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for item in items:
        item_id = item["item_id"]
        if item_id in indexed:
            raise Stage3ContractError(f"duplicate {label} item_id: {item_id}")
        indexed[item_id] = item
    return indexed


def _require_unique(values: list[Any], label: str) -> None:
    rendered = [json.dumps(value, sort_keys=True, ensure_ascii=False) for value in values]
    if len(rendered) != len(set(rendered)):
        raise Stage3ContractError(f"{label} contains duplicate items")


def _validate_dependencies(index: dict[str, dict[str, Any]]) -> None:
    for item_id, item in index.items():
        _require_unique(item["depends_on"], f"{item_id}.depends_on")
        for dependency_id in item["depends_on"]:
            if dependency_id not in index:
                raise Stage3ContractError(
                    f"{item_id} depends on unknown material {dependency_id}"
                )
            if dependency_id == item_id:
                raise Stage3ContractError(f"{item_id} cannot depend on itself")

    state: dict[str, int] = {}

    def visit(item_id: str) -> None:
        marker = state.get(item_id, 0)
        if marker == 1:
            raise Stage3ContractError(
                f"proof-dependency cycle detected at {item_id}"
            )
        if marker == 2:
            return
        state[item_id] = 1
        for dependency_id in index[item_id]["depends_on"]:
            visit(dependency_id)
        state[item_id] = 2

    for item_id in index:
        visit(item_id)


def dependency_closure(
    seed_ids: list[str], index: dict[str, dict[str, Any]]
) -> set[str]:
    closure: set[str] = set()
    pending = list(seed_ids)
    while pending:
        item_id = pending.pop()
        if item_id in closure:
            continue
        if item_id not in index:
            raise Stage3ContractError(f"unknown selected material: {item_id}")
        closure.add(item_id)
        pending.extend(index[item_id]["depends_on"])
    return closure


def validate_triage(value: dict[str, Any]) -> dict[str, dict[str, Any]]:
    validate_schema("triage", value)
    index = _index_unique(value["theory_inventory"], "triage")
    for item_id, item in index.items():
        _require_unique(item["source_spans"], f"{item_id}.source_spans")
    _validate_dependencies(index)
    return index


def validate_triage_audit(
    original: dict[str, Any], audit: dict[str, Any]
) -> dict[str, Any]:
    validate_schema("triage_audit", audit)
    validate_triage(original)
    effective = audit["effective_triage"]
    validate_triage(effective)
    if audit["status"] == "confirmed_filtered_out":
        if effective != original:
            raise Stage3ContractError(
                "confirmed_filtered_out must preserve the original triage record"
            )
        if effective["status"] != "filtered_out":
            raise Stage3ContractError(
                "confirmed_filtered_out requires a filtered effective triage"
            )
    elif effective == original:
        raise Stage3ContractError("corrected triage audit must change the record")
    return effective


def validate_target_selection(
    triage: dict[str, Any], selection: dict[str, Any]
) -> None:
    validate_schema("target_selection", selection)
    index = validate_triage(triage)

    evaluations = selection["candidate_chain_evaluations"]
    chain_index: dict[str, dict[str, Any]] = {}
    for evaluation in evaluations:
        chain_id = evaluation["chain_id"]
        if chain_id in chain_index:
            raise Stage3ContractError(f"duplicate chain_id: {chain_id}")
        chain_index[chain_id] = evaluation

        candidates = set(evaluation["candidate_ids"])
        _require_unique(
            evaluation["candidate_ids"], f"{chain_id}.candidate_ids"
        )
        for item_id in candidates:
            if item_id not in index:
                raise Stage3ContractError(
                    f"{chain_id} references unknown candidate {item_id}"
                )
            if index[item_id]["role"] != "theory_candidate":
                raise Stage3ContractError(
                    f"{chain_id} item {item_id} is not a theory_candidate"
                )

        contribution = evaluation["contribution_fidelity"]
        expected_cf_total = sum(
            contribution[field]
            for field in (
                "paper_level_contribution_recovery",
                "scientific_sufficiency",
                "scope_economy",
            )
        )
        if contribution["total"] != expected_cf_total:
            raise Stage3ContractError(
                f"{chain_id} CF_total must equal its three subscores"
            )

        difficulty = evaluation["difficulty_fidelity"]
        if difficulty is not None:
            expected_df_total = sum(
                difficulty[field]
                for field in (
                    "bottleneck_coverage",
                    "mechanism_representativeness",
                    "difficulty_distortion",
                )
            )
            if difficulty["total"] != expected_df_total:
                raise Stage3ContractError(
                    f"{chain_id} DF_total must equal its three subscores"
                )

    eligible = [
        evaluation
        for evaluation in evaluations
        if evaluation["contribution_fidelity"]["total"] >= 8
    ]
    for evaluation in evaluations:
        should_have_df = evaluation in eligible
        if should_have_df != (evaluation["difficulty_fidelity"] is not None):
            raise Stage3ContractError(
                "DF scores must be present exactly for chains with CF_total >= 8"
            )
    all_candidates = {
        item_id
        for item_id, item in index.items()
        if item["role"] == "theory_candidate"
    }
    omitted_ids = [item["item_id"] for item in selection["omitted_candidates"]]
    if len(omitted_ids) != len(set(omitted_ids)):
        raise Stage3ContractError("omitted_candidates contains duplicate item IDs")

    if not eligible:
        if selection["status"] != "stopped":
            raise Stage3ContractError(
                "no chain with CF_total >= 8 requires status stopped"
            )
        if selection["ranked_chain_ids"]:
            raise Stage3ContractError("a stopped selection cannot rank any chain")
        if set(omitted_ids) != all_candidates:
            raise Stage3ContractError(
                "a stopped selection must list every theory_candidate as omitted"
            )
        return

    if selection["status"] != "selected":
        raise Stage3ContractError(
            "an admissible candidate chain requires status selected"
        )

    ranked = sorted(
        eligible,
        key=lambda item: (
            -item["contribution_fidelity"]["total"],
            -item["difficulty_fidelity"]["total"],
            -len(item["candidate_ids"]),
            item["chain_id"],
        ),
    )
    expected_ranked_ids = [item["chain_id"] for item in ranked]
    ranked_chain_ids = selection["ranked_chain_ids"]
    _require_unique(ranked_chain_ids, "ranked_chain_ids")
    if ranked_chain_ids != expected_ranked_ids:
        raise Stage3ContractError(
            "ranked_chain_ids must order every CF>=8 chain by CF, DF, then length"
        )

    selected_chain_id = selection["selected_chain_id"]
    if selected_chain_id != ranked_chain_ids[0]:
        raise Stage3ContractError(
            "selected_chain_id must be the first correctness-blind ranked chain"
        )
    top_key = (
        ranked[0]["contribution_fidelity"]["total"],
        ranked[0]["difficulty_fidelity"]["total"],
        len(ranked[0]["candidate_ids"]),
    )
    exact_top_ties = [
        item
        for item in ranked
        if (
            item["contribution_fidelity"]["total"],
            item["difficulty_fidelity"]["total"],
            len(item["candidate_ids"]),
        )
        == top_key
    ]
    if len(exact_top_ties) > 1 and selection["selection_ambiguity"] is None:
        raise Stage3ContractError(
            "an unresolved exact selection tie requires selection_ambiguity"
        )

    selected_evaluation = chain_index[selected_chain_id]
    selected_from_chain = set(selected_evaluation["candidate_ids"])
    if set(selection["selected_candidate_ids"]) != selected_from_chain:
        raise Stage3ContractError(
            "selected_candidate_ids must equal the selected chain's candidate_ids"
        )

    selected = set(selection["selected_candidate_ids"])
    attached = set(selection["attached_material_ids"])
    _require_unique(selection["selected_candidate_ids"], "selected_candidate_ids")
    _require_unique(selection["attached_material_ids"], "attached_material_ids")
    if selected & attached:
        raise Stage3ContractError(
            "selected_candidate_ids and attached_material_ids must be disjoint"
        )

    for item_id in selected:
        if item_id not in index:
            raise Stage3ContractError(f"unknown selected candidate: {item_id}")
        if index[item_id]["role"] != "theory_candidate":
            raise Stage3ContractError(
                f"selected item {item_id} is not a theory_candidate"
            )

    for item_id in attached:
        if item_id not in index:
            raise Stage3ContractError(f"unknown attached material: {item_id}")
        if index[item_id]["role"] == "theory_candidate":
            raise Stage3ContractError(
                f"theory_candidate {item_id} must be selected or omitted, not attached"
            )

    if set(omitted_ids) != all_candidates - selected:
        raise Stage3ContractError(
            "omitted_candidates must list every unselected theory_candidate exactly once"
        )

    known_closure = dependency_closure(list(selected), index)
    for item_id in known_closure - selected:
        role = index[item_id]["role"]
        if role == "theory_candidate":
            continue
        if item_id not in attached:
            raise Stage3ContractError(
                f"known dependency {item_id} is missing from attached_material_ids"
            )


def validate_source_audit(
    triage: dict[str, Any], source_audit: dict[str, Any]
) -> dict[str, dict[str, Any]]:
    validate_schema("source_audit", source_audit)
    triage_index = validate_triage(triage)
    records = source_audit["material_records"]
    index = _index_unique(records, "source-audit")

    missing = set(triage_index) - set(index)
    if missing:
        raise Stage3ContractError(
            "source audit omitted triage materials: " + ", ".join(sorted(missing))
        )

    for item_id, record in index.items():
        _require_unique(record["source_spans"], f"{item_id}.source_spans")
        for field in ("statement_source_locations", "proof_source_locations"):
            locations = record[field]
            _require_unique(
                [
                    (item["start_line"], item["end_line"], item["label"])
                    for item in locations
                ],
                f"{item_id}.{field}",
            )
            for location in locations:
                if location["end_line"] < location["start_line"]:
                    raise Stage3ContractError(
                        f"{item_id}.{field} has end_line before start_line"
                    )
        triage_item = triage_index.get(item_id)
        if triage_item is None:
            if not record["is_added"] or record["addition_reason"] is None:
                raise Stage3ContractError(
                    f"new material {item_id} requires is_added=true and addition_reason"
                )
        else:
            if record["is_added"] or record["addition_reason"] is not None:
                raise Stage3ContractError(
                    f"existing material {item_id} cannot be marked as added"
                )
            if (
                record["role"] != triage_item["role"]
                and "theory_candidate" in {record["role"], triage_item["role"]}
            ):
                raise Stage3ContractError(
                    f"source audit changed frozen candidate role of {item_id}: "
                    f"{triage_item['role']} -> {record['role']}"
                )

        role = record["role"]
        if role in RESULT_ROLES:
            if not record["statement_source_locations"]:
                raise Stage3ContractError(
                    f"{role} {item_id} requires a statement source location"
                )
            if not record["proof_source_locations"]:
                raise Stage3ContractError(
                    f"{role} {item_id} requires a proof source location"
                )
            for field in ("proof_reconstruction", "statement_status", "proof_status"):
                if record[field] is None:
                    raise Stage3ContractError(
                        f"{role} {item_id} requires non-null {field}"
                    )
            if record["external_classification"] is not None:
                raise Stage3ContractError(
                    f"non-external material {item_id} cannot have external_classification"
                )
            if record["statement_status"] == "minor_issue":
                if record["statement_repair"] is None:
                    raise Stage3ContractError(
                        f"minor statement issue for {item_id} requires statement_repair"
                    )
            elif record["statement_repair"] is not None:
                raise Stage3ContractError(
                    f"statement_repair for {item_id} requires minor_issue"
                )
            if record["proof_status"] == "minor_error":
                if record["proof_repair"] is None:
                    raise Stage3ContractError(
                        f"minor proof error for {item_id} requires proof_repair"
                    )
            elif record["proof_repair"] is not None:
                raise Stage3ContractError(
                    f"proof_repair for {item_id} requires minor_error"
                )
            if record["statement_status"] != "clean" and not record["statement_findings"]:
                raise Stage3ContractError(
                    f"non-clean statement for {item_id} requires a finding"
                )
            if record["proof_status"] != "clean" and not record["proof_findings"]:
                raise Stage3ContractError(
                    f"non-clean proof for {item_id} requires a finding"
                )
        else:
            if not record["statement_source_locations"]:
                raise Stage3ContractError(
                    f"{role} {item_id} requires a statement source location"
                )
            null_fields = (
                "proof_reconstruction",
                "statement_status",
                "statement_repair",
                "proof_status",
                "proof_repair",
            )
            if any(record[field] is not None for field in null_fields):
                raise Stage3ContractError(
                    f"{role} {item_id} cannot contain theorem audit fields"
                )
            if record["statement_findings"] or record["proof_findings"]:
                raise Stage3ContractError(
                    f"{role} {item_id} cannot contain theorem audit findings"
                )
            if role == "external":
                if record["external_classification"] is None:
                    raise Stage3ContractError(
                        f"external material {item_id} requires external_classification"
                    )
            elif record["external_classification"] is not None:
                raise Stage3ContractError(
                    f"definition {item_id} cannot have external_classification"
                )

    _validate_dependencies(index)
    return index


def validate_source_check(
    triage: dict[str, Any],
    previous_source_audit: dict[str, Any],
    source_check: dict[str, Any],
    allowed_material_ids: set[str],
) -> dict[str, dict[str, Any]]:
    validate_schema("source_check", source_check)
    affected = source_check["affected_material_ids"]
    _require_unique(affected, "source_check.affected_material_ids")
    if not set(affected) <= allowed_material_ids:
        raise Stage3ContractError(
            "source check affected material outside the selected closure"
        )
    updated = source_check["source_audit"]
    index = validate_source_audit(triage, updated)
    if source_check["status"] == "objection_rejected":
        if updated != previous_source_audit:
            raise Stage3ContractError(
                "objection_rejected must preserve the source audit"
            )
    elif source_check["status"] == "source_record_corrected":
        if updated == previous_source_audit:
            raise Stage3ContractError(
                "source_record_corrected must change the source audit"
            )
    else:
        if not any(
            index[item_id]["statement_status"] == "major_issue"
            or index[item_id]["proof_status"] == "major_gap"
            for item_id in affected
            if index[item_id]["role"] in RESULT_ROLES
        ):
            raise Stage3ContractError(
                "paper_issue_confirmed requires a major affected source record"
            )
    return index


def derive_analysis(
    triage: dict[str, Any],
    selection: dict[str, Any],
    source_audit: dict[str, Any],
) -> dict[str, Any]:
    validate_target_selection(triage, selection)
    index = validate_source_audit(triage, source_audit)

    effective_cache: dict[str, tuple[str, list[str]]] = {}

    def effective_proof_status(item_id: str) -> tuple[str, list[str]]:
        if item_id in effective_cache:
            return effective_cache[item_id]
        item = index[item_id]
        reported = item["proof_status"]
        failed_dependencies: list[str] = []
        for dependency_id in item["depends_on"]:
            dependency = index[dependency_id]
            if dependency["role"] not in RESULT_ROLES:
                continue
            dependency_effective, _ = effective_proof_status(dependency_id)
            if (
                dependency["statement_status"] == "major_issue"
                or dependency_effective == "major_gap"
            ):
                failed_dependencies.append(dependency_id)
        effective = "major_gap" if reported == "major_gap" or failed_dependencies else reported
        effective_cache[item_id] = (effective, sorted(failed_dependencies))
        return effective_cache[item_id]

    result_statuses = []
    combined_by_id: dict[str, str] = {}
    for item_id in sorted(index):
        item = index[item_id]
        if item["role"] not in RESULT_ROLES:
            continue
        effective, failed_dependencies = effective_proof_status(item_id)
        if item["statement_status"] == "major_issue" or effective == "major_gap":
            combined = "paper_issue_confirmed"
        elif (
            item["statement_status"] == "minor_issue"
            or effective == "minor_error"
        ):
            combined = "minor_source_issue_fixed"
        else:
            combined = "clean"
        combined_by_id[item_id] = combined
        result_statuses.append(
            {
                "item_id": item_id,
                "reported_proof_status": item["proof_status"],
                "effective_proof_status": effective,
                "combined_status": combined,
                "failed_dependencies": failed_dependencies,
            }
        )

    chain_index = {
        item["chain_id"]: item
        for item in selection["candidate_chain_evaluations"]
    }
    chain_gate_results = []
    final_chain_id: str | None = None
    final_candidate_ids: list[str] = []
    selected_material_ids: list[str] = []
    for chain_id in selection["ranked_chain_ids"]:
        evaluation = chain_index[chain_id]
        candidate_ids = list(evaluation["candidate_ids"])
        material_ids = sorted(dependency_closure(candidate_ids, index))
        blocking_ids = sorted(
            item_id
            for item_id in material_ids
            if combined_by_id.get(item_id) == "paper_issue_confirmed"
        )
        blocked = bool(blocking_ids)
        chain_gate_results.append(
            {
                "chain_id": chain_id,
                "candidate_ids": candidate_ids,
                "selected_material_ids": material_ids,
                "blocking_material_ids": blocking_ids,
                "blocked": blocked,
            }
        )
        if final_chain_id is None and not blocked:
            final_chain_id = chain_id
            final_candidate_ids = candidate_ids
            selected_material_ids = material_ids

    selected_target_blocked = final_chain_id is None
    paper_level_theory_issue = any(
        item["role"] == "theory_candidate"
        and combined_by_id.get(item_id) == "paper_issue_confirmed"
        for item_id, item in index.items()
    )

    return {
        "result_statuses": result_statuses,
        "paper_level_theory_issue": paper_level_theory_issue,
        "provisional_selected_chain_id": selection["selected_chain_id"],
        "ranked_chain_ids": list(selection["ranked_chain_ids"]),
        "chain_gate_results": chain_gate_results,
        "selected_chain_id": final_chain_id,
        "selected_candidate_ids": final_candidate_ids,
        "selected_material_ids": selected_material_ids,
        "fallback_used": (
            final_chain_id is not None
            and final_chain_id != selection["selected_chain_id"]
        ),
        "selected_target_blocked": selected_target_blocked,
        "status": "stopped" if selected_target_blocked else "proceed",
        "stop_reason": "paper_issue_confirmed" if selected_target_blocked else None,
    }


def assemble_paper_analysis(
    triage: dict[str, Any],
    selection: dict[str, Any],
    source_audit: dict[str, Any],
) -> dict[str, Any]:
    value = {
        "triage": deepcopy(triage),
        "target_selection": deepcopy(selection),
        "source_audit": deepcopy(source_audit),
        "derived": derive_analysis(triage, selection, source_audit),
    }
    validate_schema("paper_analysis", value)
    return value


def build_thread_b_view(paper_analysis: dict[str, Any]) -> dict[str, Any]:
    if paper_analysis["derived"]["selected_target_blocked"]:
        raise Stage3ContractError("blocked target cannot be exposed to Thread B")
    derived = paper_analysis["derived"]
    selected_ids = set(derived["selected_material_ids"])
    records = [
        deepcopy(item)
        for item in paper_analysis["source_audit"]["material_records"]
        if item["item_id"] in selected_ids
    ]
    statuses = [
        deepcopy(item)
        for item in paper_analysis["derived"]["result_statuses"]
        if item["item_id"] in selected_ids
    ]
    original_selection = paper_analysis["target_selection"]
    selected_chain_id = derived["selected_chain_id"]
    selected_evaluation = next(
        item
        for item in original_selection["candidate_chain_evaluations"]
        if item["chain_id"] == selected_chain_id
    )
    selected_candidates = set(derived["selected_candidate_ids"])
    omitted_reason_by_id = {
        item["item_id"]: item["reason"]
        for item in original_selection["omitted_candidates"]
    }
    all_candidates = {
        item["item_id"]
        for item in paper_analysis["triage"]["theory_inventory"]
        if item["role"] == "theory_candidate"
    }
    effective_selection = deepcopy(original_selection)
    effective_selection.update(
        {
            "formalization_target": selected_evaluation["scientific_claim"],
            "candidate_chain_evaluations": [deepcopy(selected_evaluation)],
            "ranked_chain_ids": [selected_chain_id],
            "selected_chain_id": selected_chain_id,
            "selected_candidate_ids": list(selected_evaluation["candidate_ids"]),
            "attached_material_ids": sorted(selected_ids - selected_candidates),
            "target_selection_reasoning": selected_evaluation[
                "contribution_fidelity"
            ]["reason"],
            "characteristic_bottleneck": selected_evaluation[
                "claimed_characteristic_bottleneck"
            ],
            "omitted_candidates": [
                {
                    "item_id": item_id,
                    "reason": omitted_reason_by_id.get(
                        item_id,
                        "Excluded by the deterministic post-audit fallback gate.",
                    ),
                }
                for item_id in sorted(all_candidates - selected_candidates)
            ],
            "selection_ambiguity": None,
        }
    )
    return {
        "paper_type": paper_analysis["triage"]["paper_type"],
        "theory_auxiliary_subtype": paper_analysis["triage"][
            "theory_auxiliary_subtype"
        ],
        "principal_contribution": paper_analysis["triage"]["principal_contribution"],
        "target_selection": effective_selection,
        "source_gate": {
            "provisional_selected_chain_id": derived[
                "provisional_selected_chain_id"
            ],
            "selected_chain_id": selected_chain_id,
            "fallback_used": derived["fallback_used"],
            "chain_gate_results": deepcopy(derived["chain_gate_results"]),
        },
        "selected_material_records": records,
        "selected_result_statuses": statuses,
    }


def validate_compile(value: dict[str, Any]) -> None:
    validate_schema("compile", value)
    if value["status"] != "formalized":
        return
    provenance = value["provenance"]
    clauses = provenance["public_clauses"]
    steps = provenance["private_proof_steps"]
    _require_unique(
        [item["clause_id"] for item in clauses],
        "provenance.public_clauses.clause_id",
    )
    _require_unique(
        [item["step_id"] for item in steps],
        "provenance.private_proof_steps.step_id",
    )
    for item in clauses:
        _require_unique(
            item["source_material_ids"],
            f"{item['clause_id']}.source_material_ids",
        )
    for item in steps:
        _require_unique(
            item["source_material_ids"],
            f"{item['step_id']}.source_material_ids",
        )
    target_count = sum(item["kind"] == "target" for item in clauses)
    if target_count not in {1, 2}:
        raise Stage3ContractError(
            "provenance must contain one or two public target clauses"
        )
    _require_unique(provenance["notation_map"], "provenance.notation_map")
    _require_unique(
        provenance["applied_source_repairs"],
        "provenance.applied_source_repairs",
    )


def expected_prc_level(
    effective_total: int, strategy: int, technical: int
) -> str:
    if effective_total <= 3:
        return "PRC0"
    if effective_total <= 6:
        return "PRC1"
    if effective_total <= 8:
        return "PRC2"
    if effective_total <= 10:
        return "PRC3"
    if strategy == 3 and technical == 3:
        return "PRC4"
    return "PRC3"


def validate_complexity(value: dict[str, Any]) -> None:
    validate_schema("complexity", value)
    dimensions = value["proof_reconstruction_complexity"]
    scores = {
        name: dimensions[name]["score"]
        for name in (
            "strategy_discovery",
            "subgoal_structure_dependency",
            "technical_reasoning_execution",
            "capability_integration",
        )
    }
    intrinsic = sum(scores.values())
    if dimensions["intrinsic_complexity_total"] != intrinsic:
        raise Stage3ContractError(
            "intrinsic_complexity_total must equal the four dimension scores"
        )

    exposure = value["proof_route_exposure"]
    level = exposure["level"]
    if level >= 2:
        if value["status"] != "formalization_revision_required":
            raise Stage3ContractError("E2/E3 requires formalization revision")
        if exposure["required_revision"] is None:
            raise Stage3ContractError("E2/E3 requires a concrete revision")
        for field in (
            "effective_complexity_total",
            "proof_reconstruction_complexity_level",
            "benchmark_suitability",
        ):
            if value[field] is not None:
                raise Stage3ContractError(f"{field} must be null for E2/E3")
        return

    if value["status"] != "scored":
        raise Stage3ContractError("E0/E1 requires scored status")
    if exposure["required_revision"] is not None:
        raise Stage3ContractError("E0/E1 cannot require formalization revision")
    effective = max(0, intrinsic - (1 if level == 1 else 0))
    if value["effective_complexity_total"] != effective:
        raise Stage3ContractError(
            "effective_complexity_total conflicts with exposure adjustment"
        )
    expected_level = expected_prc_level(
        effective,
        scores["strategy_discovery"],
        scores["technical_reasoning_execution"],
    )
    if value["proof_reconstruction_complexity_level"] != expected_level:
        raise Stage3ContractError(
            f"PRC level must be {expected_level} for the supplied scores"
        )
    suitability = {
        "PRC0": "reject",
        "PRC1": "baseline",
        "PRC2": "primary",
        "PRC3": "primary",
        "PRC4": "stress",
    }[expected_level]
    if value["benchmark_suitability"] != suitability:
        raise Stage3ContractError(
            "benchmark_suitability conflicts with PRC level"
        )


def _has_replacement(replacements: dict[str, Any] | None) -> bool:
    return replacements is not None and any(
        value is not None for value in replacements.values()
    )


def validate_artifact_audit(value: dict[str, Any]) -> None:
    validate_schema("artifact_audit", value)
    status = value["status"]
    if status == "pass":
        failed = [
            name for name, check in value["checks"].items()
            if check["status"] != "pass"
        ]
        if failed:
            raise Stage3ContractError(
                "passing artifact audit has failed checks: " + ", ".join(failed)
            )
    elif status == "corrected":
        if not _has_replacement(value["replacements"]):
            raise Stage3ContractError(
                "corrected artifact audit requires at least one replacement"
            )
        failed = [
            name for name, check in value["checks"].items()
            if check["status"] != "pass"
        ]
        if failed:
            raise Stage3ContractError(
                "corrected artifact audit has failed checks: " + ", ".join(failed)
            )


def validate_revision(value: dict[str, Any]) -> None:
    validate_schema("revision", value)
    if value["status"] in {"formalization_error_fixed", "scoring_error_fixed"}:
        if not _has_replacement(value["replacements"]):
            raise Stage3ContractError(
                "fixed revision requires at least one replacement"
            )
        failed = [
            name for name, check in value["self_audit"].items()
            if check["status"] != "pass"
        ]
        if failed:
            raise Stage3ContractError(
                "fixed revision has failed self-audit checks: " + ", ".join(failed)
            )


def apply_replacements(
    bundle: dict[str, Any], replacements: dict[str, Any] | None
) -> dict[str, Any]:
    updated = deepcopy(bundle)
    if replacements is None:
        return updated
    for field, value in replacements.items():
        if value is not None:
            updated[field] = deepcopy(value)
    validate_compile(updated)
    return updated
