#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from runtime_support.experiment.run_utils import (  # noqa: E402
    atomic_write_json,
    infer_task_identity,
    merged_environment,
    update_run_record,
    validate_identifier,
)
from proof_experiment.llm_solver.run_llm_baseline import (  # noqa: E402
    DEFAULT_ENV_FILE,
    ProviderConfig,
    public_config,
)
from runtime_support.experiment.summary_builder import (  # noqa: E402
    build_all_paper_summaries,
)


DEFAULT_RUNS_ROOT = WORKSPACE_ROOT / ".runtime/runs"
DEFAULT_API_PROFILE = WORKSPACE_ROOT.parent / ".venv/paperproof-config/model-suite/get-api"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Initialize one closed-book LLM proof, one reference-blind validity "
            "review, and one isolated reference-based score."
        )
    )
    parser.add_argument("--task", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS_ROOT)
    parser.add_argument("--solver-env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--evaluator-api-profile", type=Path, default=DEFAULT_API_PROFILE)
    parser.add_argument("--evaluator-model", default="gpt-6-astra")
    parser.add_argument(
        "--evaluator-reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="high",
    )
    parser.add_argument("--evaluator-timeout-seconds", type=int, default=1800)
    return parser.parse_args()


def run_checked(command: list[str]) -> None:
    process = subprocess.run(
        command,
        cwd=WORKSPACE_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if process.returncode != 0:
        raise RuntimeError(
            f"command failed ({process.returncode}): {' '.join(command)}\n"
            f"{process.stderr[-4000:]}"
        )


def main() -> int:
    args = parse_args()
    started = time.monotonic()
    run_id = validate_identifier(args.run_id, "run ID")
    task_path = args.task.resolve()
    paper_id, theorem_id = infer_task_identity(task_path)
    run_dir = args.runs_root.resolve() / run_id
    if run_dir.exists():
        raise FileExistsError(f"run already exists: {run_dir}")

    solver_config = ProviderConfig.from_environment(
        merged_environment(args.solver_env_file.resolve()),
        require_credentials=True,
    )
    run_checked(
        [
            sys.executable,
            str(WORKSPACE_ROOT / "runtime_support/experiment/init_run.py"),
            "--run-id",
            run_id,
            "--runs-root",
            str(args.runs_root.resolve()),
        ]
    )
    record_path = run_dir / "run.json"
    run_record = json.loads(record_path.read_text(encoding="utf-8"))
    run_record.update(
        {
            "status": "running",
            "protocol": "closed_book_llm_then_two_stage_codex_evaluation",
            "dataset": {
                "root": "data/papers",
                "split": "dev",
                "task_type": "task_prove_theorem",
                "selection": f"{paper_id}/{theorem_id}",
                "expected_task_count": 1,
            },
            "solver": {
                "kind": "llm_single_request",
                **public_config(solver_config),
                "system_prompt": (
                    "proof_experiment/llm_solver/prompts/proof_system_prompt.md"
                ),
                "answer_template": (
                    "proof_experiment/llm_solver/prompts/proof_answer_template.md"
                ),
                "tools_enabled": False,
                "retrieval_enabled": False,
                "requests_per_task": 1,
            },
            "evaluator": {
                "kind": "two_independent_codex_agents",
                "provider": args.evaluator_api_profile.name,
                "model": args.evaluator_model,
                "reasoning_effort": args.evaluator_reasoning_effort,
                "stages": [
                    {
                        "name": "validity_reviewer",
                        "prompt": (
                            "reviewer_and_evaluator/reviewer/system_prompt.md"
                        ),
                        "private_reference_access": False,
                        "assigns_score": False,
                    },
                    {
                        "name": "reference_scorer",
                        "prompt": (
                            "reviewer_and_evaluator/evaluator/system_prompt.md"
                        ),
                        "private_reference_access": True,
                        "assigns_score": True,
                    },
                ],
                "score_scale": "integer_0_to_10",
                "evaluators_per_answer": 2,
                "network_tools": "disabled",
            },
        }
    )
    atomic_write_json(record_path, run_record)

    try:
        run_checked(
            [
                sys.executable,
                str(WORKSPACE_ROOT / "proof_experiment/llm_solver/run_llm_baseline.py"),
                "--task",
                str(task_path),
                "--run-id",
                run_id,
                "--runs-root",
                str(args.runs_root.resolve()),
                "--env-file",
                str(args.solver_env_file.resolve()),
            ]
        )
        answer_path = (
            run_dir
            / paper_id
            / theorem_id
            / "answer_for_evaluator.md"
        )
        run_checked(
            [
                sys.executable,
                str(
                    WORKSPACE_ROOT
                    / "reviewer_and_evaluator/reviewer/run_reviewer.py"
                ),
                "--task",
                str(task_path),
                "--answer",
                str(answer_path),
                "--run-id",
                run_id,
                "--runs-root",
                str(args.runs_root.resolve()),
                "--api-profile",
                str(args.evaluator_api_profile.resolve()),
                "--model",
                args.evaluator_model,
                "--reasoning-effort",
                args.evaluator_reasoning_effort,
                "--timeout-seconds",
                str(args.evaluator_timeout_seconds),
            ]
        )
        validity_report_path = (
            run_dir / paper_id / theorem_id / "validity_report.json"
        )
        run_checked(
            [
                sys.executable,
                str(WORKSPACE_ROOT / "reviewer_and_evaluator/evaluator/run_evaluator.py"),
                "--task",
                str(task_path),
                "--answer",
                str(answer_path),
                "--validity-report",
                str(validity_report_path),
                "--run-id",
                run_id,
                "--runs-root",
                str(args.runs_root.resolve()),
                "--api-profile",
                str(args.evaluator_api_profile.resolve()),
                "--model",
                args.evaluator_model,
                "--reasoning-effort",
                args.evaluator_reasoning_effort,
                "--timeout-seconds",
                str(args.evaluator_timeout_seconds),
            ]
        )
        build_all_paper_summaries(run_dir)

        completed_at = datetime.now(timezone.utc).isoformat()

        def complete(record: dict[str, Any]) -> None:
            record["status"] = "completed"
            record["completed_at"] = completed_at
            record["wall_time_seconds"] = round(time.monotonic() - started, 3)

        update_run_record(run_dir, complete)
    except Exception as error:
        failure_message = str(error)
        failed_at = datetime.now(timezone.utc).isoformat()

        def fail(record: dict[str, Any]) -> None:
            record["status"] = "failed"
            record["failed_at"] = failed_at
            record["error"] = failure_message

        update_run_record(run_dir, fail)
        raise

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
