#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from support import atomic_write_json, sha256_file


REQUIRED_FORMALIZATION_FILES = (
    "task.md",
    "proof_ground_truth.md",
    "rubric.md",
    "provenance.json",
    "status.json",
)
OPTIONAL_AUDIT_FILES = (
    "formalization/thread_b_view.json",
    "paper_analysis/paper_analysis.json",
    "paper_analysis/turn3_source_audit.json",
)
SOURCE_NAMES = (
    "extracted_text.md",
    "source.md",
    "source.tex",
    "source.html",
)
SUSPECT_STOP_REASONS = {
    "max_validation_feedback",
    "evaluator_unscorable",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def file_entry(root: Path, path: Path) -> dict[str, Any]:
    return {
        "path": path.resolve().relative_to(root.resolve()).as_posix(),
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
    }


def cohort(status: dict[str, Any]) -> str | None:
    if status.get("status") == "completed":
        return "completed"
    if status.get("paper_classification") == "suspect":
        return "suspect"
    if status.get("stop_reason") in SUSPECT_STOP_REASONS:
        return "suspect"
    return None


def freeze_selection(source_run_root: Path, include_suspect: bool) -> dict[str, Any]:
    root = source_run_root.resolve()
    papers_root = root / "papers"
    if not papers_root.is_dir():
        raise FileNotFoundError(papers_root)
    selected: dict[str, Any] = {}
    ineligible: dict[str, Any] = {}
    for paper_dir in sorted(papers_root.glob("paper_*")):
        status_path = paper_dir / "formalization/status.json"
        if not status_path.is_file():
            continue
        status = load_json(status_path)
        group = cohort(status)
        if group is None or (group == "suspect" and not include_suspect):
            continue
        files: dict[str, Any] = {}
        missing: list[str] = []
        for name in REQUIRED_FORMALIZATION_FILES:
            path = paper_dir / "formalization" / name
            if path.is_file():
                files[name] = file_entry(root, path)
            else:
                missing.append(name)
        for relative in OPTIONAL_AUDIT_FILES:
            path = paper_dir / relative
            if path.is_file():
                files[relative] = file_entry(root, path)
        source = next(
            (
                paper_dir / "private_source" / name
                for name in SOURCE_NAMES
                if (paper_dir / "private_source" / name).is_file()
            ),
            None,
        )
        if source is not None:
            files[f"private_source/{source.name}"] = file_entry(root, source)
        if missing:
            ineligible[paper_dir.name] = {
                "cohort": group,
                "reason": "missing_required_formalization_files",
                "missing": missing,
            }
            continue
        selected[paper_dir.name] = {
            "cohort": group,
            "files": files,
            "audit_ready": (
                "formalization/thread_b_view.json" in files
                and "paper_analysis/turn3_source_audit.json" in files
                and any(name.startswith("private_source/") for name in files)
            ),
        }
    return {
        "schema_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_run_root": str(root),
        "selection_policy": "completed_plus_prior_suspect"
        if include_suspect
        else "completed_only",
        "paper_count": len(selected),
        "ineligible_count": len(ineligible),
        "papers": selected,
        "ineligible": ineligible,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Freeze completed and optionally prior-suspect PaperProof packages."
    )
    parser.add_argument("--source-run-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--include-suspect", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    value = freeze_selection(args.source_run_root, args.include_suspect)
    atomic_write_json(args.output.resolve(), value)
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
