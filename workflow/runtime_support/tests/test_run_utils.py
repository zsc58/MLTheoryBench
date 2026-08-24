from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

WORKFLOW_ROOT = Path(__file__).resolve().parents[2]
if str(WORKFLOW_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKFLOW_ROOT))

from runtime_support.experiment.run_utils import update_run_task_stage


class RunUsageTests(unittest.TestCase):
    def test_stage_usage_is_preserved_and_aggregated(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            run_dir = Path(temporary)
            (run_dir / "run.json").write_text(
                json.dumps({"run_id": "test_run", "tasks": {}}),
                encoding="utf-8",
            )
            usage = {
                "input_tokens": 100,
                "cached_input_tokens": 20,
                "non_cached_input_tokens": 80,
                "output_tokens": 10,
                "reasoning_output_tokens": 3,
                "total_tokens": 110,
            }
            record = update_run_task_stage(
                run_dir,
                "paper_2026_001",
                "theorem_001",
                "solver",
                {"status": "completed", "usage": usage},
            )
            stage = record["tasks"]["paper_2026_001/theorem_001"]["solver"]
            self.assertEqual(stage["usage"], usage)
            self.assertEqual(record["usage"]["solver"], usage)
            self.assertEqual(record["usage"]["total"], usage)


if __name__ == "__main__":
    unittest.main()
