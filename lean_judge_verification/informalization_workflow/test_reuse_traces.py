"""Strict cache identity tests; no Lean or model calls."""
import copy
from pathlib import Path
import tempfile
import unittest
import trace_states as ts
from reuse_traces import matches


class TraceReuseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        source = Path(self.temp.name) / "Demo.lean"
        source.write_text("theorem demo : True := by trivial\n")
        self.cfg = {"retained_file": source, "revision": "pin", "pinned_toolchain": "lean:vX",
                    "fingerprints": {"lean-toolchain": "a", "lake-manifest.json": "b"}}
        self.trace = {"status": "success", "exit_status": 0, "source": "demo", "source_file": "Demo.lean",
                      "source_sha256": ts.sha256(source), "revision": "pin", "pinned_toolchain": "lean:vX",
                      "build_source_matches_retained": True, "build_configuration_sha256": self.cfg["fingerprints"],
                      "driver_sha256": ts.sha256(ts.DRIVER), "launcher_sha256": ts.sha256(Path(ts.__file__)),
                      "extraction_method": "original_file_reelaboration_lean_infotree",
                      "tactic_selection": "original_source_nodes", "tactic_count": 1, "tactics": [{"id": "t000001"}]}

    def test_exact_original_trace(self):
        self.assertTrue(matches(self.trace, "demo", "Demo.lean", self.cfg))

    def test_compact_or_partial_or_error_rejected(self):
        for change in ({"retention": {}}, {"status": "partial_trace"}, {"has_errors": True},
                       {"timed_out": True}, {"exit_status": 1}, {"tactic_count": 2}):
            with self.subTest(change=change):
                self.assertFalse(matches({**self.trace, **change}, "demo", "Demo.lean", self.cfg))

    def test_each_identity_must_match(self):
        for key in ("source", "source_file", "source_sha256", "revision", "pinned_toolchain",
                    "build_configuration_sha256", "build_source_matches_retained", "driver_sha256",
                    "launcher_sha256", "extraction_method", "tactic_selection"):
            with self.subTest(key=key):
                trace = copy.deepcopy(self.trace)
                trace[key] = "different"
                self.assertFalse(matches(trace, "demo", "Demo.lean", self.cfg))


if __name__ == "__main__":
    unittest.main()
