"""Offline expansion safety/receipt tests; no Lean, downloads, or model calls."""
from __future__ import annotations

import json
from pathlib import Path
import signal
import subprocess
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import Mock, call, patch

import expansion_sources as expansion


class ExpansionSourcesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.builder = expansion.load_builder()
        self.builder.BASE = self.base
        self.builder.BUNDLES = self.base / ".runtime/reference_evidence"
        self.source = {"root": "snapshot", "revision": "abc123", "repository": "https://example.invalid/demo",
                       "toolchain_folder": "pinned", "module_prefix": "Demo"}
        self.builder.CONFIG = {"sources": {"demo": self.source}, "cases": []}
        self.case = {"id": "demo/04_example", "source": "demo", "target": "Demo.example", "module": "Demo.Example"}
        self.root = self.base / "snapshot"
        (self.root / "Demo").mkdir(parents=True)
        (self.root / "Demo/Example.lean").write_text("namespace Demo\ntheorem example : True := True.intro\nend Demo\n")
        (self.root / "lean-toolchain").write_text("leanprover/lean4:v4.32.0\n")

    def selection(self, cases=None):
        return {"source": "demo", "preferred": cases if cases is not None else [self.case], "alternates": []}

    def make_bundle(self, axioms=None):
        bundle = self.builder.BUNDLES / self.case["id"]
        evidence = bundle / "evidence"
        evidence.mkdir(parents=True)
        source_path = bundle / "sources/project/Demo/Example.lean"
        source_path.parent.mkdir(parents=True)
        source_path.write_bytes((self.root / "Demo/Example.lean").read_bytes())
        for name in ("export_driver.lean", "target_build.log", "lean_check.log"):
            (evidence / name).write_text("fixture " + name + "\n")
        axioms = ["propext", "Classical.choice", "Quot.sound"] if axioms is None else axioms
        self.builder.dump(evidence / "lean_dependencies.json", {
            "target": self.case["target"], "transitive_axioms": axioms,
            "project_declaration_closure": [{"name": self.case["target"], "module": self.case["module"]}],
            "external_background_boundary": []})
        self.builder.dump(evidence / "source_files.json", [{"module": self.case["module"],
            "path": "sources/project/Demo/Example.lean", "sha256": self.builder.digest(source_path)}])
        self.builder.dump(evidence / "background_source_files.json", [])
        receipt = {"case_id": self.case["id"], "target": self.case["target"], "source_revision": "abc123",
                   "source_fingerprint": self.builder.source_fingerprint(self.root), "exit_code": 0,
                   "lean_toolchain": "leanprover/lean4:v4.32.0"}
        for key, name in {"trace_sha256": "lean_dependencies.json", "driver_sha256": "export_driver.lean",
                          "build_log_sha256": "target_build.log", "check_log_sha256": "lean_check.log"}.items():
            receipt[key] = self.builder.digest(evidence / name)
        self.builder.dump(evidence / "verification_receipt.json", receipt)
        self.builder.dump(evidence / "manifest.json", {
            "case_id": self.case["id"], "target": self.case["target"], "target_module": self.case["module"],
            "source_revision": "abc123", "source_repository": self.source["repository"],
            "lean_toolchain": receipt["lean_toolchain"], "lean_locally_verified": True,
            "proof_term_dependencies_extracted": True, "standard_axioms_only": True,
            "trace_sha256": receipt["trace_sha256"], "transitive_axioms": axioms,
            "background_source_missing": []})
        return bundle

    def test_any_subset_including_thirty_candidates(self):
        self.assertEqual(expansion.validate_selections([self.selection()], self.builder), [self.case])
        cases = [dict(self.case, id=f"demo/{i:02}_case", target=f"Demo.result{i}") for i in range(4, 34)]
        self.assertEqual(len(expansion.validate_selections([self.selection(cases)], self.builder)), 30)
        legacy = {"source": "demo", "cases": [self.case]}
        self.assertEqual(expansion.validate_selections([legacy], self.builder), [self.case])

    def test_invalid_ids_sources_and_exporter_injection(self):
        for change in ({"id": "demo/03_case"}, {"id": "demo/100_case"}, {"id": "demo/04_../x"},
                       {"id": "other/04_case"}, {"source": "other"}, {"module": "Demo;exit"},
                       {"target": "Demo.x\n#eval 1"}, {"target": "Demo.x/--"}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                expansion.validate_selections([self.selection([dict(self.case, **change)])], self.builder)

    def test_later_screening_slots_preserve_existing_numbering(self):
        for number in (34, 50, 99):
            case = dict(self.case, id=f"demo/{number:02}_later")
            self.assertEqual(expansion.validate_selections([self.selection([case])], self.builder), [case])

    def test_duplicate_id_slot_and_target(self):
        for other in (self.case, dict(self.case, id="demo/04_other", target="Demo.other"),
                      dict(self.case, id="demo/05_other")):
            with self.subTest(other=other), self.assertRaises(ValueError):
                expansion.validate_selections([self.selection([self.case, other])], self.builder)

    def test_config_target_collision(self):
        self.builder.CONFIG["cases"] = [dict(self.case, id="demo/01_accepted")]
        with self.assertRaisesRegex(ValueError, "case_config"):
            expansion.check_collisions(self.case, self.builder)

    def test_config_numeric_slot_collision(self):
        self.builder.CONFIG["cases"] = [dict(self.case, id="demo/04_accepted", target="Demo.old")]
        with self.assertRaisesRegex(ValueError, "case_config"):
            expansion.check_collisions(self.case, self.builder)

    def test_data_nested_or_renamed_slot_collision(self):
        (self.base / "data/demo/draft/04_old").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "data directory"):
            expansion.check_collisions(self.case, self.builder)

    def test_source_prefixed_data_directory_collision(self):
        (self.base / "data/demo/demo_04_existing").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "data directory"):
            expansion.check_collisions(self.case, self.builder)

    def test_source_prefixed_directory_outside_source_subdirectory_collision(self):
        (self.base / "data/draft/demo_04_existing").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "data directory"):
            expansion.check_collisions(self.case, self.builder)

    def test_same_number_in_another_source_does_not_collide(self):
        (self.base / "data/other/other_04_existing").mkdir(parents=True)
        (self.base / "data/other/04_existing").mkdir(parents=True)
        expansion.check_collisions(self.case, self.builder)

    def test_existing_evidence_slot_collision(self):
        (self.builder.BUNDLES / "demo/04_old").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "evidence slot"):
            expansion.check_collisions(self.case, self.builder)

    def test_space_is_strictly_greater_than_eight_gib(self):
        for free in (0, expansion.MIN_FREE_BYTES):
            with patch.object(expansion.shutil, "disk_usage", return_value=SimpleNamespace(free=free)):
                with self.assertRaises(ValueError):
                    expansion.require_space(self.base)
        with patch.object(expansion.shutil, "disk_usage", return_value=SimpleNamespace(free=expansion.MIN_FREE_BYTES + 1)):
            self.assertEqual(expansion.require_space(self.base), expansion.MIN_FREE_BYTES + 1)

    def test_new_bundle_decision_does_not_write(self):
        self.assertEqual(expansion.resume_decision(self.case, self.builder), ("build", {}))
        self.assertFalse(self.builder.BUNDLES.exists())

    def test_completed_receipt_resumes_without_trace_or_source_writes(self):
        bundle = self.make_bundle()
        before = {str(p): (p.read_bytes(), p.stat().st_mtime_ns) for p in bundle.rglob("*") if p.is_file()}
        with patch.object(expansion, "require_space", return_value=expansion.MIN_FREE_BYTES + 1), \
             patch.object(self.builder, "trace", side_effect=AssertionError("must not rebuild")):
            self.assertEqual(expansion.process_case(self.case, self.builder)["status"], "resumed")
        after = {str(p): (p.read_bytes(), p.stat().st_mtime_ns) for p in bundle.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_incomplete_bundle_is_preserved(self):
        bundle = self.builder.BUNDLES / self.case["id"]
        bundle.mkdir(parents=True)
        (bundle / "partial.log").write_text("keep me")
        with patch.object(expansion, "require_space", return_value=expansion.MIN_FREE_BYTES + 1), \
             patch.object(self.builder, "trace", side_effect=AssertionError("must not rebuild")):
            self.assertEqual(expansion.process_case(self.case, self.builder)["status"], "failed")
        self.assertEqual((bundle / "partial.log").read_text(), "keep me")

    def test_nonstandard_axioms_are_never_admitted(self):
        self.make_bundle(["sorryAx"])
        with self.assertRaisesRegex(ValueError, "axiom"):
            expansion.resume_decision(self.case, self.builder)

    def test_changed_source_and_receipt_are_rejected(self):
        bundle = self.make_bundle()
        (bundle / "evidence/lean_check.log").write_text("changed")
        with self.assertRaisesRegex(ValueError, "receipt file mismatch"):
            expansion.resume_decision(self.case, self.builder)

    def test_copied_project_source_hash_is_checked(self):
        bundle = self.make_bundle()
        (bundle / "sources/project/Demo/Example.lean").write_text("changed")
        with self.assertRaisesRegex(ValueError, "source hash mismatch"):
            expansion.resume_decision(self.case, self.builder)

    def test_summary_is_suppressed_and_original_methods_restored(self):
        original_summary, original_run = self.builder.summarize, self.builder.run_logged
        with expansion.guarded_builder(self.builder):
            self.builder.summarize()
            self.assertFalse((self.builder.BUNDLES / "verification_summary.json").exists())
            with self.assertRaises(ValueError):
                self.builder.run_logged(["lake", "exe", "cache", "get"], self.source, "demo", self.base / "log")
        self.assertIs(self.builder.summarize, original_summary)
        self.assertIs(self.builder.run_logged, original_run)

    def test_build_uses_pinned_lake_and_offline_prefix(self):
        process = Mock(pid=12345)
        process.wait.return_value = 0
        with patch.object(expansion.subprocess, "Popen", return_value=process) as popen, \
             patch.object(expansion, "offline_prefix", return_value=["offline-test-guard"]):
            with expansion.guarded_builder(self.builder):
                self.builder.run_logged(["lake", "build", "Demo.Example"], self.source, "demo", self.base / "log")
        command = popen.call_args.args[0]
        self.assertEqual(command, ["offline-test-guard", str(self.base / ".tools/toolchains/pinned/bin/lake"),
                                   "build", "Demo.Example"])
        self.assertTrue(popen.call_args.kwargs["start_new_session"])
        process.wait.assert_called_once_with(timeout=expansion.SUBPROCESS_TIMEOUT_SECONDS)

    def test_timeout_kills_exact_process_group_and_preserves_failure_log(self):
        process = Mock(pid=12345, returncode=None)
        process.wait.side_effect = [subprocess.TimeoutExpired(["fake-build"], 1800), 0]
        log = self.base / "timeout.log"
        with patch.object(expansion.subprocess, "Popen", return_value=process), \
             patch.object(expansion.os, "killpg") as killpg, \
             patch.object(expansion.time, "sleep"), \
             patch.object(expansion, "offline_prefix", return_value=["offline-test-guard"]):
            with expansion.guarded_builder(self.builder), self.assertRaises(TimeoutError):
                self.builder.run_logged(["lake", "build", "Demo.Example"], self.source, "demo", log)
        self.assertEqual(killpg.call_args_list, [call(12345, signal.SIGTERM), call(12345, signal.SIGKILL)])
        self.assertIn("TIMEOUT after 1800s", log.read_text())
        self.assertFalse((self.builder.BUNDLES / self.case["id"] / "evidence/verification_receipt.json").exists())

    def test_unresponsive_group_shutdown_waits_are_bounded(self):
        process = Mock(pid=12345, returncode=None)
        process.wait.side_effect = subprocess.TimeoutExpired(["fake-build"], 5)
        with patch.object(expansion.os, "killpg") as killpg, patch.object(expansion.time, "sleep"), \
             self.assertRaises(RuntimeError):
            expansion.stop_process_group(process)
        self.assertEqual(killpg.call_count, 2)
        self.assertEqual(process.wait.call_args_list,
                         [call(timeout=expansion.TERMINATION_GRACE_SECONDS)])

    def test_exited_process_group_is_safe_to_cleanup(self):
        process = Mock(pid=12345, returncode=None)
        process.wait.return_value = 0
        with patch.object(expansion.os, "killpg", side_effect=ProcessLookupError):
            expansion.stop_process_group(process)
        self.assertEqual(process.wait.call_count, 1)

    def test_reaped_pid_is_never_signalled(self):
        process = Mock(pid=12345, returncode=0)
        with patch.object(expansion.os, "killpg") as killpg:
            expansion.stop_process_group(process)
        killpg.assert_not_called()

    def test_low_space_prevents_all_bundle_access_and_builds(self):
        with patch.object(expansion, "require_space", side_effect=ValueError("disk full")), \
             patch.object(expansion, "resume_decision") as resume, \
             patch.object(self.builder, "trace") as trace:
            row = expansion.process_case(self.case, self.builder)
        self.assertEqual(row["status"], "failed")
        resume.assert_not_called()
        trace.assert_not_called()

    def test_build_system_exit_is_recorded_and_partial_files_preserved(self):
        with patch.object(expansion, "require_space", return_value=expansion.MIN_FREE_BYTES + 1), \
             patch.object(expansion, "preflight"), patch.object(expansion, "offline_prefix", return_value=[]), \
             patch.object(self.builder, "trace", side_effect=SystemExit(7)):
            row = expansion.process_case(self.case, self.builder)
        self.assertEqual(row["status"], "failed")
        self.assertIn("SystemExit: 7", row["error"])
        self.assertTrue((self.builder.BUNDLES / self.case["id"]).is_dir())

    def test_cli_case_and_pilot_limit(self):
        other = dict(self.case, id="demo/05_other", target="Demo.other")
        selection = self.base / "selection.json"
        selection.write_text(json.dumps(self.selection([self.case, other])))
        with patch.object(expansion, "load_builder", return_value=self.builder), \
             patch.object(expansion, "process_case", return_value=dict(other, status="verified")) as process:
            result = expansion.main(["--selection", str(selection), "--run", str(self.base / ".runtime/pilot"),
                                     "--case", other["id"], "--limit", "1"])
        self.assertEqual(result, 0)
        self.assertEqual(process.call_args.args[0], other)

    def test_run_stays_inside_runtime_and_outside_evidence(self):
        for path in (self.base, self.base / ".runtime", self.builder.BUNDLES / "run"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                expansion.validate_run(path, self.builder)
        valid = self.base / ".runtime/expansion/run"
        self.assertEqual(expansion.validate_run(valid, self.builder), valid.resolve())

    def test_only_pinned_tlb_dev_documentation_dependencies_may_be_absent(self):
        self.builder.CONFIG["sources"]["tlb"] = self.source
        case = dict(self.case, id="tlb/04_example", source="tlb")
        build = self.base / ".tools/builds/tlb"
        build.mkdir(parents=True)
        bindir = self.base / ".tools/toolchains/pinned/bin"
        bindir.mkdir(parents=True)
        for name in ("lake", "lean"):
            (bindir / name).write_text("fixture")
        (build / "lakefile.lean").write_text('meta if get_config? env = some "dev" then\n')
        manifest = build / "lake-manifest.json"
        manifest.write_text(json.dumps({"packages": [{"name": "MD4Lean", "type": "git"}]}))
        with patch.object(self.builder, "verify_build_sources"):
            expansion.preflight(case, self.builder)
            manifest.write_text(json.dumps({"packages": [{"name": "mathlib", "type": "git"}]}))
            with self.assertRaisesRegex(ValueError, "Missing local dependency"):
                expansion.preflight(case, self.builder)

    def test_cli_records_failures_and_continues(self):
        other = dict(self.case, id="demo/05_other", target="Demo.other")
        selection = self.base / "selection.json"
        selection.write_text(json.dumps(self.selection([self.case, other])))
        run = self.base / ".runtime/run"
        rows = [dict(self.case, status="failed", error="build failed"), dict(other, status="verified")]
        with patch.object(expansion, "load_builder", return_value=self.builder), \
             patch.object(expansion, "process_case", side_effect=rows) as process:
            result = expansion.main(["--selection", str(selection), "--run", str(run)])
        self.assertEqual(result, 1)
        self.assertEqual(process.call_count, 2)
        state = json.loads((run / expansion.STATUS_NAME).read_text())
        self.assertEqual(state["cases"][other["id"]]["status"], "verified")


if __name__ == "__main__":
    unittest.main()
