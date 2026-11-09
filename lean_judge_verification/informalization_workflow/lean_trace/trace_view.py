#!/usr/bin/env python3
"""Read selected anchored tactic-state records without invoking Lean."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def select_tactics(trace: dict, ids: list[str] | None = None,
                   lines: tuple[int, int] | None = None,
                   original_only: bool = False) -> list[dict]:
    records = trace["tactics"]
    if ids:
        wanted = set(ids)
        missing = wanted - {item["id"] for item in records}
        if missing:
            raise ValueError(f"unknown tactic IDs: {', '.join(sorted(missing))}")
        records = [item for item in records if item["id"] in wanted]
    if lines:
        first, last = lines
        if first < 1 or last < first:
            raise ValueError("--lines requires 1 <= START <= END")
        records = [item for item in records
                   if item["source_span"]["start"]["line"] <= last
                   and (item["source_span"]["end"]["line"]
                        - (item["source_span"]["end"]["column"] == 0)) >= first]
    if original_only:
        records = [item for item in records if item.get("source_kind") == "original"]
    return records


def compact_index(record: dict) -> dict:
    start, end = record["source_span"]["start"], record["source_span"]["end"]
    return {"id": record["id"], "parent_id": record["parent_id"],
            "range": f'{start["line"]}:{start["column"]}-{end["line"]}:{end["column"]}',
            "syntax_kind": record.get("syntax_kind"), "source_kind": record.get("source_kind"),
            "goals": [record["before"]["goal_count"], record["after"]["goal_count"]],
            "declaration_name": record.get("declaration_name")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trace", type=Path)
    parser.add_argument("--id", action="append", help="exact tactic ID; repeat to select several")
    parser.add_argument("--lines", help="inclusive source line interval START:END (overlapping scopes retained)")
    parser.add_argument("--index", action="store_true", help="compact anchors only, without before/after goals")
    parser.add_argument("--original-only", action="store_true", help="display original-source nodes only; raw trace remains unfiltered")
    parser.add_argument("--limit", type=int, help="maximum displayed records; report any truncation explicitly")
    args = parser.parse_args()
    try:
        trace = json.loads(args.trace.read_text(encoding="utf-8"))
        lines = None
        if args.lines:
            parts = args.lines.split(":")
            if len(parts) != 2:
                raise ValueError("--lines must be START:END")
            lines = (int(parts[0]), int(parts[1]))
        if not (args.id or lines or args.index):
            parser.error("select --id, --lines, or --index to avoid dumping every state")
        if args.limit is not None and args.limit <= 0:
            raise ValueError("--limit must be positive")
        records = select_tactics(trace, args.id, lines, args.original_only)
    except (OSError, ValueError, KeyError) as error:
        parser.error(str(error))
    selected_count = len(records)
    if args.limit is not None:
        records = records[:args.limit]
    result = {key: trace.get(key) for key in
              ("status", "source", "source_file", "source_sha256", "revision", "lean_version")}
    result.update({"trace_file": str(args.trace), "selected_tactic_count": selected_count,
                   "displayed_tactic_count": len(records), "truncated": len(records) < selected_count,
                   "original_only": args.original_only,
                   "scope_note": "Local no-goals does not mean global proof completion; display filters do not alter the raw trace."})
    if args.index:
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
        for record in records:
            print(json.dumps(compact_index(record), ensure_ascii=False, separators=(",", ":")))
    else:
        result["tactics"] = records
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
