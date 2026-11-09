#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def paired_schema(title: str, item_name: str, single: dict[str, Any]) -> dict[str, Any]:
    embedded = dict(single)
    embedded.pop("$schema", None)
    embedded.pop("title", None)
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": title,
        "type": "object",
        "additionalProperties": False,
        "required": ["answer_reports"],
        "properties": {
            "answer_reports": {
                "type": "array",
                "minItems": 1,
                "maxItems": 8,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["answer_id", item_name],
                    "properties": {
                        "answer_id": {
                            "type": "string",
                            "pattern": "^answer_[a-h]$",
                        },
                        item_name: embedded,
                    },
                },
            }
        },
    }


def main() -> int:
    pairs = (
        (
            "reviewer.schema.json",
            "paired_reviewer.schema.json",
            "Paired ML Theory Proof Validity Reports",
            "report",
        ),
        (
            "evaluator.schema.json",
            "paired_evaluator.schema.json",
            "Paired ML Theory Proof Evaluations",
            "evaluation",
        ),
    )
    for source_name, output_name, title, item_name in pairs:
        value = paired_schema(title, item_name, load_json(SCHEMAS / source_name))
        (SCHEMAS / output_name).write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
