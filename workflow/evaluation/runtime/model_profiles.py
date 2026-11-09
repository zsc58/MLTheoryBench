from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUITE_PATH = ROOT / "config/model_suite.json"
DEFAULT_PROFILES_DIR = ROOT.parent.parent / ".venv/paperproof-config/model-suite"


def load_suite() -> dict:
    return json.loads(SUITE_PATH.read_text(encoding="utf-8"))


def solver_profiles(mode: str, profiles_dir: Path) -> list[tuple[str, Path]]:
    return [(label, profiles_dir / f"{label}.env") for label in load_suite()["modes"][mode]]


def protected_write(path: Path, content: str) -> None:
    if path.is_symlink():
        raise ValueError(f"refusing to overwrite a symlink: {path}")
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    path.parent.chmod(0o700)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        os.fchmod(handle.fileno(), 0o600)
        handle.write(content)


def install_profiles(
    profiles_dir: Path,
    get_key_file: Path,
    ppio_key_file: Path | None = None,
    novita_key_file: Path | None = None,
) -> None:
    suite = load_suite()
    keys = {}
    for provider, path in (("get-api", get_key_file), ("ppio", ppio_key_file), ("novita", novita_key_file)):
        if provider not in suite["providers"]:
            continue
        if path is None:
            raise ValueError(f"key file is required for {provider}")
        if path.is_symlink() or not path.is_file() or path.stat().st_mode & 0o077:
            raise PermissionError(f"key must be a regular mode-600 file: {path}")
        key = path.read_text(encoding="utf-8").strip()
        if not key or "\n" in key or "\r" in key:
            raise ValueError(f"invalid key file: {path}")
        keys[provider] = key
    profiles_dir = profiles_dir.resolve()
    for provider, key in keys.items():
        protected_write(profiles_dir / provider / "openai_api_key", key + "\n")
    agent = suite["agent"]
    provider = agent["provider"]
    config = (
        f'model = {json.dumps(agent["model"])}\n'
        f'model_reasoning_effort = {json.dumps(agent["reasoning_effort"])}\n'
        f'model_provider = {json.dumps(provider)}\n\n'
        f'[model_providers.{provider}]\n'
        'name = "Get API"\n'
        'env_key = "OPENAI_API_KEY"\n'
        f'base_url = {json.dumps(suite["providers"][provider]["base_url"])}\n'
        'wire_api = "responses"\n'
        'requires_openai_auth = true\n'
    )
    protected_write(profiles_dir / provider / "config.toml", config)
    for label, solver in suite["solvers"].items():
        base_url = suite["providers"][solver["provider"]]["base_url"]
        if solver["wire_api"] == "anthropic_messages":
            base_url = base_url.rstrip("/").removesuffix("/v1")
        values = {
            "BASE_URL": base_url,
            "API_KEY_FILE": str(profiles_dir / solver["provider"] / "openai_api_key"),
            "MODEL": solver["model"],
            "WIRE_API": solver["wire_api"],
            "REASONING_EFFORT": solver["reasoning_effort"],
            "MAX_OUTPUT_TOKENS": suite["defaults"]["max_output_tokens"],
            "TIMEOUT_SECONDS": suite["defaults"]["timeout_seconds"],
            "STREAM": str(suite["defaults"]["stream"]).lower(),
        }
        if "enable_thinking" in solver:
            values["ENABLE_THINKING"] = str(solver["enable_thinking"]).lower()
        if "chat_token_limit_parameter" in solver:
            values["CHAT_TOKEN_LIMIT_PARAMETER"] = solver["chat_token_limit_parameter"]
        protected_write(
            profiles_dir / f"{label}.env",
            "".join(f"ML_THEORY_LLM_{name}={value}\n" for name, value in values.items()),
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Install protected profiles; never print keys.")
    parser.add_argument("--profiles-dir", type=Path, default=DEFAULT_PROFILES_DIR)
    parser.add_argument("--get-key-file", type=Path, required=True)
    parser.add_argument("--ppio-key-file", type=Path)
    parser.add_argument("--novita-key-file", type=Path)
    args = parser.parse_args()
    install_profiles(args.profiles_dir, args.get_key_file, args.ppio_key_file, args.novita_key_file)
    print(f"Installed {len(load_suite()['solvers'])} solver profiles and GPT-6 high agent profile: {args.profiles_dir}")
