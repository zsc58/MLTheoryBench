from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from contracts import validate_evaluation, validate_reviewer_report
from bare_model import ProviderConfig, build_payload
from freeze_selection import freeze_selection
from support import normalize_usage


def load_schema(name: str) -> dict:
    return json.loads((MODULE_ROOT / "schemas" / name).read_text(encoding="utf-8"))


def reviewer_report() -> dict:
    return {
        "validity_status": "valid_complete",
        "theorem_contract": {
            "assumptions": ["x is real"],
            "target": "x^2 is nonnegative",
            "quantifiers_and_scope": ["for every real x"],
        },
        "proof_steps": [
            {
                "step_id": "S1",
                "claim": "x^2 is nonnegative",
                "depends_on": [],
                "support_status": "established",
                "reason": "A square of a real number is nonnegative.",
            }
        ],
        "findings": [],
        "adversarial_checks": [
            {
                "target": "sign",
                "test": "test negative x",
                "result": "attack_neutralized",
                "reason": "squaring removes the sign",
                "related_finding_ids": [],
            }
        ],
        "summary": "Complete.",
    }


class FreezeSelectionTests(unittest.TestCase):
    def test_freezes_only_completed_papers(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for paper_id, status in (
                ("paper_2026_001", "completed"),
                ("paper_2026_002", "stopped"),
            ):
                formalization = root / "papers" / paper_id / "formalization"
                formalization.mkdir(parents=True)
                for name in (
                    "task.md",
                    "proof_ground_truth.md",
                    "rubric.md",
                    "provenance.json",
                ):
                    (formalization / name).write_text(name, encoding="utf-8")
                (formalization / "status.json").write_text(
                    json.dumps({"status": status}), encoding="utf-8"
                )
            selection = freeze_selection(root)
            self.assertEqual(selection["paper_count"], 1)
            self.assertEqual(list(selection["papers"]), ["paper_2026_001"])
            self.assertEqual(
                len(selection["papers"]["paper_2026_001"]["files"]["task.md"]["sha256"]),
                64,
            )


class ContractTests(unittest.TestCase):
    def test_valid_complete_reviewer_and_evaluator(self) -> None:
        review = validate_reviewer_report(
            reviewer_report(), load_schema("fixed_task_reviewer.schema.json")
        )
        evaluation = {
            "score": 10,
            "verdict": "fully_correct",
            "validity_review_resolution": {
                "initial_status": "valid_complete",
                "final_status": "valid_complete",
                "finding_resolutions": [],
            },
            "core_step_evaluations": [
                {
                    "step_id": "C1",
                    "step": "Show the square is nonnegative.",
                    "origin": "rubric",
                    "depends_on": [],
                    "points_available": 10,
                    "points_awarded": 10,
                    "conclusion_status": "correct",
                    "proof_status": "correct",
                    "credit": "full",
                    "dependency_analysis": "No predecessor.",
                    "reason": "Established.",
                }
            ],
            "added_core_steps": [],
            "assumption_and_tool_checks": [],
            "mathematical_errors": [],
            "alternative_proof": False,
            "justification": "Complete and correct.",
        }
        validate_evaluation(
            evaluation,
            load_schema("fixed_task_evaluator.schema.json"),
            review,
        )

    def test_rejects_score_status_mismatch(self) -> None:
        review = reviewer_report()
        evaluation = {
            "score": 9,
            "verdict": "minor_repair",
            "validity_review_resolution": {
                "initial_status": "valid_complete",
                "final_status": "valid_complete",
                "finding_resolutions": [],
            },
            "core_step_evaluations": [
                {
                    "step_id": "C1",
                    "step": "Step",
                    "origin": "rubric",
                    "depends_on": [],
                    "points_available": 10,
                    "points_awarded": 9,
                    "conclusion_status": "correct",
                    "proof_status": "partial",
                    "credit": "partial",
                    "dependency_analysis": "None.",
                    "reason": "Minor omission.",
                }
            ],
            "added_core_steps": [],
            "assumption_and_tool_checks": [],
            "mathematical_errors": [],
            "alternative_proof": False,
            "justification": "Minor omission.",
        }
        with self.assertRaisesRegex(ValueError, "valid_complete requires score 10"):
            validate_evaluation(
                evaluation,
                load_schema("fixed_task_evaluator.schema.json"),
                review,
            )


class ProviderCompatibilityTests(unittest.TestCase):
    def test_chat_payload_explicitly_enables_thinking(self) -> None:
        config = ProviderConfig(
            base_url="https://example.invalid/v1",
            api_key="test-key",
            model="reasoning-model",
            wire_api="chat_completions",
            reasoning_effort="high",
            max_output_tokens=1234,
            timeout_seconds=60,
        )
        payload = build_payload(config, "system", "user")
        self.assertEqual(payload["max_tokens"], 1234)
        self.assertEqual(payload["reasoning_effort"], "high")
        self.assertEqual(payload["thinking"], {"type": "enabled"})

    def test_normalizes_chat_completion_usage(self) -> None:
        usage = normalize_usage(
            {
                "prompt_tokens": 100,
                "completion_tokens": 40,
                "total_tokens": 140,
                "prompt_tokens_details": {"cached_tokens": 30},
                "completion_tokens_details": {"reasoning_tokens": 25},
            }
        )
        self.assertEqual(
            usage,
            {
                "input_tokens": 100,
                "cached_input_tokens": 30,
                "non_cached_input_tokens": 70,
                "output_tokens": 40,
                "reasoning_output_tokens": 25,
                "total_tokens": 140,
            },
        )


if __name__ == "__main__":
    unittest.main()
