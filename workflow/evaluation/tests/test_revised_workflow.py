from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "runtime"
PROJECT = ROOT.parent.parent
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from agent_call import AgentConfig, is_transient_codex_failure  # noqa: E402
from bare_model import (  # noqa: E402
    ProviderConfig,
    _read_chat_completions_stream,
    _read_responses_stream,
    build_followup_payload,
    build_payload,
    TransientProviderError,
)
from paired_pipeline import (  # noqa: E402
    ANSWER_IDS,
    ArtifactBundle,
    PaperInput,
    SolverSpec,
    anonymous_assignment,
    apply_audit_replacements,
    audit_context,
    parse_task_status,
    run_invalid_objection_followup,
    run_paired_evaluator,
    run_paired_reviewer,
    run_paper,
    task_audit_input,
    validate_task_audit_result,
)
from run_comparison import aggregate_solver_usage  # noqa: E402
from codex_runtime import codex_command, extract_session_id  # noqa: E402


class ExtractionIntegrityTests(unittest.TestCase):
    def test_task_audit_requires_complete_preserving_replacements(self) -> None:
        prompt = (ROOT / "prompts/task_audit.md").read_text()
        self.assertIn("complete replacement file", prompt)
        self.assertIn("Preserve every unaffected definition", prompt)
        self.assertIn("leave a referenced object undefined", prompt)
        self.assertIn("ordinary procedural language", prompt)
        self.assertIn("adversarial data-dependent rule", prompt)
        self.assertIn("statement-essential deletion test", prompt)
        self.assertIn("whose role is derivational rather than statement-essential", prompt)
        self.assertIn(
            "For `artifacts_verified`, `paper_issue_confirmed`, or `invalid_objection`",
            prompt,
        )
        schema = json.loads((ROOT / "schemas/task_audit.schema.json").read_text())
        self.assertIn("artifacts_verified", schema["properties"]["status"]["enum"])

    def test_nonrepair_audit_tolerates_redundant_self_audit(self) -> None:
        schema = json.loads((ROOT / "schemas/task_audit.schema.json").read_text())
        checks = {
            name: {"status": "pass", "evidence": "Checked."}
            for name in (
                "definition_integrity",
                "self_containment",
                "source_fidelity",
                "anti_leakage",
                "contribution_fidelity",
                "validity",
                "scope",
            )
        }
        result = {
            "status": "paper_issue_confirmed",
            "explanation": "The source target has a blocking defect.",
            "affected_material_ids": ["theory_001"],
            "source_issue_check": {
                "complete_chain_context_checked": True,
                "standing_assumptions_checked": True,
                "counterexample_satisfies_complete_source_contract": True,
                "local_clarification_or_repair_suffices": False,
                "evidence": "The counterexample satisfies every standing assumption.",
            },
            "replacements": None,
            "corrected_material_records": None,
            "self_audit": checks,
            "gt_quality_warning": None,
        }
        self.assertIs(validate_task_audit_result(result, schema), result)

    def test_paper_issue_requires_complete_source_contract_check(self) -> None:
        schema = json.loads((ROOT / "schemas/task_audit.schema.json").read_text())
        result = {
            "status": "paper_issue_confirmed",
            "explanation": "Claimed issue.",
            "affected_material_ids": ["theory_001"],
            "source_issue_check": {
                "complete_chain_context_checked": True,
                "standing_assumptions_checked": False,
                "counterexample_satisfies_complete_source_contract": True,
                "local_clarification_or_repair_suffices": False,
                "evidence": "A standing assumption was not checked.",
            },
            "replacements": None,
            "corrected_material_records": None,
            "self_audit": None,
            "gt_quality_warning": None,
        }
        with self.assertRaisesRegex(
            ValueError, "complete source-contract verification"
        ):
            validate_task_audit_result(result, schema)

    def test_source_minor_issue_requires_local_repair_and_records(self) -> None:
        schema = json.loads((ROOT / "schemas/task_audit.schema.json").read_text())
        checks = {
            name: {"status": "pass", "evidence": "Checked."}
            for name in (
                "definition_integrity",
                "self_containment",
                "source_fidelity",
                "anti_leakage",
                "contribution_fidelity",
                "validity",
                "scope",
            )
        }
        repair = {
            "original_source": "The endpoint was written with <.",
            "repaired_form": "Use <= at the same endpoint.",
            "source_evidence": "The proof and downstream use include equality.",
            "justification": "The endpoint correction preserves the claim and route.",
        }
        record = {
            "item_id": "theory_001",
            "role": "theory_candidate",
            "source_label": "Main theorem",
            "recovered_content": "Corrected theorem statement.",
            "proof_reconstruction": "Original proof with the corrected endpoint.",
            "statement_status": "minor_issue",
            "statement_findings": ["The endpoint symbol is inconsistent."],
            "statement_repair": repair,
            "proof_status": "clean",
            "proof_findings": [],
            "proof_repair": None,
            "external_classification": None,
            "source_spans": ["L10-L30"],
            "statement_source_locations": [
                {"start_line": 10, "end_line": 12, "label": "Statement"}
            ],
            "proof_source_locations": [
                {"start_line": 13, "end_line": 30, "label": "Proof"}
            ],
            "depends_on": [],
            "is_added": False,
            "addition_reason": None,
        }
        result = {
            "status": "source_minor_issue_fixed",
            "explanation": "A unique source-local endpoint repair suffices.",
            "affected_material_ids": ["theory_001"],
            "source_issue_check": {
                "complete_chain_context_checked": True,
                "standing_assumptions_checked": True,
                "counterexample_satisfies_complete_source_contract": True,
                "local_clarification_or_repair_suffices": True,
                "evidence": "The proof uniquely fixes the endpoint.",
            },
            "replacements": {
                "task_md": "# Task\nProve the corrected endpoint claim.\n",
                "proof_ground_truth_md": "# Proof\nProof.\n",
                "rubric_md": "# Rubric\nTen points.\n",
                "provenance": {
                    "public_clauses": [
                        {
                            "clause_id": "clause_001",
                            "kind": "target",
                            "source_material_ids": ["theory_001"],
                            "transformation": "equivalent_restatement",
                        }
                    ],
                    "private_proof_steps": [
                        {
                            "step_id": "step_001",
                            "source_material_ids": ["theory_001"],
                        }
                    ],
                    "notation_map": [],
                    "applied_source_repairs": ["theory_001"],
                },
            },
            "corrected_material_records": [record],
            "self_audit": checks,
            "gt_quality_warning": None,
        }
        self.assertIs(validate_task_audit_result(result, schema), result)

        result["source_issue_check"][
            "local_clarification_or_repair_suffices"
        ] = False
        with self.assertRaisesRegex(ValueError, "requires a local source repair"):
            validate_task_audit_result(result, schema)

    def test_task_audit_schema_uses_strict_objects_without_all_of(self) -> None:
        schema = json.loads((ROOT / "schemas/task_audit.schema.json").read_text())
        self.assertNotIn("allOf", schema)
        self.assertNotIn("uniqueItems", schema["properties"]["affected_material_ids"])
        self.assertFalse(schema["$defs"]["provenance"]["additionalProperties"])
        self.assertFalse(
            schema["$defs"]["material_record"]["additionalProperties"]
        )

    def test_only_solver_budget_differs_from_original_artifacts(self) -> None:
        if not (PROJECT / "workflow").is_dir():
            self.skipTest("the source workflow is not present in this deployment")
        pairs = (
            (
                PROJECT / "workflow/proof_experiment/llm_solver/prompts/proof_system_prompt.md",
                ROOT / "prompts/solver_system_prompt.md",
            ),
            (
                PROJECT / "workflow/proof_experiment/llm_solver/prompts/proof_answer_template.md",
                ROOT / "prompts/solver_answer_template.md",
            ),
            (
                PROJECT / "workflow/reviewer_and_evaluator/reviewer/system_prompt.md",
                ROOT / "prompts/reviewer_system_prompt.md",
            ),
            (
                PROJECT / "workflow/reviewer_and_evaluator/evaluator/system_prompt.md",
                ROOT / "prompts/evaluator_system_prompt.md",
            ),
            (
                PROJECT / "workflow/reviewer_and_evaluator/reviewer/output_schema.json",
                ROOT / "schemas/reviewer.schema.json",
            ),
            (
                PROJECT / "workflow/reviewer_and_evaluator/evaluator/output_schema.json",
                ROOT / "schemas/evaluator.schema.json",
            ),
        )
        for original, copied in pairs:
            original_text = original.read_text()
            copied_text = copied.read_text()
            if copied.name == "solver_system_prompt.md":
                start = copied_text.index("\n## Critical Completion Budget\n")
                end = copied_text.index("\n## 1. Validate The Task Contract\n")
                copied_text = copied_text[:start] + copied_text[end:]
            self.assertEqual(original_text, copied_text)

    def test_paired_schema_embeds_the_exact_single_schema(self) -> None:
        for single_name, paired_name, item_name in (
            ("reviewer.schema.json", "paired_reviewer.schema.json", "report"),
            ("evaluator.schema.json", "paired_evaluator.schema.json", "evaluation"),
        ):
            single = json.loads((ROOT / "schemas" / single_name).read_text())
            expected = dict(single)
            expected.pop("$schema", None)
            expected.pop("title", None)
            paired = json.loads((ROOT / "schemas" / paired_name).read_text())
            actual = paired["properties"]["answer_reports"]["items"]["properties"][
                item_name
            ]
            self.assertEqual(expected, actual)


class StreamingTests(unittest.TestCase):
    def test_followup_payload_preserves_visible_history_and_remaining_budget(self) -> None:
        config = ProviderConfig(
            base_url="https://example.invalid/v1",
            api_key="test",
            model="reasoning-model",
            wire_api="responses",
            reasoning_effort="high",
            max_output_tokens=18_000,
            timeout_seconds=60,
            stream=True,
        )
        payload = build_followup_payload(
            config,
            "system",
            "first task",
            "first objection",
            "objection rejected; solve",
        )
        self.assertEqual(payload["max_output_tokens"], 18_000)
        self.assertEqual(
            payload["input"],
            [
                {"role": "user", "content": "first task"},
                {"role": "assistant", "content": "first objection"},
                {"role": "user", "content": "objection rejected; solve"},
            ],
        )

    def test_persistent_codex_command_can_resume_the_same_thread(self) -> None:
        base = {
            "codex_bin": "codex",
            "model": "judge",
            "reasoning_effort": "high",
            "workspace": Path("/tmp/workspace"),
            "schema_path": Path("/tmp/schema.json"),
            "output_path": Path("/tmp/output.json"),
        }
        first = codex_command(**base, ephemeral=False)
        resumed = codex_command(**base, resume_session_id="thread_123")
        self.assertNotIn("--ephemeral", first)
        self.assertIn("resume", resumed)
        self.assertIn("thread_123", resumed)
        self.assertNotIn("--sandbox", resumed)
        self.assertNotIn("--cd", resumed)
        self.assertEqual(
            extract_session_id('{"type":"thread.started","thread_id":"thread_123"}'),
            "thread_123",
        )

    def test_codex_upstream_failure_is_retryable(self) -> None:
        self.assertTrue(
            is_transient_codex_failure(
                '{"type":"turn.failed","error":{"message":"upstream_error"}}',
                "",
            )
        )
        self.assertFalse(is_transient_codex_failure("invalid JSON output", ""))

    def test_codex_http_rate_limit_is_retryable(self) -> None:
        for message in ("429 Too Many Requests", "provider returned HTTP 429", "unexpected status code 429"):
            with self.subTest(message=message):
                self.assertTrue(is_transient_codex_failure("", message))
        self.assertFalse(is_transient_codex_failure("invalid JSON output at line 429", ""))

    def test_responses_upstream_failure_is_retryable(self) -> None:
        event = {
            "type": "response.failed",
            "response": {
                "status": "failed",
                "error": {
                    "code": "upstream_error",
                    "message": "Upstream request failed",
                },
            },
        }
        stream = io.BytesIO(
            ("data: " + json.dumps(event) + "\n\n").encode("utf-8")
        )
        with self.assertRaises(TransientProviderError):
            _read_responses_stream(stream)

    def test_responses_stream_read_failure_is_retryable(self) -> None:
        event = {
            "type": "error",
            "error": {
                "type": "upstream_error",
                "message": "stream_read_error",
                "code": "stream_read_error",
            },
        }
        stream = io.BytesIO(
            ("data: " + json.dumps(event) + "\n\n").encode("utf-8")
        )
        with self.assertRaises(TransientProviderError):
            _read_responses_stream(stream)

    def test_chat_internal_server_failure_is_retryable(self) -> None:
        event = {
            "error": {
                "type": "internal_server_error",
                "message": "Inference engine abort",
                "code": "internal_server_error",
            }
        }
        stream = io.BytesIO(
            ("data: " + json.dumps(event) + "\n\n").encode("utf-8")
        )
        with self.assertRaises(TransientProviderError):
            _read_chat_completions_stream(stream)

    def test_chat_payload_enables_stream_and_usage(self) -> None:
        config = ProviderConfig(
            base_url="https://example.invalid/v1",
            api_key="test",
            model="reasoning-model",
            wire_api="chat_completions",
            reasoning_effort="high",
            max_output_tokens=131072,
            timeout_seconds=60,
            stream=True,
        )
        payload = build_payload(config, "system", "user")
        self.assertTrue(payload["stream"])
        self.assertEqual(payload["stream_options"], {"include_usage": True})

    def test_reads_chat_reasoning_and_answer_chunks(self) -> None:
        events = [
            {"choices": [{"delta": {"reasoning_content": "think "}}]},
            {"choices": [{"delta": {"content": "final "}}]},
            {
                "choices": [{"delta": {"content": "answer"}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 2, "completion_tokens": 3},
            },
        ]
        stream = io.BytesIO(
            b"".join(
                f"data: {json.dumps(event)}\n\n".encode() for event in events
            )
            + b"data: [DONE]\n\n"
        )
        response = _read_chat_completions_stream(stream)
        message = response["choices"][0]["message"]
        self.assertEqual(message["reasoning_content"], "think ")
        self.assertEqual(message["content"], "final answer")
        self.assertEqual(response["usage"]["completion_tokens"], 3)

    def test_reads_concatenated_responses_events_in_one_data_record(self) -> None:
        delta = {"type": "response.output_text.delta", "delta": "answer"}
        completed = {
            "type": "response.completed",
            "response": {"usage": {"input_tokens": 2, "output_tokens": 3}},
        }
        stream = io.BytesIO(
            (
                "data: "
                + json.dumps(delta)
                + json.dumps(completed)
                + "\n\n"
            ).encode("utf-8")
        )
        response = _read_responses_stream(stream)
        self.assertEqual(response["output_text"], "answer")
        self.assertEqual(response["usage"]["output_tokens"], 3)

    def test_flat_and_nested_upstream_stream_errors_are_retryable(self) -> None:
        for event in (
            {"type": "error", "code": "upstream_stream_error", "message": "upstream failed"},
            {"type": "response.failed", "response": {"error": {"code": "upstream_stream_error"}}},
        ):
            with self.subTest(event=event):
                stream = io.BytesIO(("data: " + json.dumps(event) + "\n\n").encode())
                with self.assertRaises(TransientProviderError):
                    _read_responses_stream(stream)
        stream = io.BytesIO(b'data: {"type":"error","code":"invalid_request_error"}\n\n')
        with self.assertRaises(RuntimeError) as raised:
            _read_responses_stream(stream)
        self.assertNotIsInstance(raised.exception, TransientProviderError)

    def test_reads_concatenated_chat_events_in_one_data_record(self) -> None:
        first = {"choices": [{"delta": {"reasoning_content": "think "}}]}
        second = {
            "choices": [
                {"delta": {"content": "answer"}, "finish_reason": "stop"}
            ],
            "usage": {"prompt_tokens": 2, "completion_tokens": 3},
        }
        stream = io.BytesIO(
            (
                "data: "
                + json.dumps(first)
                + "data: "
                + json.dumps(second)
                + "\n\n"
            ).encode("utf-8")
        )
        response = _read_chat_completions_stream(stream)
        self.assertEqual(
            response["choices"][0]["message"]["reasoning_content"], "think "
        )
        self.assertEqual(
            response["choices"][0]["message"]["content"], "answer"
        )


class PipelineControlTests(unittest.TestCase):
    def test_solver_prompt_declares_the_shared_completion_budget(self) -> None:
        prompt = (ROOT / "prompts/solver_system_prompt.md").read_text()
        self.assertIn("48,000 total completion tokens", prompt)
        self.assertIn("automatically receives score `0`", prompt)

    def test_solver_usage_is_aggregated_by_model(self) -> None:
        results = [
            {
                "solver_usage_by_model": {
                    "gpt55": {"input_tokens": 10, "output_tokens": 2},
                    "gpt56": {"input_tokens": 8, "output_tokens": 3},
                }
            },
            {
                "solver_usage_by_model": {
                    "gpt55": {"input_tokens": 4, "output_tokens": 1}
                }
            },
        ]
        self.assertEqual(
            aggregate_solver_usage(results),
            {
                "gpt55": {"input_tokens": 14, "output_tokens": 3},
                "gpt56": {"input_tokens": 8, "output_tokens": 3},
            },
        )

    def make_paper(self, root: Path, *, audit_ready: bool = False) -> PaperInput:
        formalization = root / "source/formalization"
        formalization.mkdir(parents=True)
        for name, content in (
            ("task.md", "# Task\nProve 1=1.\n"),
            ("proof_ground_truth.md", "# Proof\nTrivial.\n"),
            ("rubric.md", "# Rubric\nOne step.\n"),
            ("provenance.json", "{}\n"),
        ):
            (formalization / name).write_text(content)
        paths = {
            name: formalization / name
            for name in (
                "task.md",
                "proof_ground_truth.md",
                "rubric.md",
                "provenance.json",
            )
        }
        if audit_ready:
            view = formalization / "thread_b_view.json"
            view.write_text('{"selected_material_records": []}\n')
            paths["formalization/thread_b_view.json"] = view
        return PaperInput(
            "paper_test",
            "completed",
            root / "source",
            paths,
            audit_ready,
        )

    def test_assignment_is_complete_and_deterministic(self) -> None:
        labels = [
            "gpt55",
            "gpt56_xhigh",
            "glm53",
            "deepseek",
            "gemini",
            "claude",
            "qwen38",
        ]
        first = anonymous_assignment("paper_1", "run_1", 0, labels)
        second = anonymous_assignment("paper_1", "run_1", 0, labels)
        self.assertEqual(first, second)
        self.assertEqual(set(first.values()), set(labels))

    def test_task_status_parser(self) -> None:
        answer = (
            "# Solution\n\n## Self-Assessment\n\n"
            "- **Task status:** `unscorable`\n"
            "- **Unscorable reason:** Counterexample at x=0.\n"
        )
        self.assertEqual(
            parse_task_status(answer), ("unscorable", "Counterexample at x=0.")
        )

    def test_task_status_parser_accepts_equivalent_unbulleted_format(self) -> None:
        answer = (
            "# Solution\n\n## Self-Assessment\n\n"
            "**Task status:** scorable\n"
            "**Unscorable reason:** None.\n"
        )
        self.assertEqual(parse_task_status(answer), ("scorable", "None."))

    def test_invalid_objection_followup_uses_only_remaining_budget(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            version = root / "task_versions/revision_0"
            version.mkdir(parents=True)
            (version / "task.md").write_text("# Task\nProve 1=1.\n")
            first_output = root / "models/objector"
            first_output.mkdir(parents=True)
            (first_output / "answer.md").write_text(
                "# Solution\n\n## Self-Assessment\n\n"
                "- **Task status:** `unscorable`\n"
                "- **Unscorable reason:** Claimed defect.\n"
            )
            spec = SolverSpec(
                "objector",
                ProviderConfig(
                    "https://example.invalid/v1",
                    "key",
                    "model",
                    "responses",
                    "high",
                    48_000,
                    60,
                    True,
                ),
            )
            response = {
                "output_text": (
                    "# Solution\n\nA valid proof.\n\n## Self-Assessment\n\n"
                    "- **Task status:** `scorable`\n"
                    "- **Unscorable reason:** None.\n"
                ),
                "status": "completed",
                "usage": {"input_tokens": 100, "output_tokens": 500},
            }
            with patch(
                "paired_pipeline.send_one_request", return_value=response
            ) as send:
                result = run_invalid_objection_followup(
                    spec,
                    ArtifactBundle(0, version),
                    {"usage": {"output_tokens": 30_000}},
                    first_output,
                )
            sent_config, payload = send.call_args.args
            self.assertEqual(sent_config.max_output_tokens, 18_000)
            self.assertEqual(payload["max_output_tokens"], 18_000)
            self.assertEqual(result["task_status"], "scorable")
            self.assertIsNone(result["terminal_score"])
            usage_record = json.loads(
                (first_output / "turn_2_invalid_objection/call_usage.json").read_text()
            )
            self.assertEqual(usage_record["raw_usage"], response["usage"])
            self.assertEqual(usage_record["usage"]["output_tokens"], 500)
            self.assertGreaterEqual(usage_record["wall_time_seconds"], 0)
            self.assertNotIn("api_key", usage_record)
            instruction = (
                first_output / "turn_2_invalid_objection/followup_instruction.md"
            ).read_text()
            self.assertIn("remaining completion budget is 18,000", instruction)

    def test_audit_replacement_creates_new_revision(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            version = root / "task_versions/revision_0"
            version.mkdir(parents=True)
            for name, content in (
                ("task.md", "old task\n"),
                ("proof_ground_truth.md", "proof\n"),
                ("rubric.md", "rubric\n"),
                ("provenance.json", "{}\n"),
                ("thread_b_view.json", '{"selected_material_records": []}\n'),
            ):
                (version / name).write_text(content)
            updated = apply_audit_replacements(
                ArtifactBundle(0, version),
                {
                    "replacements": {
                        "task_md": "new task",
                        "proof_ground_truth_md": None,
                        "rubric_md": None,
                        "provenance": None,
                    },
                    "corrected_material_records": None,
                },
                root,
            )
            self.assertEqual(updated.revision, 1)
            self.assertEqual(updated.task.read_text(), "new task\n")

    def test_audit_context_includes_full_map_and_complete_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source_root = root / "source"
            version = root / "task_versions/revision_0"
            version.mkdir(parents=True)
            lines = [f"line {index}" for index in range(1, 61)]
            lines[11] = "Assumption 2.1: the absolute reward series is finite."
            source_path = source_root / "private_source/extracted_text.md"
            source_path.parent.mkdir(parents=True)
            source_path.write_text("\n".join(lines) + "\n")
            view = {
                "selected_material_records": [
                    {
                        "item_id": "theory_002",
                        "source_label": "Selected theorem",
                        "statement_source_locations": [
                            {"start_line": 40, "end_line": 42, "label": "statement"}
                        ],
                        "proof_source_locations": [],
                    }
                ]
            }
            (version / "thread_b_view.json").write_text(json.dumps(view))
            source_map_path = (
                source_root / "paper_analysis/turn3_source_audit.json"
            )
            source_map_path.parent.mkdir(parents=True)
            source_map_path.write_text(
                json.dumps(
                    {
                        "material_records": [
                            {
                                "item_id": "theory_001",
                                "role": "definition",
                                "source_label": "Standing assumptions",
                                "recovered_content": "Absolute integrability.",
                                "statement_source_locations": [],
                                "proof_source_locations": [],
                                "depends_on": [],
                            },
                            {
                                "item_id": "theory_002",
                                "role": "theory_candidate",
                                "source_label": "Selected theorem",
                                "recovered_content": "A theorem.",
                                "statement_source_locations": [],
                                "proof_source_locations": [],
                                "depends_on": [],
                            },
                        ]
                    }
                )
            )
            paper = PaperInput(
                "paper_test",
                "completed",
                source_root,
                {
                    "private_source/extracted_text.md": source_path,
                    "paper_analysis/turn3_source_audit.json": source_map_path,
                },
                True,
            )
            _, source_map, context = audit_context(
                paper, ArtifactBundle(0, version)
            )
            self.assertIn("theory_001", json.dumps(source_map))
            self.assertIn("Assumption 2.1", context)
            self.assertIn("L000001: line 1", context)
            self.assertIn("L000060: line 60", context)

            for name, content in (
                ("task.md", "# Problem\n\nProve the claim.\n"),
                ("proof_ground_truth.md", "# Proof\n\nProof.\n"),
                ("rubric.md", "# Rubric\n\n10 points.\n"),
                ("provenance.json", "{}\n"),
            ):
                (version / name).write_text(content)
            bundle = ArtifactBundle(0, version)
            first_turn = task_audit_input(
                paper, bundle, [], include_full_source=True
            )
            resumed_turn = task_audit_input(
                paper, bundle, [], include_full_source=False
            )
            self.assertIn("L000060: line 60", first_turn)
            self.assertNotIn("L000060: line 60", resumed_turn)
            self.assertIn("supplied in the first audit turn", resumed_turn)

    def test_normal_path_runs_one_round(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root)
            specs = [
                SolverSpec(
                    label,
                    ProviderConfig("x", "k", label, "responses", "high", 10, 10),
                )
                for label in ("a", "b")
            ]
            solver_result = {
                label: {
                    "task_status": "scorable",
                    "unscorable_reason": None,
                    "proof": "Proof.",
                    "usage": None,
                }
                for label in ("a", "b")
            }
            reviews = {
                "answer_a": {"validity_status": "valid_complete"},
                "answer_b": {"validity_status": "valid_complete"},
            }
            evaluations = {
                "answer_a": {"evaluation_status": "scored", "score": 10},
                "answer_b": {"evaluation_status": "scored", "score": 9},
            }
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            with (
                patch("paired_pipeline.run_all_solvers", return_value=solver_result),
                patch(
                    "paired_pipeline.run_paired_reviewer",
                    return_value=(reviews, None),
                ),
                patch(
                    "paired_pipeline.run_paired_evaluator",
                    return_value=(evaluations, None),
                ),
            ):
                result = run_paper(
                    paper, "run", root / "output", specs, agent, agent
                )
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["round_count"], 1)

    def test_solver_audit_only_skips_reviewer_and_evaluator(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root)
            specs = [
                SolverSpec(
                    label,
                    ProviderConfig("x", "k", label, "responses", "high", 10, 10),
                )
                for label in ("a", "b")
            ]
            solver_results = {
                label: {
                    "task_status": "scorable",
                    "unscorable_reason": None,
                    "proof": "Proof.",
                    "usage": None,
                }
                for label in ("a", "b")
            }
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            with (
                patch(
                    "paired_pipeline.run_all_solvers", return_value=solver_results
                ),
                patch("paired_pipeline.run_paired_reviewer") as reviewer,
                patch("paired_pipeline.run_paired_evaluator") as evaluator,
            ):
                result = run_paper(
                    paper,
                    "run",
                    root / "output",
                    specs,
                    agent,
                    agent,
                    solver_audit_only=True,
                )
            reviewer.assert_not_called()
            evaluator.assert_not_called()
            self.assertEqual(result["status"], "completed")
            self.assertTrue(result["evaluation_deferred"])
            self.assertEqual(
                result["solver_outcomes"], {"a": "scorable", "b": "scorable"}
            )

    def test_no_final_answer_receives_zero_without_blocking_other_models(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root)
            specs = [
                SolverSpec(
                    label,
                    ProviderConfig("x", "k", label, "responses", "high", 10, 10),
                )
                for label in ("empty", "answered")
            ]
            solver_results = {
                "empty": {
                    "task_status": "no_final_answer",
                    "unscorable_reason": None,
                    "proof": "",
                    "usage": {"output_tokens": 30_000},
                },
                "answered": {
                    "task_status": "scorable",
                    "unscorable_reason": None,
                    "proof": "Proof.",
                    "usage": {"output_tokens": 100},
                },
            }
            reviews = {"answer_a": {"validity_status": "valid_complete"}}
            evaluations = {
                "answer_a": {"evaluation_status": "scored", "score": 9}
            }
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            with (
                patch(
                    "paired_pipeline.run_all_solvers", return_value=solver_results
                ),
                patch(
                    "paired_pipeline.run_paired_reviewer",
                    return_value=(reviews, None),
                ) as reviewer,
                patch(
                    "paired_pipeline.run_paired_evaluator",
                    return_value=(evaluations, None),
                ),
            ):
                result = run_paper(
                    paper, "run", root / "output", specs, agent, agent
                )
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["scores"], {"empty": 0, "answered": 9})
            self.assertEqual(set(reviewer.call_args.args[1].values()), {"answered"})

    def test_invalid_solver_objection_retries_only_the_objecting_solver(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root, audit_ready=True)
            specs = [
                SolverSpec(
                    label,
                    ProviderConfig("x", "k", label, "responses", "high", 10, 10),
                )
                for label in ("objector", "answered")
            ]
            first_results = {
                "objector": {
                    "task_status": "unscorable",
                    "unscorable_reason": "Claimed task defect.",
                    "proof": "",
                    "usage": {"output_tokens": 100},
                    "terminal_score": None,
                },
                "answered": {
                    "task_status": "scorable",
                    "unscorable_reason": None,
                    "proof": "Original proof.",
                    "usage": {"output_tokens": 200},
                    "terminal_score": None,
                },
            }
            followup = {
                "objector": {
                    "task_status": "scorable",
                    "unscorable_reason": None,
                    "proof": "Follow-up proof.",
                    "usage": {"output_tokens": 300},
                    "terminal_score": None,
                }
            }
            audit = {"status": "invalid_objection"}
            reviews = {
                "answer_a": {"validity_status": "valid_complete"},
                "answer_b": {"validity_status": "valid_complete"},
            }
            evaluations = {
                "answer_a": {"evaluation_status": "scored", "score": 9},
                "answer_b": {"evaluation_status": "scored", "score": 9},
            }
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            audit_thread = Mock()
            with (
                patch(
                    "paired_pipeline.run_all_solvers", return_value=first_results
                ) as run_solvers,
                patch(
                    "paired_pipeline.run_invalid_objection_followups",
                    return_value=followup,
                ) as run_followups,
                patch(
                    "paired_pipeline.run_task_audit", return_value=(audit, None)
                ),
                patch(
                    "paired_pipeline.create_agent_thread",
                    return_value=audit_thread,
                ),
                patch(
                    "paired_pipeline.run_paired_reviewer",
                    return_value=(reviews, None),
                ) as reviewer,
                patch(
                    "paired_pipeline.run_paired_evaluator",
                    return_value=(evaluations, None),
                ),
            ):
                result = run_paper(
                    paper, "run", root / "output", specs, agent, agent
                )
            run_solvers.assert_called_once()
            self.assertEqual(run_followups.call_args.args[1], {"objector"})
            self.assertEqual(
                reviewer.call_args.args[2]["answered"]["proof"], "Original proof."
            )
            self.assertEqual(
                reviewer.call_args.args[2]["objector"]["proof"], "Follow-up proof."
            )
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["round_count"], 1)
            self.assertEqual(result["validation_feedback_count"], 1)
            self.assertEqual(
                result["solver_usage_by_model"]["objector"]["output_tokens"],
                400,
            )
            self.assertEqual(
                result["solver_usage_by_model"]["answered"]["output_tokens"],
                200,
            )

    def test_repeated_invalid_objection_receives_zero_without_rerunning_peers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root, audit_ready=True)
            specs = [
                SolverSpec(
                    label,
                    ProviderConfig("x", "k", label, "responses", "high", 10, 10),
                )
                for label in ("objector", "answered")
            ]
            first_results = {
                "objector": {
                    "task_status": "unscorable",
                    "unscorable_reason": "Claimed task defect.",
                    "proof": "",
                    "usage": None,
                    "terminal_score": None,
                },
                "answered": {
                    "task_status": "scorable",
                    "unscorable_reason": None,
                    "proof": "Original proof.",
                    "usage": None,
                    "terminal_score": None,
                },
            }
            followup = {
                "objector": {
                    "task_status": "unscorable",
                    "unscorable_reason": "Repeated objection.",
                    "proof": "",
                    "usage": None,
                    "terminal_score": 0,
                }
            }
            reviews = {"answer_b": {"validity_status": "valid_complete"}}
            evaluations = {
                "answer_b": {"evaluation_status": "scored", "score": 8}
            }
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            with (
                patch(
                    "paired_pipeline.run_all_solvers", return_value=first_results
                ) as run_solvers,
                patch(
                    "paired_pipeline.anonymous_assignment",
                    return_value={"answer_a": "objector", "answer_b": "answered"},
                ),
                patch(
                    "paired_pipeline.run_invalid_objection_followups",
                    return_value=followup,
                ),
                patch(
                    "paired_pipeline.run_task_audit",
                    return_value=({"status": "invalid_objection"}, None),
                ),
                patch(
                    "paired_pipeline.create_agent_thread", return_value=Mock()
                ),
                patch(
                    "paired_pipeline.run_paired_reviewer",
                    return_value=(reviews, None),
                ) as reviewer,
                patch(
                    "paired_pipeline.run_paired_evaluator",
                    return_value=(evaluations, None),
                ),
            ):
                result = run_paper(
                    paper, "run", root / "output", specs, agent, agent
                )
            run_solvers.assert_called_once()
            self.assertEqual(set(reviewer.call_args.args[1].values()), {"answered"})
            self.assertEqual(result["scores"], {"objector": 0, "answered": 8})
            self.assertEqual(result["round_count"], 1)

    def test_evaluator_contract_retry_uses_the_same_thread(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            version = root / "task_versions/revision_0"
            version.mkdir(parents=True)
            for name, content in (
                ("task.md", "# Task\nProve 1=1.\n"),
                ("proof_ground_truth.md", "# Proof\nTrivial.\n"),
                ("rubric.md", "# Rubric\nOne step.\n"),
                ("provenance.json", "{}\n"),
            ):
                (version / name).write_text(content)
            round_dir = root / "round"
            (round_dir / "models/answered").mkdir(parents=True)
            envelope = {
                "answer_reports": [
                    {"answer_id": "answer_a", "evaluation": {"score": 3}}
                ]
            }
            thread = Mock()
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            with (
                patch(
                    "paired_pipeline.create_agent_thread", return_value=thread
                ),
                patch(
                    "paired_pipeline.run_json_agent",
                    side_effect=(
                        (envelope, {"output_tokens": 2}, {"resumed": False}),
                        (envelope, {"output_tokens": 3}, {"resumed": True}),
                    ),
                ) as run_agent,
                patch("paired_pipeline.validate_schema"),
                patch(
                    "paired_pipeline.validate_evaluation",
                    side_effect=(
                        ValueError(
                            "A-C3 receives credit through an invalid predecessor: A-C2"
                        ),
                        None,
                    ),
                ),
            ):
                evaluations, usage = run_paired_evaluator(
                    ArtifactBundle(0, version),
                    {"answer_a": "answered"},
                    {"answered": {"proof": "Proof."}},
                    {"answer_a": {"validity_status": "incomplete_major_gap"}},
                    round_dir,
                    agent,
                )
            self.assertEqual(evaluations["answer_a"]["score"], 3)
            self.assertEqual(usage, {"output_tokens": 5})
            self.assertEqual(run_agent.call_count, 2)
            self.assertIs(run_agent.call_args_list[0].kwargs["thread"], thread)
            self.assertIs(run_agent.call_args_list[1].kwargs["thread"], thread)
            self.assertIn(
                "invalid predecessor", run_agent.call_args_list[1].kwargs["inputs"]
            )
            thread.close.assert_called_once()
            retry_audit = json.loads(
                (round_dir / "paired_evaluator_audit.json").read_text()
            )
            self.assertEqual(retry_audit["contract_retry_count"], 1)

    def test_reviewer_contract_retry_uses_the_same_thread(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            version = root / "task_versions/revision_0"
            version.mkdir(parents=True)
            for name, content in (
                ("task.md", "# Task\nProve 1=1.\n"),
                ("proof_ground_truth.md", "# Proof\nTrivial.\n"),
                ("rubric.md", "# Rubric\nOne step.\n"),
                ("provenance.json", "{}\n"),
            ):
                (version / name).write_text(content)
            round_dir = root / "round"
            (round_dir / "models/answered").mkdir(parents=True)
            envelope = {
                "answer_reports": [
                    {
                        "answer_id": "answer_a",
                        "report": {"validity_status": "incomplete_major_gap"},
                    }
                ]
            }
            thread = Mock()
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            with (
                patch(
                    "paired_pipeline.create_agent_thread", return_value=thread
                ),
                patch(
                    "paired_pipeline.run_json_agent",
                    side_effect=(
                        (envelope, {"output_tokens": 2}, {"resumed": False}),
                        (envelope, {"output_tokens": 3}, {"resumed": True}),
                        (envelope, {"output_tokens": 4}, {"resumed": True}),
                    ),
                ) as run_agent,
                patch("paired_pipeline.validate_schema"),
                patch(
                    "paired_pipeline.validate_reviewer_report",
                    side_effect=(
                        ValueError(
                            "break_found requires a linked verified major or blocking finding"
                        ),
                        ValueError(
                            "minor status cannot contain a broken proof step"
                        ),
                        None,
                    ),
                ),
            ):
                reports, usage = run_paired_reviewer(
                    ArtifactBundle(0, version),
                    {"answer_a": "answered"},
                    {"answered": {"proof": "Proof."}},
                    round_dir,
                    agent,
                )
            self.assertEqual(
                reports["answer_a"]["validity_status"],
                "incomplete_major_gap",
            )
            self.assertEqual(usage, {"output_tokens": 9})
            self.assertEqual(run_agent.call_count, 3)
            self.assertIs(run_agent.call_args_list[0].kwargs["thread"], thread)
            self.assertIs(run_agent.call_args_list[1].kwargs["thread"], thread)
            self.assertIs(run_agent.call_args_list[2].kwargs["thread"], thread)
            self.assertIn(
                "break_found", run_agent.call_args_list[1].kwargs["inputs"]
            )
            self.assertIn(
                "minor status", run_agent.call_args_list[2].kwargs["inputs"]
            )
            thread.close.assert_called_once()
            retry_audit = json.loads(
                (round_dir / "paired_reviewer_audit.json").read_text()
            )
            self.assertEqual(retry_audit["contract_retry_count"], 2)

    def test_two_audits_resume_one_thread_and_rerun_every_solver(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paper = self.make_paper(root, audit_ready=True)
            specs = [
                SolverSpec(
                    label,
                    ProviderConfig("x", "k", label, "responses", "high", 10, 10),
                )
                for label in ("a", "b", "c", "d", "e", "f", "g", "h")
            ]
            first_round = {
                label: {
                    "task_status": "unscorable"
                    if label in {"a", "b"}
                    else "scorable",
                    "unscorable_reason": (
                        "The target omits an assumption."
                        if label == "a"
                        else "The stated endpoint violates the conclusion."
                    )
                    if label in {"a", "b"}
                    else None,
                    "proof": "Proof.",
                    "usage": None,
                }
                for label in ("a", "b", "c", "d", "e", "f", "g", "h")
            }
            second_round = {
                label: {
                    "task_status": "unscorable" if label == "c" else "scorable",
                    "unscorable_reason": (
                        "The revised task still omits one definition."
                        if label == "c"
                        else None
                    ),
                    "proof": "Proof.",
                    "usage": None,
                }
                for label in ("a", "b", "c", "d", "e", "f", "g", "h")
            }
            third_round = {
                label: {
                    "task_status": "scorable",
                    "unscorable_reason": None,
                    "proof": "Proof.",
                    "usage": None,
                }
                for label in ("a", "b", "c", "d", "e", "f", "g", "h")
            }
            reviews = {
                answer_id: {"validity_status": "valid_complete"}
                for answer_id in ANSWER_IDS
            }
            evaluations = {
                answer_id: {"evaluation_status": "scored", "score": 10}
                for answer_id in ANSWER_IDS
            }
            first_audit = {
                "status": "formalization_error_fixed",
                "replacements": {
                    "task_md": "# Task\nProve 1=1 under the stated assumptions.\n",
                    "proof_ground_truth_md": None,
                    "rubric_md": None,
                    "provenance": None,
                },
                "corrected_material_records": None,
            }
            second_audit = {
                **first_audit,
                "replacements": {
                    **first_audit["replacements"],
                    "task_md": "# Task\nProve 1=1 under the fully stated assumptions.\n",
                },
            }
            agent = AgentConfig(Path("."), "codex", "judge", "high", 10)
            audit_thread = Mock()
            with (
                patch(
                    "paired_pipeline.run_all_solvers",
                    side_effect=(first_round, second_round, third_round),
                ) as run_solvers,
                patch(
                    "paired_pipeline.run_task_audit",
                    side_effect=((first_audit, None), (second_audit, None)),
                ) as run_audit,
                patch(
                    "paired_pipeline.create_agent_thread",
                    return_value=audit_thread,
                ) as create_thread,
                patch(
                    "paired_pipeline.run_paired_reviewer",
                    return_value=(reviews, None),
                ),
                patch(
                    "paired_pipeline.run_paired_evaluator",
                    return_value=(evaluations, None),
                ),
            ):
                result = run_paper(
                    paper, "run", root / "output", specs, agent, agent
                )
            self.assertEqual(run_solvers.call_count, 3)
            self.assertEqual(run_audit.call_count, 2)
            create_thread.assert_called_once()
            self.assertTrue(
                all(call.args[5] is audit_thread for call in run_audit.call_args_list)
            )
            audit_thread.close.assert_called_once()
            objections = run_audit.call_args_list[0].args[2]
            self.assertEqual(len(objections), 2)
            self.assertEqual(
                {item["reason"] for item in objections},
                {
                    "The target omits an assumption.",
                    "The stated endpoint violates the conclusion.",
                },
            )
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["round_count"], 3)
            self.assertEqual(result["task_revision"], 2)
            self.assertEqual(result["validation_feedback_count"], 2)
            self.assertEqual(
                result["solver_usage_by_model"],
                {label: {} for label in ("a", "b", "c", "d", "e", "f", "g", "h")},
            )


if __name__ == "__main__":
    unittest.main()
