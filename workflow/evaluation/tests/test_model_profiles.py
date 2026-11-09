from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch

RUNTIME = Path(__file__).resolve().parents[1] / "runtime"
sys.path.insert(0, str(RUNTIME))

from bare_model import (  # noqa: E402
    ProviderConfig, TransientProviderError, _read_messages_stream,
    build_followup_payload, build_payload, endpoint_for, extract_output_text, public_config,
)
from build_paired_schemas import paired_schema  # noqa: E402
from model_profiles import install_profiles, load_suite, solver_profiles  # noqa: E402
from paired_pipeline import anonymous_assignment  # noqa: E402
from run_comparison import parse_args  # noqa: E402
from support import merged_environment, normalize_usage  # noqa: E402


class ModelProfileTests(unittest.TestCase):
    def test_cli_modes_and_non_solver_defaults(self):
        base = ["run", "--selection", "selection.json", "--run-root", "out", "--run-id", "test"]
        for extra, count, mode in (([], 2, "test"), (["--mode", "formal"], 7, "formal")):
            with patch.object(sys, "argv", base + extra):
                args = parse_args()
            self.assertEqual(len(args.solver), count)
            self.assertEqual(args.mode, mode)
            self.assertEqual(args.judge_model, "gpt-6-astra")
            self.assertEqual(args.audit_model, "gpt-6-astra")
            self.assertEqual(args.judge_reasoning_effort, "high")
            self.assertEqual(args.audit_reasoning_effort, "high")
        with patch.object(sys, "argv", base + ["--solver", "a=a.env", "--solver", "b=b.env"]):
            self.assertEqual(parse_args().mode, "custom")

    def test_eight_anonymous_answers_and_schema(self):
        labels = load_suite()["modes"]["formal"] + ["custom_eighth"]
        assignment = anonymous_assignment("paper", "run", 0, labels)
        self.assertEqual(len(assignment), 8)
        self.assertEqual(set(assignment.values()), set(labels))
        self.assertIn("answer_h", assignment)
        with self.assertRaises(ValueError):
            anonymous_assignment("paper", "run", 0, labels + ["ninth"])
        for name, item in (("reviewer", "report"), ("evaluator", "evaluation")):
            schema = json.loads((RUNTIME.parent / f"schemas/paired_{name}.schema.json").read_text())
            single = json.loads((RUNTIME.parent / f"schemas/{name}.schema.json").read_text())
            self.assertEqual(schema, paired_schema(schema["title"], item, single))
            self.assertEqual(schema["properties"]["answer_reports"]["maxItems"], 8)

    def test_install_and_payloads_do_not_leak_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            keys = [root / "get.key", root / "novita.key"]
            for index, key in enumerate(keys):
                key.write_text(f"private-test-key-{index}\n")
                key.chmod(0o600)
            profiles = root / "profiles"
            install_profiles(profiles, keys[0], novita_key_file=keys[1])
            for label, path in solver_profiles("formal", profiles):
                config = ProviderConfig.from_environment(merged_environment(path), base_dir=profiles)
                self.assertEqual(path.stat().st_mode & 0o777, 0o600)
                self.assertEqual(config.max_output_tokens, 48000)
                self.assertTrue(config.stream)
                self.assertNotIn(config.api_key, json.dumps(public_config(config)))
                self.assertNotIn(config.api_key, path.read_text())
                payloads = [build_payload(config, "system", "task"), build_followup_payload(config, "system", "task", "objection", "reply")]
                for payload in payloads:
                    self.assertNotIn("tools", payload)
                    if label in {"gpt6", "gpt56"}:
                        self.assertEqual(payload["reasoning"]["effort"], "high")
                    elif label == "claude_fable":
                        self.assertEqual(config.model, "pa/claude-fable-5")
                        self.assertEqual(endpoint_for(config), "https://api.novita.ai/anthropic/v1/messages")
                        self.assertEqual(payload["thinking"], {"type": "adaptive"})
                        self.assertEqual(payload["output_config"], {"effort": "high"})
                        self.assertNotIn("reasoning_effort", payload)
                    elif label != "claude_fable":
                        self.assertEqual(payload["thinking"], {"type": "enabled"})
                    expected_base = "https://api.novita.ai/anthropic" if label == "claude_fable" else "https://api.get-apikey.com/v1"
                    self.assertEqual(config.base_url, expected_base)
            self.assertNotIn("gpt55", load_suite()["solvers"])
            self.assertEqual([label for label, _ in solver_profiles("test", profiles)], ["gpt6", "gpt56"])
            self.assertIn('model = "gpt-6-astra"', (profiles / "get-api/config.toml").read_text())

    def test_missing_novita_key_does_not_partially_install_profiles(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            key = root / "get.key"
            key.write_text("private-test-key\n")
            key.chmod(0o600)
            profiles = root / "profiles"
            with self.assertRaisesRegex(ValueError, "key file is required for novita"):
                install_profiles(profiles, key)
            self.assertFalse(profiles.exists())

    def test_messages_stream_separates_thinking_and_counts_cache(self):
        events = [
            {"type": "message_start", "message": {"usage": {"input_tokens": 10, "cache_read_input_tokens": 20, "cache_creation_input_tokens": 3, "output_tokens": 1}}},
            {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": ""}},
            {"type": "content_block_delta", "index": 0, "delta": {"thinking": "private reasoning"}},
            {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}},
            {"type": "content_block_delta", "index": 1, "delta": {"text": "323"}},
            {"type": "message_delta", "delta": {"stop_reason": "end_turn"}, "usage": {"output_tokens": 7, "output_tokens_details": {"thinking_tokens": 3}}},
            {"type": "message_stop"},
        ]
        stream = io.BytesIO("".join("data: " + json.dumps(e) + "\n\n" for e in events).encode())
        response = _read_messages_stream(stream)
        self.assertEqual(extract_output_text(response, "anthropic_messages"), "323")
        self.assertEqual(response["status"], "end_turn")
        usage = normalize_usage(response["usage"])
        self.assertEqual(usage["input_tokens"], 33)
        self.assertEqual(usage["cached_input_tokens"], 20)
        self.assertEqual(usage["non_cached_input_tokens"], 13)
        self.assertEqual(usage["output_tokens"], 7)
        self.assertEqual(usage["reasoning_output_tokens"], 3)
        with self.assertRaises(TransientProviderError):
            _read_messages_stream(io.BytesIO(b'data: {"type":"ping"}\n'))

    def test_messages_endpoint_accepts_documented_host_and_legacy_v1(self):
        config = ProviderConfig("https://example.invalid", "key", "fable", "anthropic_messages", "high", 48000, 60, True)
        for suffix in ("", "/", "/v1", "/v1/"):
            with self.subTest(suffix=suffix):
                current = replace(config, base_url="https://example.invalid" + suffix)
                self.assertEqual(endpoint_for(current), "https://example.invalid/v1/messages")
        for protocol, operation in (("responses", "responses"), ("chat_completions", "chat/completions")):
            current = replace(config, wire_api=protocol, base_url="https://example.invalid/v1/")
            self.assertEqual(endpoint_for(current), "https://example.invalid/v1/" + operation)

    def test_messages_followup_preserves_only_visible_conversation_and_budget(self):
        config = ProviderConfig("https://example.invalid/v1", "key", "fable", "anthropic_messages", "high", 200, 60, True)
        payload = build_followup_payload(config, "system", "task", "objection", "solve instead")
        self.assertEqual(payload["messages"], [{"role": "user", "content": "task"}, {"role": "assistant", "content": "objection"}, {"role": "user", "content": "solve instead"}])
        self.assertEqual(payload["max_tokens"], 200)
        self.assertNotIn("tools", payload)
        with self.assertRaisesRegex(ValueError, "has no output text"):
            extract_output_text({"content": [{"type": "thinking", "thinking": "reasoning only"}]}, "anthropic_messages")


if __name__ == "__main__":
    unittest.main()
