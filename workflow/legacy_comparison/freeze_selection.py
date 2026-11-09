#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


from support import atomic_write_json, sha256_file


REQUIRED_FILES = (
    "task.md",
    "proof_ground_truth.md",
    "rubric.md",
    "provenance.json",
    "status.json",
)


def freeze_selection(source_run_root: Path) -> dict[str, Any]:
    source_run_root = source_run_root.resolve()
    papers_root = source_run_root / "papers"
    if not papers_root.is_dir():
        raise FileNotFoundError(f"papers directory not found: {papers_root}")

    papers: dict[str, Any] = {}
    for paper_dir in sorted(papers_root.glob("paper_*")):
        formalization = paper_dir / "formalization"
        status_path = formalization / "status.json"
        if not status_path.is_file():
            continue
        status = json.loads(status_path.read_text(encoding="utf-8"))
        if status.get("status") != "completed":
            continue
        records: dict[str, Any] = {}
        for filename in REQUIRED_FILES:
            path = formalization / filename
            if path.is_symlink() or not path.is_file():
                raise FileNotFoundError(
                    f"completed paper lacks required file: {path}"
                )
            records[filename] = {
                "path": path.relative_to(source_run_root).as_posix(),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
        papers[paper_dir.name] = {"files": records}

    if not papers:
        raise ValueError("no completed papers were discovered")
    return {
        "schema_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_run_root": str(source_run_root),
        "selection_rule": "formalization/status.json status equals completed",
        "paper_count": len(papers),
        "papers": papers,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Freeze completed PaperProof tasks.")
    parser.add_argument("--source-run-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f"selection manifest already exists: {output}")
    value = freeze_selection(args.source_run_root)
    atomic_write_json(output, value)
    print(f"{output} ({value['paper_count']} papers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
