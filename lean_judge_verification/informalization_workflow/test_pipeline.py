"""Synthetic structural/lifecycle tests; these fixtures are not mathematical evals."""
from contextlib import ExitStack, redirect_stdout
import copy
import io
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import pipeline as p
import validation as v
from boundary import dependency_coverage, validate_plan, interfaces
from io_utils import read, write, sha


class PipelineTests(unittest.TestCase):
    def test_plan_manifest_snapshot_survives_author_write_turn(self):
        manifest = self.run / "manifest.json"
        self.boundary["files_read"].append(v.relative(manifest))
        self.save_plan()
        self.plan_ready()
        p.record_turn(self.job, "write", "author", "write-1")
        p.check_plan(self.job)
        receipt = read(self.out / "plan_navigation.json")
        archived = v.read_path(receipt["snapshots"][v.relative(manifest)])
        self.assertNotEqual(sha(archived), sha(manifest))

    def test_author_single_case_manifest_is_archived_before_reviewer_turn(self):
        self.write_ready()
        manifest = self.run / "manifest.json"
        self.alignment["files_read"].append(v.relative(manifest))
        self.save_draft()
        p.freeze_draft(self.job)
        p.record_turn(self.job, "review", "reviewer", "review_1")
        v.check_frozen(self.job)
        receipt = read(self.out / "freeze.json")
        archived = v.read_path(receipt["navigation_snapshots"][v.relative(manifest)])
        self.assertNotEqual(sha(archived), sha(manifest))
        archived.write_text("corrupted snapshot\n")
        with self.assertRaises(ValueError):
            v.check_frozen(self.job)

    def test_author_manifest_does_not_allow_other_case_or_other_run(self):
        current = self.run / "manifest.json"
        metadata = read(current)
        metadata["jobs"].append("cases/other/job.json")
        write(current, metadata)
        with self.assertRaisesRegex(ValueError, "single-case"):
            v.validate_reads(self.job, [v.relative(current)])
        other = self.root / "cases/other_run/manifest.json"
        other.parent.mkdir(parents=True)
        write(other, {})
        with self.assertRaisesRegex(ValueError, "outside the declared case allowlist"):
            v.validate_reads(self.job, [v.relative(other)])

    def test_generic_schema_navigation_is_allowed_but_other_case_prose_is_not(self):
        names = [v.relative(self.workflow / n) for n in ("test_pipeline.py", "publish_reference.py")]
        v.validate_reads(self.job, names)
        other = self.root / "cases/other/draft/proof.md"
        other.parent.mkdir(parents=True)
        other.write_text("Other case mathematical proof.\n")
        with self.assertRaisesRegex(ValueError, "outside the declared case allowlist"):
            v.validate_reads(self.job, [v.relative(other)])

    def test_current_run_trace_provenance_is_allowed_and_frozen(self):
        self.write_ready()
        note = self.run / "trace_reuse.md"
        note.write_text("Exact source-hash-matched trace cache provenance.\n")
        self.alignment["files_read"].append(v.relative(note))
        self.save_draft()
        p.freeze_draft(self.job)
        v.check_frozen(self.job)
        other = self.root / "cases/other_run/trace_reuse.md"
        other.parent.mkdir(parents=True)
        other.write_text("Unrelated run.\n")
        with self.assertRaisesRegex(ValueError, "outside the declared case allowlist"):
            v.validate_reads(self.job, [v.relative(other)])
        note.write_text("Changed provenance.\n")
        with self.assertRaisesRegex(ValueError, "Frozen file changed"):
            v.check_frozen(self.job)

    def test_plan_navigation_archive_preserves_read_time_bytes(self):
        name = v.relative(self.workflow / "validation.py")
        self.boundary["files_read"].append(name)
        self.save_plan()
        self.plan_ready()
        identity = sha(self.out / "plan_freeze.json")
        (self.workflow / "validation.py").write_text("# updated navigation\n")
        p.check_plan(self.job)
        self.assertEqual(sha(self.out / "plan_freeze.json"), identity)
        receipt = read(self.out / "plan_navigation.json")
        v.read_path(receipt["snapshots"][name]).write_text("# corrupted\n")
        with self.assertRaises(ValueError):
            p.check_plan(self.job)

    def test_runner_observed_turn_identity_is_explicit(self):
        p.record_turn(self.job, "plan", "observed_agent", "spawn_1", "runner_observed_invocation")
        entry = p.turns_for(self.job)[-1]
        self.assertEqual(entry["turn_id_source"], "runner_observed_invocation")
        with self.assertRaises(ValueError):
            p.record_turn(self.job, "plan", "observed_agent", "spawn_1", "invented")

    def test_cli_runtime_scope(self):
        expected = self.root / ".runtime/runs/example"
        self.assertEqual(p.checked_run_path(expected), expected.resolve())
        for path in (self.root, self.root / ".runtime", self.root / "data/example",
                     self.root / ".runtime/../data/example"):
            with self.assertRaises(ValueError):
                p.checked_run_path(path)

    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        root = Path(self.stack.enter_context(tempfile.TemporaryDirectory())) / "project"
        workflow = root / "informalization_workflow"
        workflow.mkdir(parents=True)
        for name in v.SNAPSHOT_FILES:
            dst = workflow / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(v.WORKFLOW / name, dst)
        for name in v.NAVIGATION_FILES:
            dst = workflow / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text("# Navigation fixture\n")
        self.stack.enter_context(patch.object(v, "PROJECT", root))
        self.stack.enter_context(patch.object(v, "WORKFLOW", workflow))
        self.root, self.workflow = root, workflow
        self.case = root / "cases/fixture/01_demo"
        self.ev = self.case / "evidence"
        self.ev.mkdir(parents=True)
        self.source = self.case / "sources/project/Demo/Example.lean"
        self.source.parent.mkdir(parents=True)
        self.source.write_text("theorem helper : True := by trivial\n\ntheorem demo : True := by\n  exact helper\n")
        self.meta = {
            "case_id": "fixture/01_demo", "target": "demo", "target_module": "Demo.Example",
            "source_revision": "abc123", "source_repository": "https://example.invalid/demo",
            "lean_toolchain": "leanprover/lean4:v4.32.0",
            "lean_locally_verified": True, "standard_axioms_only": True,
        }
        write(self.ev / "manifest.json", self.meta)
        write(self.ev / "source_files.json", [{"path": "sources/project/Demo/Example.lean", "sha256": sha(self.source)}])
        write(self.ev / "background_source_files.json", [])
        self.export = {
            "target": "demo",
            "project_declaration_closure": [
                {"name": "demo", "kind": "theorem", "module": "Demo.Example",
                 "elaborated_statement": "True", "range": {"start_line": 3, "end_line": 4},
                 "type_dependencies": ["True"], "value_dependencies": ["helper"], "declaration_metadata_dependencies": []},
                {"name": "helper", "kind": "theorem", "module": "Demo.Example",
                 "range": {"start_line": 1, "end_line": 1},
                 "type_dependencies": ["True"], "value_dependencies": ["True.intro"], "declaration_metadata_dependencies": []},
            ],
            "external_background_boundary": [{"name": "True", "kind": "inductive", "module": "Init"},
                                             {"name": "True.intro", "kind": "constructor", "module": "Init"}],
        }
        write(self.ev / "lean_dependencies.json", self.export)
        receipt = {k: self.meta[k] for k in ("case_id", "target", "source_revision", "lean_toolchain")}
        receipt["exit_code"] = 0
        for field, name in (("trace_sha256", "lean_dependencies.json"), ("driver_sha256", "export_driver.lean"),
                            ("build_log_sha256", "target_build.log"), ("check_log_sha256", "lean_check.log")):
            if not (self.ev / name).exists():
                (self.ev / name).write_text("fixture\n")
            receipt[field] = sha(self.ev / name)
        write(self.ev / "verification_receipt.json", receipt)
        self.run = root / "cases/test_run"
        with redirect_stdout(io.StringIO()):
            p.prepare(self.run, [self.case])
        self.job = p.get_jobs(self.run)[0]
        self.out = v.read_path(self.job["output"])
        self.ref = {"file": "sources/project/Demo/Example.lean", "start_line": 3, "end_line": 4, "declaration": "demo"}
        self.bref = {**self.ref, "start_line": 1, "end_line": 1, "declaration": "helper"}
        self.boundary = {
            "case_id": self.meta["case_id"], "target": "demo", "expanded_obligations": ["Use the helper"],
            "background_lemmas": [{"id": "B1", "interface": "Granted helper.", "kind": "permitted_project_result",
                                   "lean_declarations": ["helper"], "source_refs": [self.bref],
                                   "reason": "Synthetic lifecycle fixture, not a meaningful benchmark boundary."}],
            "context_groups": [], "files_read": [self.job["job_file"], self.job["plan_prompt"],
                self.job["translation_prompt"], self.job["scope_file"], v.relative(self.source)],
            "limitations": [],
        }
        self.sketch = {
            "case_id": self.meta["case_id"], "target_node": "N1",
            "nodes": [{"id": "N1", "role": "target", "lean_declarations": ["demo"], "summary": "Use helper",
                       "depends_on": ["B1"], "source_refs": [self.ref]}],
            "background_ids": ["B1"], "scope_coverage": [{"obligation": "Use the helper", "node_ids": ["N1"]}],
            "limitations": [],
        }
        self.save_plan()
        self.trace_path = v.read_path(self.job["trace_files"][0])
        raw = self.source.read_bytes()
        start = raw.index(b"exact helper")
        end = start + len(b"exact helper")
        self.trace = {
            "status": "success", "source": "fixture", "source_file": "Demo/Example.lean",
            "source_sha256": sha(self.source), "revision": "abc123",
            "pinned_toolchain": self.meta["lean_toolchain"], "lean_version": "Lean 4.32.0",
            "command": ["lean", "Example.lean"], "exit_status": 0,
            "tactics": [{"id": "t000001", "parent_id": None, "tactic": "exact helper",
                        "source_span": {"start": {"line": 4, "column": 2, "byte": start},
                                        "end": {"line": 4, "column": 14, "byte": end}},
                        "before": {"goal_count": 1, "goals": [{"goal_id": "g", "pretty": "⊢ True"}]},
                        "after": {"goal_count": 0, "goals": []}}],
        }
        write(self.trace_path, self.trace)

    def save_plan(self):
        write(self.out / "plan/boundary.json", self.boundary)
        write(self.out / "plan/sketch.json", self.sketch)
        for name in ("pf_sketch.md", "standard_lemmas.md"):
            (self.out / "plan" / name).write_text("# Fixture\n\nA granted helper.\n")

    def plan_ready(self):
        p.record_turn(self.job, "plan", "author", "plan-1")
        p.freeze_plan(self.job)

    def write_ready(self):
        self.plan_ready()
        p.record_turn(self.job, "write", "author", "write-1")
        self.alignment = {
            "case_id": self.meta["case_id"], "target": "demo", "state_basis": "source_and_real_lean_tactic_traces",
            "contract": {"objects": [], "assumptions": [], "quantifiers": "None", "conclusion": "True", "source_refs": [self.ref]},
            "definitions": [], "expanded_results": ["demo"], "background_lemmas": interfaces(self.boundary),
            "proof_blocks": [{"id": "P1", "node_id": "N1", "before": ["Prove True"], "after": "True",
                              "operation": "Apply helper", "conditions_checked": [], "source_refs": [self.ref],
                              "trace_refs": [{"trace_file": v.relative(self.trace_path), "tactic_id": "t000001"}],
                              "trace_coverage": "states_attached", "trace_note": "Actual state inspected.", "output_section": "Proof"}],
            "notation_changes": [], "unresolved_issues": [], "files_read": self.boundary["files_read"] + [v.relative(self.trace_path)],
            "attribution": "Synthetic fixture",
        }
        self.save_draft()

    def save_draft(self):
        write(self.out / "draft/alignment.json", self.alignment)
        write(self.out / "draft/sketch.json", self.sketch)
        for name in ("pf_sketch.md", "standard_lemmas.md"):
            shutil.copyfile(self.out / "plan" / name, self.out / "draft" / name)
        for name in ("problem.md", "proof.md"):
            (self.out / "draft" / name).write_text("# Synthetic fixture\n\nUse the helper.\n")

    def review_ready(self):
        self.write_ready()
        p.freeze_draft(self.job)
        p.record_turn(self.job, "review", "reviewer", "review-1")
        for name in v.ARTIFACTS:
            shutil.copyfile(self.out / "draft" / name, self.out / "final" / name)
        self.review = {
            "case_id": self.meta["case_id"], "verdict": "accepted_unchanged", "summary": "Fixture",
            "checks": [{"criterion": "Structure", "evidence": ["Synthetic fixture"], "outcome": "satisfied"}],
            "issues": [], "files_read": [v.relative(self.out / "draft" / x) for x in v.ARTIFACTS]
                + [v.relative(self.source), v.relative(self.trace_path)], "limitations": [],
        }
        write(self.out / "review.json", self.review)
        (self.out / "review.md").write_text("结构测试，不是数学评审。\n")

    def test_prepare_has_no_baseline_or_per_case_scope(self):
        self.assertNotIn("scope", self.job)
        self.assertNotIn("baseline", str(self.job))
        self.assertEqual(self.job["target"], "demo")
        with self.assertRaisesRegex(ValueError, "already exists"):
            p.prepare(self.run, [self.case])

    def test_source_and_receipt_tampering_rejected(self):
        self.source.write_text("changed\n")
        with self.assertRaisesRegex(ValueError, "Frozen file changed"):
            p.get_jobs(self.run)

    def test_missing_classification_is_reported(self):
        b = copy.deepcopy(self.boundary)
        b["background_lemmas"] = []
        report = dependency_coverage(self.job, b, self.sketch)
        self.assertEqual(report["uncovered_project_theorems"], ["helper"])

    def test_context_is_not_a_dependency_stop(self):
        self.export["project_declaration_closure"][1]["value_dependencies"] = ["hidden"]
        self.export["project_declaration_closure"].append({
            "name": "hidden", "kind": "theorem", "module": "Demo.Example",
            "type_dependencies": [], "value_dependencies": [], "declaration_metadata_dependencies": []})
        write(self.ev / "lean_dependencies.json", self.export)
        b = copy.deepcopy(self.boundary)
        b["background_lemmas"] = []
        b["context_groups"] = [{"lean_declarations": ["helper"], "reason": "A wrapper"}]
        self.assertEqual(dependency_coverage(self.job, b, self.sketch)["uncovered_project_theorems"], ["hidden"])

    def test_unknown_and_double_classified_declarations_rejected(self):
        for name, message in (("fake", "not in compiled"), ("demo", "multiple")):
            b = copy.deepcopy(self.boundary)
            b["context_groups"] = [{"lean_declarations": [name], "reason": "Test"}]
            with self.assertRaisesRegex(ValueError, message):
                dependency_coverage(self.job, b, self.sketch)

    def test_plan_scope_cycle_and_anchor_checks(self):
        self.sketch["nodes"][0]["depends_on"] = ["N1"]
        self.save_plan()
        with self.assertRaisesRegex(ValueError, "cycle"):
            validate_plan(self.job)
        self.sketch["nodes"][0]["depends_on"] = ["B1"]
        self.sketch["nodes"][0]["source_refs"] = [self.bref]
        self.save_plan()
        with self.assertRaisesRegex(ValueError, "module mismatch"):
            validate_plan(self.job)

    def test_plan_freeze_and_same_author_thread(self):
        self.plan_ready()
        with self.assertRaisesRegex(ValueError, "same thread"):
            p.record_turn(self.job, "write", "another-author", "write-1")
        with self.assertRaisesRegex(ValueError, "multiple stages"):
            p.record_turn(self.job, "write", "author", "plan-1")
        p.record_turn(self.job, "write", "author", "write-1")

    def test_write_needs_plan_and_real_traces(self):
        with self.assertRaises(FileNotFoundError):
            p.record_turn(self.job, "write", "author", "write-1")
        self.plan_ready()
        self.trace_path.unlink()
        with self.assertRaisesRegex(ValueError, "traces are missing"):
            p.record_turn(self.job, "write", "author", "write-1")

    def test_trace_corruption_is_rejected(self):
        self.plan_ready()
        for field, value in (("source_sha256", "wrong"), ("revision", "wrong"), ("exit_status", 1)):
            t = copy.deepcopy(self.trace)
            t[field] = value
            write(self.trace_path, t)
            with self.assertRaises(ValueError):
                p.check_traces(self.job, require_ready=True)
        t = copy.deepcopy(self.trace)
        t["tactics"][0]["after"]["goal_count"] = 1
        write(self.trace_path, t)
        with self.assertRaisesRegex(ValueError, "goal count"):
            p.check_traces(self.job, require_ready=True)

    def test_plan_modification_is_not_silent(self):
        self.plan_ready()
        self.boundary["expanded_obligations"].append("New obligation")
        self.save_plan()
        with self.assertRaisesRegex(ValueError, "Frozen file changed"):
            p.check_plan(self.job)

    def test_reopen_archives_draft_and_needs_new_writing_turn(self):
        self.write_ready()
        with redirect_stdout(io.StringIO()):
            p.reopen_plan(self.job)
        self.assertTrue((self.out / "plan_history/revision_001/draft/proof.md").exists())
        p.record_turn(self.job, "plan", "author", "plan-2")
        p.freeze_plan(self.job)
        with self.assertRaisesRegex(ValueError, "actual writing turn"):
            p.freeze_draft(self.job)
        p.record_turn(self.job, "write", "author", "write-2")
        self.save_draft()
        p.freeze_draft(self.job)

    def test_reopened_plan_requires_a_new_planning_turn(self):
        self.plan_ready()
        with redirect_stdout(io.StringIO()):
            p.reopen_plan(self.job)
        with self.assertRaisesRegex(ValueError, "new actual planning turn"):
            p.freeze_plan(self.job)

    def test_recording_same_writing_turn_is_idempotent(self):
        self.write_ready()
        entry = next(x for x in p.turns_for(self.job) if x["phase"] == "write")
        p.record_turn(self.job, "write", entry["thread_id"], entry["turn_id"])
        self.assertEqual(sum(x["phase"] == "write" for x in p.turns_for(self.job)), 1)

    def test_draft_cannot_change_background(self):
        self.write_ready()
        self.alignment["background_lemmas"][0]["interface"] = "A stronger result"
        self.save_draft()
        with self.assertRaisesRegex(ValueError, "Background interfaces"):
            v.validate_job(self.job)

    def test_partial_and_source_only_are_distinct(self):
        self.write_ready()
        self.trace["status"] = "partial_trace"
        write(self.trace_path, self.trace)
        with self.assertRaisesRegex(ValueError, "partial-coverage"):
            v.validate_job(self.job)
        b = self.alignment["proof_blocks"][0]
        b["trace_note"] = "Partial trace: unanchored helpers omitted."
        self.save_draft()
        self.assertEqual(v.validate_job(self.job)["coverage"]["block_coverage"], {"states_attached_partial_trace": 1})
        b["trace_coverage"] = "source_only"
        self.save_draft()
        with self.assertRaisesRegex(ValueError, "source_only cannot"):
            v.validate_job(self.job)
        b["trace_refs"] = []
        b["trace_note"] = "Term-style source-only proof."
        self.save_draft()
        self.assertEqual(v.validate_job(self.job)["coverage"]["block_coverage"], {"source_only": 1})

    def test_independent_review_and_immutable_draft(self):
        self.write_ready()
        with self.assertRaises(FileNotFoundError):
            p.record_turn(self.job, "review", "reviewer", "r")
        p.freeze_draft(self.job)
        with self.assertRaisesRegex(ValueError, "different agents"):
            p.record_turn(self.job, "review", "author", "r")
        with self.assertRaisesRegex(ValueError, "Draft already frozen"):
            p.reopen_plan(self.job)
        (self.out / "draft/proof.md").write_text("Changed\n")
        with self.assertRaisesRegex(ValueError, "Frozen file changed"):
            v.check_frozen(self.job)

    def test_full_protocol_and_summary(self):
        self.review_ready()
        v.validate_job(self.job, "final", with_review=True)
        with redirect_stdout(io.StringIO()):
            v.summarize(self.run, [self.job])
        self.assertEqual(read(self.run / "review_summary.json")["verdict_counts"], {"accepted_unchanged": 1})
        self.assertEqual([x["phase"] for x in p.turns_for(self.job)], ["plan", "write", "review"])

    def test_task_instructions_require_correct_continuation(self):
        self.assertIn("fresh author", p.task(self.job, "plan"))
        self.write_ready()
        self.assertIn("SAME author thread", p.task(self.job, "write"))
        p.freeze_draft(self.job)
        self.assertIn("DIFFERENT, fresh reviewer", p.task(self.job, "review"))

    def test_no_old_mutations_or_other_case_reads(self):
        self.write_ready()
        prohibited = self.case / "controlled_pilot/public/reference_proof.md"
        prohibited.parent.mkdir(parents=True)
        prohibited.write_text("Old answer\n")
        self.alignment["files_read"].append(v.relative(prohibited))
        self.save_draft()
        with self.assertRaisesRegex(ValueError, "allowlist"):
            v.validate_job(self.job)


if __name__ == "__main__":
    unittest.main()
