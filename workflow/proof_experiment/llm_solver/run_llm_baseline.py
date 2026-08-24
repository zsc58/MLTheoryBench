#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from runtime_support.experiment.run_utils import (  # noqa: E402
    file_record,
    infer_task_identity,
    merged_environment,
    normalize_obsidian_markdown,
    normalize_usage,
    require_initialized_run,
    sha256_text,
    split_self_assessment,
    update_run_task_stage,
    validate_identifier,
)


DEFAULT_SYSTEM_PROMPT = Path(__file__).parent / "prompts/proof_system_prompt.md"
DEFAULT_ANSWER_TEMPLATE = Path(__file__).parent / "prompts/proof_answer_template.md"
DEFAULT_ENV_FILE = WORKSPACE_ROOT / ".runtime/llm.env"
DEFAULT_RUNS_ROOT = WORKSPACE_ROOT / ".runtime/runs"
TRANSIENT_RETRY_DELAYS_SECONDS = (5, 15, 30, 60, 120, 240, 300, 300)


@dataclass(frozen=True)
class ProviderConfig:
    base_url: str
    api_key: str
    model: str
    wire_api: str
    reasoning_effort: str | None
    max_output_tokens: int
    timeout_seconds: int
    stream: bool = False

    @classmethod
    def from_environment(
        cls, values: dict[str, str], *, require_credentials: bool
    ) -> "ProviderConfig":
        base_url = values.get("ML_THEORY_LLM_BASE_URL", "").strip().rstrip("/")
        api_key = values.get("ML_THEORY_LLM_API_KEY", "").strip()
        api_key_file = values.get("ML_THEORY_LLM_API_KEY_FILE", "").strip()
        if api_key and api_key_file:
            raise ValueError(
                "set only one of ML_THEORY_LLM_API_KEY and "
                "ML_THEORY_LLM_API_KEY_FILE"
            )
        if api_key_file:
            key_path = Path(api_key_file).expanduser()
            if not key_path.is_absolute():
                key_path = WORKSPACE_ROOT / key_path
            if key_path.is_symlink():
                raise ValueError(f"API key file must not be a symlink: {key_path}")
            if not key_path.is_file():
                raise FileNotFoundError(f"API key file not found: {key_path}")
            if key_path.stat().st_mode & 0o077:
                raise PermissionError(f"API key file must have mode 600: {key_path}")
            api_key = key_path.read_text(encoding="utf-8").strip()
        if api_key and ("\n" in api_key or "\r" in api_key):
            raise ValueError("API key must contain exactly one non-empty line")
        model = values.get("ML_THEORY_LLM_MODEL", "").strip()
        wire_api = values.get("ML_THEORY_LLM_WIRE_API", "responses").strip()
        if wire_api not in {"responses", "chat_completions"}:
            raise ValueError(
                "ML_THEORY_LLM_WIRE_API must be responses or chat_completions"
            )
        if require_credentials and not (base_url and api_key and model):
            raise ValueError(
                "ML_THEORY_LLM_BASE_URL, ML_THEORY_LLM_API_KEY, and "
                "ML_THEORY_LLM_MODEL are required"
            )
        return cls(
            base_url=base_url,
            api_key=api_key,
            model=model,
            wire_api=wire_api,
            reasoning_effort=(
                values.get("ML_THEORY_LLM_REASONING_EFFORT", "").strip() or None
            ),
            max_output_tokens=int(
                values.get("ML_THEORY_LLM_MAX_OUTPUT_TOKENS", "30000")
            ),
            timeout_seconds=int(
                values.get("ML_THEORY_LLM_TIMEOUT_SECONDS", "1800")
            ),
            stream=values.get("ML_THEORY_LLM_STREAM", "false").strip().lower()
            in {"1", "true", "yes", "on"},
        )


def build_user_input(task: str, answer_template: str) -> str:
    return (
        "# Proof Task\n\n"
        f"{task.rstrip()}\n\n"
        "# Required Answer Template\n\n"
        f"{answer_template.rstrip()}\n"
    )


def build_payload(
    config: ProviderConfig, system_prompt: str, user_input: str
) -> dict[str, Any]:
    if config.wire_api == "responses":
        payload: dict[str, Any] = {
            "model": config.model,
            "instructions": system_prompt,
            "input": user_input,
            "max_output_tokens": config.max_output_tokens,
        }
        if config.reasoning_effort:
            payload["reasoning"] = {"effort": config.reasoning_effort}
        if config.stream:
            payload["stream"] = True
        return payload

    payload = {
        "model": config.model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
        "max_completion_tokens": config.max_output_tokens,
    }
    if config.reasoning_effort:
        payload["reasoning_effort"] = config.reasoning_effort
    return payload


def endpoint_for(config: ProviderConfig) -> str:
    suffix = (
        "/responses"
        if config.wire_api == "responses"
        else "/chat/completions"
    )
    return config.base_url + suffix


def send_one_request(
    config: ProviderConfig, payload: dict[str, Any]
) -> dict[str, Any]:
    body = ""
    for attempt in range(len(TRANSIENT_RETRY_DELAYS_SECONDS) + 1):
        request = urllib.request.Request(
            endpoint_for(config),
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {config.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(
                request, timeout=config.timeout_seconds
            ) as response:
                if config.stream:
                    return read_responses_stream(response)
                body = response.read().decode("utf-8")
            break
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            retryable = error.code == 429 or error.code >= 500
            if not retryable or attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise RuntimeError(
                    f"provider returned HTTP {error.code}: {body[:4000]}"
                ) from error
            delay = TRANSIENT_RETRY_DELAYS_SECONDS[attempt]
            print(
                f"transient provider HTTP {error.code}; retrying in {delay}s "
                f"({attempt + 1}/{len(TRANSIENT_RETRY_DELAYS_SECONDS)})",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)
        except urllib.error.URLError as error:
            if attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise RuntimeError(
                    f"provider request failed: {error.reason}"
                ) from error
            delay = TRANSIENT_RETRY_DELAYS_SECONDS[attempt]
            print(
                f"transient provider connection error; retrying in {delay}s "
                f"({attempt + 1}/{len(TRANSIENT_RETRY_DELAYS_SECONDS)})",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)
        except TimeoutError as error:
            if attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise RuntimeError("provider request timed out") from error
            delay = TRANSIENT_RETRY_DELAYS_SECONDS[attempt]
            print(
                f"transient provider timeout; retrying in {delay}s "
                f"({attempt + 1}/{len(TRANSIENT_RETRY_DELAYS_SECONDS)})",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)
    value = json.loads(body)
    if not isinstance(value, dict):
        raise ValueError("provider response must be a JSON object")
    return value


def read_responses_stream(response: Any) -> dict[str, Any]:
    """Collect one Responses SSE stream into the usual response object."""
    text_parts: list[str] = []
    completed: dict[str, Any] | None = None
    for raw_line in response:
        line = raw_line.decode("utf-8", errors="replace").strip()
        if not line.startswith("data:"):
            continue
        data = line[5:].strip()
        if not data or data == "[DONE]":
            continue
        event = json.loads(data)
        if not isinstance(event, dict):
            continue
        event_type = event.get("type")
        if event_type == "response.output_text.delta":
            delta = event.get("delta")
            if isinstance(delta, str):
                text_parts.append(delta)
        elif event_type == "response.completed":
            candidate = event.get("response")
            if isinstance(candidate, dict):
                completed = candidate
        elif event_type in {"error", "response.failed", "response.incomplete"}:
            raise RuntimeError(
                "provider stream failed: "
                + json.dumps(event, ensure_ascii=False)[:4000]
            )
    if completed is None:
        raise ValueError("Responses stream ended without response.completed")
    if text_parts:
        completed["output_text"] = "".join(text_parts)
    return completed


def extract_output_text(response: dict[str, Any], wire_api: str) -> str:
    if wire_api == "chat_completions":
        try:
            content = response["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as error:
            raise ValueError("chat completion response has no message content") from error
        if isinstance(content, str) and content.strip():
            return content
        if isinstance(content, list):
            texts = [
                str(item.get("text", ""))
                for item in content
                if isinstance(item, dict) and item.get("type") == "text"
            ]
            if "".join(texts).strip():
                return "".join(texts)
        raise ValueError("chat completion message content is empty")

    direct = response.get("output_text")
    if isinstance(direct, str) and direct.strip():
        return direct
    texts: list[str] = []
    for item in response.get("output", []):
        if not isinstance(item, dict) or item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if not isinstance(content, dict):
                continue
            if content.get("type") in {"output_text", "text"}:
                text = content.get("text")
                if isinstance(text, str):
                    texts.append(text)
    if not "".join(texts).strip():
        raise ValueError("Responses API response has no output text")
    return "".join(texts)


def public_config(config: ProviderConfig) -> dict[str, Any]:
    return {
        "base_url": config.base_url,
        "model": config.model,
        "wire_api": config.wire_api,
        "reasoning_effort": config.reasoning_effort,
        "max_output_tokens": config.max_output_tokens,
        "timeout_seconds": config.timeout_seconds,
        "stream": config.stream,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one closed-book, single-request LLM proof baseline."
    )
    parser.add_argument("--task", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--paper-id")
    parser.add_argument("--theorem-id")
    parser.add_argument("--system-prompt", type=Path, default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--answer-template", type=Path, default=DEFAULT_ANSWER_TEMPLATE)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS_ROOT)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Record the exact request exposure audit without calling an API.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_id = validate_identifier(args.run_id, "run ID")
    task_path = args.task.resolve()
    if args.paper_id is not None and args.theorem_id is not None:
        paper_id = validate_identifier(args.paper_id, "paper ID")
        theorem_id = validate_identifier(args.theorem_id, "task ID")
    else:
        inferred_paper, inferred_theorem = infer_task_identity(task_path)
        paper_id = validate_identifier(args.paper_id or inferred_paper, "paper ID")
        theorem_id = validate_identifier(
            args.theorem_id or inferred_theorem, "task ID"
        )

    task = task_path.read_text(encoding="utf-8")
    system_prompt = args.system_prompt.resolve().read_text(encoding="utf-8")
    answer_template = args.answer_template.resolve().read_text(encoding="utf-8")
    config = ProviderConfig.from_environment(
        merged_environment(args.env_file.resolve()),
        require_credentials=not args.dry_run,
    )
    user_input = build_user_input(task, answer_template)
    payload = build_payload(config, system_prompt, user_input)

    run_dir = require_initialized_run(args.runs_root, run_id)
    output_dir = run_dir / paper_id / theorem_id
    output_dir.mkdir(parents=True, exist_ok=True)
    existing_answers = [
        path
        for path in (
            output_dir / "answer.md",
            output_dir / "answer_for_evaluator.md",
        )
        if path.exists()
    ]
    if existing_answers:
        raise FileExistsError(
            "solver output already exists: "
            + ", ".join(str(path) for path in existing_answers)
        )

    audit: dict[str, Any] = {
        "protocol": "closed_book_single_request",
        "status": "prepared" if args.dry_run else "running",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "exposures": [
            file_record(
                task_path,
                label="public_task",
                exposed_as="request.input.public_task",
            ),
            file_record(
                args.system_prompt.resolve(),
                label="system_prompt",
                exposed_as="request.instructions",
            ),
            file_record(
                args.answer_template.resolve(),
                label="answer_template",
                exposed_as="request.input.answer_template",
            ),
        ],
        "private_files_exposed": [],
    }
    update_run_task_stage(
        run_dir, paper_id, theorem_id, "solver", audit
    )
    if args.dry_run:
        print(output_dir)
        return 0

    try:
        response = send_one_request(config, payload)
        raw_answer = extract_output_text(response, config.wire_api)
        answer = normalize_obsidian_markdown(raw_answer)
        proof, _ = split_self_assessment(answer)
        (output_dir / "answer.md").write_text(answer, encoding="utf-8")
        (output_dir / "answer_for_evaluator.md").write_text(
            proof, encoding="utf-8"
        )
        audit["status"] = "completed"
        audit["completed_at"] = datetime.now(timezone.utc).isoformat()
        audit["usage"] = normalize_usage(response.get("usage"))
        audit["answer_sha256"] = sha256_text(answer)
        audit["answer_for_evaluator_sha256"] = sha256_text(proof)
        update_run_task_stage(
            run_dir, paper_id, theorem_id, "solver", audit
        )
    except Exception as error:
        audit["status"] = "failed"
        audit["completed_at"] = datetime.now(timezone.utc).isoformat()
        audit["error"] = str(error)
        update_run_task_stage(
            run_dir, paper_id, theorem_id, "solver", audit
        )
        raise

    print(output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
