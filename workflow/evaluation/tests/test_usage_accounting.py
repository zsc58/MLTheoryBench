import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "runtime"))

from usage_accounting import aggregate_agent_records, session_delta  # noqa: E402


class UsageAccountingTests(unittest.TestCase):
    def test_resumed_usage_is_increment_not_session_total(self):
        first = {"input_tokens": 100, "cached_input_tokens": 20, "output_tokens": 10}
        second = {"input_tokens": 250, "cached_input_tokens": 100, "output_tokens": 15}
        usage, issues = session_delta(second, first)
        self.assertEqual(usage["input_tokens"], 150)
        self.assertEqual(usage["cached_input_tokens"], 80)
        self.assertEqual(usage["output_tokens"], 5)
        self.assertEqual(usage["total_tokens"], 155)
        self.assertEqual(issues, [])

    def test_saved_raw_counters_override_legacy_additive_usage(self):
        rows = [(str(i), "task_audit", {
            "session_id": "one", "started_at_unix": i,
            "raw_usage": {"input_tokens": count, "output_tokens": i + 1},
            "usage": {"input_tokens": count, "output_tokens": i + 1},
        }) for i, count in enumerate((100, 250))]
        stages, issues = aggregate_agent_records(rows)
        self.assertEqual(stages["task_audit"]["input_tokens"], 250)
        self.assertEqual(stages["task_audit"]["output_tokens"], 2)
        self.assertEqual(issues, [])

    def test_independent_ephemeral_calls_are_added(self):
        stages, _ = aggregate_agent_records([
            (str(i), "task_checker", {"raw_usage": {"input_tokens": 10}})
            for i in range(2)
        ])
        self.assertEqual(stages["task_checker"]["input_tokens"], 20)

    def test_counter_reset_is_unknown_not_negative_usage(self):
        usage, issues = session_delta({"input_tokens": 10}, {"input_tokens": 100})
        self.assertIsNone(usage)
        self.assertTrue(issues)

    def test_missing_report_preserves_unknown(self):
        usage, issues = session_delta(None, {"input_tokens": 100})
        self.assertIsNone(usage)
        self.assertTrue(issues)


if __name__ == "__main__":
    unittest.main()
