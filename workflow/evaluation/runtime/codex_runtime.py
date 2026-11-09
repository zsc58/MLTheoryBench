from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from typing import Any

from support import file_record


def codex_command(
    *,
    codex_bin: str,
    model: str,
    reasoning_effort: str,
    workspace: Path,
    schema_path: Path,
    output_path: Path,
    resume_session_id: str | None = None,
    ephemeral: bool = True,
) -> list[str]:
    common = [
        "--skip-git-repo-check",
        "--ignore-rules",
        "--json",
        "--output-schema",
        str(schema_path),
        "--output-last-message",
        str(output_path),
        "--model",
        model,
        "--config",
        f'model_reasoning_effort="{reasoning_effort}"',
    ]
    prefix = [
        codex_bin,
        "--config",
        "features.hooks=false",
        "exec",
    ]
    if resume_session_id is not None:
        return [*prefix, "resume", *common, resume_session_id, "-"]
    ephemeral_args = ["--ephemeral"] if ephemeral else []
    return [
        *prefix,
        *ephemeral_args,
        *common,
        "--sandbox",
        "read-only",
        "--cd",
        str(workspace),
        "-",
    ]


def load_api_profile(profile_dir: Path) -> tuple[str, str, dict[str, Any]]:
    if profile_dir.is_symlink():
        raise ValueError(f"API profile directory must not be a symlink: {profile_dir}")
    profile = profile_dir.resolve()
    if not profile.is_dir() or profile.stat().st_mode & 0o077:
        raise PermissionError(f"API profile directory must exist with mode 700: {profile}")
    config_path = profile / "config.toml"
    key_path = profile / "openai_api_key"
    for path, label in (
        (config_path, "Codex provider config"),
        (key_path, "Codex API key"),
    ):
        if path.is_symlink() or not path.is_file():
            raise FileNotFoundError(f"{label} not found: {path}")
        if path.stat().st_mode & 0o077:
            raise PermissionError(f"{label} must have mode 600: {path}")
    config_text = config_path.read_text(encoding="utf-8").strip()
    api_key = key_path.read_text(encoding="utf-8").strip()
    if not api_key or "\n" in api_key or "\r" in api_key:
        raise ValueError("Codex API key file must contain one non-empty line")
    if api_key in config_text:
        raise ValueError("Codex provider config must not contain the API key")
    return config_text, api_key, {
        "config_sha256": file_record(
            config_path,
            label="codex_provider_config",
            exposed_as="codex_home/config.toml",
        )["sha256"],
        "api_key_source": "protected_file",
    }


def prepare_isolated_codex_home(
    root: Path, codex_bin: str, provider_config: str
) -> Path:
    codex_home = root / "codex_home"
    codex_home.mkdir(mode=0o700)
    binary = shutil.which(codex_bin)
    binary_parent = Path(binary).resolve().parent if binary else Path("/usr/bin")
    python_runtime = Path(sys.base_prefix).resolve()
    config = (
        'default_permissions = "evaluator-isolated"\n'
        'web_search = "disabled"\n\n'
        f"{provider_config}\n\n"
        "[permissions.evaluator-isolated.filesystem]\n"
        '":minimal" = "read"\n'
        f'{json.dumps(str(binary_parent))} = "read"\n'
        f'{json.dumps(str(python_runtime))} = "read"\n'
        '":workspace_roots" = { "." = "read" }\n\n'
        "[permissions.evaluator-isolated.network]\n"
        "enabled = false\n\n"
        "[shell_environment_policy]\n"
        'inherit = "core"\n'
    )
    (codex_home / "config.toml").write_text(config, encoding="utf-8")
    return codex_home


def extract_usage(events_text: str) -> dict[str, Any] | None:
    for line in reversed(events_text.splitlines()):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        usage = event.get("usage") if isinstance(event, dict) else None
        if isinstance(usage, dict):
            return usage
    return None


def extract_session_id(events_text: str) -> str | None:
    for line in events_text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        for key in ("thread_id", "session_id"):
            value = event.get(key)
            if isinstance(value, str) and value:
                return value
        thread = event.get("thread")
        if isinstance(thread, dict):
            value = thread.get("id")
            if isinstance(value, str) and value:
                return value
    return None


def extract_turn_id(events_text: str) -> str | None:
    for line in reversed(events_text.splitlines()):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        event_id = event.get("id")
        if isinstance(event_id, str) and "turn" in str(event.get("type", "")):
            return event_id
    return None
