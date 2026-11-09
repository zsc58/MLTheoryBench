"""Offline failure injection; no provider, credentials or real waiting."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import cli_transport as transport


SESSION = "01a123d7-8b69-76e3-9de3-e6335b54b375"


def events(*values):
    return "\n".join(json.dumps(x) for x in values)


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.output = self.root / "001_result.json"
        self.command = ["codex", "--config", "features.hooks=false", "exec", "--json",
                        "--output-schema", "schema.json", "--output-last-message", str(self.output),
                        "--model", "gpt-6-astra", "--sandbox", "read-only", "--cd", str(self.root), "-"]
        self.env = {"CODEX_HOME": str(self.root / "isolated")}
        sessions = self.root / "isolated/sessions"
        sessions.mkdir(parents=True)
        (sessions / f"rollout-{SESSION}.jsonl").write_text('{"private":"test fixture"}\n')
        self.clock = 0.0
        self.calls = []

    def failure(self, message="exceeded retry limit, last status: 429 Too Many Requests", **extra):
        return {"rc": 1, "stdout": events({"type": "thread.started", "thread_id": SESSION},
                {"type": "turn.failed", "error": {"message": message}}), **extra}

    def success(self, session=SESSION):
        return {"rc": 0, "output": '{"ok": true}', "stdout": events(
            {"type": "thread.started", "thread_id": session},
            {"type": "turn.completed", "usage": {"input_tokens": 300, "output_tokens": 20}})}

    def run_fixture(self, sequence, timeout=2400, command=None):
        def run(cmd, **kwargs):
            self.calls.append((cmd, kwargs))
            row = sequence[len(self.calls) - 1]
            self.clock += row.get("elapsed", 1)
            if row.get("timeout"):
                raise subprocess.TimeoutExpired(cmd, kwargs["timeout"])
            path = Path(cmd[cmd.index("--output-last-message") + 1])
            if "output" in row:
                path.write_text(row["output"])
            return subprocess.CompletedProcess(cmd, row["rc"], row.get("stdout", ""), row.get("stderr", ""))

        def sleep(seconds):
            self.clock += seconds

        with patch.object(transport.subprocess, "run", side_effect=run), \
             patch.object(transport.time, "monotonic", side_effect=lambda: self.clock), \
             patch.object(transport.time, "sleep", side_effect=sleep), \
             patch.object(transport.random, "uniform", return_value=0):
            return transport.run_with_recovery(command=command or self.command, model_input="unchanged private input",
                environment=self.env, timeout_seconds=timeout, cwd=self.root)

    def journal(self):
        return json.loads(self.output.with_suffix(".transport.json").read_text())

    def test_success_is_not_retried(self):
        proc = self.run_fixture([self.success()])
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(transport.transport_fields(proc)["transport_status"], "completed")

    def test_429_resumes_same_session_and_preserves_schema_and_input(self):
        proc = self.run_fixture([self.failure(), self.success()])
        self.assertEqual(proc.returncode, 0)
        cmd, kw = self.calls[1]
        self.assertEqual(cmd[-2:], [SESSION, "-"])
        self.assertEqual(cmd[cmd.index("exec") + 1], "resume")
        self.assertNotIn("--sandbox", cmd)
        self.assertNotIn("--cd", cmd)
        self.assertIn('sandbox_mode="read-only"', cmd)
        self.assertEqual(cmd[cmd.index("--output-schema") + 1], "schema.json")
        self.assertEqual(kw["input"], transport.RETRY_INPUT)
        self.assertEqual(kw["env"], self.env)
        self.assertEqual(json.loads(self.output.read_text()), {"ok": True})
        self.assertEqual(self.journal()["attempts"][0]["retry_delay_seconds"], 60)
        self.assertTrue(Path(self.journal()["adopted_output"]).is_file())

    def test_existing_resume_layout(self):
        cmd = transport._resume_command(self.command, SESSION, self.output)
        proc = self.run_fixture([self.failure("unexpected status 502 Bad Gateway"), self.success()], command=cmd)
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(self.calls[1][0].count("resume"), 1)

    def test_retry_limit_and_exponential_wait(self):
        proc = self.run_fixture([self.failure()] * 3)
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(self.journal()["status"], "retry_limit")
        self.assertEqual([r.get("retry_delay_seconds") for r in self.journal()["attempts"]], [60, 120, None])

    def test_retry_after(self):
        self.run_fixture([self.failure("429 Too Many Requests; Retry-After: 200"), self.success()])
        self.assertEqual(self.journal()["attempts"][0]["retry_delay_seconds"], 200)

    def test_timeout_budget_includes_waits(self):
        proc = self.run_fixture([self.failure(elapsed=2350)])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(self.journal()["status"], "insufficient_remaining_turn_budget")

    def test_timeout_is_not_retried(self):
        with self.assertRaises(subprocess.TimeoutExpired):
            self.run_fixture([{"timeout": True}])
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(self.journal()["status"], "timeout")

    def test_nonempty_answer_is_not_retried(self):
        self.run_fixture([self.failure(output='{"partial":true}')])
        self.assertEqual(self.journal()["status"], "answer_already_produced")
        self.assertEqual(self.output.read_text(), '{"partial":true}')

    def test_answer_event_prevents_retry_even_without_output_file(self):
        row = self.failure()
        row["stdout"] += "\n" + events({"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}})
        self.run_fixture([row])
        self.assertEqual(self.journal()["status"], "answer_already_produced")

    def test_empty_failed_output_is_retained(self):
        self.run_fixture([self.failure(output=""), self.success()])
        self.assertEqual(self.output.with_suffix(".transport_empty.json").read_text(), "")
        self.assertEqual(json.loads(self.output.read_text()), {"ok": True})

    def test_no_implicit_interactive_home(self):
        self.env = {}
        self.run_fixture([self.failure()])
        self.assertEqual(self.journal()["status"], "no_verified_persistent_session")

    def test_session_switch_is_rejected(self):
        proc = self.run_fixture([self.failure(), self.success("different-session")])
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(self.journal()["status"], "session_mismatch")
        self.assertFalse(self.output.exists())

    def test_unknown_error_and_auth_quota_not_retried(self):
        for text in ("unexpected CLI exit", "401 unauthorized", "429 insufficient_quota", "400 bad request", "context window exceeded", "no space left on device"):
            info = transport.failure_info(events({"type": "turn.failed", "error": {"message": text}}), "")
            self.assertFalse(info["retryable"], text)
        self.run_fixture([self.failure("429 insufficient_quota")])
        self.assertEqual(self.journal()["status"], "nonretryable_error")

    def test_all_observed_transient_classes(self):
        for text in ("429 Too Many Requests", "unexpected status 502 Bad Gateway", "503 Service Unavailable",
                     "500 Internal Server Error", "504 Gateway Timeout", "stream disconnected before completion: stream closed before response.completed"):
            self.assertTrue(transport.failure_info(events({"type": "turn.failed", "error": {"message": text}}), "")["retryable"])

    def test_does_not_classify_or_log_answer_content(self):
        info = transport.failure_info(events({"type": "item.completed", "item": {"type": "agent_message", "text": "429"}}), "other error")
        self.assertFalse(info["retryable"])
        secret = "synthetic-not-a-real-key"
        self.run_fixture([self.failure("502 Bad Gateway token=" + secret)] * 3)
        self.assertNotIn(secret, self.output.with_suffix(".transport.json").read_text())

    def test_refuses_to_overwrite_a_previous_invocation(self):
        self.output.write_text("previous answer")
        with self.assertRaises(FileExistsError):
            self.run_fixture([self.success()])
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()
