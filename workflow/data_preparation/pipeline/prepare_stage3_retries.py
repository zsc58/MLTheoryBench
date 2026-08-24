#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


GENERATED_NAMES = (
    "paper_analysis",
    "formalization",
    "validation_solver",
    "formalization_reviewer",
    "final_evaluator",
    "pipeline_manifest.json",
)


def atomic_write_json(path: Path, value: Any) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def prepare_retries(
    run_root: Path, requested_paper_ids: list[str] | None = None
) -> list[str]:
    state_path = run_root / "run.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if requested_paper_ids is None:
        selected = sorted(
            paper_id
            for paper_id, record in state["papers"].items()
            if record.get("status") == "failed"
        )
    else:
        selected = sorted(set(requested_paper_ids))
        unknown = [paper_id for paper_id in selected if paper_id not in state["papers"]]
        if unknown:
            raise ValueError("unknown run paper IDs: " + ", ".join(unknown))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    for paper_id in selected:
        paper_dir = run_root / "papers" / paper_id
        archive = run_root / "debug_attempts" / paper_id / stamp
        archive.mkdir(parents=True, exist_ok=True)
        for name in GENERATED_NAMES:
            source = paper_dir / name
            if source.exists():
                shutil.move(str(source), archive / name)
        for suffix in ("stdout.log", "stderr.log"):
            source = run_root / "logs" / f"{paper_id}.{suffix}"
            if source.exists():
                shutil.move(str(source), archive / source.name)
        previous = state["papers"][paper_id]
        state["papers"][paper_id] = {
            "status": "pending",
            "retry_count": int(previous.get("retry_count", 0)) + 1,
            "previous_status": previous.get("status"),
            "previous_exit_code": previous.get("exit_code"),
        }
    state.pop("completed_at", None)
    state.pop("summary", None)
    atomic_write_json(state_path, state)
    retry_file = run_root / "retry_ids.txt"
    retry_file.write_text(
        "".join(f"{paper_id}\n" for paper_id in selected), encoding="utf-8"
    )
    return selected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Archive failed Stage 3 outputs and prepare clean retries."
    )
    parser.add_argument("--run-root", required=True, type=Path)
    parser.add_argument(
        "--paper-ids-file",
        type=Path,
        help="Explicitly archive and rerun these papers, including terminal papers.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    requested = None
    if args.paper_ids_file is not None:
        requested = [
            line.strip()
            for line in args.paper_ids_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    failed = prepare_retries(args.run_root.resolve(), requested)
    print("\n".join(failed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
