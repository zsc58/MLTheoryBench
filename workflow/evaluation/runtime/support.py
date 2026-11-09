from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Callable


def validate_identifier(value: str, label: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", value):
        raise ValueError(f"invalid {label}: {value!r}")
    return value


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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


def locked_update_json(
    path: Path, update: Callable[[dict[str, Any]], None]
) -> dict[str, Any]:
    lock_path = path.with_suffix(path.suffix + ".lock")
    with lock_path.open("a", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        value = json.loads(path.read_text(encoding="utf-8"))
        update(value)
        atomic_write_json(path, value)
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return value


def load_env_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise FileNotFoundError(f"environment file not found: {path}")
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
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key.strip()] = value
    return values


def merged_environment(path: Path) -> dict[str, str]:
    values = load_env_file(path)
    values.update(os.environ)
    return values


def split_self_assessment(answer: str) -> tuple[str, str | None]:
    match = re.search(r"(?im)^[ \t]*##[ \t]+Self-Assessment[ \t]*$", answer)
    if match is None:
        return answer.rstrip() + "\n", None
    return (
        answer[: match.start()].rstrip() + "\n",
        answer[match.start() :].rstrip() + "\n",
    )


def normalize_obsidian_markdown(value: str) -> str:
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
    if not isinstance(value, dict):
        return None
    input_tokens = int(
        value.get("input_tokens", value.get("prompt_tokens", 0)) or 0
    )
    output_tokens = int(
        value.get("output_tokens", value.get("completion_tokens", 0)) or 0
    )
    total_tokens = int(value.get("total_tokens", 0) or 0)
    input_details = value.get(
        "input_tokens_details", value.get("prompt_tokens_details")
    )
    cached = int(value.get("cached_input_tokens", 0) or 0)
    if isinstance(input_details, dict):
        cached = int(input_details.get("cached_tokens", cached) or 0)
    output_details = value.get(
        "output_tokens_details", value.get("completion_tokens_details")
    )
    reasoning = int(value.get("reasoning_output_tokens", 0) or 0)
    if isinstance(output_details, dict):
        reasoning = int(output_details.get("reasoning_tokens", reasoning) or 0)
    if total_tokens == 0:
        total_tokens = input_tokens + output_tokens
    return {
        "input_tokens": input_tokens,
        "cached_input_tokens": cached,
        "non_cached_input_tokens": max(0, input_tokens - cached),
        "output_tokens": output_tokens,
        "reasoning_output_tokens": reasoning,
        "total_tokens": total_tokens,
    }
