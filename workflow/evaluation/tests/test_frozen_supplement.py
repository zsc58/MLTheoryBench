from __future__ import annotations

import json
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "runtime"))

from calibrated_pipeline import artifact_hashes
from paired_pipeline import ArtifactBundle
from run_frozen_supplement import (
    completed_papers, copy_frozen_bundle, follow_completed, run_supplement,
)
from support import atomic_write_json


class FrozenSupplementTests(unittest.TestCase):
    def paper(self, root: Path, paper_id="paper_2026_001") -> Path:
        paper = root / "papers" / paper_id
        bundle = ArtifactBundle(2, paper / "task_versions/revision_2")
        bundle.root.mkdir(parents=True)
        for name, content in {
            "task.md": "# Task\nLatest frozen task.",
            "proof_ground_truth.md": "PRIVATE_GT",
            "rubric.md": "PRIVATE_RUBRIC",
            "provenance.json": "{}",
            "thread_b_view.json": "{}",
        }.items():
            (bundle.root / name).write_text(content)
        atomic_write_json(paper / "frozen_artifacts.json", {
            "task_revision": 2, "checker_revision": 2,
            "checker_status": "no_issue_found", "sha256": artifact_hashes(bundle),
            "calibration_quality": {"status": "pass_with_gt_warning", "gt_quality_warning": {"reason": "Gap"}},
        })
        atomic_write_json(paper / "result.json", {
            "paper_id": paper_id, "status": "completed", "task_revision": 2,
            "cohort": "suspect", "scores": {"other_solver": 10},
        })
        return paper

    def test_only_completed_upstream_papers_are_discovered(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.paper(root)
            stopped = self.paper(root, "paper_2026_002")
            atomic_write_json(stopped / "result.json", {"status": "stopped"})
            atomic_write_json(root / "run.json", {"paper_ids": ["paper_2026_001", "paper_2026_002", "paper_2026_003"]})
            self.assertEqual(completed_papers(root), ["paper_2026_001"])
            self.paper(root, "paper_2026_003")
            self.assertEqual(completed_papers(root), ["paper_2026_001", "paper_2026_003"])

    def test_copy_preserves_latest_revision_without_source_answers(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.paper(root / "upstream")
            bundle, reference = copy_frozen_bundle(source, root / "out")
            self.assertEqual(bundle.revision, 2)
            self.assertEqual(bundle.task.read_text(), "# Task\nLatest frozen task.")
            self.assertEqual(artifact_hashes(bundle), reference["sha256"])
            self.assertNotIn("scores", reference)
            self.assertEqual(reference["calibration_quality"]["status"], "pass_with_gt_warning")
            self.assertFalse((root / "out/task_versions/revision_0").exists())
            (source / "task_versions/revision_2/task.md").write_text("Changed")
            with self.assertRaisesRegex(ValueError, "frozen source changed"):
                copy_frozen_bundle(source, root / "other")

    def exercise(self, outcome="final_answer", error=False, unscorable=False):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.paper(root / "upstream")
            before = artifact_hashes(ArtifactBundle(2, source / "task_versions/revision_2"))
            spec = Mock(label="glm53")
            with patch("run_frozen_supplement.run_solver", return_value={
                "solver_outcome": outcome, "proof": "Proof", "usage": {"output_tokens": 48000},
            }, side_effect=RuntimeError("HTTP 502") if error else None) as solver, \
                 patch("run_frozen_supplement.run_paired_reviewer", return_value=({"answer_a": {}}, {"input_tokens": 3})) as reviewer, \
                 patch("run_frozen_supplement.run_paired_evaluator", return_value=({"answer_a": {
                     "evaluation_status": "unscorable" if unscorable else "scored", "score": None if unscorable else 7,
                 }}, {"input_tokens": 4})) as evaluator:
                result = run_supplement(source, root / "out", spec, Mock())
                self.assertTrue(solver.call_args.kwargs["frozen_task"])
                self.assertEqual(solver.call_args.args[1].revision, 2)
                self.assertEqual(before, artifact_hashes(ArtifactBundle(2, source / "task_versions/revision_2")))
                if error:
                    self.assertEqual(result["status"], "failed")
                    self.assertEqual(result["scores"], {})
                    reviewer.assert_not_called()
                    evaluator.assert_not_called()
                elif outcome == "no_final_answer":
                    self.assertEqual(result["status"], "completed")
                    self.assertEqual(result["scores"], {"glm53": 0})
                    self.assertEqual(result["usage"]["reviewer"], {})
                    reviewer.assert_not_called()
                    evaluator.assert_not_called()
                    self.assertFalse((root / "out/rounds/round_0/paired_evaluator.json").exists())
                else:
                    reviewer.assert_called_once()
                    evaluator.assert_called_once()
                    self.assertEqual(reviewer.call_args.args[1], {"answer_a": "glm53"})
                    self.assertEqual(set(reviewer.call_args.args[2]), {"glm53"})
                    self.assertEqual(result["scores"], {} if unscorable else {"glm53": 7})
                    self.assertEqual(result["status"], "stopped" if unscorable else "completed")
                self.assertFalse(result["formal_feedback_enabled"])

    def test_empty_answer_skips_both_judges(self):
        self.exercise(outcome="no_final_answer")

    def test_answer_is_scored_independently(self):
        self.exercise()

    def test_transport_failure_is_not_zero(self):
        self.exercise(error=True)

    def test_unscorable_is_a_stop_without_repair(self):
        self.exercise(unscorable=True)

    def test_follow_adds_new_completions_without_duplicates_and_bounds_workers(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            upstream = root / "upstream"
            upstream.mkdir()
            atomic_write_json(upstream / "run.json", {"status": "running"})
            output = root / "out"
            output.mkdir()
            calls, running, peak = [], 0, 0
            lock = threading.Lock()
            def worker(source, dest, spec, judge):
                nonlocal running, peak
                with lock:
                    calls.append(source.name)
                    running += 1
                    peak = max(peak, running)
                time.sleep(0.02)
                with lock:
                    running -= 1
                    if len(calls) == 5 and running == 0:
                        atomic_write_json(upstream / "run.json", {"status": "completed"})
                return {"paper_id": source.name, "status": "completed", "scores": {"glm53": 0}}
            def discover(_):
                return [f"paper_2026_{i:03d}" for i in range(1, 6 if calls else 3)]
            with patch("run_frozen_supplement.completed_papers", side_effect=discover), \
                 patch("run_frozen_supplement.run_supplement", side_effect=worker):
                results = follow_completed(upstream, output, Mock(), Mock(), workers=2,
                                           follow=True, poll_seconds=0.005)
            self.assertEqual(len(results), 5)
            self.assertEqual(len(set(calls)), 5)
            self.assertEqual(peak, 2)


if __name__ == "__main__":
    unittest.main()
