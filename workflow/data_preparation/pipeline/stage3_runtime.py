from __future__ import annotations

import importlib
import os
import sys
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PREPARATION = SCRIPT_DIR.parent
WORKFLOW_ROOT = DATA_PREPARATION.parent
FORMALIZATION_SUPPORT = WORKFLOW_ROOT / "runtime_support/formalization"
CODEX_SUPPORT = WORKFLOW_ROOT / "runtime_support/codex"
for path in (FORMALIZATION_SUPPORT, CODEX_SUPPORT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from agent_backend import AgentRequest  # noqa: E402
from stage3_contracts import (  # noqa: E402
    load_schema,
    validate_artifact_audit,
    validate_compile,
    validate_complexity,
    validate_revision,
    validate_source_check,
    validate_source_audit,
    validate_target_selection,
    validate_triage,
    validate_triage_audit,
)


LOCAL_CONTRACT_SCHEMAS = {
    "stage3_triage": load_schema("triage"),
    "stage3_triage_audit": load_schema("triage_audit"),
    "stage3_target_selection": load_schema("target_selection"),
    "stage3_source_audit": load_schema("source_audit"),
    "stage3_source_check": load_schema("source_check"),
    "stage3_compile": load_schema("compile"),
    "stage3_artifact_audit": load_schema("artifact_audit"),
    "stage3_complexity": load_schema("complexity"),
    "stage3_revision": load_schema("revision"),
}


def _transport_schema_sources() -> dict[str, dict[str, Any]]:
    """Expand structured nested objects required by the strict API subset."""
    schemas = deepcopy(LOCAL_CONTRACT_SCHEMAS)
    compile_defs = schemas["stage3_compile"]["$defs"]
    for contract in ("stage3_artifact_audit", "stage3_revision"):
        schema = schemas[contract]
        # Provenance refers to the compile contract's clause, proof-step, and
        # notation definitions. Copy the complete definition closure so the
        # transport schema never contains dangling local references.
        schema["$defs"].update(deepcopy(compile_defs))
        schema["$defs"]["replacements"]["properties"]["provenance"] = {
            "anyOf": [
                {"type": "null"},
                {"$ref": "#/$defs/provenance"},
            ]
        }

    triage = schemas["stage3_triage"]
    triage_audit = schemas["stage3_triage_audit"]
    triage_audit["$defs"].update(deepcopy(triage["$defs"]))
    triage_audit["$defs"]["effective_triage"] = {
        key: deepcopy(value)
        for key, value in triage.items()
        if key not in {"$schema", "title", "$defs"}
    }
    triage_audit["properties"]["effective_triage"] = {
        "$ref": "#/$defs/effective_triage"
    }

    source_audit = schemas["stage3_source_audit"]
    base_record = source_audit["$defs"]["material_record"]
    result_record = deepcopy(base_record)
    result_record["properties"]["role"] = {
        "type": "string",
        "enum": ["theory_candidate", "internal_support"],
    }
    result_record["properties"]["proof_reconstruction"] = {
        "type": "string",
        "minLength": 1,
    }
    result_record["properties"]["statement_status"] = {
        "type": "string",
        "enum": ["clean", "minor_issue", "major_issue"],
    }
    result_record["properties"]["proof_status"] = {
        "type": "string",
        "enum": ["clean", "minor_error", "major_gap"],
    }
    result_record["properties"]["external_classification"] = {"type": "null"}
    for field in ("statement_source_locations", "proof_source_locations"):
        result_record["properties"][field]["minItems"] = 1

    definition_record = deepcopy(base_record)
    definition_record["properties"]["role"] = {
        "type": "string",
        "enum": ["definition"],
    }
    external_record = deepcopy(base_record)
    external_record["properties"]["role"] = {
        "type": "string",
        "enum": ["external"],
    }
    for record in (definition_record, external_record):
        for field in (
            "proof_reconstruction",
            "statement_status",
            "statement_repair",
            "proof_status",
            "proof_repair",
        ):
            record["properties"][field] = {"type": "null"}
        for field in ("statement_findings", "proof_findings"):
            record["properties"][field]["maxItems"] = 0
        record["properties"]["statement_source_locations"]["minItems"] = 1
        record["properties"]["proof_source_locations"]["maxItems"] = 0
    definition_record["properties"]["external_classification"] = {"type": "null"}
    external_record["properties"]["external_classification"] = {
        "type": "string",
        "enum": ["standard_independent", "nonstandard_dependency"],
    }

    source_audit["$defs"].update(
        {
            "result_material_record": result_record,
            "definition_material_record": definition_record,
            "external_material_record": external_record,
        }
    )
    source_audit["properties"]["material_records"]["items"] = {
        "anyOf": [
            {"$ref": "#/$defs/result_material_record"},
            {"$ref": "#/$defs/definition_material_record"},
            {"$ref": "#/$defs/external_material_record"},
        ]
    }

    source_check = schemas["stage3_source_check"]
    source_check["$defs"] = deepcopy(source_audit["$defs"])
    source_check["$defs"]["source_audit_payload"] = {
        key: deepcopy(value)
        for key, value in source_audit.items()
        if key not in {"$schema", "title", "$defs"}
    }
    source_check["properties"]["source_audit"] = {
        "$ref": "#/$defs/source_audit_payload"
    }
    return schemas


def _api_compatible_schema(value: Any) -> Any:
    """Remove constraints unsupported by the relay's Responses schema subset.

    The complete local schemas are still applied after every response, so this only
    relaxes transport-time validation and does not relax the pipeline contract.
    """
    if isinstance(value, dict):
        result = {
            key: _api_compatible_schema(item)
            for key, item in value.items()
            if key not in {"allOf", "uniqueItems", "minProperties"}
        }
        if "const" in result and "type" not in result:
            constant = result["const"]
            result["type"] = (
                "boolean"
                if isinstance(constant, bool)
                else "integer"
                if isinstance(constant, int)
                else "number"
                if isinstance(constant, float)
                else "string"
                if isinstance(constant, str)
                else "null"
                if constant is None
                else "object"
            )
        return result
    if isinstance(value, list):
        return [_api_compatible_schema(item) for item in value]
    return value


CONTRACT_SCHEMAS = {
    name: _api_compatible_schema(deepcopy(schema))
    for name, schema in _transport_schema_sources().items()
}


PHASE_TASKS = {
    "stage3_triage": (
        "Analyze the complete inline paper source under the Stage 3 triage "
        "instructions. Build the shallow theory inventory and return only the "
        "triage record. Do not call tools."
    ),
    "stage3_triage_audit": (
        "Independently audit the supplied filtered triage record against the "
        "complete inline paper source. Return the effective triage record and "
        "audit checks. Do not call tools."
    ),
    "stage3_target_selection": (
        "Using the triage result from the preceding turn, perform only the "
        "correctness-blind flagship target selection. Do not call tools."
    ),
    "stage3_source_audit": (
        "With the flagship target frozen, recover and audit the paper's theory "
        "materials under the source-audit instructions. Return the complete "
        "source-audit record. Do not call tools."
    ),
    "stage3_local_source_check": (
        "Adjudicate the downstream objection in the current Thread B session "
        "using only the supplied source-audit records and exact local source "
        "excerpts. Return a complete source-check result. Do not call tools."
    ),
    "stage3_compile": (
        "Compile the supplied frozen source-audited flagship view into one "
        "source-blind benchmark task, reference proof, rubric, and provenance. "
        "Do not call tools."
    ),
    "stage3_artifact_audit": (
        "Audit the formalization bundle returned in the preceding turn. Correct "
        "only formalization defects and return null for unchanged replacement "
        "fields. Do not call tools."
    ),
    "stage3_complexity": (
        "Assess the proof-reconstruction complexity and proof-route exposure of "
        "the audited solver-visible task before any solver run. Do not call tools."
    ),
    "stage3_revision": (
        "Classify and address the supplied solver, reviewer, evaluator, or "
        "deterministic-validation objection using the current source-blind "
        "formalization thread. Do not call tools."
    ),
}


def _normalize_target_chain_ids(payload: dict[str, Any]) -> None:
    """Canonicalize chain IDs and deterministically order scored eligible chains."""
    evaluations = payload.get("candidate_chain_evaluations")
    if not isinstance(evaluations, list):
        return
    original_to_canonical: dict[str, str] = {}
    selected_ids = payload.get("selected_candidate_ids")
    selected_index: int | None = None
    if payload.get("status") == "selected" and isinstance(selected_ids, list):
        matches = [
            index
            for index, evaluation in enumerate(evaluations)
            if isinstance(evaluation, dict)
            and set(evaluation.get("candidate_ids", [])) == set(selected_ids)
        ]
        if len(matches) == 1:
            selected_index = matches[0]
    for index, evaluation in enumerate(evaluations, start=1):
        if isinstance(evaluation, dict):
            canonical = f"chain_{index:03d}"
            original = evaluation.get("chain_id")
            if isinstance(original, str):
                original_to_canonical.setdefault(original, canonical)
            evaluation["chain_id"] = canonical
    ranked_ids = payload.get("ranked_chain_ids")
    if isinstance(ranked_ids, list):
        payload["ranked_chain_ids"] = [
            original_to_canonical.get(chain_id, chain_id)
            for chain_id in ranked_ids
        ]
    if payload.get("status") == "selected" and selected_index is not None:
        payload["selected_chain_id"] = f"chain_{selected_index + 1:03d}"
    eligible: list[dict[str, Any]] = []
    for evaluation in evaluations:
        if not isinstance(evaluation, dict):
            return
        contribution = evaluation.get("contribution_fidelity")
        difficulty = evaluation.get("difficulty_fidelity")
        candidates = evaluation.get("candidate_ids")
        if not (
            isinstance(contribution, dict)
            and isinstance(contribution.get("total"), int)
            and isinstance(candidates, list)
        ):
            return
        if contribution["total"] < 8:
            continue
        if not isinstance(difficulty, dict) or not isinstance(
            difficulty.get("total"), int
        ):
            return
        eligible.append(evaluation)
    if payload.get("status") != "selected" or not eligible:
        return
    ranked = sorted(
        eligible,
        key=lambda item: (
            -item["contribution_fidelity"]["total"],
            -item["difficulty_fidelity"]["total"],
            -len(item["candidate_ids"]),
            item["chain_id"],
        ),
    )
    payload["ranked_chain_ids"] = [item["chain_id"] for item in ranked]
    if isinstance(selected_ids, list) and set(ranked[0]["candidate_ids"]) == set(
        selected_ids
    ):
        payload["selected_chain_id"] = ranked[0]["chain_id"]


def _normalize_target_attached_materials(
    payload: dict[str, Any], triage: dict[str, Any]
) -> None:
    """Add non-candidate dependencies already declared by Turn A1."""
    if payload.get("status") != "selected":
        return
    inventory = triage.get("theory_inventory")
    selected_ids = payload.get("selected_candidate_ids")
    attached_ids = payload.get("attached_material_ids")
    if not (
        isinstance(inventory, list)
        and isinstance(selected_ids, list)
        and isinstance(attached_ids, list)
    ):
        return
    index = {
        item["item_id"]: item
        for item in inventory
        if isinstance(item, dict) and isinstance(item.get("item_id"), str)
    }
    closure: set[str] = set()
    pending = list(selected_ids)
    while pending:
        item_id = pending.pop()
        if item_id in closure or item_id not in index:
            continue
        closure.add(item_id)
        dependencies = index[item_id].get("depends_on")
        if isinstance(dependencies, list):
            pending.extend(
                dependency
                for dependency in dependencies
                if isinstance(dependency, str)
            )
    attached = set(attached_ids)
    attached.update(
        item_id
        for item_id in closure
        if item_id not in selected_ids
        and index[item_id].get("role") != "theory_candidate"
    )
    payload["attached_material_ids"] = sorted(attached)


def _normalize_target_omitted_candidates(
    payload: dict[str, Any], triage: dict[str, Any]
) -> None:
    """Make the exhaustive omitted-candidate ledger deterministic."""
    inventory = triage.get("theory_inventory")
    selected_ids = payload.get("selected_candidate_ids")
    omitted = payload.get("omitted_candidates")
    if not (
        isinstance(inventory, list)
        and isinstance(selected_ids, list)
        and isinstance(omitted, list)
    ):
        return
    candidate_ids = [
        item.get("item_id")
        for item in inventory
        if isinstance(item, dict)
        and item.get("role") == "theory_candidate"
        and isinstance(item.get("item_id"), str)
    ]
    selected = {item_id for item_id in selected_ids if isinstance(item_id, str)}
    reasons = {
        item.get("item_id"): item.get("reason")
        for item in omitted
        if isinstance(item, dict)
        and isinstance(item.get("item_id"), str)
        and isinstance(item.get("reason"), str)
        and item.get("reason")
    }
    payload["omitted_candidates"] = [
        {
            "item_id": item_id,
            "reason": reasons.get(
                item_id,
                "Not included in the selected flagship chain.",
            ),
        }
        for item_id in candidate_ids
        if item_id not in selected
    ]


def _normalize_triage_audit_protocol(
    payload: dict[str, Any], original: dict[str, Any]
) -> None:
    """A confirmation cannot rewrite the triage record it confirms."""
    if payload.get("status") == "confirmed_filtered_out":
        payload["effective_triage"] = deepcopy(original)


def _normalize_artifact_audit_protocol(payload: dict[str, Any]) -> None:
    """Treat an all-pass audit with no actual replacement as a pass."""
    if payload.get("status") != "corrected":
        return
    replacements = payload.get("replacements")
    has_replacement = isinstance(replacements, dict) and any(
        value is not None for value in replacements.values()
    )
    checks = payload.get("checks")
    all_pass = isinstance(checks, dict) and all(
        isinstance(check, dict) and check.get("status") == "pass"
        for check in checks.values()
    )
    if not has_replacement and all_pass:
        payload["status"] = "pass"
        payload["objection"] = None
        payload["replacements"] = None


def _remove_impossible_dependency_edges(items: list[Any]) -> None:
    index = {
        item["item_id"]: item
        for item in items
        if isinstance(item, dict) and isinstance(item.get("item_id"), str)
    }
    accepted: dict[str, list[str]] = {item_id: [] for item_id in index}

    def reaches(start: str, target: str) -> bool:
        pending = [start]
        visited: set[str] = set()
        while pending:
            current = pending.pop()
            if current == target:
                return True
            if current in visited:
                continue
            visited.add(current)
            pending.extend(accepted.get(current, []))
        return False

    for item in items:
        if not isinstance(item, dict) or item.get("item_id") not in index:
            continue
        item_id = item["item_id"]
        cleaned: list[str] = []
        for dependency in item.get("depends_on", []):
            if (
                dependency not in index
                or dependency == item_id
                or dependency in cleaned
            ):
                continue
            if dependency in index and reaches(dependency, item_id):
                continue
            cleaned.append(dependency)
        item["depends_on"] = cleaned
        accepted[item_id] = cleaned


def _normalize_triage_material_ids(payload: dict[str, Any]) -> None:
    """Canonicalize material IDs and remove impossible protocol-only edges."""
    inventory = payload.get("theory_inventory")
    if not isinstance(inventory, list):
        return
    first_mapping: dict[str, str] = {}
    for index, item in enumerate(inventory, start=1):
        if not isinstance(item, dict):
            continue
        canonical = f"theory_{index:03d}"
        original = item.get("item_id")
        if isinstance(original, str):
            first_mapping.setdefault(original, canonical)
        item["item_id"] = canonical
    for item in inventory:
        if not isinstance(item, dict) or not isinstance(item.get("depends_on"), list):
            continue
        item["depends_on"] = [
            first_mapping.get(dependency, dependency)
            for dependency in item["depends_on"]
        ]
    _remove_impossible_dependency_edges(inventory)


def _normalize_source_audit_protocol(
    payload: dict[str, Any], triage: dict[str, Any]
) -> None:
    """Normalize bookkeeping fields without changing mathematical audit content."""
    records = payload.get("material_records")
    inventory = triage.get("theory_inventory")
    if not isinstance(records, list) or not isinstance(inventory, list):
        return
    inventoried_ids = {
        item.get("item_id") for item in inventory if isinstance(item, dict)
    }
    for record in records:
        if not isinstance(record, dict):
            continue
        for field in ("statement_source_locations", "proof_source_locations"):
            locations = record.get(field)
            if not isinstance(locations, list):
                continue
            for location in locations:
                if not isinstance(location, dict):
                    continue
                start = location.get("start_line")
                end = location.get("end_line")
                if isinstance(start, int) and isinstance(end, int) and end < start:
                    location["start_line"], location["end_line"] = end, start
        if record.get("statement_status") != "minor_issue":
            record["statement_repair"] = None
        if record.get("proof_status") != "minor_error":
            record["proof_repair"] = None
        if record.get("item_id") in inventoried_ids:
            record["is_added"] = False
            record["addition_reason"] = None
        else:
            record["is_added"] = True
            if not record.get("addition_reason"):
                record["addition_reason"] = (
                    "Added during source audit to complete the recovered material closure."
                )
    _remove_impossible_dependency_edges(records)


def _promote_unrepaired_minor_findings(payload: dict[str, Any]) -> bool:
    """Conservatively close irrecoverable minor-repair contract failures."""
    records = payload.get("material_records")
    if not isinstance(records, list):
        return False
    changed = False
    for record in records:
        if not isinstance(record, dict):
            continue
        if (
            record.get("statement_status") == "minor_issue"
            and record.get("statement_repair") is None
        ):
            record["statement_status"] = "major_issue"
            findings = record.get("statement_findings")
            if isinstance(findings, list):
                findings.append(
                    "No complete source-grounded statement repair was supplied."
                )
            changed = True
        if (
            record.get("proof_status") == "minor_error"
            and record.get("proof_repair") is None
        ):
            record["proof_status"] = "major_gap"
            findings = record.get("proof_findings")
            if isinstance(findings, list):
                findings.append(
                    "No complete source-grounded proof repair was supplied."
                )
            changed = True
    return changed


def _normalize_source_check_protocol(
    payload: dict[str, Any], previous_source_audit: dict[str, Any]
) -> None:
    """Limit a local source check to its declared existing material records."""
    if payload.get("status") == "objection_rejected":
        payload["source_audit"] = deepcopy(previous_source_audit)
        return
    source_audit = payload.get("source_audit")
    records = (
        source_audit.get("material_records")
        if isinstance(source_audit, dict)
        else None
    )
    previous_records = previous_source_audit.get("material_records")
    affected = payload.get("affected_material_ids")
    if not (
        isinstance(records, list)
        and isinstance(previous_records, list)
        and isinstance(affected, list)
    ):
        return
    affected_ids = {item for item in affected if isinstance(item, str)}
    proposed = {
        item.get("item_id"): item
        for item in records
        if isinstance(item, dict) and isinstance(item.get("item_id"), str)
    }
    merged: list[dict[str, Any]] = []
    for previous in previous_records:
        if not isinstance(previous, dict):
            continue
        item_id = previous.get("item_id")
        replacement = proposed.get(item_id)
        if item_id not in affected_ids or not isinstance(replacement, dict):
            merged.append(deepcopy(previous))
            continue
        if replacement.get("role") != previous.get("role"):
            merged.append(deepcopy(previous))
            continue
        normalized = deepcopy(replacement)
        for field in ("item_id", "role", "is_added", "addition_reason"):
            normalized[field] = deepcopy(previous.get(field))
        merged.append(normalized)
    source_audit["status"] = previous_source_audit.get("status", "audited")
    source_audit["material_records"] = merged


def _normalize_nonresult_source_fields(payload: dict[str, Any]) -> None:
    """Clear theorem-only protocol fields on definitions and externals."""
    records = payload.get("material_records")
    if not isinstance(records, list):
        return
    for record in records:
        if not isinstance(record, dict) or record.get("role") not in {
            "definition",
            "external",
        }:
            continue
        for field in (
            "proof_reconstruction",
            "statement_status",
            "statement_repair",
            "proof_status",
            "proof_repair",
        ):
            record[field] = None
        record["statement_findings"] = []
        record["proof_findings"] = []
        if record["role"] == "definition":
            record["external_classification"] = None


def _contract_recovery_instruction(contract: str) -> str:
    base = (
        "Return a complete corrected replacement for the most recent JSON "
        "response. Preserve the substantive analysis and change only what is "
        "required to satisfy the deterministic validation error."
    )
    if contract == "stage3_artifact_audit":
        return (
            base
            + " Return corrected only if the supplied replacements resolve every "
            "finding and every check is pass. If material uncertainty remains, "
            "return source_check_required with "
            "null replacements and a concrete objection."
        )
    if contract == "stage3_source_audit":
        return (
            base
            + " For theory_candidate and internal_support records, supply the "
            "theorem statement, proof, status, finding, and repair fields required "
            "by the schema. For definition and external records, set all theorem "
            "audit and repair fields to null and both finding arrays to empty. Set "
            "external_classification only for external records."
        )
    if contract == "stage3_source_check":
        return (
            base
            + " Preserve the complete record, item ID, role, order, and added "
            "metadata of every material outside affected_material_ids. Do not "
            "change the role of an affected material. A minor_issue requires a "
            "complete statement_repair, and a minor_error requires a complete "
            "proof_repair. If the objection is rejected, return the prior source "
            "audit unchanged."
        )
    if contract == "stage3_revision":
        return (
            base
            + " Return a fixed status only if the replacements resolve the "
            "objection and every self-audit check is pass; otherwise use "
            "source_check_required or invalid_objection as appropriate."
        )
    if contract == "stage3_complexity":
        return (
            base
            + " Recompute all four intrinsic dimensions, their exact sum, the "
            "exposure adjustment, PRC level, and suitability. For E2 or E3, use "
            "formalization_revision_required and leave all final score fields null."
        )
    return base


class Stage3CodexBackend:
    def __init__(self, profile_dir: Path | None = None) -> None:
        pipeline_contracts = importlib.import_module("pipeline_contracts")
        codex_adapter = importlib.import_module("codex_adapter")
        pipeline_contracts.CONTRACTS.update(CONTRACT_SCHEMAS)
        codex_adapter.PHASE_TASKS.update(PHASE_TASKS)
        self._adapter = codex_adapter.CodexAPIAdapter(profile_dir=profile_dir)

    @staticmethod
    def _validate_payload(request: AgentRequest, payload: dict[str, Any]) -> None:
        contract = str(request.context["output_contract"])
        if contract == "stage3_triage":
            validate_triage(payload)
        elif contract == "stage3_target_selection":
            validate_target_selection(
                request.context["effective_triage"], payload
            )
        elif contract == "stage3_source_audit":
            validate_source_audit(
                request.context["effective_triage"], payload
            )
        elif contract == "stage3_source_check":
            validate_source_check(
                request.context["effective_triage"],
                request.context["current_source_audit"],
                payload,
                set(request.context["allowed_material_ids"]),
            )
        elif contract == "stage3_compile":
            validate_compile(payload)
        elif contract == "stage3_artifact_audit":
            validate_artifact_audit(payload)
            if (
                request.context.get("source_check_already_used")
                and payload.get("status") == "source_check_required"
            ):
                raise ValueError(
                    "the one permitted local source check has already been used; "
                    "resolve from the adjudicated source record"
                )
        elif contract == "stage3_complexity":
            validate_complexity(payload)
        elif contract == "stage3_revision":
            validate_revision(payload)
            if (
                request.context.get("source_check_already_used")
                and payload.get("status") == "source_check_required"
            ):
                raise ValueError(
                    "the one permitted local source check has already been used; "
                    "resolve from the adjudicated source record"
                )
        elif contract == "stage3_triage_audit":
            validate_triage_audit(request.context["triage_to_audit"], payload)
        else:
            raise ValueError(f"unknown Stage 3 contract: {contract}")

    async def run(self, request: AgentRequest) -> dict[str, Any]:
        current_request = request
        attempt_records: list[tuple[AgentRequest, dict[str, Any]]] = []
        last_error: Exception | None = None
        for local_attempt in range(3):
            result = await self._adapter.run(current_request)
            attempt_records.append((current_request, result))
            contract = str(current_request.context["output_contract"])
            if contract == "stage3_triage":
                _normalize_triage_material_ids(result["payload"])
            elif contract == "stage3_triage_audit":
                effective = result["payload"].get("effective_triage")
                if isinstance(effective, dict):
                    _normalize_triage_material_ids(effective)
                _normalize_triage_audit_protocol(
                    result["payload"], current_request.context["triage_to_audit"]
                )
            elif contract == "stage3_target_selection":
                _normalize_target_chain_ids(result["payload"])
                _normalize_target_attached_materials(
                    result["payload"], current_request.context["effective_triage"]
                )
                _normalize_target_omitted_candidates(
                    result["payload"], current_request.context["effective_triage"]
                )
            elif contract == "stage3_source_audit":
                _normalize_nonresult_source_fields(result["payload"])
                _normalize_source_audit_protocol(
                    result["payload"], current_request.context["effective_triage"]
                )
            elif contract == "stage3_source_check":
                _normalize_source_check_protocol(
                    result["payload"],
                    current_request.context["current_source_audit"],
                )
                source_audit = result["payload"].get("source_audit")
                if isinstance(source_audit, dict):
                    _normalize_nonresult_source_fields(source_audit)
                    _normalize_source_audit_protocol(
                        source_audit,
                        current_request.context["effective_triage"],
                    )
            elif contract == "stage3_artifact_audit":
                _normalize_artifact_audit_protocol(result["payload"])
            try:
                self._validate_payload(current_request, result["payload"])
            except Exception as error:
                last_error = error
                if local_attempt == 2:
                    if (
                        contract == "stage3_source_audit"
                        and _promote_unrepaired_minor_findings(result["payload"])
                    ):
                        self._validate_payload(current_request, result["payload"])
                        result["_stage3_attempt_records"] = attempt_records
                        return result
                    break
                recovery_context = {
                    key: request.context[key]
                    for key in (
                        "effective_triage",
                        "triage_to_audit",
                        "current_source_audit",
                        "allowed_material_ids",
                        "source_check_already_used",
                    )
                    if key in request.context
                }
                current_request = replace(
                    request,
                    resume_session_id=result["session_id"],
                    context={
                        **recovery_context,
                        "output_contract": contract,
                        "inline_no_tools": True,
                        "contract_recovery_turn": True,
                        "deterministic_validation_error": str(error),
                        "recovery_instruction": _contract_recovery_instruction(
                            contract
                        ),
                    },
                    max_retries=0,
                )
                continue
            result["_stage3_attempt_records"] = attempt_records
            return result
        assert last_error is not None
        raise last_error

    async def aclose(self) -> None:
        await self._adapter.aclose()


def configure_model(model: str, reasoning_effort: str) -> None:
    os.environ["ML_THEORY_CODEX_MODEL"] = model
    os.environ["ML_THEORY_CODEX_REASONING_EFFORT"] = reasoning_effort


__all__ = ["AgentRequest", "Stage3CodexBackend", "configure_model"]
