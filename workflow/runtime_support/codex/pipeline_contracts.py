"""Structured-output contracts shared by the runner and Codex adapter."""

from __future__ import annotations

from copy import deepcopy
import json
from typing import Any

from jsonschema import Draft202012Validator


ISSUES_SCHEMA: dict[str, Any] = {
    "type": "array",
    "items": {"type": "string", "minLength": 1},
}

THEOREM_ID_SCHEMA: dict[str, Any] = {
    "type": "string",
    "pattern": r"^theorem_[0-9]{3}$",
}

CORE_RESULT_GROUP_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "core_id",
        "paper_node_ids",
        "contribution_summary",
        "contribution_evidence",
        "selection_reason",
    ],
    "properties": {
        "core_id": {
            "type": "string",
            "pattern": r"^core_[1-9][0-9]*$",
        },
        "paper_node_ids": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "string",
                "pattern": r"^thm_[1-9][0-9]*$",
            },
        },
        "contribution_summary": {"type": "string", "minLength": 1},
        "contribution_evidence": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string", "minLength": 1},
        },
        "selection_reason": {"type": "string", "minLength": 1},
    },
}

SOURCE_SPAN_SCHEMA: dict[str, Any] = {
    "type": ["object", "null"],
    "additionalProperties": False,
    "required": ["start_line", "end_line", "label"],
    "properties": {
        "start_line": {"type": "integer", "minimum": 1},
        "end_line": {"type": "integer", "minimum": 1},
        "label": {"type": "string"},
    },
}

COARSE_PAPER_NODE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "id",
        "type",
        "scope",
        "role",
        "claim",
        "source_kind",
        "candidate_id",
        "source",
        "notes",
    ],
    "properties": {
        "id": {
            "type": "string",
            "pattern": (
                r"^(thm|prop|result|step|assumption|definition|citation)_"
                r"[1-9][0-9]*(?:_[1-9][0-9]*)*$"
            ),
        },
        "type": {
            "type": "string",
            "enum": [
                "assumption",
                "definition",
                "result",
                "citation",
                "proof_step",
                "theorem",
                "proposition",
            ],
        },
        "scope": {
            "type": ["string", "null"],
            "pattern": (
                r"^(thm|prop|result|step|assumption|definition|citation)_"
                r"[1-9][0-9]*(?:_[1-9][0-9]*)*$"
            ),
        },
        "role": {"type": "string", "minLength": 1},
        "claim": {"type": "string"},
        "source_kind": {
            "type": "string",
            "enum": [
                "lemma",
                "proposition",
                "corollary",
                "theorem",
                "assumption",
                "definition",
                "citation",
                "other",
            ],
        },
        "candidate_id": {
            "type": ["string", "null"],
            "pattern": r"^(?:thm|target)_candidate_[0-9]{3}$",
        },
        "source": {
            "type": "object",
            "additionalProperties": False,
            "required": ["statement", "proof", "evidence"],
            "properties": {
                "statement": SOURCE_SPAN_SCHEMA,
                "proof": SOURCE_SPAN_SCHEMA,
                "evidence": SOURCE_SPAN_SCHEMA,
            },
        },
        "notes": {"type": "string"},
    },
}

CONTRACTS: dict[str, dict[str, Any]] = {
    "adapter_smoke": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "observed_text",
            "output_path",
            "outside_read_status",
            "outside_observed_text",
            "command_execution_status",
        ],
        "properties": {
            "status": {"type": "string", "const": "completed"},
            "observed_text": {"type": "string", "minLength": 1},
            "output_path": {"type": "string", "minLength": 1},
            "outside_read_status": {
                "type": "string",
                "enum": ["blocked", "readable"],
            },
            "outside_observed_text": {"type": "string"},
            "command_execution_status": {
                "type": "string",
                "enum": ["completed", "aborted"],
            },
        },
    },
    "paper_admission": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["status", "decision", "scores", "average", "reason"],
        "properties": {
            "status": {"type": "string", "const": "completed"},
            "decision": {"type": "string", "enum": ["accepted", "rejected"]},
            "scores": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "ml_relevance",
                    "theoretical_focus",
                    "suitable_novelty",
                ],
                "properties": {
                    "ml_relevance": {"type": "integer", "minimum": 0, "maximum": 5},
                    "theoretical_focus": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 5,
                    },
                    "suitable_novelty": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 5,
                    },
                },
            },
            "average": {"type": "number", "minimum": 0, "maximum": 5},
            "reason": {"type": "string", "minLength": 1},
        },
    },
    "math_oc_admission": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["status", "decision", "reason"],
        "properties": {
            "status": {"type": "string", "const": "completed"},
            "decision": {
                "type": "string",
                "enum": ["accepted", "rejected", "undetermined"],
            },
            "reason": {"type": "string", "minLength": 1},
        },
    },
    "coarse_paper_bundle": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "domain",
            "title",
            "authors",
            "venue",
            "publication_date",
            "arxiv_id",
            "source_url",
            "paper_dag",
            "issues",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["completed", "needs_review"],
            },
            "domain": {
                "type": "string",
                "pattern": r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$",
            },
            "title": {"type": "string", "minLength": 1},
            "authors": {
                "type": "array",
                "minItems": 1,
                "items": {"type": "string", "minLength": 1},
            },
            "venue": {"type": "string"},
            "publication_date": {
                "type": "string",
                "pattern": r"^[0-9]{4}(-[0-9]{2}){0,2}$",
            },
            "arxiv_id": {
                "type": ["string", "null"],
            },
            "source_url": {"type": "string"},
            "paper_dag": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "schema_version",
                    "paper_id",
                    "visibility",
                    "status",
                    "theorem_count",
                    "proposition_count",
                    "formal_target_count",
                    "nodes",
                    "edges",
                    "notes",
                ],
                "properties": {
                    "schema_version": {"type": "string", "const": "1.0"},
                    "paper_id": {
                        "type": "string",
                        "pattern": r"^paper_[0-9]{4}_[0-9]{3,}$",
                    },
                    "visibility": {
                        "type": "string",
                        "const": "private_source",
                    },
                    "status": {
                        "type": "string",
                        "enum": ["complete", "needs_review"],
                    },
                    "theorem_count": {"type": "integer", "minimum": 0},
                    "proposition_count": {"type": "integer", "minimum": 0},
                    "formal_target_count": {"type": "integer", "minimum": 0},
                    "nodes": {
                        "type": "array",
                        "items": COARSE_PAPER_NODE_SCHEMA,
                    },
                    "edges": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["source_index", "target_index"],
                            "properties": {
                                "source_index": {
                                    "type": "integer",
                                    "minimum": 1,
                                },
                                "target_index": {
                                    "type": "integer",
                                    "minimum": 1,
                                },
                            },
                        },
                    },
                    "notes": {"type": "string"},
                },
            },
            "issues": ISSUES_SCHEMA,
        },
    },
    "coarse_theorem_bundle": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "paper_id",
            "theorem_id",
            "files",
            "leakage_audit_status",
            "issues",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["completed", "needs_review"],
            },
            "paper_id": {
                "type": "string",
                "pattern": r"^paper_[0-9]{4}_[0-9]{3,}$",
            },
            "theorem_id": THEOREM_ID_SCHEMA,
            "files": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "assumptions_md",
                    "citations_md",
                    "theorem_statement_original_md",
                    "theorem_statement_sanitized_md",
                    "proof_ground_truth_md",
                    "rubric_prove_theorem_md",
                    "task_prove_theorem_md",
                ],
                "properties": {
                    "assumptions_md": {"type": "string", "minLength": 1},
                    "citations_md": {"type": "string", "minLength": 1},
                    "theorem_statement_original_md": {
                        "type": "string",
                        "minLength": 1,
                    },
                    "theorem_statement_sanitized_md": {
                        "type": "string",
                        "minLength": 1,
                    },
                    "proof_ground_truth_md": {
                        "type": "string",
                        "minLength": 1,
                    },
                    "rubric_prove_theorem_md": {
                        "type": "string",
                        "minLength": 1,
                    },
                    "task_prove_theorem_md": {
                        "type": "string",
                        "minLength": 1,
                    },
                },
            },
            "leakage_audit_status": {
                "type": "string",
                "enum": ["pass", "needs_revision"],
            },
            "issues": ISSUES_SCHEMA,
        },
    },
    "accepted_paper_processing": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "domain",
            "theorem_count",
            "theorem_inventory",
            "core_result_groups",
            "issues",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["completed", "needs_review"],
            },
            "domain": {
                "type": "string",
                "pattern": r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$",
            },
            "theorem_count": {
                "type": "integer",
                "minimum": 0,
            },
            "theorem_inventory": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": [
                        "candidate_id",
                        "paper_node_id",
                        "type",
                        "location",
                        "source_scope",
                    ],
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "pattern": r"^thm_candidate_[0-9]{3}$",
                        },
                        "paper_node_id": {
                            "type": "string",
                            "pattern": r"^thm_[1-9][0-9]*$",
                        },
                        "type": {"type": "string", "const": "Theorem"},
                        "location": {"type": "string", "minLength": 1},
                        "source_scope": {
                            "type": "string",
                            "enum": [
                                "main_text",
                                "appendix",
                                "supplementary_material",
                            ],
                        },
                    },
                },
            },
            "core_result_groups": {
                "type": "array",
                "minItems": 1,
                "items": CORE_RESULT_GROUP_SCHEMA,
            },
            "issues": ISSUES_SCHEMA,
        },
    },
    "theorem_agent_stage": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "paper_id",
            "theorem_id",
            "stage",
            "output_directory",
            "issues",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["completed", "needs_review"],
            },
            "paper_id": {
                "type": "string",
                "pattern": r"^paper_[0-9]{4}_[0-9]{3,}$",
            },
            "theorem_id": THEOREM_ID_SCHEMA,
            "stage": {
                "type": "string",
                "enum": [
                    "theorem_core",
                    "proof_dag",
                    "key_lemmas",
                    "formalization",
                    "direct_task",
                    "ladder_task",
                    "direct_review",
                    "ladder_review",
                ],
            },
            "output_directory": {"type": "string", "minLength": 1},
            "issues": ISSUES_SCHEMA,
        },
    },
    "theorem_agent": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "paper_id",
            "theorem_id",
            "dag_status",
            "selected_results",
            "self_reviewed_public_tasks",
            "leakage_self_audit",
            "output_directory",
            "issues",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["completed", "needs_review"],
            },
            "paper_id": {
                "type": "string",
                "pattern": r"^paper_[0-9]{4}_[0-9]{3,}$",
            },
            "theorem_id": THEOREM_ID_SCHEMA,
            "dag_status": {
                "type": "string",
                "enum": ["complete", "needs_review"],
            },
            "selected_results": {
                "type": "array",
                "items": {
                    "type": "string",
                    "pattern": r"^result_[1-9][0-9]*_[1-9][0-9]*$",
                },
            },
            "self_reviewed_public_tasks": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": {
                    "type": "string",
                    "enum": [
                        "public_tasks/task_prove_theorem.md",
                        "public_tasks/task_prove_with_lemmas.md",
                    ],
                },
            },
            "leakage_self_audit": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "public_tasks/task_prove_theorem.md",
                    "public_tasks/task_prove_with_lemmas.md",
                ],
                "properties": {
                    "public_tasks/task_prove_theorem.md": {
                        "type": "string",
                        "enum": ["pass", "needs_revision"],
                    },
                    "public_tasks/task_prove_with_lemmas.md": {
                        "type": "string",
                        "enum": ["pass", "needs_revision"],
                    },
                },
            },
            "output_directory": {"type": "string", "minLength": 1},
            "issues": ISSUES_SCHEMA,
        },
    },
    "paper_agent_review": {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "status",
            "reviewed_theorems",
            "leakage_audit_status",
            "issues",
        ],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["completed", "needs_review"],
            },
            "reviewed_theorems": {
                "type": "array",
                "items": THEOREM_ID_SCHEMA,
            },
            "leakage_audit_status": {
                "type": "string",
                "enum": ["pass", "needs_revision"],
            },
            "issues": ISSUES_SCHEMA,
        },
    },
}

_corrected_coarse_paper_bundle = deepcopy(CONTRACTS["coarse_paper_bundle"])
_corrected_coarse_paper_bundle.pop("$schema", None)
CONTRACTS["coarse_paper_dag_review"] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "verdict",
        "checks",
        "corrected_bundle",
        "issues",
    ],
    "properties": {
        "status": {
            "type": "string",
            "enum": ["completed", "needs_review"],
        },
        "verdict": {
            "type": "string",
            "enum": ["pass", "revised", "unresolved"],
        },
        "checks": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "theorem_inventory",
                "source_grounding",
                "proof_coverage",
                "dependency_semantics",
                "global_consistency",
            ],
            "properties": {
                "theorem_inventory": {
                    "type": "string",
                    "enum": ["pass", "revised", "unresolved"],
                },
                "source_grounding": {
                    "type": "string",
                    "enum": ["pass", "revised", "unresolved"],
                },
                "proof_coverage": {
                    "type": "string",
                    "enum": ["pass", "revised", "unresolved"],
                },
                "dependency_semantics": {
                    "type": "string",
                    "enum": ["pass", "revised", "unresolved"],
                },
                "global_consistency": {
                    "type": "string",
                    "enum": ["pass", "revised", "unresolved"],
                },
            },
        },
        "corrected_bundle": {
            "anyOf": [
                {"type": "null"},
                _corrected_coarse_paper_bundle,
            ],
        },
        "issues": ISSUES_SCHEMA,
    },
}


def schema_for(contract_name: str) -> dict[str, Any]:
    try:
        return CONTRACTS[contract_name]
    except KeyError as error:
        raise ValueError(f"unknown output contract: {contract_name}") from error


def validate_payload(contract_name: str, payload: dict[str, Any]) -> None:
    validator = Draft202012Validator(schema_for(contract_name))
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.path))
    if not errors:
        return
    details = []
    for error in errors[:5]:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        details.append(f"{location}: {error.message}")
    raise ValueError(
        f"response violates {contract_name} contract: " + "; ".join(details)
    )


def parse_and_validate(contract_name: str, text: str | None) -> dict[str, Any]:
    if not text:
        raise ValueError("Codex returned no final response")
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError("Codex final response is not valid JSON") from error
    if not isinstance(payload, dict):
        raise ValueError("Codex final response must be a JSON object")
    validate_payload(contract_name, payload)
    return payload
