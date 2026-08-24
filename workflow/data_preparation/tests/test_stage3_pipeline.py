from __future__ import annotations

import asyncio
import inspect
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from typing import Any


DATA_PREPARATION = Path(__file__).resolve().parents[1]
PIPELINE = DATA_PREPARATION / "pipeline"
FORMALIZATION_SUPPORT = (
    DATA_PREPARATION.parent / "runtime_support/formalization"
)
for path in (PIPELINE, FORMALIZATION_SUPPORT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from solver_bridge import ScriptedValidation  # noqa: E402
from prepare_stage3_retries import prepare_retries  # noqa: E402
from stage3_contracts import (  # noqa: E402
    Stage3ContractError,
    assemble_paper_analysis,
    build_thread_b_view,
    validate_complexity,
    validate_source_audit,
    validate_target_selection,
)
from stage3_pipeline import (  # noqa: E402
    SourceCheckUnresolved,
    Stage3Pipeline,
    _apply_and_validate_bundle,
    _consume_source_reaudit,
    _templates_text,
)
from stage3_runtime import (  # noqa: E402
    CONTRACT_SCHEMAS,
    _contract_recovery_instruction,
    _normalize_artifact_audit_protocol,
    _normalize_nonresult_source_fields,
    _normalize_source_audit_protocol,
    _normalize_source_check_protocol,
    _normalize_target_chain_ids,
    _normalize_target_attached_materials,
    _normalize_target_omitted_candidates,
    _normalize_triage_audit_protocol,
    _normalize_triage_material_ids,
    _promote_unrepaired_minor_findings,
)
from stage3_validation import Stage3ExperimentValidation  # noqa: E402
from solver_bridge import ExperimentValidation  # noqa: E402


def triage_payload() -> dict[str, Any]:
    return {
        "status": "proceed",
        "filter_reason": None,
        "principal_contribution": "A complete synthetic theorem.",
        "theory_inventory": [
            {
                "item_id": "theory_001",
                "role": "definition",
                "source_label": "Definition 1",
                "summary": "Defines the synthetic object.",
                "source_spans": ["Definition 1"],
                "depends_on": [],
            },
            {
                "item_id": "theory_002",
                "role": "theory_candidate",
                "source_label": "Theorem 1",
                "summary": "States the synthetic result.",
                "source_spans": ["Theorem 1"],
                "depends_on": ["theory_001"],
            },
        ],
        "paper_type": "theory_core",
        "theory_auxiliary_subtype": None,
        "triage_reasoning": "The theorem is the principal contribution.",
    }


def selection_payload() -> dict[str, Any]:
    return {
        "status": "selected",
        "stop_reason": None,
        "formalization_target": "Prove the synthetic result.",
        "candidate_chain_evaluations": [
            {
                "chain_id": "chain_001",
                "candidate_ids": ["theory_002"],
                "scientific_claim": "The synthetic result holds.",
                "claimed_proof_architecture": ["Apply the defining identity."],
                "claimed_characteristic_bottleneck": "Derive the identity.",
                "contribution_fidelity": {
                    "paper_level_contribution_recovery": 3,
                    "scientific_sufficiency": 3,
                    "scope_economy": 3,
                    "total": 9,
                    "reason": "The only principal result is recovered minimally.",
                },
                "difficulty_fidelity": {
                    "bottleneck_coverage": 2,
                    "mechanism_representativeness": 2,
                    "difficulty_distortion": 2,
                    "total": 6,
                    "reason": "The only principal proof mechanism is preserved.",
                },
            }
        ],
        "ranked_chain_ids": ["chain_001"],
        "selected_chain_id": "chain_001",
        "selected_candidate_ids": ["theory_002"],
        "attached_material_ids": ["theory_001"],
        "target_selection_reasoning": "The unique candidate is selected.",
        "characteristic_bottleneck": "Derive the identity.",
        "omitted_candidates": [],
        "selection_ambiguity": None,
    }


def source_payload() -> dict[str, Any]:
    base_null = {
        "statement_findings": [],
        "statement_repair": None,
        "proof_findings": [],
        "proof_repair": None,
        "external_classification": None,
        "is_added": False,
        "addition_reason": None,
    }
    return {
        "status": "audited",
        "material_records": [
            {
                **base_null,
                "item_id": "theory_001",
                "role": "definition",
                "source_label": "Definition 1",
                "recovered_content": "Let x be a nonnegative real.",
                "proof_reconstruction": None,
                "statement_status": None,
                "proof_status": None,
                "source_spans": ["Definition 1"],
                "statement_source_locations": [
                    {"start_line": 1, "end_line": 1, "label": "Definition 1"}
                ],
                "proof_source_locations": [],
                "depends_on": [],
            },
            {
                **base_null,
                "item_id": "theory_002",
                "role": "theory_candidate",
                "source_label": "Theorem 1",
                "recovered_content": "For x >= 0, x + 1 >= 1.",
                "proof_reconstruction": "Add 1 to x >= 0.",
                "statement_status": "clean",
                "proof_status": "clean",
                "source_spans": ["Theorem 1", "Proof of Theorem 1"],
                "statement_source_locations": [
                    {"start_line": 1, "end_line": 1, "label": "Theorem 1"}
                ],
                "proof_source_locations": [
                    {
                        "start_line": 1,
                        "end_line": 1,
                        "label": "Proof of Theorem 1",
                    }
                ],
                "depends_on": ["theory_001"],
            },
        ]
    }


def compile_payload() -> dict[str, Any]:
    return {
        "status": "formalized",
        "reason": None,
        "task_md": "# Problem\n\nLet $x\\ge 0$. Prove $x+1\\ge 1$.",
        "proof_ground_truth_md": "# Reference Proof\n\nAdd one to $x\\ge0$.",
        "rubric_md": "# Rubric\n\n- 10 points: proves the inequality.",
        "provenance": {
            "public_clauses": [
                {
                    "clause_id": "clause_001",
                    "kind": "target",
                    "source_material_ids": ["theory_002"],
                    "transformation": "notation_only",
                }
            ],
            "private_proof_steps": [
                {
                    "step_id": "step_001",
                    "source_material_ids": ["theory_002"],
                }
            ],
            "notation_map": [],
            "applied_source_repairs": [],
        },
    }


def audit_payload() -> dict[str, Any]:
    check = {"status": "pass", "evidence": "The artifact passes."}
    return {
        "status": "pass",
        "checks": {
            name: dict(check)
            for name in (
                "definition_integrity", "self_containment", "source_fidelity",
                "anti_leakage", "contribution_fidelity", "validity", "scope",
            )
        },
        "findings": [],
        "objection": None,
        "replacements": None,
    }


def complexity_payload() -> dict[str, Any]:
    return {
        "status": "scored",
        "solver_obligations": ["Derive the target inequality."],
        "material_capabilities": ["Elementary order reasoning."],
        "proof_reconstruction_complexity": {
            "strategy_discovery": {"score": 1, "reason": "The route is standard."},
            "subgoal_structure_dependency": {"score": 1, "reason": "One short chain."},
            "technical_reasoning_execution": {"score": 1, "reason": "Execution is local."},
            "capability_integration": {"score": 1, "reason": "Two close modes."},
            "intrinsic_complexity_total": 4,
        },
        "proof_route_exposure": {
            "level": 0,
            "reason": "No internal route is exposed.",
            "required_revision": None,
        },
        "effective_complexity_total": 4,
        "proof_reconstruction_complexity_level": "PRC1",
        "benchmark_suitability": "baseline",
        "overall_reason": "A standard proof reconstruction.",
    }


class ScriptedAgent:
    def __init__(self) -> None:
        self.payloads = {
            "stage3_triage": triage_payload(),
            "stage3_target_selection": selection_payload(),
            "stage3_source_audit": source_payload(),
            "stage3_compile": compile_payload(),
            "stage3_artifact_audit": audit_payload(),
            "stage3_complexity": complexity_payload(),
        }
        self.calls = []

    async def run(self, request: Any) -> dict[str, Any]:
        self.calls.append(request)
        if request.resume_session_id is not None:
            session_id = request.resume_session_id
        elif request.phase.startswith("stage3_compile"):
            session_id = "thread_b"
        else:
            session_id = "thread_a"
        return {
            "payload": self.payloads[request.phase],
            "status": self.payloads[request.phase].get("status", "completed"),
            "session_id": session_id,
            "turn_id": f"turn_{len(self.calls)}",
            "usage": None,
        }


class ExposureRevisionAgent(ScriptedAgent):
    def __init__(self) -> None:
        super().__init__()
        self.complexity_calls = 0

    async def run(self, request: Any) -> dict[str, Any]:
        if request.phase == "stage3_complexity":
            self.complexity_calls += 1
            if self.complexity_calls == 1:
                payload = complexity_payload()
                payload["status"] = "formalization_revision_required"
                payload["proof_route_exposure"] = {
                    "level": 2,
                    "reason": "The task exposes a theorem-critical intermediate goal.",
                    "required_revision": "Remove the intermediate goal from the task.",
                }
                payload["effective_complexity_total"] = None
                payload["proof_reconstruction_complexity_level"] = None
                payload["benchmark_suitability"] = None
                self.payloads["stage3_complexity"] = payload
            else:
                self.payloads["stage3_complexity"] = complexity_payload()
        elif request.phase == "stage3_revision":
            self.payloads["stage3_revision"] = {
                "status": "formalization_error_fixed",
                "explanation": "Removed the exposed intermediate goal.",
                "replacements": {
                    "task_md": (
                        "# Problem\n\nLet $x\\ge 0$. Establish the final claim "
                        "$x+1\\ge 1$."
                    ),
                    "proof_ground_truth_md": None,
                    "rubric_md": None,
                    "provenance": None,
                },
                "self_audit": audit_payload()["checks"],
            }
        return await super().run(request)


class SourceCheckRevisionAgent(ScriptedAgent):
    async def run(self, request: Any) -> dict[str, Any]:
        if request.phase == "stage3_revision":
            self.payloads[request.phase] = {
                "status": "source_check_required",
                "explanation": "Check the recovered theorem against its source lines.",
                "replacements": None,
                "self_audit": None,
            }
        elif request.phase == "stage3_local_source_check":
            self.payloads[request.phase] = {
                "status": "objection_rejected",
                "explanation": "The recorded theorem and proof are source-accurate.",
                "affected_material_ids": ["theory_002"],
                "source_audit": source_payload(),
            }
        return await super().run(request)


class MaxFeedbackSourceCheckAgent(ScriptedAgent):
    def __init__(self) -> None:
        super().__init__()
        self.revision_calls = 0
        self.compile_calls = 0

    async def run(self, request: Any) -> dict[str, Any]:
        if request.phase == "stage3_compile":
            self.compile_calls += 1
            if self.compile_calls == 2:
                self.payloads[request.phase] = {
                    "status": "source_material_insufficient",
                    "reason": "The checked fallback closure remains insufficient.",
                    "task_md": None,
                    "proof_ground_truth_md": None,
                    "rubric_md": None,
                    "provenance": None,
                }
        elif request.phase == "stage3_revision":
            self.revision_calls += 1
            if self.revision_calls == 1:
                self.payloads[request.phase] = {
                    "status": "formalization_error_fixed",
                    "explanation": "Clarified the public target.",
                    "replacements": {
                        "task_md": (
                            "# Problem\n\nLet $x\\ge 0$. Prove the clarified target "
                            "$x+1\\ge 1$."
                        ),
                        "proof_ground_truth_md": None,
                        "rubric_md": None,
                        "provenance": None,
                    },
                    "self_audit": audit_payload()["checks"],
                }
            else:
                self.payloads[request.phase] = {
                    "status": "source_check_required",
                    "explanation": "Check the recovered theorem against the source.",
                    "replacements": None,
                    "self_audit": None,
                }
        elif request.phase == "stage3_local_source_check":
            self.payloads[request.phase] = {
                "status": "objection_rejected",
                "explanation": "The source record is accurate.",
                "affected_material_ids": ["theory_002"],
                "source_audit": source_payload(),
            }
        return await super().run(request)


class UnscorableEvaluatorValidation(ScriptedValidation):
    def run_evaluator(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
        evaluator_output_dir: Path,
    ) -> dict[str, Any]:
        result = super().run_evaluator(
            paper_id,
            task_path,
            solver_output_dir,
            reviewer_output_dir,
            evaluator_output_dir,
        )
        result["result"].update(
            {
                "evaluation_status": "unscorable",
                "score": None,
                "verdict": "unscorable_target_error",
                "summary": "The target has a fatal defect.",
            }
        )
        return result


class TriageRescueAgent(ScriptedAgent):
    def __init__(self) -> None:
        super().__init__()
        filtered = triage_payload()
        filtered.update(
            {
                "status": "filtered_out",
                "filter_reason": "paper_not_theory_core",
                "paper_type": "empirical_or_method_only",
                "triage_reasoning": "The initial pass misclassified the theorem.",
            }
        )
        self.payloads["stage3_triage"] = filtered
        self.payloads["stage3_triage_audit"] = {
            "status": "corrected",
            "checks": {
                "principal_contribution": {
                    "status": "fail",
                    "evidence": "The theorem is the principal contribution.",
                },
                "theory_inventory": {
                    "status": "pass",
                    "evidence": "The theoretical inventory is sufficient.",
                },
                "classification": {
                    "status": "fail",
                    "evidence": "The paper should proceed as theory_core.",
                },
            },
            "effective_triage": triage_payload(),
            "reasoning": "The independent audit rescues the paper.",
        }

    async def run(self, request: Any) -> dict[str, Any]:
        result = await super().run(request)
        if request.phase == "stage3_triage_audit":
            result["session_id"] = "triage_audit_thread"
        return result


class Stage3PipelineTests(unittest.TestCase):
    def test_reference_evaluator_backend_accepts_retry_prompt(self) -> None:
        parameters = inspect.signature(
            ExperimentValidation.run_evaluator
        ).parameters
        self.assertIn("prompt_path", parameters)

    def test_reference_evaluator_contract_retry_receives_validator_feedback(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            validation = Stage3ExperimentValidation(
                api_profile=root,
                model="model",
                reasoning_effort="high",
            )
            observed_prompts: list[str | None] = []

            def fake_run_evaluator(*_args, **kwargs):
                prompt_path = kwargs.get("prompt_path")
                observed_prompts.append(
                    None
                    if prompt_path is None
                    else prompt_path.read_text(encoding="utf-8")
                )
                if len(observed_prompts) == 1:
                    raise RuntimeError(
                        "a confirmed finding must preserve its severity"
                    )
                return {"result": {"evaluation_status": "scored", "score": 8}}

            with patch.object(
                ExperimentValidation,
                "run_evaluator",
                side_effect=fake_run_evaluator,
            ):
                result = validation.run_evaluator(
                    "paper_2026_001",
                    root / "task.md",
                    root / "solver",
                    root / "reviewer",
                    root / "evaluator",
                )

            self.assertEqual(result["contract_retry_count"], 1)
            self.assertIsNone(observed_prompts[0])
            self.assertIn(
                "a confirmed finding must preserve its severity",
                observed_prompts[1] or "",
            )

    def test_local_source_check_has_a_hard_total_cap_of_one(self) -> None:
        self.assertEqual(_consume_source_reaudit(0), 1)
        with self.assertRaises(SourceCheckUnresolved):
            _consume_source_reaudit(1)

    def test_compiler_receives_only_current_artifact_templates(self) -> None:
        templates = _templates_text()
        for name in (
            "task.template.md",
            "proof_ground_truth.template.md",
            "rubric.template.md",
            "provenance.template.json",
        ):
            self.assertIn(name, templates)
        self.assertNotIn("contribution_analysis.template.json", templates)
        self.assertNotIn("self_audit.template.json", templates)
        self.assertNotIn("difficulty_fidelity", templates)

    def test_public_task_rejects_explicit_proof_permission(self) -> None:
        bundle = compile_payload()
        bundle["task_md"] += "\n\nYou may use the key internal lemma."
        with self.assertRaises(ValueError):
            _apply_and_validate_bundle(bundle, None)

    def test_provenance_rejects_unavailable_material_id(self) -> None:
        bundle = compile_payload()
        bundle["provenance"]["private_proof_steps"][0][
            "source_material_ids"
        ] = ["theory_999"]
        with self.assertRaises(Stage3ContractError):
            _apply_and_validate_bundle(
                bundle, None, {"theory_001", "theory_002"}
            )

    def test_triage_material_ids_and_dependencies_are_canonicalized(self) -> None:
        payload = triage_payload()
        payload["theory_inventory"][0]["item_id"] = "theory_311"
        payload["theory_inventory"][1]["item_id"] = "theory_311"
        payload["theory_inventory"][1]["depends_on"] = ["theory_311"]

        _normalize_triage_material_ids(payload)

        self.assertEqual(
            [item["item_id"] for item in payload["theory_inventory"]],
            ["theory_001", "theory_002"],
        )
        self.assertEqual(
            payload["theory_inventory"][1]["depends_on"], ["theory_001"]
        )

    def test_triage_dependency_normalization_removes_self_edges_and_cycles(self) -> None:
        payload = triage_payload()
        payload["theory_inventory"][0]["depends_on"] = [
            "theory_001",
            "theory_002",
            "theory_002",
            "theory_999",
        ]
        payload["theory_inventory"][1]["depends_on"] = ["theory_001"]

        _normalize_triage_material_ids(payload)

        self.assertEqual(
            payload["theory_inventory"][0]["depends_on"], ["theory_002"]
        )
        self.assertEqual(payload["theory_inventory"][1]["depends_on"], [])

    def test_source_audit_protocol_normalizes_added_items_and_cycles(self) -> None:
        triage = triage_payload()
        source = source_payload()
        source["material_records"][0]["depends_on"] = ["theory_002"]
        source["material_records"][1]["depends_on"] = ["theory_001"]
        added = dict(source["material_records"][1])
        added["item_id"] = "theory_003"
        added["is_added"] = False
        added["addition_reason"] = None
        source["material_records"].append(added)
        source["material_records"][1]["proof_repair"] = {
            "original_source": "unused",
            "repaired_form": "unused",
            "source_evidence": "unused",
            "justification": "unused",
        }

        _normalize_source_audit_protocol(source, triage)

        self.assertEqual(source["material_records"][0]["depends_on"], ["theory_002"])
        self.assertEqual(source["material_records"][1]["depends_on"], [])
        self.assertTrue(source["material_records"][2]["is_added"])
        self.assertTrue(source["material_records"][2]["addition_reason"])
        self.assertIsNone(source["material_records"][1]["proof_repair"])

    def test_source_audit_protocol_normalizes_reversed_line_ranges(self) -> None:
        triage = triage_payload()
        source = source_payload()
        source["material_records"][1]["statement_source_locations"][0].update(
            {"start_line": 20, "end_line": 12}
        )
        source["material_records"][1]["proof_source_locations"][0].update(
            {"start_line": 45, "end_line": 30}
        )

        _normalize_source_audit_protocol(source, triage)

        record = source["material_records"][1]
        self.assertEqual(
            record["statement_source_locations"][0]["start_line"], 12
        )
        self.assertEqual(
            record["statement_source_locations"][0]["end_line"], 20
        )
        self.assertEqual(record["proof_source_locations"][0]["start_line"], 30)
        self.assertEqual(record["proof_source_locations"][0]["end_line"], 45)

    def test_unrepaired_minor_findings_are_conservatively_promoted(self) -> None:
        payload = source_payload()
        record = payload["material_records"][1]
        record["statement_status"] = "minor_issue"
        record["statement_findings"] = ["A repair is needed."]
        record["statement_repair"] = None
        record["proof_status"] = "minor_error"
        record["proof_findings"] = ["A proof repair is needed."]
        record["proof_repair"] = None

        self.assertTrue(_promote_unrepaired_minor_findings(payload))

        self.assertEqual(record["statement_status"], "major_issue")
        self.assertEqual(record["proof_status"], "major_gap")
        validate_source_audit(triage_payload(), payload)

    def test_source_check_protocol_preserves_unaffected_and_frozen_roles(self) -> None:
        previous = source_payload()
        proposed = source_payload()
        proposed["material_records"][0]["recovered_content"] = "Changed outside scope."
        proposed["material_records"][1]["role"] = "definition"
        payload = {
            "status": "source_record_corrected",
            "explanation": "A local correction was proposed.",
            "affected_material_ids": ["theory_002"],
            "source_audit": proposed,
        }

        _normalize_source_check_protocol(payload, previous)

        records = payload["source_audit"]["material_records"]
        self.assertEqual(records[0], previous["material_records"][0])
        self.assertEqual(records[1], previous["material_records"][1])

    def test_source_audit_allows_only_non_candidate_role_corrections(self) -> None:
        triage = triage_payload()
        source = source_payload()
        source["material_records"][0]["role"] = "external"
        source["material_records"][0]["external_classification"] = (
            "standard_independent"
        )
        validate_source_audit(triage, source)

        source = source_payload()
        source["material_records"][1]["role"] = "internal_support"
        with self.assertRaisesRegex(Stage3ContractError, "frozen candidate role"):
            validate_source_audit(triage, source)

    def test_failed_outputs_are_archived_for_clean_retry(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = root / "papers/paper_2026_001"
            (paper / "private_source").mkdir(parents=True)
            (paper / "paper_analysis").mkdir()
            (paper / "paper_analysis/turn1.json").write_text("{}")
            (paper / "pipeline_manifest.json").write_text("{}")
            (root / "logs").mkdir()
            (root / "logs/paper_2026_001.stderr.log").write_text("failed")
            (root / "run.json").write_text(
                json.dumps(
                    {
                        "papers": {
                            "paper_2026_001": {
                                "status": "failed",
                                "exit_code": 1,
                            }
                        }
                    }
                )
            )

            self.assertEqual(prepare_retries(root), ["paper_2026_001"])

            self.assertTrue((paper / "private_source").is_dir())
            self.assertFalse((paper / "paper_analysis").exists())
            self.assertFalse((paper / "pipeline_manifest.json").exists())
            self.assertEqual(
                json.loads((root / "run.json").read_text())["papers"]
                ["paper_2026_001"]["status"],
                "pending",
            )
            archived = list(
                (root / "debug_attempts/paper_2026_001").glob(
                    "*/paper_analysis/turn1.json"
                )
            )
            self.assertEqual(len(archived), 1)

    def test_downstream_contract_failure_is_retried_once(self) -> None:
        attempts = 0

        def operation() -> dict[str, Any]:
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise RuntimeError("invalid evaluator JSON")
            return {"status": "completed"}

        with tempfile.TemporaryDirectory() as temporary:
            result = Stage3ExperimentValidation._run_with_contract_retry(
                operation, Path(temporary), "evaluator"
            )
            self.assertEqual(attempts, 2)
            self.assertEqual(result["contract_retry_count"], 1)
            self.assertTrue((Path(temporary) / "contract_retry.json").is_file())

    def test_nonresult_source_fields_are_canonicalized(self) -> None:
        payload = source_payload()
        definition = payload["material_records"][0]
        definition["proof_reconstruction"] = "Not applicable."
        definition["statement_findings"] = ["Not applicable."]
        definition["external_classification"] = "standard_independent"

        _normalize_nonresult_source_fields(payload)

        self.assertIsNone(definition["proof_reconstruction"])
        self.assertEqual(definition["statement_findings"], [])
        self.assertIsNone(definition["external_classification"])

    def test_artifact_recovery_requires_resolved_checks(self) -> None:
        instruction = _contract_recovery_instruction("stage3_artifact_audit")
        self.assertIn("every check is pass", instruction)
        self.assertIn("source_check_required", instruction)

    def test_complexity_exposure_adjustment_and_revision_gate(self) -> None:
        value = complexity_payload()
        value["proof_route_exposure"]["level"] = 1
        value["proof_route_exposure"]["reason"] = "One mild clue is exposed."
        value["effective_complexity_total"] = 3
        value["proof_reconstruction_complexity_level"] = "PRC0"
        value["benchmark_suitability"] = "reject"
        validate_complexity(value)

        value["status"] = "formalization_revision_required"
        value["proof_route_exposure"]["level"] = 2
        value["proof_route_exposure"]["required_revision"] = (
            "Remove the internal intermediate conclusion."
        )
        value["effective_complexity_total"] = None
        value["proof_reconstruction_complexity_level"] = None
        value["benchmark_suitability"] = None
        validate_complexity(value)

    def test_source_recovery_distinguishes_material_roles(self) -> None:
        instruction = _contract_recovery_instruction("stage3_source_audit")
        self.assertIn("definition and external", instruction)
        self.assertIn("both finding arrays to empty", instruction)

    def test_target_chain_ids_are_canonicalized_by_content(self) -> None:
        payload = selection_payload()
        duplicate = dict(payload["candidate_chain_evaluations"][0])
        duplicate["candidate_ids"] = ["theory_003"]
        payload["candidate_chain_evaluations"].append(duplicate)
        payload["candidate_chain_evaluations"][0]["chain_id"] = "chain_614"
        payload["candidate_chain_evaluations"][1]["chain_id"] = "chain_614"
        payload["ranked_chain_ids"] = ["chain_614"]
        payload["selected_chain_id"] = "chain_614"

        _normalize_target_chain_ids(payload)

        self.assertEqual(
            [
                evaluation["chain_id"]
                for evaluation in payload["candidate_chain_evaluations"]
            ],
            ["chain_001", "chain_002"],
        )
        self.assertEqual(
            payload["ranked_chain_ids"], ["chain_001", "chain_002"]
        )
        self.assertEqual(payload["selected_chain_id"], "chain_001")

    def test_target_chain_ranking_is_normalized_from_structured_scores(self) -> None:
        payload = selection_payload()
        second = json.loads(
            json.dumps(payload["candidate_chain_evaluations"][0])
        )
        second["chain_id"] = "chain_002"
        second["candidate_ids"] = ["theory_003"]
        second["contribution_fidelity"]["total"] = 8
        second["contribution_fidelity"]["paper_level_contribution_recovery"] = 2
        payload["candidate_chain_evaluations"].append(second)
        payload["ranked_chain_ids"] = ["chain_002", "chain_001"]

        _normalize_target_chain_ids(payload)

        self.assertEqual(
            payload["ranked_chain_ids"], ["chain_001", "chain_002"]
        )
        self.assertEqual(payload["selected_chain_id"], "chain_001")

    def test_target_attached_materials_include_declared_dependency_closure(self) -> None:
        triage = triage_payload()
        triage["theory_inventory"].insert(
            0,
            {
                "item_id": "theory_000",
                "role": "definition",
                "source_label": "Definition 0",
                "summary": "Defines the ambient space.",
                "source_spans": ["Definition 0"],
                "depends_on": [],
            },
        )
        triage["theory_inventory"][1]["depends_on"] = ["theory_000"]
        payload = selection_payload()
        payload["attached_material_ids"] = []

        _normalize_target_attached_materials(payload, triage)

        self.assertEqual(
            payload["attached_material_ids"], ["theory_000", "theory_001"]
        )
        validate_target_selection(triage, payload)

    def test_target_omitted_candidates_are_completed_deterministically(self) -> None:
        triage = triage_payload()
        triage["theory_inventory"].append(
            {
                "item_id": "theory_003",
                "role": "theory_candidate",
                "source_label": "Theorem 2",
                "summary": "States a secondary result.",
                "source_spans": ["Theorem 2"],
                "depends_on": [],
            }
        )
        payload = selection_payload()
        payload["omitted_candidates"] = []

        _normalize_target_omitted_candidates(payload, triage)

        self.assertEqual(
            [item["item_id"] for item in payload["omitted_candidates"]],
            ["theory_003"],
        )
        validate_target_selection(triage, payload)

    def test_confirmed_triage_audit_preserves_original_record(self) -> None:
        original = triage_payload()
        original.update(
            {
                "status": "filtered_out",
                "filter_reason": "paper_not_theory_core",
                "paper_type": "empirical_or_method_only",
            }
        )
        audit = {
            "status": "confirmed_filtered_out",
            "effective_triage": triage_payload(),
        }

        _normalize_triage_audit_protocol(audit, original)

        self.assertEqual(audit["effective_triage"], original)

    def test_all_pass_artifact_audit_without_replacements_becomes_pass(self) -> None:
        payload = audit_payload()
        payload.update(
            {
                "status": "corrected",
                "replacements": {
                    "task_md": None,
                    "proof_ground_truth_md": None,
                    "rubric_md": None,
                    "provenance": None,
                },
            }
        )

        _normalize_artifact_audit_protocol(payload)

        self.assertEqual(payload["status"], "pass")
        self.assertIsNone(payload["replacements"])

    def test_ranked_source_gate_falls_back_to_first_clean_chain(self) -> None:
        triage = triage_payload()
        triage["theory_inventory"].append(
            {
                "item_id": "theory_003",
                "role": "theory_candidate",
                "source_label": "Theorem 2",
                "summary": "States an independent fallback result.",
                "source_spans": ["Theorem 2"],
                "depends_on": ["theory_001"],
            }
        )
        selection = selection_payload()
        fallback = json.loads(
            json.dumps(selection["candidate_chain_evaluations"][0])
        )
        fallback.update(
            {
                "chain_id": "chain_002",
                "candidate_ids": ["theory_003"],
                "scientific_claim": "The independent fallback result holds.",
            }
        )
        fallback["contribution_fidelity"]["paper_level_contribution_recovery"] = 2
        fallback["contribution_fidelity"]["total"] = 8
        selection["candidate_chain_evaluations"].append(fallback)
        selection["ranked_chain_ids"] = ["chain_001", "chain_002"]
        selection["omitted_candidates"] = [
            {"item_id": "theory_003", "reason": "Lower-ranked complete branch."}
        ]
        validate_target_selection(triage, selection)

        source = source_payload()
        source["material_records"][1]["statement_status"] = "major_issue"
        source["material_records"][1]["statement_findings"] = [
            "The provisional result is false."
        ]
        source["material_records"].append(
            {
                "item_id": "theory_003",
                "role": "theory_candidate",
                "source_label": "Theorem 2",
                "recovered_content": "For x >= 0, 2x >= 0.",
                "proof_reconstruction": "Multiply x >= 0 by two.",
                "statement_status": "clean",
                "statement_findings": [],
                "statement_repair": None,
                "proof_status": "clean",
                "proof_findings": [],
                "proof_repair": None,
                "external_classification": None,
                "source_spans": ["Theorem 2", "Proof of Theorem 2"],
                "statement_source_locations": [
                    {"start_line": 1, "end_line": 1, "label": "Theorem 2"}
                ],
                "proof_source_locations": [
                    {
                        "start_line": 1,
                        "end_line": 1,
                        "label": "Proof of Theorem 2",
                    }
                ],
                "depends_on": ["theory_001"],
                "is_added": False,
                "addition_reason": None,
            }
        )

        analysis = assemble_paper_analysis(triage, selection, source)
        self.assertEqual(analysis["derived"]["selected_chain_id"], "chain_002")
        self.assertTrue(analysis["derived"]["fallback_used"])
        self.assertFalse(analysis["derived"]["selected_target_blocked"])
        view = build_thread_b_view(analysis)
        self.assertEqual(
            view["target_selection"]["selected_candidate_ids"], ["theory_003"]
        )

    def test_upstream_candidate_can_remain_private_support(self) -> None:
        triage = triage_payload()
        triage["theory_inventory"].append(
            {
                "item_id": "theory_003",
                "role": "theory_candidate",
                "source_label": "Theorem 2",
                "summary": "States the final result.",
                "source_spans": ["Theorem 2"],
                "depends_on": ["theory_002"],
            }
        )
        selection = selection_payload()
        evaluation = selection["candidate_chain_evaluations"][0]
        evaluation["candidate_ids"] = ["theory_003"]
        evaluation["scientific_claim"] = "The final result holds."
        selection["selected_candidate_ids"] = ["theory_003"]
        selection["omitted_candidates"] = [
            {"item_id": "theory_002", "reason": "Private proof dependency."}
        ]
        validate_target_selection(triage, selection)

        source = source_payload()
        source["material_records"].append(
            {
                **json.loads(json.dumps(source["material_records"][1])),
                "item_id": "theory_003",
                "source_label": "Theorem 2",
                "recovered_content": "For x >= 0, x + 2 >= 2.",
                "proof_reconstruction": "Apply Theorem 1 and add one.",
                "depends_on": ["theory_002"],
            }
        )
        analysis = assemble_paper_analysis(triage, selection, source)
        view = build_thread_b_view(analysis)

        self.assertEqual(
            view["target_selection"]["selected_candidate_ids"], ["theory_003"]
        )
        self.assertEqual(
            {item["item_id"] for item in view["selected_material_records"]},
            {"theory_001", "theory_002", "theory_003"},
        )

    def test_transport_schemas_exclude_relay_unsupported_keywords(self) -> None:
        encoded = json.dumps(CONTRACT_SCHEMAS)
        self.assertNotIn('"allOf"', encoded)
        self.assertNotIn('"uniqueItems"', encoded)
        self.assertNotIn('"minProperties"', encoded)

        def check_strict_objects(value: Any, path: str = "$") -> None:
            if isinstance(value, dict):
                value_type = value.get("type")
                object_type = value_type == "object" or (
                    isinstance(value_type, list) and "object" in value_type
                )
                if object_type:
                    self.assertIs(
                        value.get("additionalProperties"),
                        False,
                        f"non-strict object at {path}",
                    )
                for key, child in value.items():
                    check_strict_objects(child, f"{path}.{key}")
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    check_strict_objects(child, f"{path}[{index}]")

        check_strict_objects(CONTRACT_SCHEMAS)

    def test_transport_schemas_have_no_dangling_local_refs(self) -> None:
        def check_refs(value: Any, definitions: dict[str, Any]) -> None:
            if isinstance(value, dict):
                reference = value.get("$ref")
                if isinstance(reference, str) and reference.startswith("#/$defs/"):
                    self.assertIn(reference.removeprefix("#/$defs/"), definitions)
                for child in value.values():
                    check_refs(child, definitions)
            elif isinstance(value, list):
                for child in value:
                    check_refs(child, definitions)

        for schema in CONTRACT_SCHEMAS.values():
            check_refs(schema, schema.get("$defs", {}))

    def test_source_audit_transport_schema_requires_result_audits(self) -> None:
        result_record = CONTRACT_SCHEMAS["stage3_source_audit"]["$defs"][
            "result_material_record"
        ]
        self.assertEqual(
            result_record["properties"]["statement_status"]["type"], "string"
        )
        self.assertEqual(
            result_record["properties"]["proof_status"]["type"], "string"
        )
        self.assertEqual(
            result_record["properties"]["proof_reconstruction"]["type"], "string"
        )

    def test_three_turn_thread_a_and_three_turn_thread_b(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = Path(temporary) / "paper_2026_001"
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "metadata.json").write_text(
                json.dumps({"paper_id": paper.name}), encoding="utf-8"
            )
            (private / "source.html").write_text(
                "<p>Definition 1. Let x >= 0.</p><p>Theorem 1. x+1 >= 1.</p>",
                encoding="utf-8",
            )
            agent = ScriptedAgent()
            validation = ScriptedValidation([], [])
            result = asyncio.run(
                Stage3Pipeline(agent, validation).run(
                    paper, formalization_only=True
                )
            )
            self.assertEqual(result.status, "formalized")
            self.assertEqual(
                [call.phase for call in agent.calls],
                [
                    "stage3_triage",
                    "stage3_target_selection",
                    "stage3_source_audit",
                    "stage3_compile",
                    "stage3_artifact_audit",
                    "stage3_complexity",
                ],
            )
            self.assertIsNone(agent.calls[0].resume_session_id)
            self.assertEqual(agent.calls[1].resume_session_id, "thread_a")
            self.assertEqual(agent.calls[2].resume_session_id, "thread_a")
            self.assertIsNone(agent.calls[3].resume_session_id)
            self.assertEqual(agent.calls[4].resume_session_id, "thread_b")
            self.assertEqual(agent.calls[5].resume_session_id, "thread_b")
            self.assertNotIn(
                "frozen_thread_b_view", agent.calls[4].context
            )
            self.assertNotIn(
                "audited_formalization_bundle", agent.calls[5].context
            )
            self.assertTrue((paper / "paper_analysis/paper_analysis.json").is_file())
            self.assertTrue((paper / "formalization/task.md").is_file())
            self.assertTrue(
                (paper / "formalization/proof_reconstruction_complexity.json").is_file()
            )

    def test_triage_audit_can_rescue_filtered_paper(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = Path(temporary) / "paper_2026_001"
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "metadata.json").write_text(
                json.dumps({"paper_id": paper.name}), encoding="utf-8"
            )
            (private / "source.html").write_text(
                "<p>Theorem 1. A substantive result holds.</p>", encoding="utf-8"
            )
            agent = TriageRescueAgent()
            result = asyncio.run(
                Stage3Pipeline(agent, ScriptedValidation([], [])).run(
                    paper, formalization_only=True
                )
            )

            self.assertEqual(result.status, "formalized")
            self.assertEqual(
                [call.phase for call in agent.calls[:4]],
                [
                    "stage3_triage",
                    "stage3_triage_audit",
                    "stage3_target_selection",
                    "stage3_source_audit",
                ],
            )
            self.assertEqual(
                agent.calls[2].resume_session_id, "triage_audit_thread"
            )

    def test_e2_exposure_revises_audits_and_reassesses_in_thread_b(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = Path(temporary) / "paper_2026_001"
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "metadata.json").write_text(
                json.dumps({"paper_id": paper.name}), encoding="utf-8"
            )
            (private / "source.html").write_text(
                "<p>Definition 1. Let x >= 0.</p><p>Theorem 1. x+1 >= 1.</p>",
                encoding="utf-8",
            )
            agent = ExposureRevisionAgent()
            result = asyncio.run(
                Stage3Pipeline(agent, ScriptedValidation([], [])).run(
                    paper, formalization_only=True
                )
            )

            self.assertEqual(result.status, "formalized")
            self.assertEqual(
                [call.phase for call in agent.calls],
                [
                    "stage3_triage",
                    "stage3_target_selection",
                    "stage3_source_audit",
                    "stage3_compile",
                    "stage3_artifact_audit",
                    "stage3_complexity",
                    "stage3_revision",
                    "stage3_artifact_audit",
                    "stage3_complexity",
                ],
            )
            for call in agent.calls[4:]:
                self.assertEqual(call.resume_session_id, "thread_b")
            complexity = json.loads(
                (paper / "formalization/proof_reconstruction_complexity.json")
                .read_text(encoding="utf-8")
            )
            self.assertEqual(complexity["status"], "scored")
            self.assertEqual(
                complexity["proof_reconstruction_complexity_level"], "PRC1"
            )

    def test_source_check_is_once_per_objection_and_returns_to_solver(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = Path(temporary) / "paper_2026_001"
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "metadata.json").write_text(
                json.dumps({"paper_id": paper.name}), encoding="utf-8"
            )
            (private / "source.html").write_text(
                "Definition 1 and Theorem 1 with its proof.", encoding="utf-8"
            )
            solver_results = [
                {
                    "status": "unscorable",
                    "reason": "The theorem appears under-specified.",
                    "answer": "- **Task status:** `unscorable`\n",
                },
                {
                    "status": "scorable",
                    "reason": "",
                    "answer": "- **Task status:** `scorable`\n",
                },
            ]
            reviewer_results = [
                {"status": "scorable", "report": {}, "exposures": []}
            ]
            agent = SourceCheckRevisionAgent()
            validation = ScriptedValidation(solver_results, reviewer_results)

            result = asyncio.run(Stage3Pipeline(agent, validation).run(paper))

            self.assertEqual(result.status, "completed")
            self.assertEqual(result.validation_feedback_count, 1)
            self.assertEqual(result.source_reaudit_count, 1)
            self.assertEqual(validation.calls, 2)
            self.assertEqual(
                sum(
                    call.phase == "stage3_local_source_check"
                    for call in agent.calls
                ),
                1,
            )
            self.assertEqual(
                sum(call.phase == "stage3_artifact_audit" for call in agent.calls),
                1,
            )
            revision_call = next(
                call for call in agent.calls if call.phase == "stage3_revision"
            )
            self.assertEqual(
                revision_call.context["downstream_objection"]["reason"],
                "The theorem appears under-specified.",
            )
            status = json.loads(
                (paper / "formalization/status.json").read_text(encoding="utf-8")
            )
            self.assertEqual(status["paper_classification"], "clean")

    def test_unresolved_source_check_after_two_feedbacks_maps_to_max_feedback(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = Path(temporary) / "paper_2026_001"
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "metadata.json").write_text(
                json.dumps({"paper_id": paper.name}), encoding="utf-8"
            )
            (private / "source.html").write_text(
                "Definition 1 and Theorem 1 with its proof.", encoding="utf-8"
            )
            validation = ScriptedValidation(
                [
                    {
                        "status": "unscorable",
                        "reason": "The first target wording is ambiguous.",
                        "answer": "- **Task status:** `unscorable`\n",
                    },
                    {
                        "status": "unscorable",
                        "reason": "The source support still appears insufficient.",
                        "answer": "- **Task status:** `unscorable`\n",
                    },
                ],
                [],
            )

            result = asyncio.run(
                Stage3Pipeline(
                    MaxFeedbackSourceCheckAgent(), validation
                ).run(paper)
            )

            self.assertEqual(result.status, "stopped")
            self.assertEqual(result.stop_reason, "max_validation_feedback")
            self.assertEqual(result.validation_feedback_count, 2)
            self.assertEqual(result.source_reaudit_count, 1)
            status = json.loads(
                (paper / "formalization/status.json").read_text(encoding="utf-8")
            )
            self.assertEqual(status["paper_classification"], "suspect")

    def test_evaluator_unscorable_stops_as_suspect(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = Path(temporary) / "paper_2026_001"
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "metadata.json").write_text(
                json.dumps({"paper_id": paper.name}), encoding="utf-8"
            )
            (private / "source.html").write_text(
                "Definition 1 and Theorem 1 with its proof.", encoding="utf-8"
            )
            validation = UnscorableEvaluatorValidation(
                [
                    {
                        "status": "scorable",
                        "reason": "",
                        "answer": "- **Task status:** `scorable`\n",
                    }
                ],
                [{"status": "scorable", "report": {}, "exposures": []}],
            )

            result = asyncio.run(
                Stage3Pipeline(ScriptedAgent(), validation).run(paper)
            )

            self.assertEqual(result.status, "stopped")
            self.assertEqual(result.stop_reason, "evaluator_unscorable")
            status = json.loads(
                (paper / "formalization/status.json").read_text(encoding="utf-8")
            )
            self.assertEqual(status["paper_classification"], "suspect")


if __name__ == "__main__":
    unittest.main()
