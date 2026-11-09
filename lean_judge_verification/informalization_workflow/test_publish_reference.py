"""Pure retention tests; no publication or model calls."""
import unittest
from publish_reference import retained_trace


class RetentionTests(unittest.TestCase):
    def test_keep_referenced_nodes_and_ancestors_in_original_order(self):
        nodes = [{"id": "t000001", "parent_id": None},
                 {"id": "t000002", "parent_id": "t000001"},
                 {"id": "t000003", "parent_id": None}]
        trace = {"tactics": nodes, "source_sha256": "source"}
        kept = retained_trace(trace, {"t000002"}, "original")
        self.assertEqual([n["id"] for n in kept["tactics"]], ["t000001", "t000002"])
        self.assertEqual(len(trace["tactics"]), 3)
        self.assertEqual(kept["retention"]["original_trace_sha256"], "original")
        self.assertEqual(kept["retention"]["retained_tactic_count"], 2)

    def test_missing_tactic_rejected(self):
        with self.assertRaises(ValueError):
            retained_trace({"tactics": []}, {"t000001"}, "original")


if __name__ == "__main__":
    unittest.main()
