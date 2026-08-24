from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

WORKFLOW_ROOT = Path(__file__).resolve().parents[2]
if str(WORKFLOW_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKFLOW_ROOT))

from proof_experiment.llm_solver.run_llm_baseline import (
    ProviderConfig,
    TRANSIENT_RETRY_DELAYS_SECONDS,
    build_payload,
    extract_output_text,
    send_one_request,
)
from reviewer_and_evaluator.evaluator.run_evaluator import (
    build_evaluator_input,
    codex_command,
    evaluator_private_files,
    load_api_profile,
    validate_evaluation,
)
from reviewer_and_evaluator.reviewer.run_reviewer import (
    build_validity_input,
    validate_validity_report,
)
from runtime_support.experiment.summary_builder import build_paper_summary
from runtime_support.experiment.run_proof_batch import (
    discover_tasks,
    recover_solver_outputs,
    validate_resume_selection,
)
from runtime_support.experiment.run_utils import (
    normalize_obsidian_markdown,
    normalize_usage,
    require_initialized_run,
    split_self_assessment,
    update_run_task_stage,
)


def valid_complete_report() -> dict:
    return {
        "validity_status": "valid_complete",
        "theorem_contract": {
            "assumptions": ["A"],
            "target": "T",
            "quantifiers_and_scope": ["For every admissible x"],
        },
        "proof_steps": [
            {
                "step_id": "S1",
                "claim": "Establish T from A.",
                "depends_on": [],
                "support_status": "established",
                "reason": "The submitted derivation is valid.",
            }
        ],
        "findings": [],
        "adversarial_checks": [
            {
                "target": "S1",
                "test": "Check the boundary case.",
                "result": "attack_neutralized",
                "reason": "The assumptions cover it.",
                "related_finding_ids": [],
            }
        ],
        "summary": "The proof is complete.",
    }


def minor_issue_report() -> dict:
    report = valid_complete_report()
    report["validity_status"] = "valid_with_minor_issue"
    report["findings"] = [
        {
            "finding_id": "F1",
            "location": "Final display",
            "kind": "calculation_error",
            "status": "verified",
            "severity": "minor",
            "description": "A harmless constant is misstated.",
            "effect_on_proof": "A local correction completes the proof.",
        }
    ]
    return report


def major_gap_report() -> dict:
    report = valid_complete_report()
    report["validity_status"] = "incomplete_major_gap"
    report["proof_steps"][0]["support_status"] = "incorrect"
    report["findings"] = [
        {
            "finding_id": "F1",
            "location": "Core step C2",
            "kind": "invalid_implication",
            "status": "verified",
            "severity": "major",
            "description": "The submitted derivation of C2 is invalid.",
            "effect_on_proof": "C2 earns no proof credit.",
        }
    ]
    return report


class LLMRunnerTests(unittest.TestCase):
    def test_transient_retry_window_covers_short_provider_outages(self) -> None:
        self.assertGreaterEqual(sum(TRANSIENT_RETRY_DELAYS_SECONDS), 15 * 60)

    def test_provider_read_timeout_is_retried(self) -> None:
        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return None

            def read(self) -> bytes:
                return b'{"output_text":"proof"}'

        config = ProviderConfig(
            base_url="https://example.invalid/v1",
            api_key="secret",
            model="model",
            wire_api="responses",
            reasoning_effort="medium",
            max_output_tokens=100,
            timeout_seconds=10,
        )
        with (
            patch(
                "proof_experiment.llm_solver.run_llm_baseline."
                "TRANSIENT_RETRY_DELAYS_SECONDS",
                (0,),
            ),
            patch(
                "proof_experiment.llm_solver.run_llm_baseline.urllib.request.urlopen",
                side_effect=[TimeoutError("read timed out"), Response()],
            ),
            patch("proof_experiment.llm_solver.run_llm_baseline.time.sleep"),
        ):
            self.assertEqual(
                send_one_request(config, {"input": "task"})["output_text"],
                "proof",
            )

    def test_responses_payload_has_one_input_and_no_tools(self) -> None:
        config = ProviderConfig(
            base_url="https://example.invalid/v1",
            api_key="secret",
            model="model",
            wire_api="responses",
            reasoning_effort="medium",
            max_output_tokens=100,
            timeout_seconds=10,
        )
        payload = build_payload(config, "system", "task")
        self.assertEqual(payload["input"], "task")
        self.assertNotIn("tools", payload)
        self.assertEqual(payload["reasoning"], {"effort": "medium"})

    def test_extract_responses_output(self) -> None:
        response = {
            "output": [
                {
                    "type": "message",
                    "content": [{"type": "output_text", "text": "proof"}],
                }
            ]
        }
        self.assertEqual(extract_output_text(response, "responses"), "proof")

    def test_self_assessment_is_removed_for_evaluator(self) -> None:
        proof, assessment = split_self_assessment(
            "# Solution\n\n## Full Proof\n\nDone.\n\n"
            "## Self-Assessment\n\n- **Claimed score:** 10\n"
        )
        self.assertNotIn("Claimed score", proof)
        self.assertIn("Claimed score", assessment or "")

    def test_obsidian_math_delimiters_are_normalized(self) -> None:
        source = (
            "Inline \\(x\\).\n\\[\ny = x^2\n\\]\n\n"
            "```text\n\\(unchanged\\)\n```\n"
        )
        self.assertEqual(
            normalize_obsidian_markdown(source),
            "Inline $x$.\n$$\ny = x^2\n$$\n\n"
            "```text\n\\(unchanged\\)\n```\n",
        )

    def test_provider_can_read_protected_key_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            key_path = Path(temporary) / "api_key"
            key_path.write_text("secret-value\n", encoding="utf-8")
            os.chmod(key_path, 0o600)
            config = ProviderConfig.from_environment(
                {
                    "ML_THEORY_LLM_BASE_URL": "https://example.invalid/v1",
                    "ML_THEORY_LLM_API_KEY_FILE": str(key_path),
                    "ML_THEORY_LLM_MODEL": "model",
                },
                require_credentials=True,
            )
            self.assertEqual(config.api_key, "secret-value")

    def test_responses_usage_is_normalized(self) -> None:
        self.assertEqual(
            normalize_usage(
                {
                    "input_tokens": 100,
                    "input_tokens_details": {"cached_tokens": 40},
                    "output_tokens": 20,
                    "output_tokens_details": {"reasoning_tokens": 7},
                    "total_tokens": 120,
                }
            ),
            {
                "input_tokens": 100,
                "cached_input_tokens": 40,
                "non_cached_input_tokens": 60,
                "output_tokens": 20,
                "reasoning_output_tokens": 7,
                "total_tokens": 120,
            },
        )


class EvaluatorInputTests(unittest.TestCase):
    def test_private_files_come_from_task_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            theorem = Path(temporary) / "paper_2026_001/selected_theorems/theorem_001"
            public = theorem / "public_tasks/task_prove_theorem.md"
            rubric = theorem / "private_gt/rubric_prove_theorem.md"
            proof_gt = theorem / "private_gt/proof_ground_truth.md"
            original = theorem / "private_gt/theorem_statement_original.md"
            sanitized = theorem / "private_gt/theorem_statement_sanitized.md"
            assumptions = theorem / "private_gt/assumptions.md"
            citations = theorem / "private_gt/citations.md"
            public.parent.mkdir(parents=True)
            rubric.parent.mkdir(parents=True)
            public.write_text("task", encoding="utf-8")
            rubric.write_text("rubric", encoding="utf-8")
            proof_gt.write_text("proof", encoding="utf-8")
            original.write_text("original", encoding="utf-8")
            sanitized.write_text("sanitized", encoding="utf-8")
            assumptions.write_text("assumptions", encoding="utf-8")
            citations.write_text("citations", encoding="utf-8")
            metadata = {
                "tasks": [
                    {
                        "public_task_file": "public_tasks/task_prove_theorem.md",
                        "exposure_policy": "single_public_task_file_only",
                        "evaluator_private_files": [
                            "private_gt/theorem_statement_original.md",
                            "private_gt/theorem_statement_sanitized.md",
                            "private_gt/assumptions.md",
                            "private_gt/rubric_prove_theorem.md",
                            "private_gt/proof_ground_truth.md",
                            "private_gt/citations.md"
                        ],
                    }
                ]
            }
            (theorem / "task_metadata.json").write_text(
                json.dumps(metadata), encoding="utf-8"
            )
            root, files = evaluator_private_files(public)
            self.assertEqual(root, theorem.resolve())
            self.assertEqual(
                files,
                [
                    original.resolve(),
                    sanitized.resolve(),
                    assumptions.resolve(),
                    rubric.resolve(),
                    proof_gt.resolve(),
                    citations.resolve(),
                ],
            )
            rubric_root, rubric_files = evaluator_private_files(
                public, "rubric-only"
            )
            self.assertEqual(rubric_root, theorem.resolve())
            self.assertEqual(rubric_files, [rubric.resolve()])

            answer = Path(temporary) / "answer.md"
            answer.write_text(
                "# Solution\n\nProof.\n\n## Self-Assessment\n\nScore 10.\n",
                encoding="utf-8",
            )
            prompt = Path(temporary) / "prompt.md"
            prompt.write_text("Evaluate rigorously.", encoding="utf-8")
            validity = Path(temporary) / "validity.json"
            validity.write_text(
                json.dumps(valid_complete_report()), encoding="utf-8"
            )
            combined, exposures = build_evaluator_input(
                public, answer, validity, prompt, root, files
            )
            self.assertIn("Proof.", combined)
            self.assertNotIn("Score 10.", combined)
            self.assertIn("rubric", combined)
            self.assertIn("proof", combined)
            self.assertIn("valid_complete", combined)
            self.assertEqual(len(exposures), 10)

    def test_validity_reviewer_gets_no_private_reference_or_self_score(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            task = root / "task.md"
            answer = root / "answer.md"
            prompt = root / "prompt.md"
            task.write_text("Prove target T.", encoding="utf-8")
            answer.write_text(
                "# Proof\n\nArgument.\n\n## Self-Assessment\n\nScore: 10.\n",
                encoding="utf-8",
            )
            prompt.write_text("Review validity.", encoding="utf-8")
            combined, exposures = build_validity_input(task, answer, prompt)
            self.assertIn("Argument.", combined)
            self.assertNotIn("Score: 10", combined)
            self.assertNotIn("Ground-Truth", combined)
            self.assertEqual(len(exposures), 3)

    def test_evaluator_loads_protected_api_profile(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            profile = Path(temporary) / "profile"
            profile.mkdir(mode=0o700)
            config = profile / "config.toml"
            key = profile / "openai_api_key"
            config.write_text('model = "test-model"\n', encoding="utf-8")
            key.write_text("secret-value\n", encoding="utf-8")
            os.chmod(config, 0o600)
            os.chmod(key, 0o600)
            config_text, api_key, record = load_api_profile(profile)
            self.assertIn("test-model", config_text)
            self.assertEqual(api_key, "secret-value")
            self.assertNotIn(api_key, json.dumps(record))

    def test_codex_command_uses_supported_noninteractive_flags(self) -> None:
        class Args:
            codex_bin = "codex"
            model = "model"
            reasoning_effort = "high"

        command = codex_command(
            Args(), Path("/tmp/workspace"), Path("/tmp/schema.json"), Path("/tmp/out")
        )
        self.assertIn("--ephemeral", command)
        self.assertIn("read-only", command)
        self.assertNotIn("--ask-for-approval", command)


class ValidityContractTests(unittest.TestCase):
    def test_complete_validity_report_is_valid(self) -> None:
        report = valid_complete_report()
        self.assertEqual(validate_validity_report(report), report)

    def test_verified_break_requires_linked_major_finding(self) -> None:
        report = valid_complete_report()
        report["adversarial_checks"][0]["result"] = "break_found"
        with self.assertRaises(ValueError):
            validate_validity_report(report)

    def test_target_suspicion_requires_verified_blocking_finding(self) -> None:
        report = major_gap_report()
        report["validity_status"] = "target_suspected_invalid"
        with self.assertRaises(ValueError):
            validate_validity_report(report)

    def test_validity_proof_dependencies_must_be_acyclic(self) -> None:
        report = valid_complete_report()
        report["proof_steps"].append(
            {
                "step_id": "S2",
                "claim": "A second claim.",
                "depends_on": ["S1"],
                "support_status": "established",
                "reason": "Derived from S1.",
            }
        )
        report["proof_steps"][0]["depends_on"] = ["S2"]
        with self.assertRaises(ValueError):
            validate_validity_report(report)


class RunInitializationTests(unittest.TestCase):
    def test_uninitialized_run_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(FileNotFoundError):
                require_initialized_run(Path(temporary), "run_missing")

    def test_initialized_run_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run = Path(temporary) / "run_test"
            run.mkdir(parents=True)
            (run / "run.json").write_text(
                json.dumps({"run_id": "run_test", "tasks": {}}),
                encoding="utf-8",
            )
            self.assertEqual(
                require_initialized_run(Path(temporary), "run_test"),
                run.resolve(),
            )

    def test_task_stage_audit_is_stored_in_root_run_record(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run = Path(temporary) / "run_test"
            run.mkdir()
            (run / "run.json").write_text(
                json.dumps({"run_id": "run_test", "tasks": {}}),
                encoding="utf-8",
            )
            update_run_task_stage(
                run,
                "paper_2026_001",
                "theorem_003",
                "solver",
                {"status": "completed", "usage": {"input_tokens": 12}},
            )
            record = json.loads((run / "run.json").read_text(encoding="utf-8"))
            task = record["tasks"]["paper_2026_001/theorem_003"]
            self.assertEqual(task["paper_id"], "paper_2026_001")
            self.assertEqual(task["solver"]["usage"]["input_tokens"], 12)
            self.assertEqual(record["usage"]["solver"]["input_tokens"], 12)
            self.assertEqual(record["usage"]["total"]["input_tokens"], 12)

            update_run_task_stage(
                run,
                "paper_2026_001",
                "theorem_003",
                "validity_reviewer",
                {"status": "completed", "usage": {"output_tokens": 7}},
            )
            record = json.loads((run / "run.json").read_text(encoding="utf-8"))
            self.assertEqual(
                record["usage"]["validity_reviewer"]["output_tokens"], 7
            )
            self.assertEqual(record["usage"]["total"]["output_tokens"], 7)


class BatchRunnerTests(unittest.TestCase):
    def test_discovers_theorem_jobs_and_rejects_duplicate_papers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            data_root = Path(temporary)
            task = (
                data_root
                / "paper_2026_001/selected_theorems/theorem_003/public_tasks"
                / "task_prove_theorem.md"
            )
            task.parent.mkdir(parents=True)
            task.write_text("Prove the theorem.", encoding="utf-8")
            jobs = discover_tasks(data_root, ["paper_2026_001"])
            self.assertEqual(len(jobs), 1)
            self.assertEqual(jobs[0].theorem_id, "theorem_003")
            with self.assertRaises(ValueError):
                discover_tasks(data_root, ["paper_2026_001", "paper_2026_001"])

    def test_recovers_missing_evaluator_answer_from_full_answer(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            answer = root / "answer.md"
            evaluator_answer = root / "answer_for_evaluator.md"
            answer.write_text(
                "# Solution\n\nProof.\n\n## Self-Assessment\n\nScore: 8.\n",
                encoding="utf-8",
            )
            recover_solver_outputs(answer, evaluator_answer)
            self.assertEqual(
                evaluator_answer.read_text(encoding="utf-8"),
                "# Solution\n\nProof.\n",
            )

    def test_extended_resume_preserves_existing_selection(self) -> None:
        existing = {"paper_2026_001": ["theorem_001"]}
        requested = {
            "paper_2026_001": ["theorem_001"],
            "paper_2026_002": ["theorem_001", "theorem_002"],
        }
        validate_resume_selection(existing, requested, extend=True)

        with self.assertRaises(ValueError):
            validate_resume_selection(
                existing,
                {"paper_2026_002": ["theorem_001"]},
                extend=True,
            )
        with self.assertRaises(ValueError):
            validate_resume_selection(
                existing,
                {"paper_2026_001": ["theorem_002"]},
                extend=True,
            )

    def test_plain_resume_requires_exact_selection(self) -> None:
        existing = {"paper_2026_001": ["theorem_001"]}
        with self.assertRaises(ValueError):
            validate_resume_selection(
                existing,
                {
                    "paper_2026_001": ["theorem_001"],
                    "paper_2026_002": ["theorem_001"],
                },
                extend=False,
            )


class EvaluationContractTests(unittest.TestCase):
    def evaluation(self) -> dict:
        return {
            "evaluation_status": "scored",
            "score": 9,
            "verdict": "minor_repair",
            "validity_review_resolution": {
                "initial_status": "valid_with_minor_issue",
                "final_status": "valid_with_minor_issue",
                "finding_resolutions": [
                    {
                        "finding_id": "F1",
                        "resolution": "confirmed",
                        "final_severity": "minor",
                        "reason": "The constant error is a local repair.",
                    }
                ],
            },
            "core_step_evaluations": [
                {
                    "step_id": "C1",
                    "step": "Establish the main estimate.",
                    "origin": "rubric",
                    "depends_on": [],
                    "points_available": 5,
                    "points_awarded": 5,
                    "conclusion_status": "correct",
                    "proof_status": "correct",
                    "credit": "full",
                    "dependency_analysis": "No predecessor is required.",
                    "reason": "The estimate is proved.",
                },
                {
                    "step_id": "C2",
                    "step": "Conclude the target.",
                    "origin": "rubric",
                    "depends_on": ["C1"],
                    "points_available": 5,
                    "points_awarded": 4,
                    "conclusion_status": "correct",
                    "proof_status": "partial",
                    "credit": "partial",
                    "dependency_analysis": "C1 supplies the needed estimate.",
                    "reason": "Only a minor constant correction is needed.",
                },
            ],
            "added_core_steps": [],
            "assumption_and_tool_checks": [],
            "mathematical_errors": [],
            "alternative_proof": False,
            "justification": "Essentially correct.",
            "artifact_assessment": {
                "public_task_status": "clean",
                "ground_truth_status": "clean",
                "source_theorem_status": "appears_valid",
                "scoring_basis": "task_as_written",
                "repairs": [],
            },
            "reference_issue": "none",
            "needs_human_review": False,
            "human_review_reason": None,
        }

    def test_scored_evaluation_is_valid(self) -> None:
        value = self.evaluation()
        self.assertEqual(validate_evaluation(value, minor_issue_report()), value)

    def test_repairable_reference_gap_does_not_require_human_review(self) -> None:
        value = self.evaluation()
        value["reference_issue"] = "repairable_core_step_omission"
        value["added_core_steps"] = ["C2"]
        value["core_step_evaluations"][1]["origin"] = "evaluator_added"
        self.assertEqual(validate_evaluation(value, minor_issue_report()), value)

    def test_unrepairable_target_is_unscorable(self) -> None:
        value = self.evaluation()
        report = major_gap_report()
        report["validity_status"] = "target_suspected_invalid"
        report["findings"][0]["severity"] = "blocking"
        value.update(
            {
                "evaluation_status": "unscorable",
                "score": None,
                "verdict": "unscorable_target_error",
                "validity_review_resolution": {
                    "initial_status": "target_suspected_invalid",
                    "final_status": "target_invalid",
                    "finding_resolutions": [
                        {
                            "finding_id": "F1",
                            "resolution": "confirmed",
                            "final_severity": "blocking",
                            "reason": "The target fails under its stated assumptions.",
                        }
                    ],
                },
                "reference_issue": "unrepairable_target_error",
                "artifact_assessment": {
                    "public_task_status": "material_target_error",
                    "ground_truth_status": "material_error",
                    "source_theorem_status": "suspected_error",
                    "scoring_basis": "unscorable",
                    "repairs": [],
                },
                "needs_human_review": True,
                "human_review_reason": "The target is false under its assumptions.",
            }
        )
        self.assertEqual(validate_evaluation(value, report), value)

    def test_evaluator_may_upgrade_confirmed_major_finding_to_blocking(self) -> None:
        value = self.evaluation()
        report = major_gap_report()
        value.update(
            {
                "evaluation_status": "unscorable",
                "score": None,
                "verdict": "unscorable_target_error",
                "validity_review_resolution": {
                    "initial_status": "incomplete_major_gap",
                    "final_status": "target_invalid",
                    "finding_resolutions": [
                        {
                            "finding_id": "F1",
                            "resolution": "confirmed",
                            "final_severity": "blocking",
                            "reason": (
                                "The private references establish that the same "
                                "defect makes the target unscorable."
                            ),
                        }
                    ],
                },
                "reference_issue": "unrepairable_target_error",
                "artifact_assessment": {
                    "public_task_status": "material_target_error",
                    "ground_truth_status": "material_error",
                    "source_theorem_status": "suspected_error",
                    "scoring_basis": "unscorable",
                    "repairs": [],
                },
                "needs_human_review": True,
                "human_review_reason": (
                    "Private-reference adjudication upgrades the verified gap to a "
                    "blocking target defect."
                ),
            }
        )
        self.assertEqual(validate_evaluation(value, report), value)

    def test_true_but_unproved_predecessor_does_not_erase_downstream_credit(self) -> None:
        value = self.evaluation()
        value.update(
            {
                "score": 5,
                "verdict": "substantial_partial_progress",
                "validity_review_resolution": {
                    "initial_status": "incomplete_major_gap",
                    "final_status": "incomplete_major_gap",
                    "finding_resolutions": [
                        {
                            "finding_id": "F1",
                            "resolution": "confirmed",
                            "final_severity": "major",
                            "reason": "The proof of C2 is invalid.",
                        }
                    ],
                },
                "core_step_evaluations": [
                    {
                        "step_id": "C2",
                        "step": "Prove the intermediate conclusion C2.",
                        "origin": "rubric",
                        "depends_on": [],
                        "points_available": 5,
                        "points_awarded": 0,
                        "conclusion_status": "correct",
                        "proof_status": "incorrect",
                        "credit": "none",
                        "dependency_analysis": "C2 is true, but its proof is invalid.",
                        "reason": "No credit for proving C2.",
                    },
                    {
                        "step_id": "C3",
                        "step": "Derive C3 from C2.",
                        "origin": "rubric",
                        "depends_on": ["C2"],
                        "points_available": 5,
                        "points_awarded": 5,
                        "conclusion_status": "correct",
                        "proof_status": "correct",
                        "credit": "full",
                        "dependency_analysis": "The conditional derivation C2 implies C3 is valid.",
                        "reason": "The downstream proof step is complete.",
                    },
                ],
            }
        )
        self.assertEqual(validate_evaluation(value, major_gap_report()), value)

    def test_uncertain_predecessor_does_not_erase_conditional_downstream_credit(self) -> None:
        value = self.evaluation()
        value.update(
            {
                "score": 5,
                "verdict": "substantial_partial_progress",
                "validity_review_resolution": {
                    "initial_status": "incomplete_major_gap",
                    "final_status": "incomplete_major_gap",
                    "finding_resolutions": [
                        {
                            "finding_id": "F1",
                            "resolution": "confirmed",
                            "final_severity": "major",
                            "reason": "The predecessor was not established.",
                        }
                    ],
                },
                "core_step_evaluations": [
                    {
                        "step_id": "C2",
                        "step": "Establish C2.",
                        "origin": "rubric",
                        "depends_on": [],
                        "points_available": 5,
                        "points_awarded": 0,
                        "conclusion_status": "uncertain",
                        "proof_status": "missing",
                        "credit": "none",
                        "dependency_analysis": "C2 is not established.",
                        "reason": "No proof is supplied.",
                    },
                    {
                        "step_id": "C3",
                        "step": "Derive C3 conditionally from C2.",
                        "origin": "rubric",
                        "depends_on": ["C2"],
                        "points_available": 5,
                        "points_awarded": 5,
                        "conclusion_status": "correct",
                        "proof_status": "correct",
                        "credit": "full",
                        "dependency_analysis": "The conditional implication is valid.",
                        "reason": "The downstream derivation is complete.",
                    },
                ],
            }
        )
        self.assertEqual(validate_evaluation(value, major_gap_report()), value)

    def test_target_suspicion_may_be_explicitly_dismissed(self) -> None:
        report = major_gap_report()
        report["validity_status"] = "target_suspected_invalid"
        report["findings"][0].update(
            {
                "kind": "target_counterexample",
                "status": "verified",
                "severity": "blocking",
            }
        )
        value = self.evaluation()
        value.update(
            {
                "score": 10,
                "verdict": "fully_correct",
                "validity_review_resolution": {
                    "initial_status": "target_suspected_invalid",
                    "final_status": "valid_complete",
                    "finding_resolutions": [
                        {
                            "finding_id": "F1",
                            "resolution": "dismissed",
                            "final_severity": "none",
                            "reason": "The public task explicitly permits this alternative conclusion.",
                        }
                    ],
                },
            }
        )
        for step in value["core_step_evaluations"]:
            step["points_awarded"] = step["points_available"]
            step["proof_status"] = "correct"
            step["credit"] = "full"
        self.assertEqual(validate_evaluation(value, report), value)

    def test_target_suspicion_may_use_an_accepted_task_alternative(self) -> None:
        report = major_gap_report()
        report["validity_status"] = "target_suspected_invalid"
        report["findings"][0].update(
            {
                "kind": "target_counterexample",
                "status": "verified",
                "severity": "blocking",
            }
        )
        value = self.evaluation()
        value.update(
            {
                "score": 10,
                "verdict": "fully_correct",
                "validity_review_resolution": {
                    "initial_status": "target_suspected_invalid",
                    "final_status": "valid_complete",
                    "finding_resolutions": [
                        {
                            "finding_id": "F1",
                            "resolution": "accepted_task_alternative",
                            "final_severity": "none",
                            "reason": "The task expressly permits a rigorous counterexample route.",
                        }
                    ],
                },
            }
        )
        for step in value["core_step_evaluations"]:
            step["points_awarded"] = step["points_available"]
            step["proof_status"] = "correct"
            step["credit"] = "full"
        self.assertEqual(validate_evaluation(value, report), value)

    def test_false_predecessor_blocks_dependent_downstream_credit(self) -> None:
        value = self.evaluation()
        value.update(
            {
                "score": 5,
                "verdict": "substantial_partial_progress",
                "validity_review_resolution": {
                    "initial_status": "incomplete_major_gap",
                    "final_status": "incomplete_major_gap",
                    "finding_resolutions": [
                        {
                            "finding_id": "F1",
                            "resolution": "confirmed",
                            "final_severity": "major",
                            "reason": "C2 is false.",
                        }
                    ],
                },
                "core_step_evaluations": [
                    {
                        "step_id": "C2",
                        "step": "Establish C2.",
                        "origin": "rubric",
                        "depends_on": [],
                        "points_available": 5,
                        "points_awarded": 0,
                        "conclusion_status": "incorrect",
                        "proof_status": "incorrect",
                        "credit": "none",
                        "dependency_analysis": "C2 is false.",
                        "reason": "The step fails.",
                    },
                    {
                        "step_id": "C3",
                        "step": "Use C2 to conclude C3.",
                        "origin": "rubric",
                        "depends_on": ["C2"],
                        "points_available": 5,
                        "points_awarded": 5,
                        "conclusion_status": "correct",
                        "proof_status": "correct",
                        "credit": "full",
                        "dependency_analysis": "This derivation relies on C2.",
                        "reason": "Formal manipulation only.",
                    },
                ],
            }
        )
        with self.assertRaises(ValueError):
            validate_evaluation(value, major_gap_report())

    def test_paper_summary_reads_flat_theorem_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run = Path(temporary)
            paper = run / "paper_2026_001"
            theorem = paper / "theorem_003"
            theorem.mkdir(parents=True)
            (theorem / "evaluation.json").write_text(
                json.dumps(self.evaluation()), encoding="utf-8"
            )
            run_record = {
                "tasks": {
                    "paper_2026_001/theorem_003": {
                        "paper_id": "paper_2026_001",
                        "theorem_id": "theorem_003",
                        "validity_reviewer": {"status": "completed"},
                        "evaluator": {"status": "completed"},
                    },
                    "paper_2026_001/theorem_004": {
                        "paper_id": "paper_2026_001",
                        "theorem_id": "theorem_004",
                        "validity_reviewer": {"status": "completed"},
                        "evaluator": {"status": "failed"},
                    },
                }
            }
            build_paper_summary(
                run,
                run_record,
                "paper_2026_001",
                ["theorem_003", "theorem_004"],
            )
            summary = json.loads(
                (paper / "summary.json").read_text(encoding="utf-8")
            )
            self.assertEqual(summary["evaluated_theorem_count"], 1)
            self.assertEqual(summary["theorems"][0]["theorem_id"], "theorem_003")
            self.assertEqual(summary["mean_score"], 9)
            self.assertEqual(summary["status"], "partial")
            self.assertEqual(summary["failed_theorems"], ["theorem_004"])


if __name__ == "__main__":
    unittest.main()
