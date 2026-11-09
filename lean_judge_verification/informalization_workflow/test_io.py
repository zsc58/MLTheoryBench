#!/usr/bin/env python3
"""Local structural tests; no network, Lean, or model execution."""
from pathlib import Path
import tempfile
import unittest

from io_utils import check_schema, read, sha, validate_markdown
from validation import in_tree


class PipelineTests(unittest.TestCase):
    def test_schema_required_and_extra(self):
        schema = {"type": "object", "required": ["x"], "properties": {"x": {"type": "string"}}, "additionalProperties": False}
        check_schema({"x": "ok"}, schema)
        for value in ({}, {"x": 1}, {"x": "ok", "y": True}):
            with self.assertRaises(ValueError):
                check_schema(value, schema)

    def test_refs_and_integer(self):
        schema = {"$defs": {"v": {"type": "integer", "minimum": 1}}, "$ref": "#/$defs/v"}
        check_schema(1, schema)
        for value in (0, True, "1"):
            with self.assertRaises(ValueError):
                check_schema(value, schema)

    def test_path_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                in_tree(Path(tmp), "../outside")

    def test_math_and_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "proof.md"
            p.write_text("# Proof\n\nLet $x=1$.\n\n$$x^2=1.$$\n", encoding="utf-8")
            validate_markdown(p)
            before = sha(p)
            p.write_text("A broken $formula", encoding="utf-8")
            self.assertNotEqual(before, sha(p))
            with self.assertRaises(ValueError):
                validate_markdown(p)

    def test_tex_row_spacing_is_not_display_delimiter(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "problem.md"
            p.write_text(r"$$\begin{cases}x,&x>0,\\[2mm]0,&x=0.\end{cases}$$", encoding="utf-8")
            validate_markdown(p)
            p.write_text(r"\[x=0\]", encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_markdown(p)

    def test_standalone_single_dollar_is_not_a_display_delimiter(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "proof.md"
            p.write_text("# Proof\n\n$\nx=0\n$\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "double-dollar"):
                validate_markdown(p)
            p.write_text("# Proof\n\n$$\nx=0\n$$\n", encoding="utf-8")
            validate_markdown(p)


if __name__ == "__main__":
    unittest.main()
