from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Protocol


WORKFLOW_ROOT = Path(__file__).resolve().parents[2]
SOLVER = WORKFLOW_ROOT / "proof_experiment/llm_solver"
REVIEWER = WORKFLOW_ROOT / "reviewer_and_evaluator/reviewer"
EVALUATOR = WORKFLOW_ROOT / "reviewer_and_evaluator/evaluator"
EXPERIMENT_RUNTIME = WORKFLOW_ROOT / "runtime_support/experiment"


class ValidationBackend(Protocol):
    def run_solver(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
    ) -> dict[str, Any]: ...

    def run_reviewer(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
    ) -> dict[str, Any]: ...

    def run_evaluator(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
        evaluator_output_dir: Path,
        *,
        prompt_path: Path | None = None,
    ) -> dict[str, Any]: ...


def parse_validation_answer(answer: str) -> tuple[str, str]:
    match = re.search(
        r"(?im)^\s*-\s*\*\*Task status:\*\*\s*`?(scorable|unscorable)`?\s*$",
        answer,
    )
    if match is None:
        raise ValueError("solver answer lacks a scorable/unscorable Task status")
    status = match.group(1).lower()
    reason_match = re.search(
        r"(?im)^\s*-\s*\*\*Unscorable reason:\*\*\s*(.*)$",
        answer,
    )
    reason = reason_match.group(1).strip().strip("`") if reason_match else ""
    if status == "unscorable" and not reason:
        raise ValueError("an unscorable solver result requires a reason")
    return status, reason


class ScriptedValidation:
    def __init__(
        self,
        solver_results: list[dict[str, Any]],
        reviewer_results: list[dict[str, Any]],
    ) -> None:
        self.solver_results = list(solver_results)
        self.reviewer_results = list(reviewer_results)
        self.calls = 0
        self.reviewer_calls = 0
        self.evaluator_calls = 0
        self.events: list[str] = []

    def run_solver(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
    ) -> dict[str, Any]:
        if not self.solver_results:
            raise RuntimeError("no scripted solver result remains")
        self.calls += 1
        self.events.append("solver")
        solver_result = self.solver_results.pop(0)
        solver_output_dir.mkdir(parents=True, exist_ok=True)
        (solver_output_dir / "answer.md").write_text(
            solver_result["answer"], encoding="utf-8"
        )
        (solver_output_dir / "validation.json").write_text(
            json.dumps(solver_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return solver_result

    def run_reviewer(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
    ) -> dict[str, Any]:
        if not self.reviewer_results:
            raise RuntimeError("no scripted reviewer result remains")
        self.reviewer_calls += 1
        self.events.append("reviewer")
        reviewer_result = self.reviewer_results.pop(0)
        reviewer_output_dir.mkdir(parents=True, exist_ok=True)
        (reviewer_output_dir / "review.json").write_text(
            json.dumps(reviewer_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return reviewer_result

    def run_evaluator(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
        evaluator_output_dir: Path,
        *,
        prompt_path: Path | None = None,
    ) -> dict[str, Any]:
        self.evaluator_calls += 1
        self.events.append("evaluator")
        evaluator_output_dir.mkdir(parents=True, exist_ok=True)
        evaluation_result = {
            "evaluation_status": "scored",
            "score": 10,
            "verdict": "fully_correct",
            "summary": "Scripted evaluation.",
        }
        (evaluator_output_dir / "evaluation.json").write_text(
            json.dumps(evaluation_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        evaluation = {
            "result": evaluation_result,
            "usage": None,
            "exposures": [],
            "protocol": "scripted_reference_evaluator",
        }
        return evaluation


class ExperimentValidation:
    """Run solver, reviewer, and evaluator as interruptible isolated stages."""

    def __init__(
        self,
        *,
        api_profile: Path,
        model: str,
        reasoning_effort: str,
        timeout_seconds: int = 1800,
        solver_env_file: Path | None = None,
        local_agent_auth: bool = False,
        codex_bin: str = "codex",
    ) -> None:
        self.api_profile = api_profile.resolve()
        self.model = model
        self.reasoning_effort = reasoning_effort
        self.timeout_seconds = timeout_seconds
        self.local_agent_auth = local_agent_auth
        self.codex_bin = codex_bin
        self.solver_env_file = (
            solver_env_file.resolve()
            if solver_env_file is not None
            else (WORKFLOW_ROOT / ".runtime/llm.env").resolve()
        )

    @contextmanager
    def _workspace(self, paper_id: str, task_path: Path):
        with tempfile.TemporaryDirectory(prefix="data-v2-validation-") as temporary:
            root = Path(temporary)
            compatibility_task = (
                root
                / paper_id
                / "selected_theorems/theorem_001/public_tasks/task_prove_theorem.md"
            )
            compatibility_task.parent.mkdir(parents=True)
            shutil.copy2(task_path, compatibility_task)
            theorem_root = compatibility_task.parent.parent
            private_gt = theorem_root / "private_gt"
            private_gt.mkdir()
            formalization = task_path.parent
            task_text = task_path.read_text(encoding="utf-8")
            for name in (
                "theorem_statement_original.md",
                "theorem_statement_sanitized.md",
                "assumptions.md",
            ):
                (private_gt / name).write_text(task_text, encoding="utf-8")
            shutil.copy2(
                formalization / "proof_ground_truth.md",
                private_gt / "proof_ground_truth.md",
            )
            shutil.copy2(
                formalization / "rubric.md",
                private_gt / "rubric_prove_theorem.md",
            )
            provenance = (formalization / "provenance.json").read_text(
                encoding="utf-8"
            )
            (private_gt / "citations.md").write_text(
                "# Private Provenance And Citations\n\n```json\n"
                + provenance.rstrip()
                + "\n```\n",
                encoding="utf-8",
            )
            private_files = [
                "private_gt/theorem_statement_original.md",
                "private_gt/theorem_statement_sanitized.md",
                "private_gt/assumptions.md",
                "private_gt/proof_ground_truth.md",
                "private_gt/citations.md",
                "private_gt/rubric_prove_theorem.md",
            ]
            (theorem_root / "task_metadata.json").write_text(
                json.dumps(
                    {
                        "schema_version": "2.0",
                        "paper_id": paper_id,
                        "theorem_id": "theorem_001",
                        "visibility": "private_metadata",
                        "split": "dev",
                        "status": "ready",
                        "private_gt_files": private_files,
                        "tasks": [
                            {
                                "task_id": "task_prove_theorem",
                                "task_type": "prove_theorem",
                                "public_task_file": "public_tasks/task_prove_theorem.md",
                                "exposure_policy": "single_public_task_file_only",
                                "leakage_audit_status": "pass",
                                "evaluator_private_files": private_files,
                                "notes": "Contribution-level compatibility package.",
                            }
                        ],
                    },
                    ensure_ascii=False,
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            runs_root = root / "runs"
            run_id = "validation_" + uuid.uuid4().hex[:12]
            self._run_checked(
                [
                    sys.executable,
                    str(EXPERIMENT_RUNTIME / "init_run.py"),
                    "--run-id",
                    run_id,
                    "--runs-root",
                    str(runs_root),
                ],
                "validation run initialization",
            )
            theorem_output = runs_root / run_id / paper_id / "theorem_001"
            yield root, compatibility_task, runs_root, run_id, theorem_output

    @staticmethod
    def _run_checked(command: list[str], label: str) -> None:
        process = subprocess.run(
            command,
            check=False,
            cwd=WORKSPACE_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if process.returncode != 0:
            detail = process.stderr[-4000:] or process.stdout[-4000:]
            raise RuntimeError(f"{label} failed: {detail}")

    @staticmethod
    def _stage_audit(
        runs_root: Path, run_id: str, paper_id: str, stage: str
    ) -> dict[str, Any]:
        run_record = json.loads(
            (runs_root / run_id / "run.json").read_text(encoding="utf-8")
        )
        return (
            run_record.get("tasks", {})
            .get(f"{paper_id}/theorem_001", {})
            .get(stage, {})
        )

    def _agent_options(self) -> list[str]:
        options = [
            "--codex-bin",
            self.codex_bin,
            "--api-profile",
            str(self.api_profile),
            "--model",
            self.model,
            "--reasoning-effort",
            self.reasoning_effort,
            "--timeout-seconds",
            str(self.timeout_seconds),
        ]
        if self.local_agent_auth:
            options.append("--local-auth")
        return options

    def run_solver(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
    ) -> dict[str, Any]:
        solver_output_dir.mkdir(parents=True, exist_ok=True)
        with self._workspace(paper_id, task_path) as (
            _,
            compatibility_task,
            runs_root,
            run_id,
            theorem_output,
        ):
            self._run_checked(
                [
                    sys.executable,
                    str(SOLVER / "run_llm_baseline.py"),
                    "--task",
                    str(compatibility_task),
                    "--run-id",
                    run_id,
                    "--runs-root",
                    str(runs_root),
                    "--env-file",
                    str(self.solver_env_file),
                ],
                "bare-model solver",
            )
            answer = (theorem_output / "answer.md").read_text(encoding="utf-8")
            status, reason = parse_validation_answer(answer)
            audit = self._stage_audit(runs_root, run_id, paper_id, "solver")
            result = {
                "status": status,
                "reason": reason,
                "answer": answer,
                "usage": audit.get("usage"),
                "protocol": "experiments.llm_solver.single_request_no_tools",
            }
            (solver_output_dir / "answer.md").write_text(answer, encoding="utf-8")
            (solver_output_dir / "validation.json").write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            return result

    def run_reviewer(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
    ) -> dict[str, Any]:
        reviewer_output_dir.mkdir(parents=True, exist_ok=True)
        answer_path = solver_output_dir / "answer.md"
        if not answer_path.is_file():
            raise FileNotFoundError(answer_path)
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
            command.extend(self._agent_options())
            self._run_checked(command, "validity reviewer")
            report = json.loads(
                (theorem_output / "validity_report.json").read_text(encoding="utf-8")
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
            (reviewer_output_dir / "review.json").write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            return result

    def run_evaluator(
        self,
        paper_id: str,
        task_path: Path,
        solver_output_dir: Path,
        reviewer_output_dir: Path,
        evaluator_output_dir: Path,
        *,
        prompt_path: Path | None = None,
    ) -> dict[str, Any]:
        evaluator_output_dir.mkdir(parents=True, exist_ok=True)
        answer_path = solver_output_dir / "answer.md"
        reviewer_path = reviewer_output_dir / "review.json"
        if not answer_path.is_file():
            raise FileNotFoundError(answer_path)
        if not reviewer_path.is_file():
            raise FileNotFoundError(reviewer_path)
        reviewer_result = json.loads(reviewer_path.read_text(encoding="utf-8"))
        if reviewer_result.get("status") != "scorable":
            raise ValueError("evaluator requires a scorable reviewer result")
        with self._workspace(paper_id, task_path) as (
            root,
            compatibility_task,
            runs_root,
            run_id,
            theorem_output,
        ):
            validity_path = root / "validity_report.json"
            validity_path.write_text(
                json.dumps(reviewer_result["report"], ensure_ascii=False, indent=2)
                + "\n",
                encoding="utf-8",
            )
            command = [
                sys.executable,
                str(EVALUATOR / "run_evaluator.py"),
                "--task",
                str(compatibility_task),
                "--answer",
                str(answer_path),
                "--validity-report",
                str(validity_path),
                "--run-id",
                run_id,
                "--runs-root",
                str(runs_root),
            ]
            if prompt_path is not None:
                command.extend(["--prompt", str(prompt_path)])
            command.extend(self._agent_options())
            self._run_checked(command, "reference evaluator")
            evaluation_result = json.loads(
                (theorem_output / "evaluation.json").read_text(encoding="utf-8")
            )
            audit = self._stage_audit(runs_root, run_id, paper_id, "evaluator")
            (evaluator_output_dir / "evaluation.json").write_text(
                json.dumps(evaluation_result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            return {
                "result": evaluation_result,
                "usage": audit.get("usage"),
                "exposures": audit.get("exposures", []),
                "protocol": "experiments.evaluator.reference_scorer",
            }
