#!/usr/bin/env python3
"""Offline checks for trace provenance and Unicode/scope-preserving readers."""

from __future__ import annotations

import unittest

import trace_states
from lean_trace.trace_view import compact_index, select_tactics


def raw_tactic(index, parent, start, end, line=1):
    return {"index": index, "parent_index": parent,
            "source_span": {"start": {"line": line, "column": 0, "byte": start},
                            "end": {"line": line, "column": 3, "byte": end}},
            "before": {"goal_count": 1, "goals": [{"goal_id": "g", "pretty": "h : α\n⊢ α"}]},
            "after": {"goal_count": 0, "goals": []}}


class TraceTests(unittest.TestCase):
    def test_crlf_normalized_parser_offsets_map_to_original_bytes(self):
        source = "α := by\r\n  exact α\r\n".encode()
        normalized = source.replace(b"\r\n", b"\n")
        start = normalized.index(b"exact")
        end = normalized.index(b"\n", start)
        record = trace_states.finalize_tactics([raw_tactic(0, None, start, end, 2)], source)[0]
        self.assertEqual(record["tactic"], "exact α")
        self.assertEqual(record["source_span"]["start"]["byte"], source.index(b"exact"))
        self.assertEqual(record["source_span"]["end"]["byte"], source.index(b"\r\n", source.index(b"exact")))

    def test_utf8_slice_and_nested_ids(self):
        source = "α := by\n  exact α\n".encode()
        start = source.index(b"exact")
        result = trace_states.finalize_tactics([
            raw_tactic(0, None, 0, len(source)),
            raw_tactic(1, 0, start, len(source) - 1, 2),
        ], source)
        self.assertEqual(result[1]["tactic"], "exact α")
        self.assertEqual(result[1]["parent_id"], "t000001")
        self.assertEqual(result[1]["after"]["goals"], [])
        self.assertNotIn("proof_complete", result[1])

    def test_bad_source_span_rejected(self):
        with self.assertRaises(ValueError):
            trace_states.finalize_tactics([raw_tactic(0, None, 0, 100)], b"by")

    def test_forward_parent_rejected(self):
        with self.assertRaises(ValueError):
            trace_states.finalize_tactics([raw_tactic(0, 1, 0, 2)], b"by")

    def test_reader_keeps_overlapping_parent_and_child(self):
        records = trace_states.finalize_tactics([
            raw_tactic(0, None, 0, 2), raw_tactic(1, 0, 0, 2, 3)], b"by")
        records[0]["source_span"]["end"]["line"] = 5
        self.assertEqual(len(select_tactics({"tactics": records}, lines=(3, 3))), 2)
        self.assertEqual(select_tactics({"tactics": records}, ids=["t000002"]), [records[1]])
        with self.assertRaises(ValueError):
            select_tactics({"tactics": records}, ids=["t999999"])

    def test_reader_end_exclusive_line(self):
        records = trace_states.finalize_tactics([raw_tactic(0, None, 0, 2)], b"by")
        records[0]["source_span"]["end"] = {"line": 3, "column": 0, "byte": 2}
        self.assertEqual(select_tactics({"tactics": records}, lines=(3, 3)), [])

    def test_display_filter_does_not_relabel_or_mutate_raw_nodes(self):
        records = trace_states.finalize_tactics([
            raw_tactic(0, None, 0, 2), raw_tactic(1, 0, 0, 2)], b"by")
        records[0]["source_kind"] = "original"
        records[1]["source_kind"] = "synthetic"
        filtered = select_tactics({"tactics": records}, original_only=True)
        self.assertEqual(filtered, [records[0]])
        self.assertEqual(len(records), 2)
        self.assertEqual(records[1]["source_kind"], "synthetic")
        self.assertEqual(compact_index(records[0])["goals"], [1, 0])

    def test_retained_source_and_build_match(self):
        for source, filename in (("ai4slt", "SLT/MatrixInfra/EYM.lean"),
                                 ("tlb", "TestingLowerBounds/Testing/Risk.lean")):
            with self.subTest(source=source):
                if not (trace_states.BASE / ".tools/builds" / source).exists():
                    self.skipTest(f"{source} build environment is not installed; restore it for this integration check")
                config = trace_states.source_configuration(source, filename)
                self.assertEqual(trace_states.sha256(config["retained_file"]),
                                 trace_states.sha256(config["build_file"]))

    def test_source_traversal_refused(self):
        for filename in ("../Risk.lean", "/tmp/Risk.lean", "Mathlib/Foo.lean"):
            with self.assertRaises(ValueError):
                trace_states.source_configuration("tlb", filename)


if __name__ == "__main__":
    unittest.main()
