"""Bounded same-session recovery of unfinished CLI transport requests.

No retry on a produced answer, validation failure, timeout, quota exhaustion or
unknown error. Each physical invocation has its own output and a safe journal;
successful retries still pass the caller's ordinary scientific validators.
"""
from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
from pathlib import Path
import random
import re
import shutil
import subprocess
import time


TRANSPORT_POLICY = "2026-10-11-same-session-transport-v1"
MAX_RETRIES = 2
RETRY_INPUT = (
    "The preceding request was interrupted by a transport failure before a final answer. "
    "Complete that same unfinished request using its existing instructions, supplied materials "
    "and exact output schema. Do not advance to another result or change the audit criteria. "
    "Return the requested JSON object only."
)


def _events(stdout):
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict):
            yield event


def event_metadata(stdout):
    usage, session = None, None
    for event in _events(stdout):
        if isinstance(event.get("usage"), dict):
            usage = event["usage"]
        for key in ("thread_id", "session_id"):
            if session is None and isinstance(event.get(key), str):
                session = event[key]
        thread = event.get("thread")
        if session is None and isinstance(thread, dict) and isinstance(thread.get("id"), str):
            session = thread["id"]
    return usage, session


def failure_info(stdout, stderr):
    """Classify error events only, never classify mathematical answer text.

    Store fixed codes and a digest rather than raw provider response bodies or
    headers (which can contain credentials or identifying request metadata).
    """
    errors = []
    for event in _events(stdout):
        if event.get("type") in ("error", "turn.failed"):
            value = event.get("error", event.get("message", ""))
            errors.append(value if isinstance(value, str) else json.dumps(value))
    raw = errors[-1] if errors else stderr
    lower = raw.lower()
    category = "unknown_cli_error"
    patterns = (
        ("quota_exhausted", r"insufficient.quota|exceeded.{0,30}(?:quota|billing)|credit.{0,20}(?:exhaust|insufficient)|余额不足|额度耗尽"),
        ("authentication_error", r"\b(?:401|403)\b|unauthorized|authentication failed"),
        ("context_limit", r"context.{0,25}(?:exceed|limit|length)|maximum.{0,20}tokens|prompt.{0,15}too long"),
        ("bad_request", r"\b400\b|bad request"),
        ("local_resource_error", r"no space left|out of memory|permission denied|too many open files"),
        ("http_429", r"\b429\b|too many requests"),
        ("http_5xx", r"\b(?:500|502|503|504)\b|internal server error|bad gateway|service unavailable|gateway timeout"),
        ("stream_disconnect", r"stream.{0,30}(?:disconnect|interrupt|closed)|error decoding response body|error sending request"),
    )
    for label, pattern in patterns:
        if re.search(pattern, lower):
            category = label
            break
    # Retry-After is usually absent from the CLI event, but honor it if exposed.
    delay = None
    match = re.search(r"retry-after[\"']?\s*[:=]\s*[\"']?([^\r\n\"'}]+)", raw, re.I)
    if match:
        value = match[1].strip()
        try:
            delay = max(0.0, float(value))
        except ValueError:
            try:
                when = parsedate_to_datetime(value)
                delay = max(0.0, (when - datetime.now(timezone.utc)).total_seconds())
            except (ValueError, TypeError, OverflowError):
                pass
    return {"category": category,
            "retryable": category in {"http_429", "http_5xx", "stream_disconnect"},
            "retry_after_seconds": delay,
            "error_sha256": hashlib.sha256(raw.encode()).hexdigest(),
            "source": "stdout_error_event" if errors else "stderr"}


def _has_answer(stdout):
    return any(e.get("type") == "turn.completed" or (
        isinstance(e.get("item"), dict) and e["item"].get("type") == "agent_message"
    ) for e in _events(stdout))


def _resume_command(command, session, output):
    """Transform only the two command layouts produced by this runner."""
    cmd = list(command)
    cmd[cmd.index("--output-last-message") + 1] = str(output)
    i = cmd.index("exec")
    if cmd[i + 1] == "resume":
        if cmd[-1] != "-" or cmd[-2] != session:
            raise ValueError("Unexpected resume command layout")
        return cmd
    if cmd[-1] != "-":
        raise ValueError("Unexpected initial command layout")
    cmd.insert(i + 1, "resume")
    # exec resume takes sandbox configuration, not exec's --sandbox/--cd flags.
    for flag in ("--sandbox", "--cd"):
        if flag in cmd:
            j = cmd.index(flag)
            if flag == "--sandbox" and cmd[j + 1] != "read-only":
                raise ValueError("Only read-only audit commands can be retried")
            del cmd[j:j + 2]
    cmd[-1:] = ["--config", 'sandbox_mode="read-only"', session, "-"]
    return cmd


def _session_exists(environment, session):
    # Never inspect or modify the user's interactive login directory.
    home = environment.get("CODEX_HOME")
    if not home or not re.fullmatch(r"[A-Za-z0-9-]+", session):
        return False
    return any(p.stat().st_size for p in (Path(home) / "sessions").rglob(f"*{session}.jsonl"))


def transport_fields(process):
    return getattr(process, "transport_metadata", {})


def run_with_recovery(*, command, model_input, environment, timeout_seconds, cwd):
    output = Path(command[command.index("--output-last-message") + 1])
    journal = output.with_suffix(".transport.json")
    if journal.exists() or output.exists():
        raise FileExistsError(f"Refusing to overwrite CLI invocation: {output}")
    deadline = time.monotonic() + timeout_seconds
    data = {"policy": TRANSPORT_POLICY, "started_at": datetime.now(timezone.utc).isoformat(),
            "timeout_seconds": timeout_seconds, "max_retries": MAX_RETRIES,
            "logical_input_sha256": hashlib.sha256(model_input.encode()).hexdigest(),
            "retry_input": RETRY_INPUT, "attempts": []}

    def save():
        temporary = journal.with_name(journal.name + ".tmp")
        temporary.write_text(json.dumps(data, indent=2) + "\n")
        temporary.replace(journal)

    current_command, current_input, current_output = command, model_input, output
    expected_session = command[-2] if "resume" in command else None
    for number in range(MAX_RETRIES + 1):
        row = {"attempt": number + 1, "status": "running",
               "started_at": datetime.now(timezone.utc).isoformat(),
               "input_sha256": hashlib.sha256(current_input.encode()).hexdigest(),
               "output_path": str(current_output), "mode": "initial" if "resume" not in current_command else "resume"}
        data["attempts"].append(row)
        save()
        try:
            proc = subprocess.run(current_command, input=current_input, text=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  timeout=max(0.001, deadline - time.monotonic()), check=False,
                                  env=environment, cwd=cwd)
        except subprocess.TimeoutExpired:
            row.update(status="timeout", completed_at=datetime.now(timezone.utc).isoformat())
            data["status"] = "timeout"
            save()
            raise
        usage, session = event_metadata(proc.stdout)
        row.update(returncode=proc.returncode, usage=usage, session_id=session,
                   completed_at=datetime.now(timezone.utc).isoformat())
        if current_output.is_file():
            row["output_sha256"] = hashlib.sha256(current_output.read_bytes()).hexdigest()
        error = failure_info(proc.stdout, proc.stderr) if proc.returncode else None
        row.update(status="failed" if proc.returncode else "completed", error=error)
        if expected_session and session != expected_session:
            # Do not adopt even an otherwise successful answer from a new thread.
            row["session_mismatch"] = True
            proc = subprocess.CompletedProcess(proc.args, 1, proc.stdout, "Persistent session ID mismatch")
            reason = "session_mismatch"
        elif not proc.returncode:
            reason = "completed"
            if number:
                # Failed empty files are evidence too. Never replace nonempty output.
                if output.exists():
                    if output.stat().st_size:
                        raise RuntimeError("Original output changed during recovery")
                    output.rename(output.with_suffix(".transport_empty.json"))
                if current_output.is_file():
                    shutil.copyfile(current_output, output)
                    data["adopted_output"] = str(current_output)
        elif not error["retryable"]:
            reason = "nonretryable_error"
        elif _has_answer(proc.stdout) or (current_output.exists() and current_output.stat().st_size):
            reason = "answer_already_produced"
        elif not session or not _session_exists(environment, session):
            reason = "no_verified_persistent_session"
        elif number == MAX_RETRIES:
            reason = "retry_limit"
        else:
            delay = max(60 * (2 ** number) + random.uniform(0, 30), error["retry_after_seconds"] or 0)
            if deadline - time.monotonic() < delay + 60:
                reason = "insufficient_remaining_turn_budget"
            else:
                next_output = output.with_name(output.stem + f".transport_retry_{number + 1:02d}" + output.suffix)
                if next_output.exists():
                    raise FileExistsError(next_output)
                current_command = _resume_command(command, session, next_output)
                current_input, current_output, expected_session = RETRY_INPUT, next_output, session
                row["retry_delay_seconds"] = delay
                save()
                # Chunk the wait so interrupt/termination remains responsive.
                until = time.monotonic() + delay
                while time.monotonic() < until:
                    time.sleep(max(0, min(30, until - time.monotonic())))
                continue
        data.update(status=reason, completed_at=datetime.now(timezone.utc).isoformat())
        save()
        proc.transport_metadata = {"transport_policy": TRANSPORT_POLICY, "transport_log_path": str(journal),
                                   "transport_invocations": len(data["attempts"]), "transport_status": reason,
                                   "cli_error": error}
        if proc.returncode:
            # The callers previously printed only stderr, often an empty string.
            proc.stderr = json.dumps({"cli_failure": reason, "error": error, "transport_log_path": str(journal)})
        return proc
