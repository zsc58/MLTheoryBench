#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from runtime_support.experiment.run_utils import (  # noqa: E402
    atomic_write_json,
    validate_identifier,
)


DEFAULT_RUNS_ROOT = WORKSPACE_ROOT / ".runtime/runs"
DEFAULT_TEMPLATE = Path(__file__).parent / "run_template.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize one empty proof experiment run."
    )
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS_ROOT)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_id = validate_identifier(args.run_id, "run ID")
    config = json.loads(args.template.resolve().read_text(encoding="utf-8"))
    config["run_id"] = run_id
    config["created_at"] = datetime.now(timezone.utc).isoformat()

    run_dir = args.runs_root.resolve() / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    atomic_write_json(run_dir / "run.json", config)
    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
