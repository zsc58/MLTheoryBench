#!/usr/bin/env python3
"""Audit one paper in one persistent Codex thread.

Turn 1 receives the complete supplied paper representation, paper-wide Thread-A
and later-chain issue context, the complete result inventory, the lean result-node
schema, and the first target. Later turns resume the same thread. The runner
validates each combined finding/repair/result-impact output, maintains the
established-findings ledger, optionally traces honest repairs into unmarked
downstream theory candidates, runs one final paper-impact turn, and assembles a
paper-level audit JSON using the supplied schema version.

Full source text is never copied into the run directory. The private manifest
records source exposures, hashes, sizes, model usage, and per-turn output paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import jsonschema
from structured_output import write_transport_schema, repair_invalid_output, BOOKKEEPING_RULES, REPAIR_POLICY_VERSION
from audit_metrics import last_cumulative_usage
from cli_transport import run_with_recovery, transport_fields

from validate_result_node_audits import (
    make_paper_validator,
    paper_impact_semantic_errors,
    paper_semantic_errors,
    result_findings,
    semantic_errors,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROMPT = ROOT / "prompts" / "result_node_audit_prompt.md"
DEFAULT_PROPAGATION_PROMPT = ROOT / "prompts" / "propagation_audit_prompt.md"
DEFAULT_PAPER_IMPACT_PROMPT = ROOT / "prompts" / "paper_impact_prompt.md"
DEFAULT_RESULT_SCHEMA = ROOT / "schemas" / "result_node_audit.schema.json"
DEFAULT_PAPER_IMPACT_SCHEMA = ROOT / "schemas" / "paper_impact_output.schema.json"
DEFAULT_PAPER_SCHEMA = ROOT / "schemas" / "paper_audit.schema.json"
DEFAULT_PROPAGATION_SCHEMA = ROOT / "schemas" / "propagation_audit.schema.json"
DEFAULT_RUNS_ROOT = ROOT / ".runtime" / "runs"
AUDITABLE_ROLES = {"theory_candidate", "internal_support"}
ISSUE_STATEMENT_STATUSES = {"minor_issue", "major_issue"}
ISSUE_PROOF_STATUSES = {"minor_error", "major_gap"}
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")
SOURCE_FIDELITIES = {"original_tex_or_html", "extracted_text", "ocr", "unknown"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Open one local-login Codex session for a paper and audit every explicitly "
            "issue-marked theory_candidate/internal_support node, one result per turn."
        )
    )
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--theory-topic", required=True)
    parser.add_argument("--source-file", required=True, type=Path)
    parser.add_argument(
        "--source-fidelity",
        choices=sorted(SOURCE_FIDELITIES),
        help=(
            "Fidelity of --source-file. Defaults to original_tex_or_html for .tex/.html, "
            "extracted_text for a file named extracted_text.*, and unknown otherwise."
        ),
    )
    parser.add_argument("--turn3-audit", required=True, type=Path)
    parser.add_argument(
        "--later-chain-leads",
        type=Path,
        help="Optional JSON object mapping result_id to a list of later-chain issue leads.",
    )
    parser.add_argument(
        "--result-id",
        action="append",
        dest="result_ids",
        help=(
            "Explicit exact target override; repeat for several nodes. Otherwise select explicit "
            "issue-marked records only."
        ),
    )
    parser.add_argument(
        "--prompt",
        type=Path,
        default=DEFAULT_PROMPT,
        help="Ordinary result-audit prompt.",
    )
    parser.add_argument(
        "--propagation-prompt",
        type=Path,
        default=DEFAULT_PROPAGATION_PROMPT,
        help="Dedicated prompt injected only for the optional propagation turn.",
    )
    parser.add_argument(
        "--paper-impact-prompt", type=Path, default=DEFAULT_PAPER_IMPACT_PROMPT
    )
    parser.add_argument("--result-schema", type=Path, default=DEFAULT_RESULT_SCHEMA)
    parser.add_argument(
        "--paper-impact-schema", type=Path, default=DEFAULT_PAPER_IMPACT_SCHEMA
    )
    parser.add_argument("--paper-schema", type=Path, default=DEFAULT_PAPER_SCHEMA)
    parser.add_argument(
        "--enable-propagation-audit",
        action="store_true",
        help=(
            "After explicit issue-node audits, run one targeted downstream propagation turn "
            "before the paper-impact turn."
        ),
    )
    parser.add_argument(
        "--propagation-schema", type=Path, default=DEFAULT_PROPAGATION_SCHEMA
    )
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS_ROOT)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument(
        "--auth-mode",
        choices=["current_local_codex_login", "isolated_vm_api_profile"],
        default="current_local_codex_login",
        help="Manifest label only; the batch launcher configures VM authentication.",
    )
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument(
        "--reasoning-effort",
        default="high",
        choices=["low", "medium", "high", "xhigh", "max", "ultra"],
    )
    parser.add_argument("--timeout-seconds", type=int, default=1800)
    parser.add_argument("--max-output-repairs", type=int, choices=(0, 1, 2), default=2)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def read_required_bytes(path: Path) -> bytes:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_bytes()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_safe_id(value: str, label: str) -> str:
    if not SAFE_ID.fullmatch(value):
        raise ValueError(f"invalid {label}: {value!r}")
    return value


def infer_source_fidelity(path: Path) -> str:
    if path.suffix.lower() in {".tex", ".html", ".htm"}:
        return "original_tex_or_html"
    if path.name.lower().startswith("extracted_text."):
        return "extracted_text"
    return "unknown"


def material_records(turn3: dict[str, Any]) -> list[dict[str, Any]]:
    records = turn3.get("material_records")
    if not isinstance(records, list):
        raise ValueError("Turn-3 audit has no material_records array")
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"material_records[{index}] must be an object")
        result_id = record.get("item_id")
        if not isinstance(result_id, str) or not result_id:
            raise ValueError(f"material_records[{index}] has no item_id")
        validate_safe_id(result_id, "result ID")
        if result_id in seen:
            raise ValueError(f"duplicate Turn-3 material record {result_id!r}")
        seen.add(result_id)
        output.append(record)
    return output


def normalize_later_leads(value: Any) -> dict[str, list[str]]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValueError("later-chain leads must be a JSON object mapping result_id to string arrays")
    normalized: dict[str, list[str]] = {}
    for raw_result_id, raw_leads in value.items():
        result_id = validate_safe_id(raw_result_id, "later-lead result ID")
        if isinstance(raw_leads, str):
            leads = [raw_leads]
        elif isinstance(raw_leads, list) and all(
            isinstance(lead, str) and lead.strip() for lead in raw_leads
        ):
            leads = raw_leads
        else:
            raise ValueError(f"later-chain leads for {result_id} must be non-empty strings")
        if leads:
            normalized[result_id] = leads
    return normalized


def infer_result_kind(record: dict[str, Any]) -> str:
    role = record.get("role")
    if role == "definition":
        return "definition"
    if role == "external":
        return "external_result"
    label = str(record.get("source_label") or "").strip().casefold()
    for prefix, kind in (
        ("theorem", "theorem"),
        ("lemma", "lemma"),
        ("proposition", "proposition"),
        ("corollary", "corollary"),
        ("definition", "definition"),
    ):
        if label.startswith(prefix):
            return kind
    if "chain" in label:
        return "result_chain"
    return "unnumbered_claim"


def location_locator(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    if not isinstance(value, dict):
        return None
    start = value.get("start_line")
    end = value.get("end_line")
    label = value.get("label")
    parts: list[str] = []
    if isinstance(label, str) and label.strip():
        parts.append(label.strip())
    if isinstance(start, int) and isinstance(end, int):
        parts.append(f"L{start}-L{end}")
    elif isinstance(start, int):
        parts.append(f"L{start}")
    return ": ".join(parts) if parts else None


def record_locations(record: dict[str, Any], key: str, *, fallback_spans: bool) -> list[dict[str, str]]:
    raw = record.get(key, [])
    if raw is None:
        raw = []
    if not isinstance(raw, list):
        raise ValueError(f"{record['item_id']}: {key} must be an array")
    locators = [locator for item in raw if (locator := location_locator(item))]
    if not locators and fallback_spans:
        spans = record.get("source_spans", [])
        if isinstance(spans, list):
            locators = [span.strip() for span in spans if isinstance(span, str) and span.strip()]
    return [{"source_id": "paper_source", "locator": locator} for locator in dict.fromkeys(locators)]


def build_result_inventory(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    inventory: list[dict[str, Any]] = []
    for record in records:
        role = record.get("role")
        if role not in {"theory_candidate", "internal_support", "definition", "external"}:
            continue
        inventory.append(
            {
                "result_id": record["item_id"],
                "inventory_role": role,
                "result_kind": infer_result_kind(record),
                "source_label": str(record.get("source_label") or record["item_id"]),
                "statement_status": str(record.get("statement_status") or "not_applicable"),
                "proof_status": str(record.get("proof_status") or "not_applicable"),
                "depends_on": list(record.get("depends_on") or []),
                "statement_locations": record_locations(
                    record, "statement_source_locations", fallback_spans=True
                ),
                "proof_locations": record_locations(
                    record, "proof_source_locations", fallback_spans=False
                ),
            }
        )
    if not inventory:
        raise ValueError("Turn-3 audit contains no material result inventory")
    return inventory


def validate_lead_array(record: dict[str, Any], key: str) -> list[str]:
    value = record.get(key, [])
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise ValueError(f"{record['item_id']}: {key} must be a string array")
    return value


def build_issue_leads(
    records: list[dict[str, Any]], later_leads: dict[str, list[str]]
) -> list[dict[str, str]]:
    leads: list[dict[str, str]] = []
    known_ids = {record["item_id"] for record in records}
    for result_id in later_leads:
        if result_id not in known_ids:
            raise ValueError(f"later-chain lead targets unknown result {result_id!r}")

    for record in records:
        result_id = record["item_id"]
        role = record.get("role")
        if role not in {"theory_candidate", "internal_support", "definition", "external"}:
            continue
        groups = (
            ("turn3_statement", validate_lead_array(record, "statement_findings")),
            ("turn3_proof", validate_lead_array(record, "proof_findings")),
            ("later_chain", later_leads.get(result_id, [])),
        )
        for origin, claims in groups:
            for index, claim in enumerate(claims):
                leads.append(
                    {
                        "lead_id": f"{result_id}::{origin}::{index:03d}",
                        "result_id": result_id,
                        "origin": origin,
                        "claim": claim,
                    }
                )
    return leads


def leads_for_result(issue_leads: list[dict[str, str]], result_id: str) -> list[dict[str, str]]:
    return [lead for lead in issue_leads if lead["result_id"] == result_id]


def select_targets(
    records: list[dict[str, Any]],
    later_leads: dict[str, list[str]],
    explicit_ids: list[str] | None,
) -> list[dict[str, Any]]:
    by_id = {record["item_id"]: record for record in records}
    for result_id in later_leads:
        record = by_id.get(result_id)
        if record is None:
            raise ValueError(f"later-chain lead targets unknown result {result_id!r}")
        if record.get("role") not in AUDITABLE_ROLES:
            raise ValueError(
                f"later-chain lead targets role {record.get('role')!r} at {result_id}; "
                "only theory_candidate/internal_support nodes are auditable"
            )

    if explicit_ids:
        requested = [validate_safe_id(value, "result ID") for value in explicit_ids]
        if len(set(requested)) != len(requested):
            raise ValueError("duplicate --result-id values")
        missing = [result_id for result_id in requested if result_id not in by_id]
        if missing:
            raise ValueError(f"unknown explicit target(s): {', '.join(missing)}")
        requested_set = set(requested)
        targets = [record for record in records if record["item_id"] in requested_set]
    else:
        targets = []
        for record in records:
            if record.get("role") not in AUDITABLE_ROLES:
                continue
            result_id = record["item_id"]
            explicitly_marked = (
                record.get("statement_status") in ISSUE_STATEMENT_STATUSES
                or record.get("proof_status") in ISSUE_PROOF_STATUSES
                or bool(later_leads.get(result_id))
            )
            if explicitly_marked:
                targets.append(record)

    for record in targets:
        if record.get("role") not in AUDITABLE_ROLES:
            raise ValueError(
                f"{record['item_id']} has role {record.get('role')!r}; "
                "only theory_candidate/internal_support nodes are auditable"
            )
    if not targets:
        raise ValueError("no explicit issue-marked theory_candidate/internal_support targets found")
    return order_targets_dependency_first(targets)


def order_targets_dependency_first(targets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Topologically order audited targets while preserving inventory order for ties.

    Only dependencies among selected targets constrain the order. Upstream definitions,
    external results, and clean unaudited nodes remain available through the paper inventory
    but do not need a finding ledger entry.
    """

    by_id = {record["item_id"]: record for record in targets}
    target_ids = set(by_id)
    ordered: list[dict[str, Any]] = []
    permanent: set[str] = set()
    temporary: set[str] = set()

    def visit(result_id: str) -> None:
        if result_id in permanent:
            return
        if result_id in temporary:
            raise ValueError(f"cycle among selected result dependencies at {result_id!r}")
        temporary.add(result_id)
        raw_dependencies = by_id[result_id].get("depends_on", [])
        if raw_dependencies is None:
            raw_dependencies = []
        if not isinstance(raw_dependencies, list) or not all(
            isinstance(item, str) and item for item in raw_dependencies
        ):
            raise ValueError(f"{result_id}: depends_on must be a string array")
        for upstream_id in raw_dependencies:
            if upstream_id in target_ids:
                visit(upstream_id)
        temporary.remove(result_id)
        permanent.add(result_id)
        ordered.append(by_id[result_id])

    for record in targets:
        visit(record["item_id"])
    return ordered


def shortest_dependency_path(
    *,
    upstream_result_id: str,
    downstream_result_id: str,
    result_inventory: list[dict[str, Any]],
) -> list[str] | None:
    """Return one deterministic shortest upstream-to-downstream dependency path."""

    downstream_by_upstream: dict[str, list[str]] = {
        item["result_id"]: [] for item in result_inventory
    }
    for item in result_inventory:
        for dependency_id in item["depends_on"]:
            downstream_by_upstream.setdefault(dependency_id, []).append(item["result_id"])

    queue: list[list[str]] = [[upstream_result_id]]
    visited = {upstream_result_id}
    while queue:
        path = queue.pop(0)
        current = path[-1]
        if current == downstream_result_id:
            return path
        for next_result_id in downstream_by_upstream.get(current, []):
            if next_result_id in visited:
                continue
            visited.add(next_result_id)
            queue.append([*path, next_result_id])
    return None


def build_propagation_assignment(
    *,
    result_inventory: list[dict[str, Any]],
    result_outputs: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """Build a narrow finding-to-unmarked-theory-candidate propagation assignment."""

    findings_by_result: dict[str, list[str]] = {}
    for output in result_outputs:
        finding_ids = list(result_findings(output))
        if finding_ids:
            findings_by_result[output["result_id"]] = finding_ids
    if not findings_by_result:
        return None

    audited_result_ids = {output["result_id"] for output in result_outputs}
    candidate_rows: list[dict[str, Any]] = []
    relevant_result_ids = set(findings_by_result)
    for item in result_inventory:
        downstream_result_id = item["result_id"]
        if item["inventory_role"] != "theory_candidate":
            continue
        if downstream_result_id in audited_result_ids:
            continue
        paths: list[list[str]] = []
        upstream_result_ids: list[str] = []
        upstream_finding_ids: list[str] = []
        for upstream_result_id, finding_ids in findings_by_result.items():
            path = shortest_dependency_path(
                upstream_result_id=upstream_result_id,
                downstream_result_id=downstream_result_id,
                result_inventory=result_inventory,
            )
            if path is None:
                continue
            paths.append(path)
            upstream_result_ids.append(upstream_result_id)
            upstream_finding_ids.extend(finding_ids)
            relevant_result_ids.update(path)
        if not paths:
            continue
        candidate_rows.append(
            {
                "downstream_result_id": downstream_result_id,
                "upstream_result_ids": upstream_result_ids,
                "upstream_finding_ids": list(dict.fromkeys(upstream_finding_ids)),
                "dependency_paths": paths,
            }
        )

    if not candidate_rows:
        return None

    inventory_by_id = {item["result_id"]: item for item in result_inventory}
    ordered_relevant_ids = [
        item["result_id"]
        for item in result_inventory
        if item["result_id"] in relevant_result_ids
    ]
    return {
        "source_result_ids": list(findings_by_result),
        "source_finding_ids": [
            finding_id
            for finding_ids in findings_by_result.values()
            for finding_id in finding_ids
        ],
        "candidate_downstream_results": candidate_rows,
        "relevant_result_inventory": [
            inventory_by_id[result_id] for result_id in ordered_relevant_ids
        ],
    }


def extract_event_metadata(stdout: str) -> tuple[dict[str, Any] | None, str | None]:
    usage: dict[str, Any] | None = None
    session_id: str | None = None
    for raw in stdout.splitlines():
        try:
            event = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        if isinstance(event.get("usage"), dict):
            usage = event["usage"]
        for key in ("thread_id", "session_id"):
            if session_id is None and isinstance(event.get(key), str):
                session_id = event[key]
        thread = event.get("thread")
        if session_id is None and isinstance(thread, dict) and isinstance(thread.get("id"), str):
            session_id = thread["id"]
    return usage, session_id


def first_turn_input(
    *,
    instructions: str,
    result_schema: dict[str, Any],
    paper_id: str,
    source_text: str,
    source_fidelity: str,
    turn3: dict[str, Any],
    later_leads: dict[str, list[str]],
    paper_context: dict[str, Any],
    result_inventory: list[dict[str, Any]],
    issue_leads: list[dict[str, str]],
    targets: list[dict[str, Any]],
    established_prior_findings: list[dict[str, str]],
) -> str:
    target = targets[0]
    target_queue = [record["item_id"] for record in targets]
    current_inventory = next(
        item for item in result_inventory if item["result_id"] == target["item_id"]
    )
    current_leads = leads_for_result(issue_leads, target["item_id"])
    return f"""{instructions.rstrip()}

# Concrete paper-session assignment

- paper_id: {paper_id}
- total_target_results: {len(targets)}
- current_turn: 1
- current_result_id: {target['item_id']}

The complete supplied paper representation follows. Its fidelity is exactly `{source_fidelity}`. It is private construction input. Read it as a whole to recover paper-wide and section-wide assumptions. Never reproduce identifying paper metadata in the output.

<complete_paper_source>
{source_text}
</complete_paper_source>

# Complete Thread-A Turn-3 source audit

This is issue-location and dependency context, not ground truth. Independently verify it against the source.

<turn3_source_audit_json>
{json.dumps(turn3, ensure_ascii=False, indent=2)}
</turn3_source_audit_json>

# All later-chain issue leads

<all_later_chain_leads>
{json.dumps(later_leads, ensure_ascii=False, indent=2)}
</all_later_chain_leads>

# Paper-level context and source registry

Use only the listed `source_id` values in output locations. Do not copy paths into the result-node object.

<paper_context>
{json.dumps(paper_context, ensure_ascii=False, indent=2)}
</paper_context>

# Complete paper result inventory

<result_inventory>
{json.dumps(result_inventory, ensure_ascii=False, indent=2)}
</result_inventory>

# Complete paper issue-lead registry

<issue_leads>
{json.dumps(issue_leads, ensure_ascii=False, indent=2)}
</issue_leads>

# Ordered target queue

<target_result_ids>
{json.dumps(target_queue, ensure_ascii=False, indent=2)}
</target_result_ids>

# Current target

<current_result_inventory_item>
{json.dumps(current_inventory, ensure_ascii=False, indent=2)}
</current_result_inventory_item>

<current_target_turn3_record>
{json.dumps(target, ensure_ascii=False, indent=2)}
</current_target_turn3_record>

Adjudicate exactly these current-result leads, once each:

<current_issue_leads>
{json.dumps(current_leads, ensure_ascii=False, indent=2)}
</current_issue_leads>

# Exact per-turn output schema

Follow this schema literally. Do not invent, rename, flatten, or relocate fields.

<result_node_output_schema>
{json.dumps(result_schema, ensure_ascii=False, indent=2)}
</result_node_output_schema>

# Established prior findings ledger

Only IDs in this ledger may appear in `dependencies[].upstream_finding_ids`. It is empty on the first audited result.

<established_prior_findings>
{json.dumps(established_prior_findings, ensure_ascii=False, indent=2)}
</established_prior_findings>

Return exactly one JSON object for {target['item_id']}. Return no prose or Markdown fence.
"""


def resumed_turn_input(
    *,
    paper_id: str,
    turn_number: int,
    target: dict[str, Any],
    current_inventory: dict[str, Any],
    current_leads: list[dict[str, str]],
    source_ids: list[str],
    established_prior_findings: list[dict[str, str]],
) -> str:
    return f"""Continue the same private paper-session audit. Reuse the complete paper source, full Thread-A record, later-chain leads, paper context, source registry, result inventory, taxonomy definitions, and exact result-node JSON Schema supplied on turn 1.

Audit exactly this next result and no other result:

- paper_id: {paper_id}
- current_turn: {turn_number}
- current_result_id: {target['item_id']}

<current_result_inventory_item>
{json.dumps(current_inventory, ensure_ascii=False, indent=2)}
</current_result_inventory_item>

<current_target_turn3_record>
{json.dumps(target, ensure_ascii=False, indent=2)}
</current_target_turn3_record>

Adjudicate exactly these current-result leads, once each:

<current_issue_leads>
{json.dumps(current_leads, ensure_ascii=False, indent=2)}
</current_issue_leads>

Every output location must use one of these paper-level source IDs:

<allowed_source_ids>
{json.dumps(source_ids, ensure_ascii=False, indent=2)}
</allowed_source_ids>

Only finding IDs in this ledger may appear in `dependencies[].upstream_finding_ids`:

<established_prior_findings>
{json.dumps(established_prior_findings, ensure_ascii=False, indent=2)}
</established_prior_findings>

Apply the full-source standing-assumption rule. Explicitly reverse or reframe any original issue lead that controlling paper context resolves. Continue proof-step review after counterfactually repairing earlier errors. Return exactly one schema-compliant JSON object for {target['item_id']}, with no prose or Markdown fence.
"""


def initial_command(args: argparse.Namespace, workspace: Path, output_path: Path,
                    output_schema: Path | None = None) -> list[str]:
    return [
        args.codex_bin,
        "--config", "features.hooks=false",
        "exec",
        "--skip-git-repo-check",
        "--ignore-rules",
        "--json",
        *(["--output-schema", str(output_schema)] if output_schema else []),
        "--output-last-message", str(output_path),
        "--model", args.model,
        "--config", f'model_reasoning_effort="{args.reasoning_effort}"',
        "--sandbox", "read-only",
        "--cd", str(workspace),
        "-",
    ]


def resume_command(args: argparse.Namespace, session_id: str, output_path: Path,
                   output_schema: Path | None = None) -> list[str]:
    return [
        args.codex_bin,
        "--config", "features.hooks=false",
        "exec",
        "resume",
        "--skip-git-repo-check",
        "--ignore-rules",
        "--json",
        *(["--output-schema", str(output_schema)] if output_schema else []),
        "--output-last-message", str(output_path),
        "--model", args.model,
        "--config", f'model_reasoning_effort="{args.reasoning_effort}"',
        "--config", 'sandbox_mode="read-only"',
        session_id,
        "-",
    ]


def run_codex(
    *,
    command: list[str],
    model_input: str,
    environment: dict[str, str],
    timeout_seconds: int,
    cwd: Path,
) -> subprocess.CompletedProcess[str]:
    return run_with_recovery(command=command, model_input=model_input,
                             environment=environment, timeout_seconds=timeout_seconds, cwd=cwd)


def validate_turn_output(
    *,
    output_path: Path,
    result_schema: dict[str, Any],
    target: dict[str, Any],
    current_lead_ids: set[str],
    allowed_source_ids: set[str],
    established_prior_finding_ids: set[str],
) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    try:
        output = read_json(output_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return None, [f"invalid JSON output: {exc}"]
    if not isinstance(output, dict):
        return None, ["output must be one JSON object"]
    validator = jsonschema.Draft202012Validator(result_schema)
    structural_errors = list(validator.iter_errors(output))
    for error in sorted(structural_errors, key=lambda item: list(item.absolute_path)):
        json_path = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        errors.append(f"{json_path}: {error.message}")
    if structural_errors:
        return output, errors
    if output["result_id"] != target["item_id"]:
        errors.append(f"result_id {output['result_id']!r} does not match {target['item_id']!r}")
    errors.extend(
        semantic_errors(
            output,
            expected_lead_ids=current_lead_ids,
            allowed_source_ids=allowed_source_ids,
            allowed_upstream_error_ids=established_prior_finding_ids,
        )
    )
    return output, errors


def finding_ledger_entries(output: dict[str, Any]) -> list[dict[str, Any]]:
    if output.get("audit_status") == "rejected_missing_proof_source":
        return []
    entries: list[dict[str, Any]] = []
    for finding_id, (dimension, finding) in result_findings(output).items():
        entries.append(
            {
                "result_id": output["result_id"],
                "finding_id": finding_id,
                "dimension": dimension,
                "subtype": finding["subtype"],
                "error_statement": finding["error_statement"],
                "repair_assessment": finding["repair_assessment"],
                "source_result_impact_assessment": output["result_impact_assessment"],
            }
        )
    return entries


def paper_summary_result_ledger(
    result_outputs: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Keep only validated fields needed for paper-level contribution impact."""

    ledger: list[dict[str, Any]] = []
    for output in result_outputs:
        if output.get("audit_status") == "rejected_missing_proof_source":
            ledger.append({
                "result_id": output["result_id"],
                "audit_status": output["audit_status"],
                "open_questions": output["open_questions"],
            })
            continue
        ledger.append(
            {
                "result_id": output["result_id"],
                "theorem_failure_status": output["theorem_failure"]["status"],
                "findings": [
                    {
                        "finding_id": finding_id,
                        "dimension": dimension,
                        "subtype": finding["subtype"],
                        "error_statement": finding["error_statement"],
                        "selected_honest_repair": finding["repair_assessment"][
                            "selected_honest_repair"
                        ],
                    }
                    for finding_id, (dimension, finding) in result_findings(
                        output
                    ).items()
                ],
                "result_impact_assessment": output["result_impact_assessment"],
            }
        )
    return ledger


def propagation_turn_input(
    *,
    instructions: str,
    paper_id: str,
    turn_number: int,
    propagation_schema: dict[str, Any],
    propagation_assignment: dict[str, Any],
    source_finding_ledger: list[dict[str, Any]],
    source_ids: list[str],
) -> str:
    return f"""{instructions.rstrip()}

# Concrete propagation assignment

- paper_id: {paper_id}
- current_turn: {turn_number}
- propagation_candidate_count: {len(propagation_assignment['candidate_downstream_results'])}

These validated source findings, selected honest repairs, and source-result impact assessments are fixed inputs. Do not modify them.

<validated_source_finding_ledger>
{json.dumps(source_finding_ledger, ensure_ascii=False, indent=2)}
</validated_source_finding_ledger>

The runner computed these candidates from declared `depends_on` edges. Assess every candidate exactly once. Verify its statement, standing assumptions, dependency use, and relevant proof slice against the complete paper source retained in this session.

<propagation_assignment>
{json.dumps(propagation_assignment, ensure_ascii=False, indent=2)}
</propagation_assignment>

Every location must use one of these source IDs:

<allowed_source_ids>
{json.dumps(source_ids, ensure_ascii=False, indent=2)}
</allowed_source_ids>

Follow this schema literally. Do not return an ordinary result audit and do not output prose outside the JSON object.

<propagation_output_schema>
{json.dumps(propagation_schema, ensure_ascii=False, indent=2)}
</propagation_output_schema>

Return exactly one schema-compliant propagation JSON object and no Markdown fence.
"""


def propagation_affected_result_ids(output: dict[str, Any] | None) -> set[str]:
    if output is None:
        return set()
    return {
        item["downstream_result_id"]
        for item in output["downstream_assessments"]
        if item["propagated_result_impact_assessment"] is not None
    }


def validate_propagation_output(
    *,
    output_path: Path,
    propagation_schema: dict[str, Any],
    propagation_assignment: dict[str, Any],
    allowed_source_ids: set[str],
) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        output = read_json(output_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return None, [f"invalid JSON output: {exc}"]
    if not isinstance(output, dict):
        return None, ["output must be one JSON object"]

    errors: list[str] = []
    validator = jsonschema.Draft202012Validator(propagation_schema)
    structural_errors = list(validator.iter_errors(output))
    for error in sorted(structural_errors, key=lambda item: list(item.absolute_path)):
        json_path = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        errors.append(f"{json_path}: {error.message}")
    if structural_errors:
        return output, errors

    candidate_by_id = {
        item["downstream_result_id"]: item
        for item in propagation_assignment["candidate_downstream_results"]
    }
    assessment_ids = [
        item["downstream_result_id"] for item in output["downstream_assessments"]
    ]
    if assessment_ids != list(candidate_by_id):
        errors.append(
            "downstream_assessments must appear exactly once in candidate order; got "
            f"{assessment_ids!r}, expected {list(candidate_by_id)!r}"
        )

    for assessment in output["downstream_assessments"]:
        result_id = assessment["downstream_result_id"]
        candidate = candidate_by_id.get(result_id)
        if candidate is None:
            continue
        if set(assessment["upstream_finding_ids"]) != set(candidate["upstream_finding_ids"]):
            errors.append(
                f"{result_id}: upstream_finding_ids must match the assigned path findings"
            )
        for index, location in enumerate(assessment["use_locations"]):
            if location["source_id"] not in allowed_source_ids:
                errors.append(
                    f"{result_id}: use_locations[{index}] uses unknown source_id "
                    f"{location['source_id']!r}"
                )

        status = assessment["propagation_status"]
        impact = assessment["propagated_result_impact_assessment"]
        if status == "unaffected_interface_not_used" and impact is not None:
            errors.append(f"{result_id}: unaffected propagation requires a null impact field")
        if status != "unaffected_interface_not_used" and impact is None:
            errors.append(f"{result_id}: affected or indeterminate propagation requires an impact object")
        if impact is not None:
            level = impact["result_impact_level"]
            driver = impact["primary_driver_finding_id"]
            if status == "indeterminate":
                if level is not None or driver is not None:
                    errors.append(
                        f"{result_id}: indeterminate propagation requires null level and driver"
                    )
            else:
                if status == "survives_under_selected_repair" and level != 1:
                    errors.append(
                        f"{result_id}: a surviving original contract requires result impact Level 1"
                    )
                if level is None or driver is None:
                    errors.append(
                        f"{result_id}: determinate affected propagation requires level and driver"
                    )
                elif driver not in assessment["upstream_finding_ids"]:
                    errors.append(
                        f"{result_id}: impact driver is not one of its upstream finding IDs"
                    )

    return output, errors


def paper_summary_turn_input(
    *,
    instructions: str,
    paper_id: str,
    paper_impact_schema: dict[str, Any],
    result_outputs: list[dict[str, Any]],
    propagation_output: dict[str, Any] | None,
    source_ids: list[str],
) -> str:
    return f"""{instructions.rstrip()}

# Concrete paper-summary assignment

- paper_id: {paper_id}
- audited_result_count: {len(result_outputs)}

This lean ledger contains the validated findings, selected repairs, theorem-failure statuses, and result-impact assessments needed for paper-level evaluation. Treat it as fixed input; the complete preceding result turns remain in the session context.

<validated_result_impact_ledger>
{json.dumps(paper_summary_result_ledger(result_outputs), ensure_ascii=False, indent=2)}
</validated_result_impact_ledger>

The following targeted propagation audit is also a fixed validated input. It does not create source findings; use it to determine which unmarked downstream results and advertised contributions inherit the audited repairs. If it is null, no propagation turn was run or no eligible downstream theory candidate existed.

<validated_propagation_audit>
{json.dumps(propagation_output, ensure_ascii=False, indent=2)}
</validated_propagation_audit>

Every evidence location must use one of these source IDs:

<allowed_source_ids>
{json.dumps(source_ids, ensure_ascii=False, indent=2)}
</allowed_source_ids>

Follow this output schema literally:

<paper_impact_output_schema>
{json.dumps(paper_impact_schema, ensure_ascii=False, indent=2)}
</paper_impact_output_schema>

Return exactly one schema-compliant JSON object and no prose or Markdown fence.
"""


def validate_paper_impact_output(
    *,
    output_path: Path,
    paper_impact_schema: dict[str, Any],
    result_outputs: list[dict[str, Any]],
    propagation_output: dict[str, Any] | None,
    allowed_source_ids: set[str],
) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        output = read_json(output_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return None, [f"invalid JSON output: {exc}"]
    if not isinstance(output, dict):
        return None, ["output must be one JSON object"]
    errors: list[str] = []
    validator = jsonschema.Draft202012Validator(paper_impact_schema)
    structural_errors = list(validator.iter_errors(output))
    for error in sorted(structural_errors, key=lambda item: list(item.absolute_path)):
        json_path = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        errors.append(f"{json_path}: {error.message}")
    if not structural_errors:
        errors.extend(
            paper_impact_semantic_errors(
                output["paper_impact_assessment"],
                result_outputs=result_outputs,
                allowed_source_ids=allowed_source_ids,
                additional_affected_result_ids=propagation_affected_result_ids(
                    propagation_output
                ),
            )
        )
        if any(r.get("audit_status") == "rejected_missing_proof_source" for r in result_outputs) and not any(
            question.strip() for question in output["paper_open_questions"]
        ):
            errors.append("paper with rejected proof resources must record its coverage limitation in paper_open_questions")
    return output, errors


def write_manifest(run_dir: Path, manifest: dict[str, Any]) -> None:
    usage, errors = last_cumulative_usage(manifest.get("turns", []))
    manifest["usage"] = usage
    manifest["usage_errors"] = errors
    manifest["usage_basis"] = "last_observed_session_cumulative_counter"
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    try:
        paper_id = validate_safe_id(args.paper_id, "paper ID")
        if not re.fullmatch(r"paper_2026_[0-9]{3,}", paper_id):
            raise ValueError(f"paper ID must match paper_2026_<sequence>: {paper_id!r}")
        theory_topic = args.theory_topic.strip()
        if not theory_topic:
            raise ValueError("--theory-topic must be non-empty")
        source_path = args.source_file.resolve()
        source_fidelity = args.source_fidelity or infer_source_fidelity(source_path)
        turn3_path = args.turn3_audit.resolve()
        prompt_path = args.prompt.resolve()
        propagation_prompt_path = args.propagation_prompt.resolve()
        paper_impact_prompt_path = args.paper_impact_prompt.resolve()
        result_schema_path = args.result_schema.resolve()
        paper_impact_schema_path = args.paper_impact_schema.resolve()
        propagation_schema_path = args.propagation_schema.resolve()
        paper_schema_path = args.paper_schema.resolve()

        source_bytes = read_required_bytes(source_path)
        source_text = source_bytes.decode("utf-8", errors="replace")
        turn3_bytes = read_required_bytes(turn3_path)
        turn3 = json.loads(turn3_bytes.decode("utf-8"))
        if not isinstance(turn3, dict):
            raise ValueError("Turn-3 audit must be one JSON object")
        instructions = prompt_path.read_text(encoding="utf-8")
        propagation_instructions = (
            propagation_prompt_path.read_text(encoding="utf-8")
            if args.enable_propagation_audit
            else ""
        )
        paper_impact_instructions = paper_impact_prompt_path.read_text(encoding="utf-8")
        result_schema = read_json(result_schema_path)
        paper_impact_schema = read_json(paper_impact_schema_path)
        propagation_schema = read_json(propagation_schema_path)
        paper_schema = read_json(paper_schema_path)
        if not all(
            isinstance(schema, dict)
            for schema in (
                result_schema,
                paper_impact_schema,
                propagation_schema,
                paper_schema,
            )
        ):
            raise ValueError("output schemas must be JSON objects")
        jsonschema.Draft202012Validator.check_schema(result_schema)
        jsonschema.Draft202012Validator.check_schema(paper_impact_schema)
        jsonschema.Draft202012Validator.check_schema(propagation_schema)
        jsonschema.Draft202012Validator.check_schema(paper_schema)

        later_path = args.later_chain_leads.resolve() if args.later_chain_leads else None
        later_bytes = read_required_bytes(later_path) if later_path else None
        later_value = json.loads(later_bytes.decode("utf-8")) if later_bytes else None
        later_leads = normalize_later_leads(later_value)
        records = material_records(turn3)
        targets = select_targets(records, later_leads, args.result_ids)
        result_inventory = build_result_inventory(records)
        issue_leads = build_issue_leads(records, later_leads)

        sources: list[dict[str, Any]] = [
            {
                "source_id": "paper_source",
                "kind": "original_paper",
                "path": str(source_path),
                "fidelity": source_fidelity,
            },
            {
                "source_id": "turn3_audit",
                "kind": "thread_a_turn3",
                "path": str(turn3_path),
            },
        ]
        if later_path:
            sources.append(
                {
                    "source_id": "later_chain_leads",
                    "kind": "later_chain_leads",
                    "path": str(later_path),
                }
            )
        paper_context = {"theory_topic": theory_topic, "sources": sources}
        source_ids = [source["source_id"] for source in sources]
        target_result_ids = [target["item_id"] for target in targets]
    except (
        OSError,
        UnicodeError,
        ValueError,
        json.JSONDecodeError,
        jsonschema.SchemaError,
    ) as exc:
        print(f"input error: {exc}", file=sys.stderr)
        return 2

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + f"_{paper_id}_paper_session"
    run_dir = args.runs_root.resolve() / run_id
    if run_dir.exists():
        print(f"refusing to overwrite run directory: {run_dir}", file=sys.stderr)
        return 2
    outputs_dir = run_dir / "outputs"
    outputs_dir.mkdir(parents=True)
    shutil.copy2(prompt_path, run_dir / "prompt_snapshot.md")
    shutil.copy2(paper_impact_prompt_path, run_dir / "paper_impact_prompt_snapshot.md")
    shutil.copy2(result_schema_path, run_dir / "result_schema_snapshot.json")
    shutil.copy2(paper_impact_schema_path, run_dir / "paper_impact_schema_snapshot.json")
    if args.enable_propagation_audit:
        shutil.copy2(
            propagation_prompt_path,
            run_dir / "propagation_prompt_snapshot.md",
        )
        shutil.copy2(propagation_schema_path, run_dir / "propagation_schema_snapshot.json")
    shutil.copy2(paper_schema_path, run_dir / "paper_schema_snapshot.json")
    result_wire_schema = write_transport_schema(result_schema, run_dir / "result_transport_schema.json")
    impact_wire_schema = write_transport_schema(paper_impact_schema, run_dir / "impact_transport_schema.json")
    propagation_wire_schema = (
        write_transport_schema(propagation_schema, run_dir / "propagation_transport_schema.json")
        if args.enable_propagation_audit else None
    )

    paper_session_input = {
        "schema_version": "paper_session_input_v3",
        "paper_id": paper_id,
        "paper_context": paper_context,
        "result_inventory": result_inventory,
        "target_result_ids": target_result_ids,
        "issue_leads": issue_leads,
    }
    write_json(run_dir / "paper_session_input.json", paper_session_input)

    private_exposures = [
        {
            "kind": "complete_paper_source",
            "source_id": "paper_source",
            "path": str(source_path),
            "sha256": sha256_bytes(source_bytes),
            "bytes": len(source_bytes),
            "first_turn_only": True,
        },
        {
            "kind": "complete_turn3_source_audit",
            "source_id": "turn3_audit",
            "path": str(turn3_path),
            "sha256": sha256_bytes(turn3_bytes),
            "bytes": len(turn3_bytes),
            "first_turn_only": True,
        },
    ]
    if later_path and later_bytes is not None:
        private_exposures.append(
            {
                "kind": "later_chain_leads",
                "source_id": "later_chain_leads",
                "path": str(later_path),
                "sha256": sha256_bytes(later_bytes),
                "bytes": len(later_bytes),
                "first_turn_only": True,
            }
        )

    manifest: dict[str, Any] = {
        "schema_version": (
            "paper_result_audit_run_v3_with_propagation"
            if args.enable_propagation_audit
            else "paper_result_audit_run_v3"
        ),
        "run_id": run_id,
        "paper_id": paper_id,
        "theory_topic": theory_topic,
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "auth_mode": args.auth_mode,
        "thread_mode": "one_persistent_session_per_paper",
        "result_turn_policy": "one_combined_finding_repair_and_result_impact_audit_per_result",
        "propagation_turn_policy": (
            "one_targeted_repair_to_downstream_contract_turn"
            if args.enable_propagation_audit
            else "disabled"
        ),
        "paper_summary_turn_policy": "one_final_paper_impact_turn_after_all_results",
        "agent_sandbox": "read-only",
        "network_tools": "disabled",
        "structured_output_mode": "cli_output_schema_plus_canonical_client_validation",
        "max_output_repairs": args.max_output_repairs,
        "target_selection": (
            "explicit_override"
            if args.result_ids
            else "explicit_issue_nodes_only"
        ),
        "target_result_ids": target_result_ids,
        "private_exposures": private_exposures,
        "prompt_sha256": sha256_bytes(instructions.encode("utf-8")),
        "propagation_prompt_sha256": (
            sha256_bytes(propagation_instructions.encode("utf-8"))
            if args.enable_propagation_audit
            else None
        ),
        "paper_impact_prompt_sha256": sha256_bytes(
            paper_impact_instructions.encode("utf-8")
        ),
        "result_schema_sha256": sha256_bytes(result_schema_path.read_bytes()),
        "propagation_schema_sha256": (
            sha256_bytes(propagation_schema_path.read_bytes())
            if args.enable_propagation_audit
            else None
        ),
        "paper_impact_schema_sha256": sha256_bytes(
            paper_impact_schema_path.read_bytes()
        ),
        "paper_schema_sha256": sha256_bytes(paper_schema_path.read_bytes()),
        "paper_session_input_path": str(run_dir / "paper_session_input.json"),
        "paper_audit_path": None,
        "started_at": utc_now(),
        "status": "dry_run" if args.dry_run else "running",
        "session_id": None,
        "turns": [],
    }
    write_manifest(run_dir, manifest)
    if args.dry_run:
        manifest["completed_at"] = utc_now()
        write_manifest(run_dir, manifest)
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
        return 0

    environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    session_id: str | None = None
    established_prior_findings: list[dict[str, Any]] = []
    result_outputs: list[dict[str, Any]] = []
    propagation_output: dict[str, Any] | None = None
    paper_summary_output: dict[str, Any] | None = None
    with tempfile.TemporaryDirectory(prefix=f"paperproof-taxonomy-{paper_id}-") as temp:
        workspace = Path(temp) / "workspace"
        workspace.mkdir()
        for index, target in enumerate(targets, 1):
            result_id = target["item_id"]
            output_path = outputs_dir / f"{index:03d}_{result_id}.json"
            current_inventory = next(
                item for item in result_inventory if item["result_id"] == result_id
            )
            current_leads = leads_for_result(issue_leads, result_id)
            if index == 1:
                model_input = first_turn_input(
                    instructions=instructions,
                    result_schema=result_schema,
                    paper_id=paper_id,
                    source_text=source_text,
                    source_fidelity=source_fidelity,
                    turn3=turn3,
                    later_leads=later_leads,
                    paper_context=paper_context,
                    result_inventory=result_inventory,
                    issue_leads=issue_leads,
                    targets=targets,
                    established_prior_findings=established_prior_findings,
                )
                command = initial_command(args, workspace, output_path, result_wire_schema)
            else:
                if session_id is None:
                    manifest.update({"status": "failed_no_session_id", "completed_at": utc_now()})
                    write_manifest(run_dir, manifest)
                    print("cannot resume: first turn yielded no session ID", file=sys.stderr)
                    return 1
                model_input = resumed_turn_input(
                    paper_id=paper_id,
                    turn_number=index,
                    target=target,
                    current_inventory=current_inventory,
                    current_leads=current_leads,
                    source_ids=source_ids,
                    established_prior_findings=established_prior_findings,
                )
                command = resume_command(args, session_id, output_path, result_wire_schema)

            model_input += "\n\n" + BOOKKEEPING_RULES
            turn_manifest: dict[str, Any] = {
                "output_bookkeeping_policy": REPAIR_POLICY_VERSION,
                "turn_number": index,
                "result_id": result_id,
                "mode": "initial" if index == 1 else "resume",
                "model_input_sha256": sha256_bytes(model_input.encode("utf-8")),
                "model_input_bytes": len(model_input.encode("utf-8")),
                "started_at": utc_now(),
                "status": "running",
                "output_path": str(output_path),
                "current_lead_ids": [lead["lead_id"] for lead in current_leads],
                "established_prior_finding_ids": [
                    entry["finding_id"] for entry in established_prior_findings
                ],
            }
            manifest["turns"].append(turn_manifest)
            write_manifest(run_dir, manifest)
            try:
                process = run_codex(
                    command=command,
                    model_input=model_input,
                    environment=environment,
                    timeout_seconds=args.timeout_seconds,
                    cwd=workspace,
                )
            except subprocess.TimeoutExpired:
                turn_manifest.update({"status": "timeout", "completed_at": utc_now()})
                manifest.update({"status": "timeout", "completed_at": utc_now()})
                write_manifest(run_dir, manifest)
                print(f"turn {index} timed out after {args.timeout_seconds}s", file=sys.stderr)
                return 1

            usage, observed_session_id = extract_event_metadata(process.stdout)
            turn_manifest.update(transport_fields(process))
            if index == 1:
                session_id = observed_session_id
                manifest["session_id"] = session_id
            elif observed_session_id and observed_session_id != session_id:
                turn_manifest["session_id_warning"] = (
                    f"resume reported {observed_session_id}, expected {session_id}"
                )
            turn_manifest.update(
                {
                    "completed_at": utc_now(),
                    "returncode": process.returncode,
                    "usage": usage,
                    "session_id": observed_session_id,
                }
            )
            if process.returncode != 0:
                turn_manifest["status"] = "failed"
                turn_manifest["error_tail"] = process.stderr[-2000:]
                manifest.update({"status": "failed", "completed_at": utc_now()})
                write_manifest(run_dir, manifest)
                print(f"turn {index} failed ({process.returncode}): {process.stderr[-2000:]}", file=sys.stderr)
                return 1
            if not output_path.is_file():
                turn_manifest["status"] = "failed_no_output"
                manifest.update({"status": "failed_no_output", "completed_at": utc_now()})
                write_manifest(run_dir, manifest)
                print(f"turn {index} completed without an output file", file=sys.stderr)
                return 1

            output, validation_errors = validate_turn_output(
                output_path=output_path,
                result_schema=result_schema,
                target=target,
                current_lead_ids={lead["lead_id"] for lead in current_leads},
                allowed_source_ids=set(source_ids),
                established_prior_finding_ids={
                    entry["finding_id"] for entry in established_prior_findings
                },
            )
            output, validation_errors, output_path = repair_invalid_output(
                runtime=sys.modules[__name__], args=args, output_path=output_path,
                output=output, errors=validation_errors, turn=turn_manifest,
                schema=result_schema, wire_schema_path=result_wire_schema,
                session_id=session_id, environment=environment, workspace=workspace,
                validate=lambda path: validate_turn_output(
                    output_path=path, result_schema=result_schema, target=target,
                    current_lead_ids={lead["lead_id"] for lead in current_leads},
                    allowed_source_ids=set(source_ids),
                    established_prior_finding_ids={entry["finding_id"] for entry in established_prior_findings}),
                checkpoint=lambda: write_manifest(run_dir, manifest))
            turn_manifest.update(
                {
                    "output_path": str(output_path),
                    "output_sha256": sha256_bytes(output_path.read_bytes()),
                    "output_bytes": output_path.stat().st_size,
                    "validation_errors": validation_errors,
                    "status": "completed" if not validation_errors else "invalid_output",
                }
            )
            write_manifest(run_dir, manifest)
            if validation_errors:
                manifest.update({"status": "invalid_output", "completed_at": utc_now()})
                write_manifest(run_dir, manifest)
                print(f"turn {index} output failed validation:", file=sys.stderr)
                for message in validation_errors:
                    print(f"- {message}", file=sys.stderr)
                print(f"preserved output for review: {output_path}", file=sys.stderr)
                return 1
            assert output is not None
            result_outputs.append(output)
            established_prior_findings.extend(finding_ledger_entries(output))

        if session_id is None:
            manifest.update({"status": "failed_no_session_id", "completed_at": utc_now()})
            write_manifest(run_dir, manifest)
            print("cannot run paper summary: no session ID", file=sys.stderr)
            return 1

        turn_cursor = len(targets)
        if args.enable_propagation_audit:
            propagation_assignment = build_propagation_assignment(
                result_inventory=result_inventory,
                result_outputs=result_outputs,
            )
            if propagation_assignment is None:
                manifest["propagation_audit"] = {
                    "status": "not_run_no_source_findings_or_eligible_descendants"
                }
                write_manifest(run_dir, manifest)
            else:
                turn_cursor += 1
                propagation_output_path = (
                    outputs_dir / f"{turn_cursor:03d}_propagation_audit.json"
                )
                propagation_input = propagation_turn_input(
                    instructions=propagation_instructions,
                    paper_id=paper_id,
                    turn_number=turn_cursor,
                    propagation_schema=propagation_schema,
                    propagation_assignment=propagation_assignment,
                    source_finding_ledger=[
                        entry
                        for entry in established_prior_findings
                        if entry["finding_id"]
                        in set(propagation_assignment["source_finding_ids"])
                    ],
                    source_ids=source_ids,
                )
                propagation_manifest: dict[str, Any] = {
                    "turn_number": turn_cursor,
                    "result_id": None,
                    "turn_kind": "propagation_audit",
                    "mode": "resume",
                    "model_input_sha256": sha256_bytes(
                        propagation_input.encode("utf-8")
                    ),
                    "model_input_bytes": len(propagation_input.encode("utf-8")),
                    "started_at": utc_now(),
                    "status": "running",
                    "output_path": str(propagation_output_path),
                    "source_finding_ids": propagation_assignment[
                        "source_finding_ids"
                    ],
                    "candidate_downstream_result_ids": [
                        item["downstream_result_id"]
                        for item in propagation_assignment[
                            "candidate_downstream_results"
                        ]
                    ],
                }
                manifest["turns"].append(propagation_manifest)
                write_manifest(run_dir, manifest)
                try:
                    process = run_codex(
                        command=resume_command(
                            args, session_id, propagation_output_path, propagation_wire_schema
                        ),
                        model_input=propagation_input,
                        environment=environment,
                        timeout_seconds=args.timeout_seconds,
                        cwd=workspace,
                    )
                except subprocess.TimeoutExpired:
                    propagation_manifest.update(
                        {"status": "timeout", "completed_at": utc_now()}
                    )
                    manifest.update(
                        {"status": "timeout", "completed_at": utc_now()}
                    )
                    write_manifest(run_dir, manifest)
                    print(
                        "propagation turn timed out after "
                        f"{args.timeout_seconds}s",
                        file=sys.stderr,
                    )
                    return 1

                usage, observed_session_id = extract_event_metadata(process.stdout)
                propagation_manifest.update(transport_fields(process))
                if observed_session_id and observed_session_id != session_id:
                    propagation_manifest["session_id_warning"] = (
                        f"resume reported {observed_session_id}, expected {session_id}"
                    )
                propagation_manifest.update(
                    {
                        "completed_at": utc_now(),
                        "returncode": process.returncode,
                        "usage": usage,
                        "session_id": observed_session_id,
                    }
                )
                if process.returncode != 0:
                    propagation_manifest["status"] = "failed"
                    propagation_manifest["error_tail"] = process.stderr[-2000:]
                    manifest.update(
                        {"status": "failed", "completed_at": utc_now()}
                    )
                    write_manifest(run_dir, manifest)
                    print(
                        "propagation turn failed "
                        f"({process.returncode}): {process.stderr[-2000:]}",
                        file=sys.stderr,
                    )
                    return 1
                if not propagation_output_path.is_file():
                    propagation_manifest["status"] = "failed_no_output"
                    manifest.update(
                        {"status": "failed_no_output", "completed_at": utc_now()}
                    )
                    write_manifest(run_dir, manifest)
                    print(
                        "propagation turn completed without an output file",
                        file=sys.stderr,
                    )
                    return 1

                propagation_output, propagation_errors = validate_propagation_output(
                    output_path=propagation_output_path,
                    propagation_schema=propagation_schema,
                    propagation_assignment=propagation_assignment,
                    allowed_source_ids=set(source_ids),
                )
                propagation_output, propagation_errors, propagation_output_path = repair_invalid_output(
                    runtime=sys.modules[__name__], args=args, output_path=propagation_output_path,
                    output=propagation_output, errors=propagation_errors, turn=propagation_manifest,
                    schema=propagation_schema, wire_schema_path=propagation_wire_schema,
                    session_id=session_id, environment=environment, workspace=workspace,
                    validate=lambda path: validate_propagation_output(
                        output_path=path, propagation_schema=propagation_schema,
                        propagation_assignment=propagation_assignment, allowed_source_ids=set(source_ids)),
                    checkpoint=lambda: write_manifest(run_dir, manifest))
                propagation_manifest.update(
                    {
                        "output_path": str(propagation_output_path),
                        "output_sha256": sha256_bytes(
                            propagation_output_path.read_bytes()
                        ),
                        "output_bytes": propagation_output_path.stat().st_size,
                        "validation_errors": propagation_errors,
                        "status": (
                            "completed" if not propagation_errors else "invalid_output"
                        ),
                    }
                )
                write_manifest(run_dir, manifest)
                if propagation_errors:
                    manifest.update(
                        {"status": "invalid_output", "completed_at": utc_now()}
                    )
                    write_manifest(run_dir, manifest)
                    print("propagation output failed validation:", file=sys.stderr)
                    for message in propagation_errors:
                        print(f"- {message}", file=sys.stderr)
                    print(
                        f"preserved output for review: {propagation_output_path}",
                        file=sys.stderr,
                    )
                    return 1
                assert propagation_output is not None

        summary_turn_number = turn_cursor + 1
        summary_output_path = outputs_dir / f"{summary_turn_number:03d}_paper_impact.json"
        summary_input = paper_summary_turn_input(
            instructions=paper_impact_instructions,
            paper_id=paper_id,
            paper_impact_schema=paper_impact_schema,
            result_outputs=result_outputs,
            propagation_output=propagation_output,
            source_ids=source_ids,
        )
        summary_manifest: dict[str, Any] = {
            "turn_number": summary_turn_number,
            "result_id": None,
            "turn_kind": "paper_summary",
            "mode": "resume",
            "model_input_sha256": sha256_bytes(summary_input.encode("utf-8")),
            "model_input_bytes": len(summary_input.encode("utf-8")),
            "started_at": utc_now(),
            "status": "running",
            "output_path": str(summary_output_path),
        }
        manifest["turns"].append(summary_manifest)
        write_manifest(run_dir, manifest)
        try:
            process = run_codex(
                command=resume_command(args, session_id, summary_output_path, impact_wire_schema),
                model_input=summary_input,
                environment=environment,
                timeout_seconds=args.timeout_seconds,
                cwd=workspace,
            )
        except subprocess.TimeoutExpired:
            summary_manifest.update({"status": "timeout", "completed_at": utc_now()})
            manifest.update({"status": "timeout", "completed_at": utc_now()})
            write_manifest(run_dir, manifest)
            print(
                f"paper-summary turn timed out after {args.timeout_seconds}s",
                file=sys.stderr,
            )
            return 1

        usage, observed_session_id = extract_event_metadata(process.stdout)
        summary_manifest.update(transport_fields(process))
        if observed_session_id and observed_session_id != session_id:
            summary_manifest["session_id_warning"] = (
                f"resume reported {observed_session_id}, expected {session_id}"
            )
        summary_manifest.update(
            {
                "completed_at": utc_now(),
                "returncode": process.returncode,
                "usage": usage,
                "session_id": observed_session_id,
            }
        )
        if process.returncode != 0:
            summary_manifest["status"] = "failed"
            summary_manifest["error_tail"] = process.stderr[-2000:]
            manifest.update({"status": "failed", "completed_at": utc_now()})
            write_manifest(run_dir, manifest)
            print(
                f"paper-summary turn failed ({process.returncode}): {process.stderr[-2000:]}",
                file=sys.stderr,
            )
            return 1
        if not summary_output_path.is_file():
            summary_manifest["status"] = "failed_no_output"
            manifest.update({"status": "failed_no_output", "completed_at": utc_now()})
            write_manifest(run_dir, manifest)
            print("paper-summary turn completed without an output file", file=sys.stderr)
            return 1

        paper_summary_output, summary_errors = validate_paper_impact_output(
            output_path=summary_output_path,
            paper_impact_schema=paper_impact_schema,
            result_outputs=result_outputs,
            propagation_output=propagation_output,
            allowed_source_ids=set(source_ids),
        )
        paper_summary_output, summary_errors, summary_output_path = repair_invalid_output(
            runtime=sys.modules[__name__], args=args, output_path=summary_output_path,
            output=paper_summary_output, errors=summary_errors, turn=summary_manifest,
            schema=paper_impact_schema, wire_schema_path=impact_wire_schema,
            session_id=session_id, environment=environment, workspace=workspace,
            validate=lambda path: validate_paper_impact_output(
                output_path=path, paper_impact_schema=paper_impact_schema,
                result_outputs=result_outputs, propagation_output=propagation_output,
                allowed_source_ids=set(source_ids)),
            checkpoint=lambda: write_manifest(run_dir, manifest))
        summary_manifest.update(
            {
                "output_path": str(summary_output_path),
                "output_sha256": sha256_bytes(summary_output_path.read_bytes()),
                "output_bytes": summary_output_path.stat().st_size,
                "validation_errors": summary_errors,
                "status": "completed" if not summary_errors else "invalid_output",
            }
        )
        write_manifest(run_dir, manifest)
        if summary_errors:
            manifest.update({"status": "invalid_output", "completed_at": utc_now()})
            write_manifest(run_dir, manifest)
            print("paper-summary output failed validation:", file=sys.stderr)
            for message in summary_errors:
                print(f"- {message}", file=sys.stderr)
            print(f"preserved output for review: {summary_output_path}", file=sys.stderr)
            return 1

    assert paper_summary_output is not None
    paper_audit = {
        "schema_version": paper_schema["properties"]["schema_version"]["const"],
        "paper_id": paper_id,
        "paper_context": paper_context,
        "result_inventory": result_inventory,
        "target_result_ids": target_result_ids,
        "issue_leads": issue_leads,
        "result_audits": result_outputs,
        "paper_impact_assessment": paper_summary_output["paper_impact_assessment"],
        "paper_open_questions": paper_summary_output["paper_open_questions"],
    }
    if args.enable_propagation_audit:
        paper_audit["propagation_audit"] = propagation_output
    paper_validator = make_paper_validator(
        paper_schema,
        result_schema,
        propagation_schema,
    )
    final_errors = [error.message for error in paper_validator.iter_errors(paper_audit)]
    final_errors.extend(paper_semantic_errors(paper_audit))
    if final_errors:
        manifest.update(
            {
                "status": "invalid_paper_assembly",
                "completed_at": utc_now(),
                "paper_assembly_errors": final_errors,
            }
        )
        write_manifest(run_dir, manifest)
        print("paper-level assembly failed validation:", file=sys.stderr)
        for message in final_errors:
            print(f"- {message}", file=sys.stderr)
        return 1

    paper_audit_path = run_dir / "paper_audit.json"
    write_json(paper_audit_path, paper_audit)
    manifest.update(
        {
            "status": "completed",
            "completed_at": utc_now(),
            "paper_audit_path": str(paper_audit_path),
            "paper_audit_sha256": sha256_bytes(paper_audit_path.read_bytes()),
        }
    )
    write_manifest(run_dir, manifest)
    print(f"completed paper-session audit: {paper_id}")
    print(f"results: {len(targets)}")
    print(f"paper audit: {paper_audit_path}")
    print(f"run directory: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
