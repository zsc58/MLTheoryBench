from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent
SCHEMA_DIR = ROOT / "schemas"


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


_BUNDLE_SCHEMA = load_schema("formalization_bundle.schema.json")
_DRAFT_SCHEMA = load_schema("formalization_draft.schema.json")
_AUDIT_SCHEMA = load_schema("formalization_audit.schema.json")
_DRAFT_SCHEMA["properties"]["analysis"] = _BUNDLE_SCHEMA["properties"]["analysis"]
_PROVENANCE_SCHEMA = _BUNDLE_SCHEMA["properties"]["files"]["oneOf"][1]["properties"]["provenance"]
_DRAFT_SCHEMA["properties"]["provenance"] = {
    "anyOf": [{"type": "null"}, _PROVENANCE_SCHEMA]
}
_AUDIT_SCHEMA["properties"]["self_audit"] = _BUNDLE_SCHEMA["properties"]["self_audit"]
_AUDIT_SCHEMA["properties"]["analysis"] = {
    "anyOf": [{"type": "null"}, _BUNDLE_SCHEMA["properties"]["analysis"]]
}
_AUDIT_SCHEMA["properties"]["provenance"] = {
    "anyOf": [{"type": "null"}, _PROVENANCE_SCHEMA]
}
_AUDIT_SCHEMA["$defs"] = _BUNDLE_SCHEMA["$defs"]

_TRIAGE_SCHEMA = deepcopy(_DRAFT_SCHEMA)
_TRIAGE_SCHEMA["title"] = "Inline Paper Triage Result"
_TRIAGE_SCHEMA["properties"]["status"]["enum"] = ["proceed", "filtered_out"]
_TRIAGE_SCHEMA["properties"]["stop_reason"]["enum"] = [
    None,
    "paper_not_theory_core",
    "paper_too_weak",
]
for _field in (
    "task_md",
    "proof_ground_truth_md",
    "rubric_md",
    "provenance",
):
    _TRIAGE_SCHEMA["properties"][_field] = {"type": "null"}
for _field in (
    "difficulty",
    "proof_difficulty_level",
    "benchmark_suitability",
    "difficulty_fidelity",
):
    _TRIAGE_SCHEMA["properties"]["analysis"]["properties"][_field] = {
        "type": "null"
    }

_TRIAGE_AUDIT_SCHEMA = deepcopy(_AUDIT_SCHEMA)
_TRIAGE_AUDIT_SCHEMA["title"] = "Inline Paper Triage Audit"
_TRIAGE_AUDIT_SCHEMA["properties"]["status"]["enum"] = ["filtered_out"]
_TRIAGE_AUDIT_SCHEMA["properties"]["stop_reason"] = {
    "type": "string",
    "enum": ["paper_not_theory_core", "paper_too_weak"],
}

_FORMALIZATION_AUDIT_SCHEMA = deepcopy(_AUDIT_SCHEMA)
_FORMALIZATION_AUDIT_SCHEMA["properties"]["status"]["enum"] = [
    "formalized",
    "stopped",
]

CONTRACTS = {
    "v2_formalization_bundle": _BUNDLE_SCHEMA,
    "v2_formalization_result": load_schema("formalization_result.schema.json"),
    "v2_formalization_draft": _DRAFT_SCHEMA,
    "v2_formalization_audit": _FORMALIZATION_AUDIT_SCHEMA,
    "v2_triage_result": _TRIAGE_SCHEMA,
    "v2_triage_audit": _TRIAGE_AUDIT_SCHEMA,
}


def expected_source_status(source_audit: dict[str, Any]) -> str:
    if (
        source_audit["statement_status"] == "major_issue"
        or source_audit["proof_status"] == "major_gap"
    ):
        return "paper_issue_suspected"
    if (
        source_audit["statement_status"] == "minor_issue"
        or source_audit["proof_status"] == "minor_error"
    ):
        return "minor_source_issue_fixed"
    return "clean"


ADMITTED_AUXILIARY_SUBTYPE = {
    "representative": True,
    "complete_closure": True,
    "generic": False,
}


def normalize_contract_payload(name: str, value: Any) -> Any:
    """Derive protocol-only triage fields from the model's substantive decision."""
    if name != "v2_triage_result" or not isinstance(value, dict):
        return value
    analysis = value.get("analysis")
    if not isinstance(analysis, dict):
        return value

    paper_type = analysis.get("paper_type")
    if paper_type == "empirical_or_method_only":
        value["status"] = "filtered_out"
        value["stop_reason"] = "paper_not_theory_core"
    elif paper_type == "theory_core":
        value["status"] = "proceed"
        value["stop_reason"] = None
    elif paper_type == "theory_auxiliary":
        if analysis.get("theory_auxiliary_subtype") == ADMITTED_AUXILIARY_SUBTYPE:
            value["status"] = "proceed"
            value["stop_reason"] = None
        else:
            value["status"] = "filtered_out"
            value["stop_reason"] = "paper_too_weak"
    return value


def filtered_reason(analysis: dict[str, Any]) -> str | None:
    """Return the unique filtered-out reason, if the analysis is rejectable."""
    paper_type = analysis.get("paper_type")
    if paper_type == "empirical_or_method_only":
        return "paper_not_theory_core"
    if (
        paper_type == "theory_auxiliary"
        and analysis.get("theory_auxiliary_subtype")
        != ADMITTED_AUXILIARY_SUBTYPE
    ):
        return "paper_too_weak"
    return None


def validate_auxiliary_subtype(analysis: dict[str, Any]) -> None:
    paper_type = analysis["paper_type"]
    subtype = analysis["theory_auxiliary_subtype"]
    if paper_type == "theory_auxiliary":
        if subtype is None:
            raise ValueError(
                "theory_auxiliary requires theory_auxiliary_subtype"
            )
    elif subtype is not None:
        raise ValueError(
            "theory_auxiliary_subtype must be null unless paper_type is "
            "theory_auxiliary"
        )


def validate_contract(name: str, value: Any) -> dict[str, Any]:
    schema = CONTRACTS[name]
    errors = sorted(
        Draft202012Validator(schema).iter_errors(value),
        key=lambda error: list(error.absolute_path),
    )
    if errors:
        rendered = []
        for error in errors[:10]:
            location = ".".join(str(item) for item in error.absolute_path) or "$"
            rendered.append(f"{location}: {error.message}")
        raise ValueError(f"invalid {name}: " + "; ".join(rendered))

    analysis = value.get("analysis") if isinstance(value, dict) else None
    if isinstance(analysis, dict):
        validate_auxiliary_subtype(analysis)

    if name == "v2_triage_result":
        status = value["status"]
        analysis = value["analysis"]
        paper_type = analysis["paper_type"]
        stop_reason = value["stop_reason"]
        expected_reason = {
            "empirical_or_method_only": "paper_not_theory_core",
            "theory_auxiliary": "paper_too_weak",
        }.get(paper_type)
        if status == "proceed":
            if paper_type == "empirical_or_method_only":
                raise ValueError("empirical_or_method_only cannot proceed")
            if (
                paper_type == "theory_auxiliary"
                and analysis["theory_auxiliary_subtype"]
                != ADMITTED_AUXILIARY_SUBTYPE
            ):
                raise ValueError(
                    "theory_auxiliary can proceed only with representative=true, "
                    "complete_closure=true, and generic=false"
                )
            if stop_reason is not None:
                raise ValueError("proceed requires null stop_reason")
        else:
            if expected_reason is None:
                raise ValueError("theory_core cannot use filtered_out")
            if stop_reason != expected_reason:
                raise ValueError(
                    f"{paper_type} requires stop_reason {expected_reason}"
                )
            if (
                paper_type == "theory_auxiliary"
                and analysis["theory_auxiliary_subtype"]
                == ADMITTED_AUXILIARY_SUBTYPE
            ):
                raise ValueError(
                    "admitted theory_auxiliary cannot be filtered_out"
                )
        if any(
            value[field] is not None
            for field in (
                "task_md",
                "proof_ground_truth_md",
                "rubric_md",
                "provenance",
            )
        ):
            raise ValueError("triage must not contain formalization files")
        if any(
            analysis[field] is not None
            for field in (
                "difficulty",
                "proof_difficulty_level",
                "benchmark_suitability",
                "difficulty_fidelity",
            )
        ):
            raise ValueError("triage requires null difficulty and suitability fields")

    if name == "v2_formalization_bundle":
        status = value["status"]
        analysis = value["analysis"]
        paper_type = analysis["paper_type"]
        suitability = analysis["benchmark_suitability"]
        difficulty = analysis["difficulty"]
        difficulty_level = analysis["proof_difficulty_level"]
        difficulty_fidelity = analysis["difficulty_fidelity"]
        files = value["files"]
        stop_reason = value.get("stop_reason")
        source_audit = value["self_audit"]["source_audit"]

        if source_audit is not None:
            expected_source = expected_source_status(source_audit)
            if source_audit["combined_status"] != expected_source:
                raise ValueError(
                    "source_audit.combined_status conflicts with statement_status "
                    "and proof_status"
                )

        if status == "formalized":
            if files is None or stop_reason is not None:
                raise ValueError("formalized requires files and no stop_reason")
            if difficulty is None or difficulty_level is None or difficulty_fidelity is None:
                raise ValueError("formalized requires all difficulty fields")
            components = (
                "conceptual_insight",
                "dependency_depth",
                "technical_lemma_burden",
                "closure_difficulty",
                "compressibility",
            )
            if difficulty["total"] != sum(difficulty[key] for key in components):
                raise ValueError(
                    "difficulty.total must equal the five component scores"
                )
            expected_level = (
                "D0"
                if difficulty["total"] <= 2
                else "D1"
                if difficulty["total"] <= 4
                else "D2"
                if difficulty["total"] <= 6
                else "D3"
                if difficulty["total"] <= 8
                else "D4"
            )
            if difficulty_level != expected_level:
                raise ValueError(
                    "proof_difficulty_level conflicts with difficulty.total"
                )
            if paper_type == "empirical_or_method_only":
                raise ValueError("empirical_or_method_only cannot be formalized")
            if (
                paper_type == "theory_auxiliary"
                and analysis["theory_auxiliary_subtype"]
                != ADMITTED_AUXILIARY_SUBTYPE
            ):
                raise ValueError(
                    "formalized theory_auxiliary requires the admitted subtype"
                )
            expected_suitability = {
                "D0": "reject",
                "D1": "baseline",
                "D2": "primary",
                "D3": "primary",
                "D4": "stress",
            }[difficulty_level]
            if suitability != expected_suitability:
                raise ValueError(
                    "benchmark_suitability conflicts with proof_difficulty_level"
                )
            if source_audit is None:
                raise ValueError("formalized requires source_audit")
            if source_audit["combined_status"] == "paper_issue_suspected":
                raise ValueError("formalized cannot contain a major source issue")
            repairs = files["provenance"]["source_repairs"]
            if source_audit["combined_status"] == "minor_source_issue_fixed":
                if not repairs:
                    raise ValueError(
                        "minor_source_issue_fixed requires a provenance source repair"
                    )
                if not all(
                    repair["claim_preserved"]
                    and repair["proof_architecture_preserved"]
                    for repair in repairs
                ):
                    raise ValueError(
                        "minor source repairs must preserve the claim and proof architecture"
                    )
            elif repairs:
                raise ValueError("clean source_audit requires no source repairs")
            roles = {item["role"] for item in analysis["proof_closure"]}
            if "target_claim" not in roles or not roles & {
                "material_internal",
                "technical_internal",
            }:
                raise ValueError(
                    "formalized proof_closure requires a target and material obligation"
                )
            failed_audits = [
                key
                for key, item in value["self_audit"].items()
                if key not in {"findings", "source_audit"}
                and item["status"] != "pass"
            ]
            if failed_audits:
                raise ValueError(
                    "formalized requires passing audits: " + ", ".join(failed_audits)
                )
        elif status == "filtered_out":
            if files is not None:
                raise ValueError("filtered_out must not generate task files")
            expected_reason = {
                "empirical_or_method_only": "paper_not_theory_core",
                "theory_auxiliary": "paper_too_weak",
            }.get(paper_type)
            if expected_reason is None:
                raise ValueError("theory_core cannot use filtered_out")
            if stop_reason != expected_reason:
                raise ValueError(
                    f"{paper_type} requires stop_reason {expected_reason}"
                )
            if (
                paper_type == "theory_auxiliary"
                and analysis["theory_auxiliary_subtype"]
                == ADMITTED_AUXILIARY_SUBTYPE
            ):
                raise ValueError(
                    "admitted theory_auxiliary cannot be filtered_out"
                )
            if suitability is not None:
                raise ValueError("filtered_out requires null benchmark_suitability")
            if source_audit is not None:
                raise ValueError("filtered_out requires null source_audit")
            if any(
                item is not None
                for item in (difficulty, difficulty_level, difficulty_fidelity)
            ):
                raise ValueError("filtered_out requires null difficulty fields")
        else:
            if files is not None or stop_reason is None:
                raise ValueError("stopped requires null files and a stop_reason")
            if stop_reason in {"paper_not_theory_core", "paper_too_weak"}:
                raise ValueError("screening reasons must use filtered_out")
            if paper_type == "empirical_or_method_only":
                raise ValueError("empirical_or_method_only cannot enter formalization")
            if (
                paper_type == "theory_auxiliary"
                and analysis["theory_auxiliary_subtype"]
                != ADMITTED_AUXILIARY_SUBTYPE
            ):
                raise ValueError(
                    "stopped theory_auxiliary must have passed triage"
                )
            if suitability is not None:
                raise ValueError("stopped requires null benchmark_suitability")
            if stop_reason in {
                "paper_issue_suspected",
                "formalization_not_self_containable",
            }:
                if source_audit is None:
                    raise ValueError(
                        "semantic stopped reasons require source_audit"
                    )
            if stop_reason == "paper_issue_suspected":
                if value["resolution"] != "paper_issue_suspected":
                    raise ValueError(
                        "paper_issue_suspected requires matching resolution"
                    )
                if source_audit["combined_status"] != "paper_issue_suspected":
                    raise ValueError(
                        "paper_issue_suspected requires a major statement or proof issue"
                    )
            if any(
                item is not None
                for item in (difficulty, difficulty_level, difficulty_fidelity)
            ):
                raise ValueError("stopped requires null difficulty fields")

    return value
