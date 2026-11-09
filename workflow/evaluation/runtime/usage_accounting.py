from __future__ import annotations

from typing import Any

from support import normalize_usage


def session_delta(
    current: dict[str, int] | None, previous: dict[str, int] | None,
) -> tuple[dict[str, int] | None, list[str]]:
    if current is None:
        return None, ["session usage was not returned"]
    previous = previous or {}
    keys = ("input_tokens", "cached_input_tokens", "output_tokens")
    if any(current.get(k, 0) < previous.get(k, 0) for k in keys):
        return None, ["session counter decreased; incremental usage is unknown"]
    delta = {k: current.get(k, 0) - previous.get(k, 0) for k in keys}
    reasoning = current.get("reasoning_output_tokens", 0) - previous.get("reasoning_output_tokens", 0)
    issues = ["reasoning counter decreased"] if reasoning < 0 else []
    delta["reasoning_output_tokens"] = max(0, reasoning)
    return normalize_usage(delta), issues


def aggregate_agent_records(
    records: list[tuple[str, str, dict[str, Any]]],
) -> tuple[dict[str, dict[str, int]], list[str]]:
    """CLI raw usage is session cumulative; bare API usage is handled elsewhere."""
    sessions: dict[tuple[str, str], dict[str, int]] = {}
    stages: dict[str, dict[str, int]] = {}
    issues: list[str] = []
    for identity, stage, record in sorted(records, key=lambda row: row[2].get("started_at_unix", 0)):
        raw = record.get("raw_usage")
        if isinstance(raw, dict):
            current = normalize_usage(raw)
            key = (stage, record.get("session_id") or identity)
            _, warnings = session_delta(current, sessions.get(key))
            issues.extend(f"{identity}: {warning}" for warning in warnings)
            sessions[key] = current or {}
        else:
            for key, value in (record.get("usage") or {}).items():
                bucket = stages.setdefault(stage, {})
                bucket[key] = bucket.get(key, 0) + int(value or 0)
    for (stage, _), usage in sessions.items():
        bucket = stages.setdefault(stage, {})
        for key, value in usage.items():
            bucket[key] = bucket.get(key, 0) + value
    return stages, issues
