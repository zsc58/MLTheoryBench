"""Protected provider setup adapted from the existing PaperProof VM helper.

Only run mode loads a key into memory. Never log, hash, copy or expose its value.
"""
import hashlib
import json
import os
import re
import shutil
import sys
import tomllib
from pathlib import Path

from plugin_cache import attach_plugin_cache


def load_profile(profile):
    if profile.is_symlink() or not profile.is_dir() or profile.stat().st_mode & 0o077:
        raise ValueError("API profile must be a real directory with mode 700")
    config_path, key_path = profile / "config.toml", profile / "openai_api_key"
    for path in (config_path, key_path):
        if path.is_symlink() or not path.is_file() or path.stat().st_mode & 0o077:
            raise ValueError("Provider files must be regular protected files with mode 600")
    config = config_path.read_text(encoding="utf-8").strip()
    key = key_path.read_text(encoding="utf-8").strip()
    if not key or "\n" in key or "\r" in key or key in config:
        raise ValueError("Invalid provider profile; credentials must be separate from config")
    parsed = tomllib.loads(config)
    provider = parsed["model_provider"]
    env_key = parsed["model_providers"][provider].get("env_key", "OPENAI_API_KEY")
    if not re.fullmatch(r"[A-Z][A-Z0-9_]*", env_key):
        raise ValueError("Invalid provider authentication variable")
    return config, key, env_key, {"provider": provider, "config_sha256": hashlib.sha256(config.encode()).hexdigest()}


def stage_environment(directory, codex_bin, profile, plugin_cache=None):
    config, key, env_key, _ = profile
    home = directory / "codex_home"
    home.mkdir(mode=0o700)
    if plugin_cache is not None:
        attach_plugin_cache(home, plugin_cache)
    binary = shutil.which(codex_bin)
    binary_parent = Path(binary).resolve().parent if binary else Path("/usr/bin")
    content = (
        'default_permissions = "evaluator-isolated"\nweb_search = "disabled"\n\n'
        + config + '\n\n[permissions.evaluator-isolated.filesystem]\n":minimal" = "read"\n'
        + f'{json.dumps(str(binary_parent))} = "read"\n'
        + f'{json.dumps(str(Path(sys.base_prefix).resolve()))} = "read"\n'
        + '":workspace_roots" = { "." = "read" }\n\n'
        + '[permissions.evaluator-isolated.network]\nenabled = false\n\n'
        + '[shell_environment_policy]\ninherit = "core"\n'
    )
    path = home / "config.toml"
    path.write_text(content, encoding="utf-8")
    path.chmod(0o600)
    return {**os.environ, "CODEX_HOME": str(home), env_key: key}
