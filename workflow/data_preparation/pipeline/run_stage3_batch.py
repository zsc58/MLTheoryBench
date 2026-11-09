#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import fcntl
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
WORKFLOW_ROOT = SCRIPT_DIR.parents[1]
DEFAULT_API_PROFILE = (
    WORKFLOW_ROOT.parent / ".venv/paperproof-config/model-suite/get-api"
)
RESULT_LINE = re.compile(
    r"^(paper_[A-Za-z0-9_]+): ([a-z_]+); feedback=(\d+); "
    r"source_reaudits=(\d+); stop_reason=(.*)$"
)
TERMINAL_STATUSES = {"completed", "filtered_out", "stopped"}
GENERATED_NAMES = (
    "paper_analysis",
    "formalization",
    "validation_solver",
    "formalization_reviewer",
    "final_evaluator",
    "pipeline_manifest.json",
)
SOURCE_NAMES = ("source.html", "source.tex", "extracted_text.md", "source.pdf")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def usage_leaf(usage: Any) -> dict[str, int]:
    if not isinstance(usage, dict):
        return {}
    leaf = usage.get("last") if isinstance(usage.get("last"), dict) else usage
    values: dict[str, int] = {}
    for key in (
        "input_tokens",
        "cached_input_tokens",
        "output_tokens",
        "reasoning_output_tokens",
        "total_tokens",
    ):
        if isinstance(leaf.get(key), int):
            values[key] = leaf[key]
    if "cached_input_tokens" not in values:
        details = leaf.get("input_tokens_details")
        if isinstance(details, dict) and isinstance(details.get("cached_tokens"), int):
            values["cached_input_tokens"] = details["cached_tokens"]
    return values


def summarize_usage(paper_dir: Path) -> dict[str, Any]:
    manifest_path = paper_dir / "pipeline_manifest.json"
    if not manifest_path.is_file():
        return {"calls": 0, "calls_with_usage": 0, "by_role": {}, "total": {}}
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    by_role: dict[str, Counter[str]] = defaultdict(Counter)
    total: Counter[str] = Counter()
    calls_with_usage = 0
    for call in manifest.get("calls", []):
        values = usage_leaf(call.get("usage"))
        if not values:
            continue
        calls_with_usage += 1
        by_role[str(call.get("role", "unknown"))].update(values)
        total.update(values)
    total["noncached_input_tokens"] = max(
        0, total.get("input_tokens", 0) - total.get("cached_input_tokens", 0)
    )
    return {
        "calls": len(manifest.get("calls", [])),
        "calls_with_usage": calls_with_usage,
        "by_role": {key: dict(value) for key, value in sorted(by_role.items())},
        "total": dict(total),
    }


def official_cost(tokens: dict[str, int]) -> float:
    return (
        tokens.get("noncached_input_tokens", 0) * 5.0
        + tokens.get("cached_input_tokens", 0) * 0.5
        + tokens.get("output_tokens", 0) * 30.0
    ) / 1_000_000


def parse_result(stdout: str) -> dict[str, Any]:
    for line in reversed(stdout.splitlines()):
        match = RESULT_LINE.match(line.strip())
        if match:
            reason = match.group(5)
            return {
                "status": match.group(2),
                "validation_feedback_count": int(match.group(3)),
                "source_reaudit_count": int(match.group(4)),
                "stop_reason": None if reason == "None" else reason,
            }
    return {}


def validate_private_source(private_source: Path, paper_id: str) -> None:
    metadata_path = private_source / "metadata.json"
    if not metadata_path.is_file():
        raise FileNotFoundError(metadata_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if metadata.get("paper_id") != paper_id:
        raise ValueError(f"metadata paper_id mismatch for {paper_id}")
    declared = metadata.get("content_source_file")
    if declared is not None:
        if declared not in SOURCE_NAMES:
            raise ValueError(
                f"unsupported content_source_file for {paper_id}: {declared}"
            )
        if not (private_source / declared).is_file():
            raise FileNotFoundError(private_source / declared)
    elif not any((private_source / name).is_file() for name in SOURCE_NAMES):
        raise ValueError(f"no readable source file for {paper_id}")


def stage_paper(source_root: Path, run_root: Path, paper_id: str) -> Path:
    source = source_root / paper_id / "private_source"
    if not source.is_dir():
        raise FileNotFoundError(source)
    validate_private_source(source, paper_id)
    target = run_root / "papers" / paper_id
    target.mkdir(parents=True, exist_ok=True)
    target_source = target / "private_source"
    if not target_source.exists():
        shutil.copytree(source, target_source)
    else:
        try:
            validate_private_source(target_source, paper_id)
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            shutil.rmtree(target_source)
            shutil.copytree(source, target_source)
    validate_private_source(target_source, paper_id)
    return target


def archive_incomplete_attempt(run_root: Path, paper_id: str) -> bool:
    paper_dir = run_root / "papers" / paper_id
    present = [name for name in GENERATED_NAMES if (paper_dir / name).exists()]
    log_paths = [
        run_root / "logs" / f"{paper_id}.{suffix}.log"
        for suffix in ("stdout", "stderr")
    ]
    if not present and not any(path.exists() for path in log_paths):
        return False
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    archive = run_root / "debug_attempts" / paper_id / stamp
    archive.mkdir(parents=True, exist_ok=False)
    for name in present:
        shutil.move(str(paper_dir / name), archive / name)
    for path in log_paths:
        if path.exists():
            shutil.move(str(path), archive / path.name)
    return True


def acquire_run_lock(run_root: Path):
    lock_path = run_root / ".run.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as error:
        handle.close()
        raise RuntimeError(f"another batch supervisor holds {lock_path}") from error
    handle.seek(0)
    handle.truncate()
    handle.write(json.dumps({"pid": os.getpid(), "started_at": utc_now()}) + "\n")
    handle.flush()
    return handle


def load_ids(args: argparse.Namespace) -> list[str]:
    if args.paper_ids:
        return args.paper_ids
    if args.paper_ids_file is None:
        raise ValueError("provide --paper-ids or --paper-ids-file")
    return [
        line.strip()
        for line in args.paper_ids_file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


async def run_batch(args: argparse.Namespace) -> int:
    paper_ids = load_ids(args)
    if len(paper_ids) != len(set(paper_ids)):
        raise ValueError("paper list contains duplicates")
    run_root = args.run_root.resolve()
    run_lock = acquire_run_lock(run_root)
    logs = run_root / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    state_path = run_root / "run.json"
    state = (
        json.loads(state_path.read_text(encoding="utf-8"))
        if state_path.is_file()
        else {
            "created_at": utc_now(),
            "configuration": {
                "paper_ids": paper_ids,
                "workers": args.workers,
                "model": args.model,
                "reasoning_effort": args.reasoning_effort,
            },
            "papers": {paper_id: {"status": "pending"} for paper_id in paper_ids},
        }
    )
    configuration = state.setdefault("configuration", {})
    for key, expected in (
        ("model", args.model),
        ("reasoning_effort", args.reasoning_effort),
        ("source_papers_root", str(args.source_papers_root.resolve())),
    ):
        existing = configuration.get(key)
        if existing is not None and existing != expected:
            run_lock.close()
            raise ValueError(
                f"run configuration mismatch for {key}: {existing!r} != {expected!r}"
            )
        configuration[key] = expected
    configuration["workers"] = args.workers
    configured_ids = configuration.setdefault("paper_ids", [])
    for paper_id in paper_ids:
        if paper_id not in configured_ids:
            configured_ids.append(paper_id)
        state.setdefault("papers", {}).setdefault(paper_id, {"status": "pending"})
    for paper_id in paper_ids:
        paper_dir = stage_paper(args.source_papers_root, run_root, paper_id)
        status_path = paper_dir / "formalization/status.json"
        if status_path.is_file():
            status = json.loads(status_path.read_text(encoding="utf-8"))
            if status.get("status") in TERMINAL_STATUSES:
                state["papers"][paper_id] = {
                    **status,
                    "usage": summarize_usage(paper_dir),
                }
                continue
        previous = state["papers"][paper_id]
        archived = archive_incomplete_attempt(run_root, paper_id)
        state["papers"][paper_id] = {
            "status": "pending",
            "retry_count": int(previous.get("retry_count", 0)) + int(archived),
        }
    atomic_write_json(state_path, state)

    semaphore = asyncio.Semaphore(args.workers)

    async def run_one(paper_id: str) -> None:
        if state["papers"][paper_id].get("status") in TERMINAL_STATUSES:
            return
        async with semaphore:
            paper_dir = run_root / "papers" / paper_id
            prior_retries = int(
                state["papers"][paper_id].get("retry_count", 0)
            )
            for attempt in range(1, args.paper_attempts + 1):
                if attempt > 1:
                    archive_incomplete_attempt(run_root, paper_id)
                started = utc_now()
                retry_count = prior_retries + attempt - 1
                state["papers"][paper_id] = {
                    "status": "running",
                    "started_at": started,
                    "attempt": attempt,
                    "retry_count": retry_count,
                }
                atomic_write_json(state_path, state)
                command = [
                    str(args.python_bin),
                    str(SCRIPT_DIR / "run_stage3_pipeline.py"),
                    "--paper-dir", str(paper_dir),
                    "--api-profile", str(args.api_profile),
                    "--model", args.model,
                    "--reasoning-effort", args.reasoning_effort,
                    "--timeout-seconds", str(args.timeout_seconds),
                    "--codex-bin", str(args.codex_bin),
                ]
                process = await asyncio.create_subprocess_exec(
                    *command,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    cwd=str(WORKFLOW_ROOT),
                    env={**os.environ, "ML_THEORY_CODEX_BIN": str(args.codex_bin)},
                )
                try:
                    stdout_bytes, stderr_bytes = await process.communicate()
                except asyncio.CancelledError:
                    process.terminate()
                    try:
                        await asyncio.wait_for(process.wait(), timeout=10)
                    except asyncio.TimeoutError:
                        process.kill()
                        await process.wait()
                    state["papers"][paper_id] = {
                        "status": "interrupted",
                        "started_at": started,
                        "completed_at": utc_now(),
                        "attempt": attempt,
                        "retry_count": retry_count,
                    }
                    atomic_write_json(state_path, state)
                    raise
                stdout = stdout_bytes.decode("utf-8", errors="replace")
                stderr = stderr_bytes.decode("utf-8", errors="replace")
                (logs / f"{paper_id}.stdout.log").write_text(
                    stdout, encoding="utf-8"
                )
                (logs / f"{paper_id}.stderr.log").write_text(
                    stderr, encoding="utf-8"
                )
                result = parse_result(stdout)
                status_path = paper_dir / "formalization/status.json"
                persisted_status = (
                    json.loads(status_path.read_text(encoding="utf-8"))
                    if status_path.is_file()
                    else {}
                )
                status = (
                    persisted_status.get("status")
                    or result.get("status")
                    or "failed"
                )
                state["papers"][paper_id] = {
                    **result,
                    **persisted_status,
                    "status": status,
                    "exit_code": process.returncode,
                    "started_at": started,
                    "completed_at": utc_now(),
                    "attempt": attempt,
                    "retry_count": retry_count,
                    "usage": summarize_usage(paper_dir),
                }
                atomic_write_json(state_path, state)
                if status in TERMINAL_STATUSES:
                    break

    await asyncio.gather(*(run_one(paper_id) for paper_id in paper_ids))

    total: Counter[str] = Counter()
    by_role: dict[str, Counter[str]] = defaultdict(Counter)
    status_counts: Counter[str] = Counter()
    classification_counts: Counter[str] = Counter()
    for record in state["papers"].values():
        status_counts[record.get("status", "unknown")] += 1
        classification = record.get("paper_classification")
        if classification is not None:
            classification_counts[classification] += 1
        usage = record.get("usage", {})
        total.update(usage.get("total", {}))
        for role, values in usage.get("by_role", {}).items():
            by_role[role].update(values)
    state["completed_at"] = utc_now()
    state["summary"] = {
        "status_counts": dict(sorted(status_counts.items())),
        "paper_classification_counts": dict(sorted(classification_counts.items())),
        "usage_total": dict(total),
        "usage_by_role": {
            role: dict(values) for role, values in sorted(by_role.items())
        },
        "official_equivalent_cost_usd": official_cost(dict(total)),
        "relay_tenth_estimate_usd": official_cost(dict(total)) / 10,
    }
    atomic_write_json(state_path, state)
    atomic_write_json(run_root / "summary.json", state["summary"])
    run_lock.close()
    nonterminal_failures = sum(
        status_counts.get(status, 0)
        for status in ("failed", "unknown", "running", "pending", "interrupted")
    )
    return 1 if nonterminal_failures else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a resumable Stage 3 paper batch.")
    parser.add_argument("--source-papers-root", required=True, type=Path)
    parser.add_argument("--run-root", required=True, type=Path)
    parser.add_argument("--paper-ids", nargs="*")
    parser.add_argument("--paper-ids-file", type=Path)
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--python-bin", type=Path, default=Path(sys.executable))
    parser.add_argument("--api-profile", type=Path, default=DEFAULT_API_PROFILE)
    parser.add_argument("--codex-bin", required=True, type=Path)
    parser.add_argument("--model", default="gpt-6-astra")
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--timeout-seconds", type=int, default=2400)
    parser.add_argument("--paper-attempts", type=int, default=2)
    return parser.parse_args()


def main() -> int:
    return asyncio.run(run_batch(parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
