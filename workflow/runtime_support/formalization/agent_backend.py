from __future__ import annotations

import importlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from base_contracts import CONTRACTS, normalize_contract_payload, validate_contract


WORKFLOW_ROOT = Path(__file__).resolve().parents[2]
CODEX_SUPPORT = WORKFLOW_ROOT / "runtime_support/codex"


@dataclass(frozen=True)
class AgentRequest:
    role: str
    phase: str
    paper_id: str
    theorem_id: str | None
    instructions_files: tuple[str, ...]
    read_paths: tuple[str, ...]
    write_paths: tuple[str, ...]
    context: dict[str, Any]
    resume_session_id: str | None = None
    timeout_seconds: int = 3600
    max_retries: int = 1


class AgentBackend(Protocol):
    async def run(self, request: AgentRequest) -> dict[str, Any]: ...

    async def aclose(self) -> None: ...


class ScriptedBackend:
    """Deterministic backend used by tests and local smoke checks."""

    def __init__(self, responses: dict[str, list[dict[str, Any]]]) -> None:
        self.responses = {key: list(values) for key, values in responses.items()}
        self.calls: list[AgentRequest] = []
        self._next_session = 1

    async def run(self, request: AgentRequest) -> dict[str, Any]:
        self.calls.append(request)
        queue = self.responses.get(request.phase, [])
        if not queue:
            raise RuntimeError(f"no scripted response for phase {request.phase}")
        payload = queue.pop(0)
        contract = str(request.context["output_contract"])
        payload = normalize_contract_payload(contract, payload)
        validate_contract(contract, payload)
        session_id = request.resume_session_id
        if session_id is None:
            session_id = f"mock_session_{self._next_session:03d}"
            self._next_session += 1
        return {
            "status": payload["status"],
            "payload": payload,
            "session_id": session_id,
            "turn_id": f"mock_turn_{len(self.calls):03d}",
            "usage": {
                "input_tokens": 0,
                "cached_input_tokens": 0,
                "output_tokens": 0,
                "total_tokens": 0,
            },
            "attempts": 1,
        }

    async def aclose(self) -> None:
        return None


class ExistingCodexBackend:
    """Codex SDK agent backend with isolated, resumable thread workspaces."""

    def __init__(self, profile_dir: Path | None = None) -> None:
        if str(CODEX_SUPPORT) not in sys.path:
            sys.path.insert(0, str(CODEX_SUPPORT))
        pipeline_contracts = importlib.import_module("pipeline_contracts")
        codex_adapter = importlib.import_module("codex_adapter")
        pipeline_contracts.CONTRACTS.update(CONTRACTS)
        codex_adapter.PHASE_TASKS.update(
            {
                "v2_triage_paper": (
                    "Read the complete inline paper source and perform only paper "
                    "triage. Return proceed or filtered_out. Do not formalize, audit, "
                    "or call tools."
                ),
                "v2_audit_triage": (
                    "Audit only the filtered-out triage decision from the preceding "
                    "turn under the triage-audit instructions. The result must remain "
                    "filtered_out. Do not formalize or call tools."
                ),
                "v2_revise_triage": (
                    "Correct only the supplied deterministic defect in the filtered-"
                    "out triage result. The result must remain filtered_out. Do not "
                    "formalize or call tools."
                ),
                "v2_generate_formalization_draft": (
                    "The paper passed triage in the preceding turn. Use the source "
                    "already in this thread and the inline templates to generate one "
                    "contribution-level draft. Return formalized or stopped, never "
                    "filtered_out. Apply the supplied source statement and proof audit "
                    "standards, but do not perform the mandatory self-audit in this "
                    "turn. Do not call tools."
                ),
                "v2_audit_formalization_draft": (
                    "Audit the draft returned in the preceding turn under the "
                    "formalization-audit instructions. Correct only fields that need "
                    "correction and return null for unchanged fields. Do not call tools."
                ),
                "v2_revise_formalization": (
                    "Verify the supplied unscorable objections against the source and "
                    "formalization already in this thread under the revision "
                    "instructions. Return only necessary field replacements and a fresh "
                    "self-audit. Do not call tools."
                ),
            }
        )
        self._adapter = codex_adapter.CodexAPIAdapter(profile_dir=profile_dir)

    async def run(self, request: AgentRequest) -> dict[str, Any]:
        result = await self._adapter.run(request)
        contract = str(request.context["output_contract"])
        result["payload"] = normalize_contract_payload(contract, result["payload"])
        result["status"] = result["payload"]["status"]
        validate_contract(contract, result["payload"])
        return result

    async def aclose(self) -> None:
        await self._adapter.aclose()


def dump_request(path: Path, request: AgentRequest) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(request.__dict__, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
