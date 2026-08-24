from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable

from solver_bridge import EVALUATOR, REVIEWER, ExperimentValidation


VALIDITY_REVIEWER_PROMPT = (
    REVIEWER / "system_prompt.md"
)
REFERENCE_EVALUATOR_PROMPT = (
    EVALUATOR / "system_prompt.md"
)
STAGE3_CONTRACT_RULES = """
## Stage 3 Output-Contract Consistency

Keep the mathematical judgment unchanged, but make all JSON fields consistent:

- `valid_complete` permits no active finding and no `partial`, `unsupported`, or
  `incorrect` proof step.
- `valid_with_minor_issue` requires at least one active `minor` finding, no active
  `major` or `blocking` finding, and no `unsupported` or `incorrect` proof step.
- `incomplete_major_gap` requires an active `major` or `blocking` finding, or a
  `partial`, `unsupported`, or `incorrect` proof step.
- `target_suspected_invalid` requires a `verified` `blocking` finding.
- Every adversarial check marked `break_found` must reference at least one
  `verified` finding of severity `major` or `blocking` through
  `related_finding_ids`.
- A `resolved_nonissue` finding has severity `none`; every active finding has a
  non-`none` severity.

Do not weaken, strengthen, or silently repair the review merely to satisfy this
contract. Choose the status, findings, proof-step support labels, and links that
faithfully encode the same substantive judgment.
"""


class Stage3ExperimentValidation(ExperimentValidation):
    """Retry transient reviewer/evaluator contract failures once."""

    @staticmethod
    def _run_with_contract_retry(
        operation: Callable[[], dict[str, Any]], output_dir: Path, stage: str
    ) -> dict[str, Any]:
        failures: list[str] = []
        for attempt in range(2):
            try:
                result = operation()
                if failures:
                    result["contract_retry_count"] = len(failures)
                    (output_dir / "contract_retry.json").write_text(
                        json.dumps(
                            {"stage": stage, "errors": failures},
                            ensure_ascii=False,
                            indent=2,
                        )
                        + "\n",
                        encoding="utf-8",
                    )
                return result
            except RuntimeError as error:
                failures.append(str(error))
                if attempt == 1:
                    raise
        raise AssertionError("unreachable")

    def run_reviewer(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
    ) -> dict[str, Any]:
        reviewer_output_dir.mkdir(parents=True, exist_ok=True)
        (reviewer_output_dir / "contract_retry_prompt.md").unlink(missing_ok=True)
        answer_path = solver_output_dir / "answer.md"
        if not answer_path.is_file():
            raise FileNotFoundError(answer_path)

        failures: list[str] = []
        stage3_prompt = reviewer_output_dir / "stage3_reviewer_prompt.md"
        for attempt in range(2):
            with self._workspace(paper_id, task_path) as (
                _,
                compatibility_task,
                runs_root,
                run_id,
                theorem_output,
            ):
                command = [
                    sys.executable,
                    str(REVIEWER / "run_reviewer.py"),
                    "--task",
                    str(compatibility_task),
                    "--answer",
                    str(answer_path),
                    "--run-id",
                    run_id,
                    "--runs-root",
                    str(runs_root),
                ]
                prompt_text = (
                    VALIDITY_REVIEWER_PROMPT.read_text(encoding="utf-8")
                    + "\n\n"
                    + STAGE3_CONTRACT_RULES.strip()
                    + "\n"
                )
                if attempt:
                    feedback = failures[-1][-2000:]
                    prompt_text += (
                        "\n## Output Contract Retry\n\n"
                        + "The previous response was rejected by the output-contract "
                        + "validator. Correct the JSON consistency issue without "
                        + "silently changing the mathematical review. Validator "
                        + f"feedback:\n\n```text\n{feedback}\n```\n"
                    )
                stage3_prompt.write_text(prompt_text, encoding="utf-8")
                command.extend(["--prompt", str(stage3_prompt)])
                command.extend(self._agent_options())
                try:
                    self._run_checked(command, "validity reviewer")
                except RuntimeError as error:
                    failures.append(str(error))
                    if attempt == 1:
                        raise
                    continue

                report = json.loads(
                    (theorem_output / "validity_report.json").read_text(
                        encoding="utf-8"
                    )
                )
                audit = self._stage_audit(
                    runs_root, run_id, paper_id, "validity_reviewer"
                )
                result = {
                    "status": (
                        "unscorable"
                        if report["validity_status"] == "target_suspected_invalid"
                        else "scorable"
                    ),
                    "report": report,
                    "usage": audit.get("usage"),
                    "protocol": "experiments.evaluator.validity_reviewer",
                    "exposures": audit.get("exposures", []),
                }
                if failures:
                    result["contract_retry_count"] = len(failures)
                    (reviewer_output_dir / "contract_retry.json").write_text(
                        json.dumps(
                            {"stage": "reviewer", "errors": failures},
                            ensure_ascii=False,
                            indent=2,
                        )
                        + "\n",
                        encoding="utf-8",
                    )
                (reviewer_output_dir / "review.json").write_text(
                    json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                stage3_prompt.unlink(missing_ok=True)
                return result
        raise AssertionError("unreachable")

    def run_evaluator(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
        evaluator_output_dir: Path,
    ) -> dict[str, Any]:
        evaluator_output_dir.mkdir(parents=True, exist_ok=True)
        retry_prompt = evaluator_output_dir / "contract_retry_prompt.md"
        retry_prompt.unlink(missing_ok=True)
        failures: list[str] = []
        for attempt in range(2):
            prompt_path: Path | None = None
            if attempt:
                feedback = failures[-1][-2000:]
                retry_prompt.write_text(
                    REFERENCE_EVALUATOR_PROMPT.read_text(encoding="utf-8")
                    + "\n\n## Output Contract Retry\n\n"
                    + "The previous response was rejected by the deterministic "
                    + "output validator. Preserve the mathematical judgment and "
                    + "correct only the JSON consistency error. In particular, a "
                    + "finding resolved as `confirmed` must preserve the validity "
                    + "reviewer's original severity, except that `major` may be "
                    + "upgraded to `blocking` when the private references establish "
                    + "that the same defect makes the target unscorable. Explain that "
                    + "target-level attribution precisely. Validator feedback:\n\n"
                    + f"```text\n{feedback}\n```\n",
                    encoding="utf-8",
                )
                prompt_path = retry_prompt
            try:
                result = super().run_evaluator(
                    paper_id,
                    task_path,
                    solver_output_dir,
                    reviewer_output_dir,
                    evaluator_output_dir,
                    prompt_path=prompt_path,
                )
            except RuntimeError as error:
                failures.append(str(error))
                if attempt == 1:
                    raise
                continue
            if failures:
                result["contract_retry_count"] = len(failures)
                (evaluator_output_dir / "contract_retry.json").write_text(
                    json.dumps(
                        {"stage": "evaluator", "errors": failures},
                        ensure_ascii=False,
                        indent=2,
                    )
                    + "\n",
                    encoding="utf-8",
                )
            retry_prompt.unlink(missing_ok=True)
            return result
        raise AssertionError("unreachable")
