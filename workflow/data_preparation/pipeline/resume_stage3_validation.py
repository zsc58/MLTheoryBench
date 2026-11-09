#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PREPARATION = SCRIPT_DIR.parent
WORKFLOW_ROOT = DATA_PREPARATION.parent
FORMALIZATION_SUPPORT = WORKFLOW_ROOT / "runtime_support/formalization"
for path in (SCRIPT_DIR, FORMALIZATION_SUPPORT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from pipeline_io import record_evaluator_call, record_reviewer_call  # noqa: E402
from stage3_pipeline import persist_status  # noqa: E402
from stage3_validation import Stage3ExperimentValidation  # noqa: E402


DEFAULT_API_PROFILE = (
    WORKFLOW_ROOT.parent / ".venv/paperproof-config/model-suite/get-api"
)


def run(args: argparse.Namespace) -> int:
    paper_dir = args.paper_dir.resolve()
    paper_id = paper_dir.name
    task_path = paper_dir / "formalization/task.md"
    solver_dir = paper_dir / "validation_solver"
    if not task_path.is_file():
        raise FileNotFoundError(task_path)
    if not (solver_dir / "answer.md").is_file():
        raise FileNotFoundError(solver_dir / "answer.md")

    validation = Stage3ExperimentValidation(
        api_profile=args.api_profile,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        timeout_seconds=args.timeout_seconds,
        local_agent_auth=args.local_agent_auth,
        codex_bin=args.codex_bin,
    )
    reviewer_result = validation.run_reviewer(
        paper_id,
        task_path,
        solver_dir,
        paper_dir / "formalization_reviewer",
    )
    record_reviewer_call(paper_dir, reviewer_result)
    if reviewer_result["status"] != "scorable":
        print(f"{paper_id}: reviewer returned unscorable; full feedback loop required")
        return 2

    evaluator_result = validation.run_evaluator(
        paper_id,
        task_path,
        solver_dir,
        paper_dir / "formalization_reviewer",
        paper_dir / "final_evaluator",
    )
    record_evaluator_call(paper_dir, evaluator_result)
    if evaluator_result["result"]["evaluation_status"] == "unscorable":
        persist_status(
            paper_dir,
            status="stopped",
            stop_reason="evaluator_unscorable",
            validation_feedback_count=0,
            source_reaudit_count=0,
        )
        print(f"{paper_id}: stopped; evaluator_unscorable")
        return 0
    persist_status(
        paper_dir,
        status="completed",
        stop_reason=None,
        validation_feedback_count=0,
        source_reaudit_count=0,
    )
    print(f"{paper_id}: completed validation resume")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Resume Stage 3 after an infrastructure-level reviewer/evaluator failure."
        )
    )
    parser.add_argument("--paper-dir", required=True, type=Path)
    parser.add_argument("--api-profile", type=Path, default=DEFAULT_API_PROFILE)
    parser.add_argument("--local-agent-auth", action="store_true")
    parser.add_argument("--model", default="gpt-6-astra")
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="high",
    )
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument(
        "--codex-bin",
        default=os.environ.get("ML_THEORY_CODEX_BIN", "codex"),
    )
    return parser.parse_args()


def main() -> int:
    return run(parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
