from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "runtime"))
from bare_model import (  # noqa: E402
    ProviderConfig, TransientProviderError, _read_chat_completions_stream,
    _read_responses_stream, build_payload, build_followup_payload, send_one_request,
)
from paired_pipeline import (  # noqa: E402
    ArtifactBundle, SolverSpec, SolverBatchError, anonymous_assignment,
    has_final_answer, run_solver, run_all_solvers,
)
from run_comparison import recover_recorded_usage  # noqa: E402


def config():
    return ProviderConfig("https://example.invalid/v1", "test-secret", "test-model",
                          "chat_completions", "high", 48000, 10, stream=True)


def response(answer, finish="stop"):
    return {"choices": [{"message": {"content": answer}, "finish_reason": finish}],
            "usage": {"prompt_tokens": 20, "completion_tokens": 40}}


class RecoveryTests(unittest.TestCase):
    def test_audit_checks_repairs_and_information_access(self):
        prompt = (Path(__file__).resolve().parents[1] / "prompts/task_audit.md").read_text()
        self.assertIn("Distinguish when a quantity is fixed from when it is revealed", prompt)
        self.assertIn("every proposed repair", prompt)

    def test_limit_parameter_for_first_and_followup_payloads(self):
        cfg = replace(config(), chat_token_limit_parameter="max_completion_tokens")
        for payload in (build_payload(cfg, "system", "task"),
                        build_followup_payload(cfg, "system", "task", "first", "retry")):
            self.assertEqual(payload["max_completion_tokens"], 48000)
            self.assertNotIn("max_tokens", payload)
        self.assertEqual(build_payload(config(), "s", "u")["max_tokens"], 48000)

    def test_responses_output_limit_is_not_a_transport_failure(self):
        event = {"type": "response.incomplete", "response": {
            "incomplete_details": {"reason": "max_output_tokens"},
            "usage": {"input_tokens": 10, "output_tokens": 64}, "output": [],
        }}
        result = _read_responses_stream(io.BytesIO(("data: " + json.dumps(event) + "\n\n").encode()))
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["usage"]["output_tokens"], 64)

    def test_partial_chat_disconnect_is_not_a_final_answer(self):
        stream = io.BytesIO(b'data: {"choices":[{"delta":{"content":"partial"}}]}\n\n')
        with self.assertRaises(TransientProviderError):
            _read_chat_completions_stream(stream)
        with self.assertRaises(TransientProviderError):
            _read_responses_stream(io.BytesIO(b'data: {"type":"response.created"}\n\n'))

    def test_only_markup_is_empty_but_short_math_is_preserved(self):
        for value in ("", " \n", "$\n", '">#', "```\n```", "# * $\n"):
            self.assertFalse(has_final_answer(value))
        for value in ("0", "$x=0$", "$\\emptyset$", "I could not prove it."):
            self.assertTrue(has_final_answer(value))

    def test_all_empty_assignment_is_allowed(self):
        self.assertEqual(anonymous_assignment("p", "r", 0, []), {})

    def test_solver_reuses_only_exact_verified_request(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bundle_root = root / "bundle"
            bundle_root.mkdir()
            (bundle_root / "task.md").write_text("Prove 1=1.")
            bundle = ArtifactBundle(0, bundle_root)
            spec = SolverSpec("test", config())
            with patch("paired_pipeline.send_one_request", return_value=response("A proof.")) as request:
                first = run_solver(spec, bundle, root / "solver")
                second = run_solver(spec, bundle, root / "solver")
                self.assertEqual(first, second)
                request.assert_called_once()
                (bundle_root / "task.md").write_text("Prove 2=2.")
                with self.assertRaisesRegex(Exception, "different inputs"):
                    run_solver(spec, bundle, root / "solver")
                request.assert_called_once()
            usage_text = (root / "solver/call_usage.json").read_text()
            self.assertNotIn("test-secret", usage_text)

    def test_markup_only_answer_is_zero_and_raw_answer_is_retained(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "task.md").write_text("Prove 1=1.")
            with patch("paired_pipeline.send_one_request", return_value=response("$", "length")):
                result = run_solver(SolverSpec("test", config()), ArtifactBundle(0, root), root / "solver")
            self.assertEqual(result["terminal_score"], 0)
            self.assertEqual(result["proof"], "")
            self.assertEqual((root / "solver/answer.md").read_text().strip(), "$")

    def test_failed_transport_is_not_zero_and_preserves_other_models(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def call(spec, bundle, output):
                if spec.label == "bad":
                    raise RuntimeError("provider HTTP 502")
                return {"usage": {"input_tokens": 20}, "proof": "valid proof"}
            with patch("paired_pipeline.run_solver", side_effect=call):
                with self.assertRaises(SolverBatchError) as caught:
                    run_all_solvers([SolverSpec("good", config()), SolverSpec("bad", config())],
                                    ArtifactBundle(0, root), root)
            self.assertEqual(set(caught.exception.results), {"good"})
            self.assertEqual(set(caught.exception.errors), {"bad"})
            self.assertNotIn("terminal_score", caught.exception.results["good"])

    def test_failure_usage_recovery_counts_returned_calls_once(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            paths = [root / "pre_solver_audit/call_audit.json",
                     root / "rounds/round_0/models/gpt/call_usage.json",
                     root / "rounds/round_0/models/gpt/turn_2_invalid_objection/call_usage.json"]
            for path in paths:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps({"usage": {"input_tokens": 20, "output_tokens": 10}}))
            recovered = recover_recorded_usage(root)
            self.assertEqual(recovered["usage"]["task_audit"]["input_tokens"], 20)
            self.assertEqual(recovered["solver_usage_by_model"]["gpt"]["input_tokens"], 40)

    def test_stream_error_retry_records_all_attempts(self):
        failed = io.BytesIO(b'data: {"type":"error","code":"upstream_stream_error"}\n\n')
        succeeded = io.BytesIO(b'data: {"type":"response.completed","response":{"output_text":"ok","usage":{"input_tokens":1,"output_tokens":1}}}\n\n')
        records = []
        cfg = replace(config(), wire_api="responses")
        with patch("bare_model.urllib.request.urlopen", side_effect=[failed, succeeded]), \
             patch("bare_model.TRANSIENT_RETRY_DELAYS_SECONDS", (0,)), \
             patch("bare_model.time.sleep"):
            returned = send_one_request(cfg, {}, attempt_callback=records.append)
        self.assertEqual(returned["output_text"], "ok")
        self.assertEqual([record["status"] for record in records], ["error", "returned"])
        self.assertIsNone(records[0]["raw_usage"])
        self.assertNotIn("test-secret", json.dumps(records))


if __name__ == "__main__":
    unittest.main()
