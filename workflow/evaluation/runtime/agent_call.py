from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from codex_runtime import (
    codex_command,
    extract_session_id,
    extract_turn_id,
    extract_usage,
    load_api_profile,
    prepare_isolated_codex_home,
)
from support import normalize_usage, sha256_text
from usage_accounting import session_delta


TRANSIENT_CODEX_RETRY_DELAYS_SECONDS = (5, 15, 30, 60, 120)
TRANSIENT_CODEX_MARKERS = (
    "rate_limit",
    "too many requests",
    "http 429",
    "status code 429",
    "server_error",
    "temporarily_unavailable",
    "upstream request failed",
    "upstream_error",
    "remote end closed connection",
)


@dataclass(frozen=True)
class AgentConfig:
    api_profile: Path
    codex_bin: str
    model: str
    reasoning_effort: str
    timeout_seconds: int


class AgentCallError(RuntimeError):
    def __init__(self, message: str, usage: dict[str, int] | None = None) -> None:
        super().__init__(message)
        self.usage = usage


@dataclass
class AgentThread:
    temporary: tempfile.TemporaryDirectory[str]
    root: Path
    workspace: Path
    codex_home: Path
    api_key: str
    provider_record: dict[str, Any]
    session_id: str | None = None
    turn_count: int = 0
    cumulative_usage: dict[str, int] | None = None

    def close(self) -> None:
        self.temporary.cleanup()


def create_agent_thread(config: AgentConfig, label: str) -> AgentThread:
    temporary = tempfile.TemporaryDirectory(prefix=f"paperproof-{label}-")
    root = Path(temporary.name)
    workspace = root / "workspace"
    workspace.mkdir()
    provider_config, api_key, provider_record = load_api_profile(
        config.api_profile.resolve()
    )
    codex_home = prepare_isolated_codex_home(
        root, config.codex_bin, provider_config
    )
    return AgentThread(
        temporary=temporary,
        root=root,
        workspace=workspace,
        codex_home=codex_home,
        api_key=api_key,
        provider_record=provider_record,
    )


def is_transient_codex_failure(stdout: str, stderr: str) -> bool:
    combined = f"{stdout}\n{stderr}".lower()
    return any(marker in combined for marker in TRANSIENT_CODEX_MARKERS)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def run_json_agent(
    *,
    instructions: str,
    inputs: str,
    schema_path: Path,
    config: AgentConfig,
    output_label: str,
    thread: AgentThread | None = None,
) -> tuple[dict[str, Any], dict[str, int] | None, dict[str, Any]]:
    owns_thread = thread is None
    active_thread = thread or create_agent_thread(config, output_label)
    try:
        turn_index = active_thread.turn_count + 1
        schema_copy = (
            active_thread.workspace / f"{output_label}.turn_{turn_index}.schema.json"
        )
        shutil.copy2(schema_path.resolve(), schema_copy)
        output_path = active_thread.root / f"{output_label}.turn_{turn_index}.json"
        resumed = active_thread.session_id is not None
        full_input = (
            f"{instructions.rstrip()}\n\n"
            f"{inputs.rstrip()}\n\n"
            "# Exact Output Contract\n\n"
            "Return exactly one JSON object matching the supplied output schema. "
            "Do not add prose or Markdown fences.\n"
        )
        environment = {
            **os.environ,
            "CODEX_HOME": str(active_thread.codex_home),
            "OPENAI_API_KEY": active_thread.api_key,
            "PYTHONDONTWRITEBYTECODE": "1",
        }
        transient_retry_count = 0
        call_started = time.time()
        for attempt in range(len(TRANSIENT_CODEX_RETRY_DELAYS_SECONDS) + 1):
            output_path.unlink(missing_ok=True)
            command = codex_command(
                codex_bin=config.codex_bin,
                model=config.model,
                reasoning_effort=config.reasoning_effort,
                workspace=active_thread.workspace,
                schema_path=schema_copy,
                output_path=output_path,
                resume_session_id=(
                    active_thread.session_id if not owns_thread else None
                ),
                ephemeral=owns_thread,
            )
            process = subprocess.run(
                command,
                input=full_input,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=config.timeout_seconds,
                check=False,
                env=environment,
            )
            stdout = process.stdout.replace(
                active_thread.api_key, "[REDACTED_API_KEY]"
            )
            stderr = process.stderr.replace(
                active_thread.api_key, "[REDACTED_API_KEY]"
            )
            if not owns_thread and active_thread.session_id is None:
                active_thread.session_id = extract_session_id(stdout)
            if process.returncode == 0 or not is_transient_codex_failure(
                stdout, stderr
            ):
                break
            if attempt == len(TRANSIENT_CODEX_RETRY_DELAYS_SECONDS):
                break
            transient_retry_count += 1
            time.sleep(TRANSIENT_CODEX_RETRY_DELAYS_SECONDS[attempt])
        cumulative_usage = normalize_usage(extract_usage(stdout))
        usage, usage_issues = session_delta(cumulative_usage, active_thread.cumulative_usage)
        if cumulative_usage is not None:
            active_thread.cumulative_usage = cumulative_usage
        if process.returncode != 0:
            raise AgentCallError(
                f"Codex {output_label} exited {process.returncode}: "
                f"stderr={stderr[-2500:]} stdout={stdout[-4000:]}",
                usage,
            )
        if not output_path.is_file():
            raise AgentCallError(
                f"Codex {output_label} produced no output file", usage
            )
        try:
            value = load_json(output_path)
        except Exception as error:
            raise AgentCallError(
                f"invalid {output_label} JSON: {error}", usage
            ) from error
        if not owns_thread and active_thread.session_id is None:
            raise AgentCallError(
                f"Codex {output_label} returned no resumable thread ID", usage
            )
        if not owns_thread:
            active_thread.turn_count += 1
        audit = {
            "started_at_unix": call_started,
            "wall_time_seconds": round(time.time() - call_started, 3),
            "raw_usage": extract_usage(stdout),
            "usage": usage,
            "usage_scope": "codex_session_delta",
            "session_cumulative_usage": cumulative_usage,
            "usage_tracking_issues": usage_issues,
            "event_counts": dict(Counter(
                event.get("type", "unknown")
                for line in stdout.splitlines()
                if line.lstrip().startswith("{")
                for event in _json_events(line)
            )),
            "item_type_counts": dict(Counter(
                event["item"].get("type", "unknown")
                for line in stdout.splitlines()
                for event in _json_events(line)
                if event.get("type") == "item.completed" and isinstance(event.get("item"), dict)
            )),
            "network_tools": "disabled",
            "workspace_policy": "isolated_read_only",
            "model": config.model,
            "reasoning_effort": config.reasoning_effort,
            "provider": active_thread.provider_record,
            "transient_retry_count": transient_retry_count,
            "session_id": active_thread.session_id,
            "turn_id": extract_turn_id(stdout),
            "resumed": resumed,
            "input_sha256": sha256_text(full_input),
            "input_bytes": len(full_input.encode("utf-8")),
            "schema_sha256": sha256_text(
                schema_path.read_text(encoding="utf-8")
            ),
        }
        return value, usage, audit
    finally:
        if owns_thread:
            active_thread.close()


def _json_events(line: str) -> list[dict[str, Any]]:
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        return []
    return [event] if isinstance(event, dict) else []
