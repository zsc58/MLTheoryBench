from __future__ import annotations

import hashlib
import fcntl
import json
import os
import re
import tempfile
from pathlib import Path
from collections.abc import Callable
from typing import Any


IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
RUN_LOCKS_ROOT = WORKSPACE_ROOT / ".runtime/run-locks"
USAGE_KEYS = (
    "input_tokens",
    "cached_input_tokens",
    "non_cached_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)


def validate_identifier(value: str, label: str) -> str:
    if not IDENTIFIER_RE.fullmatch(value):
        raise ValueError(
            f"{label} must contain only letters, digits, dot, underscore, or hyphen"
        )
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def file_record(path: Path, *, label: str, exposed_as: str) -> dict[str, Any]:
    if path.is_symlink():
        raise ValueError(f"{label} must not be a symlink: {path}")
    resolved = path.resolve()
    if not resolved.is_file():
        raise FileNotFoundError(f"{label} is not a regular file: {resolved}")
    return {
        "label": label,
        "source_path": str(resolved),
        "exposed_as": exposed_as,
        "sha256": sha256_file(resolved),
        "bytes": resolved.stat().st_size,
    }


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def load_env_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    values: dict[str, str] = {}
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            raise ValueError(f"invalid env line {line_number} in {path}")
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value[:1] == value[-1:] and value.startswith(("'", '"')):
            value = value[1:-1]
        values[key] = value
    return values


def merged_environment(path: Path | None) -> dict[str, str]:
    values = load_env_file(path) if path is not None else {}
    values.update(os.environ)
    return values


def infer_task_identity(task_path: Path) -> tuple[str, str]:
    theorem_dir = task_path.resolve().parent.parent
    paper_dir = theorem_dir.parent.parent
    if not theorem_dir.name.startswith("theorem_"):
        raise ValueError(f"cannot infer theorem ID from {task_path}")
    if not paper_dir.name.startswith("paper_"):
        raise ValueError(f"cannot infer paper ID from {task_path}")
    return paper_dir.name, theorem_dir.name


def require_initialized_run(runs_root: Path, run_id: str) -> Path:
    run_dir = runs_root.resolve() / run_id
    record_path = run_dir / "run.json"
    if not record_path.is_file():
        raise FileNotFoundError(
            f"run is not initialized: {record_path}; run init_run.py first"
        )
    record = json.loads(record_path.read_text(encoding="utf-8"))
    if record.get("run_id") != run_id:
        raise ValueError(
            f"run.json has run_id={record.get('run_id')!r}, expected {run_id!r}"
        )
    return run_dir


def update_run_record(
    run_dir: Path, update: Callable[[dict[str, Any]], None]
) -> dict[str, Any]:
    """Update run.json safely when multiple theorem processes share one run."""
    run_dir = run_dir.resolve()
    record_path = run_dir / "run.json"
    if not record_path.is_file():
        raise FileNotFoundError(f"run record not found: {record_path}")

    RUN_LOCKS_ROOT.mkdir(parents=True, exist_ok=True)
    lock_name = sha256_text(str(run_dir))[:24] + ".lock"
    with (RUN_LOCKS_ROOT / lock_name).open("a", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        record = json.loads(record_path.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            raise ValueError(f"run record must be a JSON object: {record_path}")
        update(record)
        atomic_write_json(record_path, record)
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return record


def update_run_task_stage(
    run_dir: Path,
    paper_id: str,
    theorem_id: str,
    stage: str,
    stage_record: dict[str, Any],
) -> dict[str, Any]:
    if stage not in {"solver", "validity_reviewer", "evaluator"}:
        raise ValueError(f"unsupported run task stage: {stage}")

    def update(record: dict[str, Any]) -> None:
        stored_stage = dict(stage_record)
        # Keep per-stage usage available to callers that consume the isolated
        # run record, while also adding it to the run-level aggregate below.
        stage_usage = stored_stage.get("usage")
        task_key = f"{paper_id}/{theorem_id}"
        task = record.setdefault("tasks", {}).setdefault(
            task_key,
            {"paper_id": paper_id, "theorem_id": theorem_id},
        )
        task[stage] = stored_stage
        if isinstance(stage_usage, dict):
            usage = record.setdefault(
                "usage",
                {
                    "scope": "clean_experiment_only",
                    "solver": {key: 0 for key in USAGE_KEYS},
                    "validity_reviewer": {key: 0 for key in USAGE_KEYS},
                    "evaluator": {key: 0 for key in USAGE_KEYS},
                    "total": {key: 0 for key in USAGE_KEYS},
                },
            )
            if not isinstance(usage, dict):
                raise ValueError("run usage must be a JSON object")
            for bucket in (stage, "total"):
                totals = usage.setdefault(bucket, {key: 0 for key in USAGE_KEYS})
                for key in USAGE_KEYS:
                    totals[key] = int(totals.get(key, 0) or 0) + int(
                        stage_usage.get(key, 0) or 0
                    )

    return update_run_record(run_dir, update)


def split_self_assessment(answer: str) -> tuple[str, str | None]:
    match = re.search(
        r"(?im)^[ \t]*##[ \t]+Self-Assessment[ \t]*$",
        answer,
    )
    if match is None:
        return answer.rstrip() + "\n", None
    proof = answer[: match.start()].rstrip() + "\n"
    self_assessment = answer[match.start() :].rstrip() + "\n"
    return proof, self_assessment


def normalize_obsidian_markdown(value: str) -> str:
    """Normalize model Markdown without changing fenced code blocks."""
    normalized: list[str] = []
    in_fence = False
    for line in value.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            normalized.append(line)
            continue
        if in_fence:
            normalized.append(line)
            continue
        normalized.append(
            line.replace(r"\[", "$$")
            .replace(r"\]", "$$")
            .replace(r"\(", "$")
            .replace(r"\)", "$")
        )
    return "\n".join(normalized).rstrip() + "\n"


def normalize_usage(value: Any) -> dict[str, int] | None:
    """Normalize Responses API and Codex usage objects for run accounting."""
    if not isinstance(value, dict):
        return None

    input_tokens = int(value.get("input_tokens", 0) or 0)
    output_tokens = int(value.get("output_tokens", 0) or 0)
    total_tokens = int(value.get("total_tokens", 0) or 0)

    input_details = value.get("input_tokens_details")
    cached_input_tokens = int(value.get("cached_input_tokens", 0) or 0)
    if isinstance(input_details, dict):
        cached_input_tokens = int(
            input_details.get("cached_tokens", cached_input_tokens) or 0
        )

    output_details = value.get("output_tokens_details")
    reasoning_output_tokens = int(value.get("reasoning_output_tokens", 0) or 0)
    if isinstance(output_details, dict):
        reasoning_output_tokens = int(
            output_details.get("reasoning_tokens", reasoning_output_tokens) or 0
        )

    if total_tokens == 0:
        total_tokens = input_tokens + output_tokens
    return {
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_input_tokens,
        "non_cached_input_tokens": max(0, input_tokens - cached_input_tokens),
        "output_tokens": output_tokens,
        "reasoning_output_tokens": reasoning_output_tokens,
        "total_tokens": total_tokens,
    }
