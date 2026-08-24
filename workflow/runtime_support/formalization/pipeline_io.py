from __future__ import annotations

import json
import hashlib
import re
import shutil
import tempfile
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from agent_backend import AgentBackend, AgentRequest
from base_contracts import filtered_reason, load_schema, validate_contract
from solver_bridge import ValidationBackend


WORKFLOW_ROOT = Path(__file__).resolve().parents[2]
PROMPT_DIR = WORKFLOW_ROOT / "data_preparation/prompts"
FORMALIZER_PROMPT = PROMPT_DIR / "thread_b_turn1_compile.md"
TRIAGE_PROMPT = PROMPT_DIR / "thread_a_turn1_triage.md"
FORMALIZATION_DRAFT_PROMPT = PROMPT_DIR / "thread_a_turn3_source_audit.md"
TRIAGE_AUDIT_PROMPT = PROMPT_DIR / "thread_a_triage_audit.md"
FORMALIZATION_AUDIT_PROMPT = PROMPT_DIR / "thread_b_turn2_artifact_audit.md"
FORMALIZATION_REVISION_PROMPT = PROMPT_DIR / "thread_b_revision.md"
FORMALIZATION_TEMPLATE_DIR = WORKFLOW_ROOT / "data_preparation/templates"
MAX_SELF_AUDIT_REPAIRS = 2
MAX_VALIDATION_FEEDBACK_RETURNS = 2


@dataclass(frozen=True)
class PipelineResult:
    paper_id: str
    status: str
    revision_count: int
    stop_reason: str | None


def atomic_write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as handle:
        handle.write(value.rstrip() + "\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def exposed_file_records(paths: tuple[str, ...]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for raw_path in paths:
        path = Path(raw_path).resolve()
        files = sorted(item for item in path.rglob("*") if item.is_file()) if path.is_dir() else [path]
        for item in files:
            records.append(
                {
                    "path": str(item),
                    "sha256": sha256_file(item),
                    "bytes": item.stat().st_size,
                }
            )
    return records


def record_agent_call(
    paper_dir: Path,
    request: AgentRequest,
    result: dict[str, Any],
    additional_exposed_paths: tuple[str, ...] = (),
) -> None:
    path = paper_dir / "pipeline_manifest.json"
    manifest = (
        json.loads(path.read_text(encoding="utf-8"))
        if path.is_file()
        else {"paper_id": paper_dir.name, "calls": []}
    )
    manifest["calls"].append(
        {
            "role": request.role,
            "phase": request.phase,
            "session_id": result.get("session_id"),
            "turn_id": result.get("turn_id"),
            "resumed": request.resume_session_id is not None,
            "exposed_files": exposed_file_records(
                request.instructions_files
                + request.read_paths
                + additional_exposed_paths
            ),
            "usage": result.get("usage"),
        }
    )
    atomic_write_json(path, manifest)


def record_solver_call(
    paper_dir: Path, task_path: Path, result: dict[str, Any]
) -> None:
    path = paper_dir / "pipeline_manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["calls"].append(
        {
            "role": "validation_solver",
            "phase": "single_turn_closed_book_validation",
            "session_id": None,
            "turn_id": None,
            "resumed": False,
            "exposed_files": exposed_file_records((str(task_path),)),
            "usage": result.get("usage"),
            "protocol": result.get("protocol"),
        }
    )
    atomic_write_json(path, manifest)


def record_reviewer_call(paper_dir: Path, result: dict[str, Any]) -> None:
    path = paper_dir / "pipeline_manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["calls"].append(
        {
            "role": "validity_reviewer",
            "phase": "independent_task_and_proof_validity_review",
            "session_id": None,
            "turn_id": None,
            "resumed": False,
            "exposed_files": result.get("exposures", []),
            "usage": result.get("usage"),
            "protocol": result.get("protocol"),
        }
    )
    atomic_write_json(path, manifest)


def record_evaluator_call(paper_dir: Path, result: dict[str, Any]) -> None:
    path = paper_dir / "pipeline_manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["calls"].append(
        {
            "role": "reference_evaluator",
            "phase": "final_reference_based_scoring",
            "session_id": None,
            "turn_id": None,
            "resumed": False,
            "exposed_files": result.get("exposures", []),
            "usage": result.get("usage"),
            "protocol": result.get("protocol"),
        }
    )
    atomic_write_json(path, manifest)


def readable_source(private_source: Path) -> Path:
    metadata_path = private_source / "metadata.json"
    if metadata_path.is_file():
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        declared = metadata.get("content_source_file")
        allowed = {
            "source.html",
            "source.tex",
            "extracted_text.md",
            "source.pdf",
        }
        if declared is not None:
            if declared not in allowed:
                raise ValueError(
                    f"unsupported metadata content_source_file: {declared}"
                )
            selected = private_source / declared
            if not selected.is_file():
                raise FileNotFoundError(
                    f"metadata content source does not exist: {selected}"
                )
            return selected

    candidates = [
        private_source / "source.html",
        private_source / "source.tex",
        private_source / "extracted_text.md",
        private_source / "source.pdf",
    ]
    available = [path for path in candidates if path.is_file()]
    if not available:
        raise ValueError(
            "private_source requires source.html, source.tex, extracted_text.md, "
            "or source.pdf"
        )
    return available[0]


def validate_input(paper_dir: Path) -> tuple[str, Path]:
    if not paper_dir.name.startswith("paper_"):
        raise ValueError("paper directory name must start with paper_")
    private_source = paper_dir / "private_source"
    metadata = private_source / "metadata.json"
    if not metadata.is_file():
        raise FileNotFoundError(metadata)
    data = json.loads(metadata.read_text(encoding="utf-8"))
    if data.get("paper_id") != paper_dir.name:
        raise ValueError("metadata paper_id does not match directory name")
    return paper_dir.name, readable_source(private_source)


def inline_source(path: Path) -> str:
    if path.suffix.lower() != ".pdf":
        return path.read_text(encoding="utf-8", errors="replace")
    try:
        from pypdf import PdfReader
    except ImportError as error:
        raise RuntimeError(
            "pypdf is required to inline a PDF-only paper source"
        ) from error
    return "\n\n".join(page.extract_text() or "" for page in PdfReader(path).pages)


def inline_templates() -> str:
    sections = []
    for path in sorted(FORMALIZATION_TEMPLATE_DIR.glob("*")):
        if path.is_file():
            sections.append(f"## {path.name}\n\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(sections)


def persist_bundle(paper_dir: Path, bundle: dict[str, Any]) -> None:
    validate_contract("v2_formalization_bundle", bundle)
    target = paper_dir / "formalization"
    files = bundle["files"]
    if files is not None:
        validate_public_task_policy(files["task_md"])
    atomic_write_json(target / "contribution_analysis.json", bundle["analysis"])
    atomic_write_json(target / "self_audit.json", bundle["self_audit"])
    if files is not None:
        atomic_write_text(target / "task.md", files["task_md"])
        atomic_write_text(
            target / "proof_ground_truth.md", files["proof_ground_truth_md"]
        )
        atomic_write_text(target / "rubric.md", files["rubric_md"])
        atomic_write_json(target / "provenance.json", files["provenance"])
    else:
        for name in ("task.md", "proof_ground_truth.md", "rubric.md", "provenance.json"):
            (target / name).unlink(missing_ok=True)


def validate_public_task_policy(task: str) -> None:
    forbidden = {
        "Allowed Background Results heading": r"(?im)^\s*#{1,6}\s+allowed\s+background\s+results\s*$",
        "solver permission phrase": r"(?i)\byou\s+may\s+use\b",
        "task-specific standard-background permission": r"(?i)\b(?:allowed|permitted)\s+(?:standard\s+)?background\s+results?\b",
    }
    violations = [label for label, pattern in forbidden.items() if re.search(pattern, task)]
    if violations:
        raise ValueError(
            "public task contains forbidden proof permissions: "
            + ", ".join(violations)
        )


def draft_bundle(payload: dict[str, Any]) -> dict[str, Any]:
    validate_contract("v2_formalization_draft", payload)
    fields = None
    if payload["status"] == "formalized":
        required = (
            "task_md",
            "proof_ground_truth_md",
            "rubric_md",
            "provenance",
        )
        missing = [name for name in required if payload[name] is None]
        if missing:
            raise ValueError("formalized draft lacks: " + ", ".join(missing))
        fields = {
            "task_md": payload["task_md"],
            "proof_ground_truth_md": payload["proof_ground_truth_md"],
            "rubric_md": payload["rubric_md"],
            "provenance": payload["provenance"],
        }
    elif any(
        payload[name] is not None
        for name in (
            "task_md",
            "proof_ground_truth_md",
            "rubric_md",
            "provenance",
        )
    ):
        raise ValueError("non-formalized draft must not contain task files")
    return {
        "status": payload["status"],
        "resolution": payload["resolution"],
        "analysis": payload["analysis"],
        "files": fields,
        "self_audit": None,
        "stop_reason": payload["stop_reason"],
    }


def triage_bundle(payload: dict[str, Any]) -> dict[str, Any]:
    validate_contract("v2_triage_result", payload)
    return {
        "status": payload["status"],
        "resolution": payload["resolution"],
        "analysis": payload["analysis"],
        "files": None,
        "self_audit": None,
        "stop_reason": payload["stop_reason"],
    }


def apply_audit(
    current: dict[str, Any], payload: dict[str, Any], *, contract: str
) -> dict[str, Any]:
    validate_contract(contract, payload)
    updated = {
        "status": payload["status"],
        "resolution": payload["resolution"],
        "analysis": deepcopy(payload["analysis"] or current["analysis"]),
        "files": deepcopy(current["files"]),
        "self_audit": payload["self_audit"],
        "stop_reason": payload["stop_reason"],
    }
    if updated["status"] != "formalized":
        updated["files"] = None
        updated["analysis"]["difficulty"] = None
        updated["analysis"]["proof_difficulty_level"] = None
        updated["analysis"]["benchmark_suitability"] = None
        updated["analysis"]["difficulty_fidelity"] = None
        if contract == "v2_triage_audit":
            reason = filtered_reason(updated["analysis"])
            if reason is not None:
                updated["status"] = "filtered_out"
                updated["stop_reason"] = reason
    else:
        if updated["files"] is None:
            updated["files"] = {}
        replacements = {
            "task_md": payload["task_md"],
            "proof_ground_truth_md": payload["proof_ground_truth_md"],
            "rubric_md": payload["rubric_md"],
        }
        for name, value in replacements.items():
            if value is not None:
                updated["files"][name] = value
        if payload["provenance"] is not None:
            updated["files"]["provenance"] = payload["provenance"]
    return updated


def load_written_bundle(
    paper_dir: Path, turn_result: dict[str, Any]
) -> dict[str, Any]:
    validate_contract("v2_formalization_result", turn_result)
    formalization = paper_dir / "formalization"
    common = {"contribution_analysis.json", "self_audit.json"}
    complete = common | {
        "task.md",
        "proof_ground_truth.md",
        "rubric.md",
        "provenance.json",
    }
    expected = complete if turn_result["status"] == "formalized" else common
    if set(turn_result["written_files"]) != expected:
        raise ValueError(
            "formalizer written_files do not match status: expected "
            + ", ".join(sorted(expected))
        )
    missing = [name for name in expected if not (formalization / name).is_file()]
    if missing:
        raise FileNotFoundError(
            "formalizer did not write declared files: " + ", ".join(sorted(missing))
        )
    files = None
    if turn_result["status"] == "formalized":
        files = {
            "task_md": (formalization / "task.md").read_text(encoding="utf-8"),
            "proof_ground_truth_md": (
                formalization / "proof_ground_truth.md"
            ).read_text(encoding="utf-8"),
            "rubric_md": (formalization / "rubric.md").read_text(encoding="utf-8"),
            "provenance": json.loads(
                (formalization / "provenance.json").read_text(encoding="utf-8")
            ),
        }
    bundle = {
        "status": turn_result["status"],
        "resolution": turn_result["resolution"],
        "analysis": json.loads(
            (formalization / "contribution_analysis.json").read_text(encoding="utf-8")
        ),
        "files": files,
        "self_audit": json.loads(
            (formalization / "self_audit.json").read_text(encoding="utf-8")
        ),
        "stop_reason": turn_result["stop_reason"],
    }
    validate_contract("v2_formalization_bundle", bundle)
    return bundle


def persist_status(paper_dir: Path, value: dict[str, Any]) -> None:
    schema = load_schema("status.schema.json")
    errors = list(Draft202012Validator(schema).iter_errors(value))
    if errors:
        raise ValueError("invalid status: " + "; ".join(error.message for error in errors))
    atomic_write_json(paper_dir / "formalization/status.json", value)


def reset_validation_outputs(paper_dir: Path) -> None:
    for name in ("validation_solver", "formalization_reviewer", "final_evaluator"):
        shutil.rmtree(paper_dir / name, ignore_errors=True)


def stop_after_failed_self_audit(
    bundle: dict[str, Any], validation_error: str
) -> dict[str, Any]:
    stopped = deepcopy(bundle)
    stopped["status"] = "stopped"
    stopped["files"] = None
    stopped["stop_reason"] = "failed_after_max_revisions"
    stopped["analysis"]["difficulty"] = None
    stopped["analysis"]["proof_difficulty_level"] = None
    stopped["analysis"]["benchmark_suitability"] = None
    stopped["analysis"]["difficulty_fidelity"] = None
    audit = stopped.get("self_audit")
    if isinstance(audit, dict):
        findings = audit.setdefault("findings", [])
        findings.append(
            "Deterministic validation remained unsatisfied after the maximum "
            f"self-audit revisions: {validation_error}"
        )
    validate_contract("v2_formalization_bundle", stopped)
    return stopped


def solver_objection(result: dict[str, Any]) -> list[dict[str, Any]]:
    if result["status"] != "unscorable":
        return []
    return [
        {
            "source": "solver",
            "category": "solver_unscorable_objection",
            "description": result.get("reason", ""),
        }
    ]


def reviewer_objections(result: dict[str, Any]) -> list[dict[str, Any]]:
    if result["status"] != "unscorable":
        return []
    report = result["report"]
    findings = [
        finding
        for finding in report.get("findings", [])
        if finding.get("status") == "verified"
        and finding.get("severity") in {"blocking", "major"}
    ]
    return [
        {
            "source": "reviewer",
            "category": finding.get("kind", "other"),
            "location": finding.get("location", "unspecified"),
            "description": finding.get("description", ""),
            "mathematical_consequence": finding.get("effect_on_proof", ""),
        }
        for finding in findings
    ] or [
        {
            "source": "reviewer",
            "category": "target_suspected_invalid",
            "description": report.get("summary", ""),
        }
    ]


class ContributionPipeline:
    def __init__(
        self,
        agent_backend: AgentBackend,
        validation_backend: ValidationBackend,
        *,
        formalizer_prompt: Path | None = None,
        triage_prompt: Path = TRIAGE_PROMPT,
        formalization_draft_prompt: Path = FORMALIZATION_DRAFT_PROMPT,
        triage_audit_prompt: Path = TRIAGE_AUDIT_PROMPT,
        formalization_audit_prompt: Path = FORMALIZATION_AUDIT_PROMPT,
        formalization_revision_prompt: Path = FORMALIZATION_REVISION_PROMPT,
    ) -> None:
        self.agent = agent_backend
        self.validation = validation_backend
        if formalizer_prompt is not None:
            prompts = {
                "triage": formalizer_prompt,
                "formalization_draft": formalizer_prompt,
                "triage_audit": formalizer_prompt,
                "formalization_audit": formalizer_prompt,
                "formalization_revision": formalizer_prompt,
            }
        else:
            prompts = {
                "triage": triage_prompt,
                "formalization_draft": formalization_draft_prompt,
                "triage_audit": triage_audit_prompt,
                "formalization_audit": formalization_audit_prompt,
                "formalization_revision": formalization_revision_prompt,
            }
        self.formalizer_prompts = {
            phase: prompt.resolve() for phase, prompt in prompts.items()
        }
        for prompt in self.formalizer_prompts.values():
            if not prompt.is_file():
                raise FileNotFoundError(prompt)

    async def _triage(
        self,
        paper_dir: Path,
        paper_id: str,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        source = readable_source(paper_dir / "private_source")
        exposure_paths = (
            str(paper_dir / "private_source/metadata.json"),
            str(source),
        )
        request = AgentRequest(
            role="contribution_formalizer",
            phase="v2_triage_paper",
            paper_id=paper_id,
            theorem_id=None,
            instructions_files=(str(self.formalizer_prompts["triage"]),),
            read_paths=(),
            write_paths=(),
            context={
                "output_contract": "v2_triage_result",
                "inline_no_tools": True,
                "single_principal_contribution": True,
                "metadata": json.loads(
                    (paper_dir / "private_source/metadata.json").read_text(
                        encoding="utf-8"
                    )
                ),
                "paper_source": inline_source(source),
            },
            resume_session_id=None,
            max_retries=0,
        )
        result = await self.agent.run(request)
        record_agent_call(paper_dir, request, result, exposure_paths)
        return triage_bundle(result["payload"]), result

    async def _generate_formalization(
        self,
        paper_dir: Path,
        paper_id: str,
        triage: dict[str, Any],
        session_id: str,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        request = AgentRequest(
            role="contribution_formalizer",
            phase="v2_generate_formalization_draft",
            paper_id=paper_id,
            theorem_id=None,
            instructions_files=(
                str(self.formalizer_prompts["formalization_draft"]),
            ),
            read_paths=(),
            write_paths=(),
            context={
                "output_contract": "v2_formalization_draft",
                "inline_no_tools": True,
                "single_principal_contribution": True,
                "output_budget_enabled": False,
                "triage_status": "proceed",
                "triage_analysis": triage["analysis"],
                "templates": inline_templates(),
            },
            resume_session_id=session_id,
            max_retries=0,
        )
        result = await self.agent.run(request)
        record_agent_call(
            paper_dir,
            request,
            result,
            (str(FORMALIZATION_TEMPLATE_DIR),),
        )
        return draft_bundle(result["payload"]), result

    async def _audit_or_revise(
        self,
        paper_dir: Path,
        paper_id: str,
        current: dict[str, Any],
        session_id: str,
        objections: list[dict[str, Any]] | None = None,
        triage_only: bool = False,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        revision = objections is not None
        if triage_only:
            phase = "v2_revise_triage" if revision else "v2_audit_triage"
            output_contract = "v2_triage_audit"
            prompt_key = "formalization_revision" if revision else "triage_audit"
        else:
            phase = (
                "v2_revise_formalization"
                if revision
                else "v2_audit_formalization_draft"
            )
            output_contract = "v2_formalization_audit"
            prompt_key = (
                "formalization_revision" if revision else "formalization_audit"
            )
        request = AgentRequest(
            role="contribution_formalizer",
            phase=phase,
            paper_id=paper_id,
            theorem_id=None,
            instructions_files=(str(self.formalizer_prompts[prompt_key]),),
            read_paths=(),
            write_paths=(),
            context={
                "output_contract": output_contract,
                "inline_no_tools": True,
                "current_status": current["status"],
                "objections": objections or [],
                "triage_only": triage_only,
                "output_budget_enabled": False,
            },
            resume_session_id=session_id,
            max_retries=0,
        )
        result = await self.agent.run(request)
        record_agent_call(paper_dir, request, result)
        return apply_audit(
            current,
            result["payload"],
            contract=output_contract,
        ), result

    async def _repair_failed_audit(
        self,
        paper_dir: Path,
        paper_id: str,
        bundle: dict[str, Any],
        session_id: str,
        revision_count: int,
        triage_only: bool = False,
    ) -> tuple[dict[str, Any], int]:
        repair_count = 0
        while True:
            try:
                validate_contract("v2_formalization_bundle", bundle)
                return bundle, revision_count
            except ValueError as error:
                if repair_count >= MAX_SELF_AUDIT_REPAIRS:
                    if triage_only:
                        raise ValueError(
                            "triage validation remained unsatisfied after repairs: "
                            + str(error)
                        )
                    return stop_after_failed_self_audit(bundle, str(error)), revision_count
                repair_count += 1
                revision_count += 1
                findings = bundle.get("self_audit", {}).get("findings", [])
                objections = [
                    {
                        "source": "formalizer_self_audit",
                        "category": "failed_self_audit",
                        "description": str(error),
                        "findings": findings,
                    }
                ]
                bundle, result = await self._audit_or_revise(
                    paper_dir,
                    paper_id,
                    bundle,
                    session_id,
                    objections=objections,
                    triage_only=triage_only,
                )
                if result["session_id"] != session_id:
                    raise RuntimeError(
                        "formalization self-revision did not resume its thread"
                    )

    async def run(
        self,
        paper_dir: Path,
        *,
        formalization_only: bool = False,
    ) -> PipelineResult:
        paper_dir = paper_dir.resolve()
        paper_id, _ = validate_input(paper_dir)
        revision_count = 0
        validation_feedback_count = 0
        session_id: str | None = None
        status = {
            "paper_id": paper_id,
            "status": "formalizing",
            "revision_count": 0,
            "validation_feedback_count": 0,
            "formalizer_session_id": None,
            "solver_validation_status": None,
            "reviewer_status": None,
            "evaluator_status": None,
            "unscorable_source": None,
            "stop_reason": None,
        }

        try:
            bundle, formalizer_result = await self._triage(
                paper_dir, paper_id
            )
            session_id = formalizer_result["session_id"]

            if bundle["status"] == "proceed":
                bundle, generation_result = await self._generate_formalization(
                    paper_dir,
                    paper_id,
                    bundle,
                    session_id,
                )
                if generation_result["session_id"] != session_id:
                    raise RuntimeError(
                        "formalization generation did not resume its triage thread"
                    )
                triage_only = False
            else:
                triage_only = True

            bundle, audit_result = await self._audit_or_revise(
                paper_dir,
                paper_id,
                bundle,
                session_id,
                triage_only=triage_only,
            )
            if audit_result["session_id"] != session_id:
                raise RuntimeError("formalization audit did not resume its thread")
            bundle, revision_count = await self._repair_failed_audit(
                paper_dir,
                paper_id,
                bundle,
                session_id,
                revision_count,
                triage_only=triage_only,
            )
            persist_bundle(paper_dir, bundle)
            reset_validation_outputs(paper_dir)
            status["formalizer_session_id"] = session_id
            status["revision_count"] = revision_count
            persist_status(paper_dir, status)

            while True:
                if bundle["status"] in {"filtered_out", "stopped"}:
                    pipeline_status = bundle["status"]
                    status.update(
                        {
                            "status": pipeline_status,
                            "revision_count": revision_count,
                            "stop_reason": bundle["stop_reason"],
                        }
                    )
                    persist_status(paper_dir, status)
                    return PipelineResult(
                        paper_id,
                        pipeline_status,
                        revision_count,
                        bundle["stop_reason"],
                    )

                if formalization_only:
                    status.update(
                        {
                            "status": "formalizing",
                            "solver_validation_status": None,
                            "reviewer_status": None,
                            "evaluator_status": None,
                            "unscorable_source": None,
                            "stop_reason": None,
                        }
                    )
                    persist_status(paper_dir, status)
                    return PipelineResult(
                        paper_id,
                        "formalizing",
                        revision_count,
                        None,
                    )

                reset_validation_outputs(paper_dir)
                status.update(
                    {
                        "solver_validation_status": None,
                        "reviewer_status": None,
                        "evaluator_status": None,
                        "unscorable_source": None,
                    }
                )
                persist_status(paper_dir, status)

                solver_result = self.validation.run_solver(
                    paper_id,
                    paper_dir / "formalization/task.md",
                    paper_dir / "validation_solver",
                )
                record_solver_call(
                    paper_dir,
                    paper_dir / "formalization/task.md",
                    solver_result,
                )
                status["solver_validation_status"] = solver_result["status"]
                persist_status(paper_dir, status)

                objections = solver_objection(solver_result)
                if not objections:
                    reviewer_result = self.validation.run_reviewer(
                        paper_id,
                        paper_dir / "formalization/task.md",
                        paper_dir / "validation_solver",
                        paper_dir / "formalization_reviewer",
                    )
                    record_reviewer_call(paper_dir, reviewer_result)
                    status["reviewer_status"] = reviewer_result["status"]
                    persist_status(paper_dir, status)
                    objections = reviewer_objections(reviewer_result)

                if not objections:
                    evaluation = self.validation.run_evaluator(
                        paper_id,
                        paper_dir / "formalization/task.md",
                        paper_dir / "validation_solver",
                        paper_dir / "formalization_reviewer",
                        paper_dir / "final_evaluator",
                    )
                    record_evaluator_call(paper_dir, evaluation)
                    status["evaluator_status"] = evaluation["result"][
                        "evaluation_status"
                    ]
                    status.update(
                        {
                            "status": "completed",
                            "revision_count": revision_count,
                            "unscorable_source": None,
                            "stop_reason": None,
                        }
                    )
                    persist_status(paper_dir, status)
                    return PipelineResult(paper_id, "completed", revision_count, None)

                status["unscorable_source"] = objections[0]["source"]
                persist_status(paper_dir, status)
                if validation_feedback_count >= MAX_VALIDATION_FEEDBACK_RETURNS:
                    status.update(
                        {
                            "status": "stopped",
                            "revision_count": revision_count,
                            "validation_feedback_count": validation_feedback_count,
                            "stop_reason": "failed_after_max_validation_feedback",
                        }
                    )
                    persist_status(paper_dir, status)
                    return PipelineResult(
                        paper_id,
                        "stopped",
                        revision_count,
                        "failed_after_max_validation_feedback",
                    )

                validation_feedback_count += 1
                revision_count += 1
                bundle, formalizer_result = await self._audit_or_revise(
                    paper_dir,
                    paper_id,
                    bundle,
                    session_id,
                    objections=objections,
                    triage_only=False,
                )
                if formalizer_result["session_id"] != session_id:
                    raise RuntimeError("formalization revision did not resume its thread")
                bundle, revision_count = await self._repair_failed_audit(
                    paper_dir,
                    paper_id,
                    bundle,
                    session_id,
                    revision_count,
                    triage_only=False,
                )
                persist_bundle(paper_dir, bundle)
                status["revision_count"] = revision_count
                status["validation_feedback_count"] = validation_feedback_count
                persist_status(paper_dir, status)
        except Exception as error:
            status.update(
                {
                    "status": "failed",
                    "revision_count": revision_count,
                    "validation_feedback_count": validation_feedback_count,
                    "formalizer_session_id": session_id,
                    "stop_reason": str(error),
                }
            )
            persist_status(paper_dir, status)
            raise
