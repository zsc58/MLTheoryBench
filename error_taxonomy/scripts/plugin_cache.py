"""Share only Codex's plugin bootstrap scratch area across private API sessions.

The installed CLI uses .tmp/plugins, plugins.sha and plugins.sync.lock together.
Link their parent, not individual files: refreshes may atomically replace files,
and concurrent processes must use the same CLI synchronization lock. Sessions,
SQLite state, config and credentials remain in each attempt's CODEX_HOME.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import subprocess


def private_directory(path: Path) -> Path:
    path = Path(path).absolute()
    # Reject aliases before creating anything, including an aliased parent.
    if any(parent.is_symlink() for parent in (path, *path.parents)):
        raise ValueError("Shared plugin cache must not have symlink components")
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    info = path.stat()
    if not path.is_dir() or info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise ValueError("Shared plugin cache must be an owned directory with mode 700")
    return path


def prepare_plugin_cache(root: Path, codex_bin: str) -> dict:
    """Select a batch-local, CLI-version-specific cache without a model call."""
    version = subprocess.run([codex_bin, "--version"], check=True, text=True,
                             capture_output=True, timeout=30).stdout.strip()
    if not version or len(version) > 200 or "\n" in version:
        raise ValueError("Unexpected Codex version response")
    fingerprint = hashlib.sha256(version.encode()).hexdigest()[:16]
    root = private_directory(root)
    scratch = private_directory(root / fingerprint / "plugin_tmp")
    return {"mode": "shared_plugin_tmp_only", "cli_version": version,
            "path": str(scratch), "session_state": "per_attempt_codex_home"}


def attach_plugin_cache(home: Path, scratch: Path) -> None:
    """Attach only to a fresh home; never move, delete or overwrite old caches."""
    scratch = private_directory(scratch)
    home = Path(home).resolve(strict=True)
    if scratch == home or home in scratch.parents or scratch in home.parents:
        raise ValueError("Plugin scratch must be separate from the session home")
    destination = home / ".tmp"
    if destination.exists() or destination.is_symlink():
        raise ValueError("Refusing to replace an existing session scratch area")
    destination.symlink_to(scratch, target_is_directory=True)
