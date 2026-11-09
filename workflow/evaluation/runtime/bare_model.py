from __future__ import annotations

import http.client
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


TRANSIENT_RETRY_DELAYS_SECONDS = (5, 15, 30, 60, 120, 240, 300, 300)
TRANSIENT_STREAM_ERROR_CODES = {
    "internal_server_error",
    "rate_limit_exceeded",
    "server_error",
    "temporarily_unavailable",
    "upstream_error",
    "upstream_stream_error",
    "stream_read_error",
}


class TransientProviderError(RuntimeError):
    pass


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
    enable_thinking: bool | None = None
    chat_token_limit_parameter: str = "max_tokens"

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
        if wire_api not in {"responses", "chat_completions", "anthropic_messages"}:
            raise ValueError("wire API must be responses, chat_completions, or anthropic_messages")
        if require_credentials and not (base_url and api_key and model):
            raise ValueError("base URL, API key, and model are required")
        limit_parameter = values.get("ML_THEORY_LLM_CHAT_TOKEN_LIMIT_PARAMETER", "max_tokens")
        if limit_parameter not in {"max_tokens", "max_completion_tokens"}:
            raise ValueError("unsupported Chat Completions token limit parameter")
        return cls(
            base_url=base_url,
            api_key=api_key,
            model=model,
            wire_api=wire_api,
            reasoning_effort=(
                values.get("ML_THEORY_LLM_REASONING_EFFORT", "").strip() or None
            ),
            max_output_tokens=int(
                values.get("ML_THEORY_LLM_MAX_OUTPUT_TOKENS", "48000")
            ),
            timeout_seconds=int(
                values.get("ML_THEORY_LLM_TIMEOUT_SECONDS", "1800")
            ),
            stream=values.get("ML_THEORY_LLM_STREAM", "false").strip().lower()
            in {"1", "true", "yes", "on"},
            enable_thinking=(
                values["ML_THEORY_LLM_ENABLE_THINKING"].strip().lower()
                in {"1", "true", "yes", "on"}
                if "ML_THEORY_LLM_ENABLE_THINKING" in values else None
            ),
            chat_token_limit_parameter=limit_parameter,
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
    if config.wire_api == "anthropic_messages":
        return _messages_payload(config, system_prompt, [{"role": "user", "content": user_input}])
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
        config.chat_token_limit_parameter: config.max_output_tokens,
    }
    if config.reasoning_effort:
        payload["reasoning_effort"] = config.reasoning_effort
        payload["thinking"] = {"type": "enabled"}
    if config.enable_thinking is not None:
        payload["enable_thinking"] = config.enable_thinking
    if config.stream:
        payload["stream"] = True
        payload["stream_options"] = {"include_usage": True}
    return payload


def build_followup_payload(
    config: ProviderConfig,
    system_prompt: str,
    first_user_input: str,
    first_assistant_output: str,
    followup_input: str,
) -> dict[str, Any]:
    history = [
        {"role": "user", "content": first_user_input},
        {"role": "assistant", "content": first_assistant_output},
        {"role": "user", "content": followup_input},
    ]
    if config.wire_api == "anthropic_messages":
        return _messages_payload(config, system_prompt, history)
    if config.wire_api == "responses":
        payload: dict[str, Any] = {
            "model": config.model,
            "instructions": system_prompt,
            "input": history,
            "max_output_tokens": config.max_output_tokens,
        }
        if config.reasoning_effort:
            payload["reasoning"] = {"effort": config.reasoning_effort}
        if config.stream:
            payload["stream"] = True
        return payload
    payload = {
        "model": config.model,
        "messages": [{"role": "system", "content": system_prompt}, *history],
        config.chat_token_limit_parameter: config.max_output_tokens,
    }
    if config.reasoning_effort:
        payload["reasoning_effort"] = config.reasoning_effort
        payload["thinking"] = {"type": "enabled"}
    if config.enable_thinking is not None:
        payload["enable_thinking"] = config.enable_thinking
    if config.stream:
        payload["stream"] = True
        payload["stream_options"] = {"include_usage": True}
    return payload


def endpoint_for(config: ProviderConfig) -> str:
    base_url = config.base_url.rstrip("/")
    if config.wire_api == "anthropic_messages":
        # Anthropic client guides use an unversioned host; accept legacy /v1 profiles too.
        return base_url + ("/messages" if base_url.endswith("/v1") else "/v1/messages")
    suffix = {"responses": "/responses", "chat_completions": "/chat/completions"}[config.wire_api]
    return base_url + suffix


def _messages_payload(config: ProviderConfig, system_prompt: str, messages: list[dict[str, str]]) -> dict[str, Any]:
    payload = {
        "model": config.model,
        "system": system_prompt,
        "messages": messages,
        "max_tokens": config.max_output_tokens,
        "stream": config.stream,
    }
    if config.reasoning_effort:
        payload["thinking"] = {"type": "adaptive"}
        payload["output_config"] = {"effort": config.reasoning_effort}
    return payload


def _normalize_messages_response(message: dict[str, Any]) -> dict[str, Any]:
    usage = message.get("usage")
    if isinstance(usage, dict):
        # Anthropic reports uncached input separately from cache read/write input.
        cached = int(usage.get("cache_read_input_tokens", 0) or 0)
        written = int(usage.get("cache_creation_input_tokens", 0) or 0)
        output_details = dict(usage.get("output_tokens_details") or {})
        if "thinking_tokens" in output_details and "reasoning_tokens" not in output_details:
            output_details["reasoning_tokens"] = output_details["thinking_tokens"]
        message = {
            **message,
            "provider_usage": usage,
            "usage": {
                **usage,
                "input_tokens": int(usage.get("input_tokens", 0) or 0) + cached + written,
                "input_tokens_details": {"cached_tokens": cached, "cache_write_tokens": written},
                "output_tokens_details": output_details,
            },
        }
    return {**message, "status": message.get("stop_reason")}


def _read_messages_stream(response: Any) -> dict[str, Any]:
    message: dict[str, Any] | None = None
    blocks: dict[int, dict[str, Any]] = {}
    stopped = False
    for raw_line in response:
        line = raw_line.decode("utf-8", errors="replace").strip()
        if not line.startswith("data:"):
            continue
        for event in _decode_sse_data(line[5:].strip()):
            if not isinstance(event, dict):
                continue
            kind = event.get("type")
            if kind == "error":
                detail = event.get("error") or {}
                error_type = detail.get("type") if isinstance(detail, dict) else None
                exception = TransientProviderError if error_type in {"overloaded_error", "api_error", "rate_limit_error"} else RuntimeError
                raise exception("Messages stream failed: " + json.dumps(detail)[:1500])
            if kind == "message_start":
                message = dict(event["message"])
            elif kind == "content_block_start":
                blocks[event["index"]] = dict(event["content_block"])
            elif kind == "content_block_delta":
                block = blocks.setdefault(event["index"], {})
                delta = event.get("delta", {})
                for field in ("text", "thinking", "signature"):
                    if isinstance(delta.get(field), str):
                        block[field] = block.get(field, "") + delta[field]
            elif kind == "message_delta" and message is not None:
                message.update(event.get("delta") or {})
                message["usage"] = {**(message.get("usage") or {}), **(event.get("usage") or {})}
            elif kind == "message_stop":
                stopped = True
    if message is None or not stopped:
        raise TransientProviderError("Messages stream ended without message_stop")
    message["content"] = [blocks[index] for index in sorted(blocks)]
    return _normalize_messages_response(message)


def _decode_sse_data(data: str) -> list[Any]:
    events: list[Any] = []
    decoder = json.JSONDecoder()
    cursor = 0
    while cursor < len(data):
        while cursor < len(data) and data[cursor].isspace():
            cursor += 1
        if data.startswith("data:", cursor):
            cursor += len("data:")
            continue
        if data.startswith("[DONE]", cursor):
            cursor += len("[DONE]")
            continue
        if cursor >= len(data):
            break
        event, cursor = decoder.raw_decode(data, cursor)
        events.append(event)
    return events


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
        for event in _decode_sse_data(data):
            if not isinstance(event, dict):
                continue
            event_type = event.get("type")
            if event_type == "response.output_text.delta":
                delta = event.get("delta")
                if isinstance(delta, str):
                    text_parts.append(delta)
            elif event_type in {"response.completed", "response.incomplete"} and isinstance(
                event.get("response"), dict
            ):
                completed = event["response"]
                if event_type == "response.incomplete":
                    reason = (completed.get("incomplete_details") or {}).get("reason")
                    if reason != "max_output_tokens":
                        raise RuntimeError(f"provider response incomplete: {reason}")
                    completed["status"] = "incomplete"
            elif event_type in {
                "error",
                "response.failed",
            }:
                details = event.get("response")
                if not isinstance(details, dict):
                    details = event
                error = details.get("error")
                code = (
                    error.get("code")
                    if isinstance(error, dict)
                    else details.get("code")
                )
                exception = (
                    TransientProviderError
                    if code in TRANSIENT_STREAM_ERROR_CODES
                    else RuntimeError
                )
                raise exception(
                    "provider stream failed: "
                    + json.dumps(event, ensure_ascii=False)[:4000]
                )
    if completed is None:
        raise TransientProviderError("Responses stream ended without a terminal response")
    if text_parts:
        completed["output_text"] = "".join(text_parts)
    return completed


def _read_chat_completions_stream(response: Any) -> dict[str, Any]:
    text_parts: list[str] = []
    reasoning_parts: list[str] = []
    usage: dict[str, Any] | None = None
    finish_reason: str | None = None
    saw_event = False
    for raw_line in response:
        line = raw_line.decode("utf-8", errors="replace").strip()
        if not line.startswith("data:"):
            continue
        data = line[5:].strip()
        if not data or data == "[DONE]":
            continue
        for event in _decode_sse_data(data):
            if not isinstance(event, dict):
                continue
            saw_event = True
            if isinstance(event.get("usage"), dict):
                usage = event["usage"]
            error = event.get("error")
            if error:
                code = error.get("code") if isinstance(error, dict) else None
                exception = (
                    TransientProviderError
                    if code in TRANSIENT_STREAM_ERROR_CODES
                    else RuntimeError
                )
                raise exception(
                    "provider stream failed: "
                    + json.dumps(error, ensure_ascii=False)[:4000]
                )
            choices = event.get("choices")
            if not isinstance(choices, list):
                continue
            for choice in choices:
                if not isinstance(choice, dict):
                    continue
                delta = choice.get("delta")
                if isinstance(delta, dict):
                    content = delta.get("content")
                    if isinstance(content, str):
                        text_parts.append(content)
                    reasoning = delta.get("reasoning_content")
                    if not isinstance(reasoning, str):
                        reasoning = delta.get("reasoning")
                    if isinstance(reasoning, str):
                        reasoning_parts.append(reasoning)
                if choice.get("finish_reason") is not None:
                    finish_reason = str(choice["finish_reason"])
    if not saw_event:
        raise TransientProviderError("Chat Completions stream ended without data events")
    if finish_reason is None:
        raise TransientProviderError("Chat Completions stream ended without finish_reason")
    return {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "".join(text_parts),
                    "reasoning_content": "".join(reasoning_parts),
                },
                "finish_reason": finish_reason,
            }
        ],
        "usage": usage,
    }


def send_one_request(
    config: ProviderConfig, payload: dict[str, Any],
    *, attempt_callback: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    body = ""
    for attempt in range(len(TRANSIENT_RETRY_DELAYS_SECONDS) + 1):
        started = time.monotonic()
        def record_attempt(**details: Any) -> None:
            if attempt_callback is not None:
                attempt_callback({
                    "attempt": attempt + 1, "model": config.model,
                    "wall_time_seconds": round(time.monotonic() - started, 3),
                    **details,
                })
        request = urllib.request.Request(
            endpoint_for(config),
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {config.api_key}",
                "Content-Type": "application/json",
                **({"anthropic-version": "2023-06-01"} if config.wire_api == "anthropic_messages" else {}),
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(
                request, timeout=config.timeout_seconds
            ) as response:
                if config.stream:
                    if config.wire_api == "responses":
                        value = _read_responses_stream(response)
                    elif config.wire_api == "anthropic_messages":
                        value = _read_messages_stream(response)
                    else:
                        value = _read_chat_completions_stream(response)
                else:
                    value = json.loads(response.read().decode("utf-8"))
                    if not isinstance(value, dict):
                        raise ValueError("provider response must be a JSON object")
                    if config.wire_api == "anthropic_messages":
                        value = _normalize_messages_response(value)
            record_attempt(status="returned", raw_usage=value.get("usage"))
            return value
        except urllib.error.HTTPError as error:
            retry_reason = f"HTTP_{error.code}"
            body = error.read().decode("utf-8", errors="replace")
            body = body.replace(config.api_key, "[REDACTED_API_KEY]")
            retryable = error.code == 429 or error.code >= 500
            record_attempt(status="error", error_type=retry_reason, retryable=retryable, raw_usage=None)
            if not retryable or attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise RuntimeError(
                    f"provider returned HTTP {error.code}: {body[:4000]}"
                ) from error
        except (
            urllib.error.URLError,
            TimeoutError,
            http.client.RemoteDisconnected,
            http.client.IncompleteRead,
        ) as error:
            retry_reason = type(error).__name__
            record_attempt(status="error", error_type=retry_reason, retryable=True, raw_usage=None)
            if attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise RuntimeError(f"provider request failed: {error}") from error
        except TransientProviderError:
            retry_reason = "transient_stream_error"
            record_attempt(status="error", error_type=retry_reason, retryable=True, raw_usage=None)
            if attempt == len(TRANSIENT_RETRY_DELAYS_SECONDS):
                raise
        except Exception as error:
            record_attempt(status="error", error_type=type(error).__name__, retryable=False, raw_usage=None)
            raise
        delay = TRANSIENT_RETRY_DELAYS_SECONDS[attempt]
        print(
            f"transient provider error; model={config.model}; "
            f"reason={retry_reason}; retrying in {delay}s",
            file=sys.stderr,
        )
        time.sleep(delay)
    raise AssertionError("unreachable")


def extract_output_text(response: dict[str, Any], wire_api: str) -> str:
    if wire_api == "anthropic_messages":
        text = "".join(block.get("text", "") for block in response.get("content", []) if block.get("type") == "text")
        if not text.strip():
            raise ValueError("Messages API response has no output text")
        return text
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
        "enable_thinking": config.enable_thinking,
        "chat_token_limit_parameter": config.chat_token_limit_parameter,
    }
