#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from runtime_support.experiment.run_utils import (  # noqa: E402
    require_initialized_run,
    validate_identifier,
)
from runtime_support.experiment.summary_builder import (  # noqa: E402
    build_all_paper_summaries,
)


DEFAULT_RUNS_ROOT = WORKSPACE_ROOT / ".runtime/runs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build deterministic paper summaries after theorem evaluations finish."
    )
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS_ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_id = validate_identifier(args.run_id, "run ID")
    run_dir = require_initialized_run(args.runs_root, run_id)
    summaries = build_all_paper_summaries(run_dir)
    print(
        json.dumps(
            {
                "run_id": run_id,
                "paper_count": len(summaries),
                "completed_papers": sum(
                    value["status"] == "completed" for value in summaries.values()
                ),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
