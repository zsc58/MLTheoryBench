from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
from calibrated_pipeline import (  # noqa: E402
    checker_input, run_calibrated_paper, run_checker, validate_checker,
)
from paired_pipeline import (  # noqa: E402
    ArtifactBundle, PaperInput, SolverSpec, audit_quality_summary, run_solver,
    validate_task_audit_result,
)
from bare_model import ProviderConfig  # noqa: E402
from run_comparison import build_summary  # noqa: E402


class CalibratedPipelineTests(unittest.TestCase):
    def test_audit_allows_routine_repairs_without_weakening_source_fidelity(self):
        prompt = (ROOT / "prompts/task_audit.md").read_text()
        self.assertIn("routine derivations, elementary estimates, or local case splits", prompt)
        self.assertIn("do not by themselves establish a source-paper error", prompt)
        self.assertIn("identify the exact dependency or gap in the private reference proof", prompt)
        self.assertIn("do not use these rules to add a genuinely substantive assumption", prompt)
        self.assertIn("no new substantive mathematical idea, structural assumption", prompt)
        self.assertNotIn("the repair needs no new lemma, estimate", prompt)

    def test_frozen_prompt_only_removes_objection_instructions(self):
        original = (ROOT / "prompts/solver_system_prompt.md").read_text()
        frozen = (ROOT / "prompts/frozen_solver_system_prompt.md").read_text()
        start = original.index("## 1. Validate The Task Contract")
        end = original.index("## 2. Standard Background Results")
        expected = original[:start] + original[end:]
        expected = expected.replace("proof, partial proof, or concrete task objection", "proof or partial proof")
        expected = re.sub(r"## ([2-7])\.", lambda match: f"## {int(match[1])-1}.", expected)
        self.assertEqual(expected, frozen)
        original_template = (ROOT / "prompts/solver_answer_template.md").read_text()
        self.assertEqual(
            "\n".join(line for line in original_template.splitlines()
                      if not line.startswith(("- **Task status:", "- **Unscorable reason:"))) + "\n",
            (ROOT / "prompts/frozen_solver_answer_template.md").read_text(),
        )

    def test_checker_copies_existing_mathematical_standards(self):
        original = (ROOT / "prompts/solver_system_prompt.md").read_text()
        checker = (ROOT / "prompts/task_checker.md").read_text()
        for start, end in (("## 2. Standard Background Results", "## 3. Claim Discipline"),
                           ("## 3. Claim Discipline", "## 4. Organize And Prioritize The Proof")):
            self.assertIn(original[original.index(start):original.index(end)].strip(), checker)
        contract = original[original.index("Before proving"):original.index("## 2.")].strip()
        self.assertIn(contract, checker)

    def make_paper(self, root):
        source = root / "original"
        source.mkdir()
        files = {}
        for name, content in {
            "task.md": "# Task\nProve x=x.", "proof_ground_truth.md": "PRIVATE_GT_MARKER",
            "rubric.md": "PRIVATE_RUBRIC_MARKER", "provenance.json": "{}",
            "thread_b_view.json": '{"selected_material_records": []}',
        }.items():
            path = source / name
            path.write_text(content)
            files["formalization/thread_b_view.json" if name == "thread_b_view.json" else name] = path
        return PaperInput("paper_test", "completed", source, files, True)

    def test_checker_exposure_is_only_task_and_gt(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            paper = self.make_paper(root)
            text = checker_input(ArtifactBundle(0, paper.source_root))
            self.assertIn("PRIVATE_GT_MARKER", text)
            self.assertIn("Prove x=x", text)
            self.assertNotIn("PRIVATE_RUBRIC_MARKER", text)
            self.assertNotIn("selected_material_records", text)

    def test_checker_report_consistency(self):
        validate_checker({"status": "inconclusive", "summary": "Cannot resolve.", "findings": []})
        with self.assertRaises(ValueError):
            validate_checker({"status": "issues_found", "summary": "Wrong.", "findings": []})

    def test_checker_uses_a_fresh_thread_and_latest_artifacts(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            paper = self.make_paper(root)
            report = {"status": "no_issue_found", "summary": "Checked.", "findings": []}
            with patch("calibrated_pipeline.run_json_agent", return_value=(report, {}, {})) as call:
                for index in (1, 2):
                    (paper.source_root / "task.md").write_text(f"LATEST_TASK_{index}")
                    run_checker(ArtifactBundle(index, paper.source_root), root / f"check_{index}", Mock())
            for index, request in enumerate(call.call_args_list, 1):
                self.assertNotIn("thread", request.kwargs)
                self.assertIn(f"LATEST_TASK_{index}", request.kwargs["inputs"])
                exposure = json.loads((root / f"check_{index}/exposure.json").read_text())
                self.assertTrue(exposure["fresh_thread"])
                self.assertFalse(exposure["previous_checker_visible"])

    def exercise(self, checker_status="no_issue_found", audit_status="invalid_objection",
                 reviewer_invalid=False, evaluator_invalid=False, empty=False,
                 gt_warning=None, checker_sequence=None, proactive_repair=False):
        with tempfile.TemporaryDirectory() as temp, ExitStack() as stack:
            root = Path(temp)
            paper = self.make_paper(root)
            thread = Mock()
            stack.enter_context(patch("calibrated_pipeline.create_agent_thread", return_value=thread))
            audits = stack.enter_context(patch("calibrated_pipeline.run_task_audit", side_effect=[
                ({"status": "formalization_error_fixed" if proactive_repair else "artifacts_verified"}, {"input_tokens": 3}),
                ({"status": audit_status, "gt_quality_warning": gt_warning}, {"input_tokens": 4}),
                ({"status": audit_status, "gt_quality_warning": gt_warning}, {"input_tokens": 4}),
            ]))
            statuses = checker_sequence or ([checker_status, "no_issue_found"]
                                           if checker_status != "no_issue_found" else [checker_status])
            reports = [{"status": status, "summary": "All findings.",
                        "findings": [{"finding_id": "F1"}, {"finding_id": "F2"}]
                        if status == "issues_found" else []} for status in statuses]
            checks = stack.enter_context(patch("calibrated_pipeline.run_checker",
                side_effect=[(report, {"input_tokens": 2}) for report in reports]))
            def repaired(bundle, audit, output, paper):
                import shutil
                new = output / f"task_versions/revision_{bundle.revision + 1}"
                shutil.copytree(bundle.root, new)
                (new / "task.md").write_text(f"REPAIRED_TASK_{bundle.revision + 1}")
                return ArtifactBundle(bundle.revision + 1, new)
            stack.enter_context(patch("calibrated_pipeline.apply_audit_replacements", side_effect=repaired))
            solvers = stack.enter_context(patch("calibrated_pipeline.run_all_solvers", return_value={
                "a": {"solver_outcome": "no_final_answer" if empty else "final_answer", "usage": {"output_tokens": 5}},
                "b": {"solver_outcome": "no_final_answer" if empty else "final_answer", "usage": {"output_tokens": 6}},
            }))
            reviewer = stack.enter_context(patch("calibrated_pipeline.run_paired_reviewer", return_value=({
                "answer_a": {"validity_status": "target_suspected_invalid" if reviewer_invalid else "valid_complete"},
                "answer_b": {"validity_status": "valid_complete"},
            }, {"input_tokens": 7})))
            evaluator = stack.enter_context(patch("calibrated_pipeline.run_paired_evaluator", return_value=({
                "answer_a": {"evaluation_status": "unscorable" if evaluator_invalid else "scored", "score": None if evaluator_invalid else 9},
                "answer_b": {"evaluation_status": "scored", "score": 10},
            }, {"input_tokens": 8})))
            result = run_calibrated_paper(paper, "test", root / "run",
                                          [Mock(label="a"), Mock(label="b")], Mock(), Mock())
            self.assertEqual((paper.source_root / "task.md").read_text(), "# Task\nProve x=x.")
            thread.close.assert_called_once()
            if audit_status == "paper_issue_confirmed" and statuses[0] != "no_issue_found":
                solvers.assert_not_called()
                reviewer.assert_not_called()
                evaluator.assert_not_called()
                self.assertEqual(result["stop_reason"], "paper_issue")
                return
            self.assertEqual(checks.call_count, len(statuses))
            self.assertEqual(result["checker_count"], len(statuses))
            self.assertEqual(result["calibration_feedback_count"], len(statuses) - 1)
            self.assertEqual(audits.call_count, len(statuses))
            self.assertEqual(result["usage"]["task_checker"]["input_tokens"], 2 * len(statuses))
            for index, call in enumerate(audits.call_args_list[1:]):
                self.assertIs(audits.call_args_list[0].args[5], call.args[5])
                self.assertFalse(call.kwargs["include_full_source"])
                self.assertEqual(call.args[2][0]["report"], reports[index])
            if statuses[-1] != "no_issue_found":
                solvers.assert_not_called()
                reviewer.assert_not_called()
                evaluator.assert_not_called()
                self.assertEqual(result["stop_reason"], "max_checker_feedback")
                self.assertEqual(result["calibration_quality"]["status"], "not_passed")
                self.assertEqual(result["checker_history"][-1]["status"], statuses[-1])
                self.assertFalse((root / "run/frozen_artifacts.json").exists())
                return result
            solvers.assert_called_once()
            self.assertTrue(solvers.call_args.kwargs["frozen_task"])
            self.assertEqual(result["validation_feedback_count"], 0)
            if empty:
                reviewer.assert_not_called()
                evaluator.assert_not_called()
                self.assertEqual(result["scores"], {"a": 0, "b": 0})
            else:
                evaluator.assert_called_once()
                if evaluator_invalid:
                    self.assertEqual(result["stop_reason"], "evaluator_unscorable")
                    self.assertEqual(result["scores"], {})
                else:
                    self.assertEqual(result["status"], "completed")
            frozen = json.loads((root / "run/frozen_artifacts.json").read_text())
            self.assertFalse(frozen["formal_feedback_enabled"])
            self.assertEqual(frozen["checker_revision"], frozen["task_revision"])
            self.assertEqual(frozen["checker_status"], "no_issue_found")
            self.assertEqual(frozen["post_feedback_checker_rerun"], len(statuses) > 1)
            self.assertEqual(frozen["sha256"], result["checker_history"][-1]["sha256"])
            self.assertEqual(solvers.call_args.args[1].revision, frozen["checker_revision"])
            self.assertEqual(frozen["calibration_quality"], result["calibration_quality"])
            self.assertEqual(result["calibration_quality"]["status"],
                             "pass_with_gt_warning" if gt_warning else "pass")
            self.assertEqual(result["calibration_quality"]["gt_quality_warning"], gt_warning)
            return result

    def test_no_issue_proceeds_without_repair(self):
        self.exercise()

    def test_inconclusive_requires_audit_and_new_checker(self):
        self.exercise(checker_status="inconclusive")

    def test_all_findings_return_to_same_thread_then_recheck(self):
        self.exercise(checker_status="issues_found", audit_status="formalization_error_fixed")

    def test_invalid_objection_requires_new_check_without_revision(self):
        self.exercise(checker_status="issues_found")

    def test_two_repairs_and_final_check_allow_revision_three(self):
        result = self.exercise(checker_sequence=["issues_found", "issues_found", "no_issue_found"],
                               audit_status="formalization_error_fixed", proactive_repair=True)
        self.assertEqual(result["task_revision"], 3)
        self.assertEqual([item["task_revision"] for item in result["checker_history"]], [1, 2, 3])

    def test_final_check_issues_stop_before_solver(self):
        self.exercise(checker_sequence=["issues_found"] * 3,
                      audit_status="formalization_error_fixed", proactive_repair=True)

    def test_final_check_inconclusive_stops_before_solver(self):
        self.exercise(checker_sequence=["issues_found", "issues_found", "inconclusive"])

    def test_unrepaired_objection_cannot_bypass_final_check(self):
        result = self.exercise(checker_sequence=["issues_found"] * 3)
        self.assertEqual(result["task_revision"], 0)

    def test_source_issue_stops_before_formal_solver(self):
        self.exercise(checker_status="issues_found", audit_status="paper_issue_confirmed")

    def test_reviewer_and_evaluator_never_reopen_audit(self):
        self.exercise(reviewer_invalid=True)
        self.exercise(reviewer_invalid=True, evaluator_invalid=True)

    def test_all_empty_answers_are_zero_without_judges(self):
        self.exercise(empty=True)

    def test_gt_warning_survives_freezing_and_scoring(self):
        warning = {"public_task_verified": True, "affected_checks": ["validity"],
                   "unresolved_obligations": ["Specialized reference lemma remains unproved."]}
        self.exercise(checker_status="issues_found", audit_status="formalization_error_fixed",
                      gt_warning=warning)

    def test_gt_quality_validation(self):
        import copy

        schema = json.loads((ROOT / "schemas/task_audit.schema.json").read_text())
        result = {
            "status": "formalization_error_fixed", "explanation": "Repaired.",
            "affected_material_ids": [], "source_issue_check": None,
            "corrected_material_records": None,
            "replacements": {"task_md": None, "proof_ground_truth_md": "Proof with an explicit gap.",
                             "rubric_md": None, "provenance": None},
            "self_audit": {name: {"status": "pass", "evidence": "Verified."}
                           for name in schema["$defs"]["checks"]["required"]},
            "gt_quality_warning": None,
        }
        validate_task_audit_result(result, schema)
        self.assertEqual(audit_quality_summary(result)["status"], "pass")
        result["self_audit"]["validity"] = {"status": "fail", "evidence": "GT lemma unproved."}
        with self.assertRaisesRegex(ValueError, "explicit GT-only"):
            validate_task_audit_result(result, schema)
        result["gt_quality_warning"] = {
            "public_task_verified": True, "affected_checks": ["validity"],
            "unresolved_obligations": ["Derive the specialized bound in GT section 2."],
        }
        validate_task_audit_result(result, schema)
        self.assertEqual(audit_quality_summary(result)["status"], "pass_with_gt_warning")
        for mutation in ("extra_task_failure", "unverified_task", "mismatched_checks",
                         "duplicate_checks", "blank_obligation", "missing_self_audit",
                         "disallowed_check", "paper_issue"):
            bad = copy.deepcopy(result)
            if mutation == "extra_task_failure":
                bad["self_audit"]["definition_integrity"]["status"] = "fail"
            elif mutation == "unverified_task":
                bad["gt_quality_warning"]["public_task_verified"] = False
            elif mutation == "mismatched_checks":
                bad["gt_quality_warning"]["affected_checks"] = ["self_containment"]
            elif mutation == "duplicate_checks":
                bad["gt_quality_warning"]["affected_checks"] *= 2
            elif mutation == "blank_obligation":
                bad["gt_quality_warning"]["unresolved_obligations"] = ["  "]
            elif mutation == "missing_self_audit":
                bad["self_audit"] = None
            elif mutation == "disallowed_check":
                bad["gt_quality_warning"]["affected_checks"] = ["anti_leakage"]
            else:
                bad.update(status="paper_issue_confirmed", replacements=None, source_issue_check={
                    "complete_chain_context_checked": True, "standing_assumptions_checked": True,
                    "counterexample_satisfies_complete_source_contract": True,
                    "local_clarification_or_repair_suffices": False, "evidence": "Confirmed source defect.",
                })
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                validate_task_audit_result(bad, schema)
        for status in ("artifacts_verified", "invalid_objection"):
            unchanged = copy.deepcopy(result)
            unchanged.update(status=status, replacements=None)
            validate_task_audit_result(unchanged, schema)

    def test_summary_distinguishes_calibration_quality(self):
        with tempfile.TemporaryDirectory() as temp:
            summary = build_summary(Path(temp), [
                {"status": "completed", "calibration_quality": {"status": "pass"}},
                {"status": "completed", "calibration_quality": {"status": "pass_with_gt_warning"}},
                {"status": "stopped", "calibration_quality": {"status": "not_passed"}},
                {"status": "failed"},
            ])
        self.assertEqual(summary["calibration_quality_counts"],
                         {"pass": 1, "pass_with_gt_warning": 1, "not_passed": 1})

    def test_formal_solver_never_receives_gt_or_checker_and_does_not_parse_status(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            paper = self.make_paper(root)
            config = ProviderConfig("https://example.invalid/v1", "test", "model", "responses", "high", 48000, 60, True)
            response = {"output_text": "# Solution\nProof.\n\n## Self-Assessment\n- **Claimed score:** `1`",
                        "usage": {"input_tokens": 2, "output_tokens": 3}}
            with patch("paired_pipeline.recorded_solver_request", return_value=response) as request:
                result = run_solver(SolverSpec("test", config), ArtifactBundle(0, paper.source_root), root / "out", frozen_task=True)
            payload = json.dumps(request.call_args.args[1])
            self.assertNotIn("PRIVATE_GT_MARKER", payload)
            self.assertNotIn("PRIVATE_RUBRIC_MARKER", payload)
            self.assertNotIn("Task status", payload)
            self.assertEqual(result["task_status"], "not_requested")
            self.assertNotIn("Claimed score", result["proof"])


if __name__ == "__main__":
    unittest.main()
