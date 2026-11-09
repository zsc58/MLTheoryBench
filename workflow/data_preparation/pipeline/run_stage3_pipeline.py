#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
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

from stage3_pipeline import Stage3Pipeline  # noqa: E402
from stage3_runtime import Stage3CodexBackend, configure_model  # noqa: E402
from stage3_validation import Stage3ExperimentValidation  # noqa: E402


DEFAULT_API_PROFILE = (
    WORKFLOW_ROOT.parent / ".venv/paperproof-config/model-suite/get-api"
)


async def run(args: argparse.Namespace) -> int:
    configure_model(args.model, args.reasoning_effort)
    agent = Stage3CodexBackend(
        profile_dir=None if args.local_agent_auth else args.api_profile
    )
    validation = Stage3ExperimentValidation(
        api_profile=args.api_profile,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        timeout_seconds=args.timeout_seconds,
        local_agent_auth=args.local_agent_auth,
        codex_bin=args.codex_bin,
    )
    try:
        result = await Stage3Pipeline(
            agent, validation, timeout_seconds=args.timeout_seconds
        ).run(
            args.paper_dir,
            overwrite=args.overwrite,
            formalization_only=args.formalization_only,
        )
    finally:
        await agent.aclose()
    print(
        f"{result.paper_id}: {result.status}; "
        f"feedback={result.validation_feedback_count}; "
        f"source_reaudits={result.source_reaudit_count}; "
        f"stop_reason={result.stop_reason}"
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Stage 3 contribution-level pipeline for one paper."
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
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--formalization-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    return asyncio.run(run(parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
