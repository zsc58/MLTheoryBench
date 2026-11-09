"""Offline structural tests; --artifacts checks all configured built bundles."""
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

import build_cases as b


class ParserTests(unittest.TestCase):
    def test_receipt_rejects_changed_driver_or_unsuccessful_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            ev = Path(tmp)
            case, source = {"id": "test", "target": "T"}, {"revision": "rev"}
            receipt = {"case_id": "test", "target": "T", "source_revision": "rev",
                       "source_fingerprint": "fp", "lean_toolchain": "tc", "exit_code": 0}
            for key, name in {"trace_sha256": "lean_dependencies.json", "driver_sha256": "export_driver.lean", "build_log_sha256": "target_build.log", "check_log_sha256": "lean_check.log"}.items():
                (ev / name).write_text(name)
                receipt[key] = b.digest(ev / name)
            b.validate_receipt(ev, receipt, case, source, "fp", "tc")
            with self.assertRaises(ValueError):
                b.validate_receipt(ev, dict(receipt, exit_code=1), case, source, "fp", "tc")
            (ev / "export_driver.lean").write_text("changed")
            with self.assertRaises(ValueError):
                b.validate_receipt(ev, receipt, case, source, "fp", "tc")

    def test_nested_comments_and_strings(self):
        text = 'import Real.Module\n/- import Fake.A /- nested -/ -/\n-- import Fake.B\ndef s := "import Fake.C"\n'
        clean = b.uncomment(text)
        self.assertEqual(len(clean), len(text))
        self.assertEqual(clean.count("\n"), text.count("\n"))
        self.assertIn("import Real.Module", clean)
        self.assertNotIn("Fake", clean)

    def test_import_cycle_and_missing_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "A.lean").write_text("import B\nimport Mathlib.X\n")
            (root / "B.lean").write_text("import A\n")
            result = b.closure(root, "A")
            self.assertEqual(set(result["project_modules"]), {"A", "B"})
            self.assertEqual(result["external_module_boundary"], ["Mathlib.X"])
            with self.assertRaises(FileNotFoundError):
                b.closure(root, "Missing")

    def test_active_blueprint_and_multi_declaration_node(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "blueprint/src"
            src.mkdir(parents=True)
            (src / "content.tex").write_text("\\input{active}\n% \\input{unused}\n")
            (src / "active.tex").write_text(
                r"\begin{lemma}\label{up}\lean{Ns.up} U\end{lemma}" + "\n" +
                r"\begin{theorem}\label{main}\lean{Ns.a, Ns.b} T\end{theorem}" + "\n" +
                r"\begin{proof}\uses{up} P\end{proof}")
            (src / "unused.tex").write_text(r"\begin{lemma}\label{unused} X\end{lemma}")
            result = b.blueprint_closure(root, "Ns.b")
            self.assertEqual(set(result["nodes"]), {"up", "main"})
            self.assertEqual(result["root_labels"], ["main"])
            self.assertEqual(result["unresolved_labels"], [])


class ArtifactTests(unittest.TestCase):
    def test_configured_verified_targets(self):
        configured = [case["id"] for case in b.CONFIG["cases"]]
        index = json.loads((b.BUNDLES / "index.json").read_text())
        self.assertTrue(configured)
        self.assertEqual(len(configured), len(set(configured)))
        self.assertEqual(set(configured), {case["case_id"] for case in index["cases"]})
        for case in b.CONFIG["cases"]:
            with self.subTest(case=case["id"]):
                folder = b.BUNDLES / case["id"]
                ev = folder / "evidence"
                manifest = json.loads((ev / "manifest.json").read_text())
                trace = json.loads((ev / "lean_dependencies.json").read_text())
                receipt = json.loads((ev / "verification_receipt.json").read_text())
                self.assertTrue(manifest["lean_locally_verified"])
                self.assertTrue(manifest["standard_axioms_only"])
                self.assertEqual(manifest["trace_sha256"], b.digest(ev / "lean_dependencies.json"))
                self.assertEqual(receipt["trace_sha256"], manifest["trace_sha256"])
                source = b.CONFIG["sources"][case["source"]]
                b.validate_receipt(ev, receipt, case, source, b.source_fingerprint(b.BASE / source["root"]), manifest["lean_toolchain"])
                self.assertEqual(trace["target"], case["target"])
                nodes = {n["name"]: n for n in trace["project_declaration_closure"]}
                self.assertIn(case["target"], nodes)
                self.assertEqual(nodes[case["target"]]["kind"], "theorem")
                self.assertTrue(nodes[case["target"]]["proof_or_definition_body_available"])
                self.assertTrue(nodes[case["target"]]["value_dependencies"])
                imports = json.loads((ev / "import_closure.json").read_text())
                self.assertLessEqual({n["module"] for n in nodes.values()}, set(imports["project_modules"]))
                boundary = {n["name"] for n in trace["external_background_boundary"]}
                for node in nodes.values():
                    if node["kind"] == "theorem":
                        self.assertTrue(node["proof_or_definition_body_available"], node["name"])
                    self.assertLessEqual(set(node["type_dependencies"] + node["value_dependencies"] + node["declaration_metadata_dependencies"]), set(nodes) | boundary)
                if case["id"] == "tlb/01_bayes_optimality":
                    for name in ["ProbabilityTheory.estimationProblem", "ProbabilityTheory.HasGenBayesEstimator", "ProbabilityTheory.IsGenBayesEstimator"]:
                        self.assertIn(name + ".mk", nodes)
                for record in json.loads((ev / "source_files.json").read_text()):
                    self.assertEqual(b.digest(folder / record["path"]), record["sha256"])
                self.assertEqual(manifest["background_source_missing"], [])
                for record in json.loads((ev / "background_source_files.json").read_text()):
                    self.assertEqual(b.digest(folder / record["path"]), record["sha256"])
                current = b.BASE / "data" / case["source"] / case["id"].replace("/", "_")
                self.assertTrue((current / "proof.md").is_file())
                self.assertFalse((current / "final").exists())

    def test_local_document_links_and_math_delimiters(self):
        for path in (b.BASE / "data").rglob("*.md"):
            if any(part in path.parts for part in ("sources", "evidence", "snapshot")):
                continue
            text = path.read_text()
            text = re.sub(r"```.*?```", "", text, flags=re.S)
            self.assertEqual(text.count("$$") % 2, 0, str(path))
            self.assertNotRegex(text, r"(?<!\\)\\[\[\]]", str(path))
            link_text = re.sub(r"\$\$.*?\$\$|(?<!\\)\$[^$\n]*\$", "", text, flags=re.S)
            for target in re.findall(r"\]\(([^)]+)\)", link_text):
                target = target.split("#", 1)[0]
                if not target or "://" in target:
                    continue
                self.assertTrue((path.parent / target).is_file(), f"{path}: {target}")


if __name__ == "__main__":
    with_artifacts = "--artifacts" in sys.argv
    sys.argv = [s for s in sys.argv if s != "--artifacts"]
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ParserTests)
    if with_artifacts:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ArtifactTests))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful())
