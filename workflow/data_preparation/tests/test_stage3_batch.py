from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


PIPELINE = Path(__file__).resolve().parents[1] / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from run_stage3_batch import (  # noqa: E402
    acquire_run_lock,
    archive_incomplete_attempt,
    stage_paper,
)
from prepare_stage3_retries import prepare_retries  # noqa: E402


class Stage3BatchTests(unittest.TestCase):
    def _source_paper(self, root: Path, paper_id: str) -> Path:
        private = root / paper_id / "private_source"
        private.mkdir(parents=True)
        (private / "metadata.json").write_text(
            json.dumps(
                {
                    "paper_id": paper_id,
                    "content_source_file": "source.html",
                }
            ),
            encoding="utf-8",
        )
        (private / "source.html").write_text(
            "<p>Theorem 1 and its proof.</p>", encoding="utf-8"
        )
        return private

    def test_stage_paper_replaces_an_incomplete_staged_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source_root = root / "source"
            run_root = root / "run"
            paper_id = "paper_2026_001"
            self._source_paper(source_root, paper_id)
            incomplete = run_root / "papers" / paper_id / "private_source"
            incomplete.mkdir(parents=True)
            (incomplete / "metadata.json").write_text(
                json.dumps({"paper_id": paper_id}), encoding="utf-8"
            )

            paper_dir = stage_paper(source_root, run_root, paper_id)

            self.assertTrue((paper_dir / "private_source/source.html").is_file())

    def test_archive_incomplete_attempt_preserves_private_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run_root = Path(temporary)
            paper_id = "paper_2026_001"
            paper = run_root / "papers" / paper_id
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "source.html").write_text("source", encoding="utf-8")
            analysis = paper / "paper_analysis"
            analysis.mkdir()
            (analysis / "turn1_triage.json").write_text("{}", encoding="utf-8")
            logs = run_root / "logs"
            logs.mkdir()
            (logs / f"{paper_id}.stderr.log").write_text(
                "failure", encoding="utf-8"
            )

            archived = archive_incomplete_attempt(run_root, paper_id)

            self.assertTrue(archived)
            self.assertTrue((private / "source.html").is_file())
            self.assertFalse(analysis.exists())
            attempts = list((run_root / "debug_attempts" / paper_id).iterdir())
            self.assertEqual(len(attempts), 1)
            self.assertTrue((attempts[0] / "paper_analysis").is_dir())
            self.assertTrue(
                (attempts[0] / f"{paper_id}.stderr.log").is_file()
            )

    def test_run_lock_rejects_a_second_supervisor(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run_root = Path(temporary)
            first = acquire_run_lock(run_root)
            try:
                with self.assertRaisesRegex(RuntimeError, "another batch supervisor"):
                    acquire_run_lock(run_root)
            finally:
                first.close()

    def test_explicit_retry_can_archive_a_terminal_paper(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run_root = Path(temporary)
            paper_id = "paper_2026_001"
            paper = run_root / "papers" / paper_id
            private = paper / "private_source"
            private.mkdir(parents=True)
            (private / "source.html").write_text("source", encoding="utf-8")
            generated = paper / "formalization"
            generated.mkdir()
            (generated / "status.json").write_text("{}", encoding="utf-8")
            (run_root / "run.json").write_text(
                json.dumps(
                    {
                        "papers": {
                            paper_id: {"status": "completed", "retry_count": 1}
                        },
                        "summary": {},
                    }
                ),
                encoding="utf-8",
            )

            selected = prepare_retries(run_root, [paper_id])

            self.assertEqual(selected, [paper_id])
            self.assertTrue((private / "source.html").is_file())
            self.assertFalse(generated.exists())
            state = json.loads((run_root / "run.json").read_text(encoding="utf-8"))
            self.assertEqual(state["papers"][paper_id]["status"], "pending")
            self.assertEqual(state["papers"][paper_id]["retry_count"], 2)
            self.assertEqual(
                state["papers"][paper_id]["previous_status"], "completed"
            )


if __name__ == "__main__":
    unittest.main()
