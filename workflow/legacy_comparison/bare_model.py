from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


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
        cls,
        values: dict[str, str],
        *,
        require_credentials: bool = True,
        base_dir: Path | None = None,
    ) -> "ProviderConfig":
        base_url = values.get("ML_THEORY_LLM_BASE_URL", "").strip().rstrip("/")
        api_key = values.get("ML_THEORY_LLM_API_KEY", "").strip()
        api_key_file = values.get("ML_THEORY_LLM_API_KEY_FILE", "").strip()
        if api_key and api_key_file:
            raise ValueError(
                "set only one of ML_THEORY_LLM_API_KEY and ML_THEORY_LLM_API_KEY_FILE"
            )
        if api_key_file:
            key_path = Path(api_key_file).expanduser()
            if not key_path.is_absolute() and base_dir is not None:
                key_path = base_dir / key_path
            if key_path.is_symlink() or not key_path.is_file():
                raise FileNotFoundError(f"API key file not found: {key_path}")
            if key_path.stat().st_mode & 0o077:
                raise PermissionError(f"API key file must have mode 600: {key_path}")
            api_key = key_path.read_text(encoding="utf-8").strip()
        if api_key and ("\n" in api_key or "\r" in api_key):
            raise ValueError("API key must contain exactly one non-empty line")
        model = values.get("ML_THEORY_LLM_MODEL", "").strip()
        wire_api = values.get("ML_THEORY_LLM_WIRE_API", "responses").strip()
        if wire_api not in {"responses", "chat_completions"}:
            raise ValueError("wire API must be responses or chat_completions")
        if require_credentials and not (base_url and api_key and model):
            raise ValueError("base URL, API key, and model are required")
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
        "max_tokens": config.max_output_tokens,
    }
    if config.reasoning_effort:
        payload["reasoning_effort"] = config.reasoning_effort
        payload["thinking"] = {"type": "enabled"}
    return payload


def endpoint_for(config: ProviderConfig) -> str:
    suffix = "/responses" if config.wire_api == "responses" else "/chat/completions"
    return config.base_url + suffix


def _read_responses_stream(response: Any) -> dict[str, Any]:
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
        elif event_type == "response.completed" and isinstance(
            event.get("response"), dict
        ):
            completed = event["response"]
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
                    return _read_responses_stream(response)
                body = response.read().decode("utf-8")
            break
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            retryable = error.code == 429 or error.code >= 500
            if not retryable or attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise RuntimeError(
                    f"provider returned HTTP {error.code}: {body[:4000]}"
                ) from error
        except (urllib.error.URLError, TimeoutError) as error:
            if attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise RuntimeError(f"provider request failed: {error}") from error
        delay = TRANSIENT_RETRY_DELAYS_SECONDS[attempt]
        print(f"transient provider error; retrying in {delay}s", file=sys.stderr)
        time.sleep(delay)
    value = json.loads(body)
    if not isinstance(value, dict):
        raise ValueError("provider response must be a JSON object")
    return value


def extract_output_text(response: dict[str, Any], wire_api: str) -> str:
    if wire_api == "chat_completions":
        choice = response["choices"][0]
        message = choice["message"]
        content = message.get("content")
        if isinstance(content, str) and content.strip():
            return content
        reasoning = message.get("reasoning_content")
        reasoning_length = len(reasoning) if isinstance(reasoning, str) else 0
        raise ValueError(
            "chat completion response has no message text: "
            f"finish_reason={choice.get('finish_reason')!r}, "
            f"reasoning_chars={reasoning_length}, "
            f"usage={json.dumps(response.get('usage'), ensure_ascii=False)}"
        )
    direct = response.get("output_text")
    if isinstance(direct, str) and direct.strip():
        return direct
    texts: list[str] = []
    for item in response.get("output", []):
        if not isinstance(item, dict) or item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if isinstance(content, dict) and content.get("type") in {
                "output_text",
                "text",
            }:
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
