"""Request-time JSON constraints and bounded, recorded same-session format repair.

The canonical schema and semantic validator remain authoritative. No output is
silently patched, no failed file is overwritten, and repair never selects a new
mathematical verdict to make validation pass.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
from collections import Counter
import jsonschema


REPAIR_POLICY_VERSION = "2026-10-11-bookkeeping-patch-v2"


BOOKKEEPING_RULES = (
    "Serialization check (the mathematical standard is unchanged): assessed_after_repairing contains "
    "only other findings in this SAME result, with no self-reference or cycle. Upstream findings "
    "belong in dependencies[].upstream_finding_ids, never in assessed_after_repairing. Dependency "
    "use_status and ID lists must agree: valid_use has both lists empty; invalid_use has local IDs "
    "only; inherited_blocker has upstream IDs only; mixed has both. Do not invent or drop an error "
    "to meet this table; use indeterminate when the interface judgment is unresolved. In reviewer "
    "output, group proposals sharing final IDs into one retained row, preserving the explanations "
    "for each candidate; cover each supplied candidate and final ID exactly once."
)


def regroup_review_rows(value):
    """Combine overlapping retained mapping groups, retaining every old rationale.

    The result audit is untouched. Conflicting candidate decisions and disjoint
    target assignments are not resolved here. The raw mapping remains on disk.
    """
    rows = value.get("proposal_reviews") if isinstance(value, dict) else None
    if not isinstance(rows, list):
        return value
    if any(not isinstance(r, dict) or set(r) != {"candidate_ids", "final_ids", "verdict", "explanation", "locations"}
           or not all(isinstance(r[k], list) for k in ("candidate_ids", "final_ids", "locations"))
           or not all(isinstance(x, str) for k in ("candidate_ids", "final_ids") for x in r[k])
           or not isinstance(r["explanation"], str) for r in rows):
        return value
    groups = []
    for i, row in enumerate(rows):
        connected = [g for g in groups if row["verdict"] == "retained" and row["final_ids"]
                     and any(rows[j]["verdict"] == "retained"
                             and set(rows[j]["final_ids"]) & set(row["final_ids"]) for j in g)]
        if connected:
            merged = [i]
            for g in connected:
                merged.extend(g); groups.remove(g)
            groups.append(sorted(merged))
        else:
            groups.append([i])
    if all(len(g) == 1 for g in groups):
        return value
    new_rows = []
    for group in sorted(groups, key=min):
        members = [rows[i] for i in group]
        if len(group) == 1:
            new_rows.append(copy.deepcopy(members[0])); continue
        new_rows.append({"candidate_ids": list(dict.fromkeys(x for r in members for x in r["candidate_ids"])),
                         "final_ids": list(dict.fromkeys(x for r in members for x in r["final_ids"])),
                         "verdict": "retained",
                         "explanation": "\n\n".join("[" + ", ".join(r["candidate_ids"]) + "]\n" + r["explanation"] for r in members),
                         "locations": list({json.dumps(loc, sort_keys=True): loc for r in members for loc in r["locations"]}.values())})
    covered = Counter(x for r in new_rows for x in r["candidate_ids"])
    if any(n != 1 for n in covered.values()):
        return value  # Conflicting or otherwise unresolved candidate assignments.
    result = copy.deepcopy(value)
    result["proposal_reviews"] = new_rows
    return result


def normalize_bookkeeping(value):
    """Two deterministic, logged representation fixes; no scientific selection."""
    updated = regroup_review_rows(value)
    actions = ["regroup_retained_proposal_rows_preserving_all_rationales"] if updated != value else []
    updated = copy.deepcopy(updated)
    if not isinstance(updated, dict):
        return updated, actions
    root = updated.get("result_audit", updated)
    if not isinstance(root, dict):
        return updated, actions
    dependencies = root.get("dependencies", [])
    if not isinstance(dependencies, list): return updated, actions
    upstream = {fid for d in dependencies if isinstance(d, dict)
                and isinstance(d.get("upstream_finding_ids"), list)
                for fid in d["upstream_finding_ids"] if isinstance(fid, str)}
    local = {f["finding_id"] for f in _findings(root)}
    for f in _findings(root):
        ids = f.get("assessed_after_repairing")
        if not isinstance(ids, list):
            continue
        # An upstream reference is removed here only if its dependency record
        # already retains it. Unknown IDs and actual local cycles stay unresolved.
        removed = [x for x in ids if isinstance(x, str) and x in upstream and x not in local]
        if removed:
            f["assessed_after_repairing"] = [x for x in ids if x not in removed]
            actions.append({"finding_id": f["finding_id"], "remove_already_recorded_upstream_ids_from_local_order": removed})
    return updated, actions


def bookkeeping_slots(value):
    """Paths a repair agent may replace without regenerating scientific prose."""
    slots = {}
    counts = Counter(f["finding_id"] for f in _findings(value))
    def walk(node, path=""):
        if isinstance(node, dict):
            if isinstance(node.get("finding_id"), str) and "assessed_after_repairing" in node:
                slots[path + "/assessed_after_repairing"] = node["assessed_after_repairing"]
                if counts[node["finding_id"]] > 1:
                    slots[path + "/finding_id"] = node["finding_id"]
            for k, v in node.items():
                child = path + "/" + k.replace("~", "~0").replace("/", "~1")
                if k in ("primary_driver_finding_id", "primary_driver_result_id"):
                    slots[child] = v
                if k == "dependencies" and isinstance(v, list):
                    for i, dep in enumerate(v):
                        if isinstance(dep, dict):
                            for field in ("use_status", "local_finding_ids", "upstream_finding_ids"):
                                if field in dep: slots[f"{child}/{i}/{field}"] = dep[field]
                if k == "proposal_reviews" and isinstance(v, list):
                    for i, row in enumerate(v):
                        if isinstance(row, dict) and "final_ids" in row:
                            slots[f"{child}/{i}/final_ids"] = row["final_ids"]
                walk(v, child)
        elif isinstance(node, list):
            for i, v in enumerate(node): walk(v, path + f"/{i}")
    walk(value)
    return slots


def bookkeeping_patch_schema(slots):
    return {"type": "object", "additionalProperties": False, "required": ["edits", "unresolved_reason"],
            "properties": {
                "edits": {"type": "array", "items": {"type": "object", "additionalProperties": False,
                    "required": ["path", "value_json"], "properties": {
                        "path": {"type": "string", "enum": list(slots)},
                        "value_json": {"type": "string"}}}},
                "unresolved_reason": {"type": "string"}}}


def apply_bookkeeping_patch(original, patch, slots):
    errors = [e.message for e in jsonschema.Draft202012Validator(bookkeeping_patch_schema(slots)).iter_errors(patch)]
    if errors:
        raise ValueError("Invalid bookkeeping patch: " + "; ".join(errors))
    result = copy.deepcopy(original)
    seen = set()
    for edit in patch["edits"]:
        path = edit["path"]
        if path in seen: raise ValueError("Repeated patch path: " + path)
        seen.add(path)
        keys = [x.replace("~1", "/").replace("~0", "~") for x in path.split("/")[1:]]
        parent = result
        for key in keys[:-1]: parent = parent[int(key)] if isinstance(parent, list) else parent[key]
        parent[keys[-1]] = json.loads(edit["value_json"])
    return result


def transport_schema(schema):
    """Project canonical nullable unions to the supported structured-output subset.

    uniqueItems is checked by the unchanged client schema. The only oneOf form
    accepted here is null versus a non-null object; anyOf is equivalent for it.
    Reject optional properties and external references instead of inventing data.
    """
    definitions = schema.get("$defs", {})

    def visit(node):
        if isinstance(node, list):
            return [visit(x) for x in node]
        if not isinstance(node, dict):
            return node
        out = {}
        for key, value in node.items():
            if key in {"$schema", "$id", "uniqueItems"}:
                continue
            if key == "$ref" and not value.startswith("#/$defs/"):
                raise ValueError("Wire schema needs resolved local references")
            if key == "oneOf":
                alternatives = []
                for branch in value:
                    resolved = branch
                    if "$ref" in branch:
                        ref = branch["$ref"]
                        if not ref.startswith("#/$defs/"):
                            raise ValueError("External nullable reference")
                        resolved = definitions[ref[len("#/$defs/"):]]
                    alternatives.append(resolved.get("type"))
                if len(alternatives) != 2 or set(alternatives) != {"null", "object"}:
                    raise ValueError("Only disjoint null/object oneOf is supported")
                out["anyOf"] = visit(value)
            elif key == "const":
                out["enum"] = [copy.deepcopy(value)]
            else:
                out[key] = visit(value)
        if node.get("type") == "object":
            if set(node.get("properties", {})) != set(node.get("required", [])):
                raise ValueError("Wire schema requires all properties to be required")
            if node.get("additionalProperties") is not False:
                raise ValueError("Wire schema requires additionalProperties=false")
        return out

    return visit(schema)


def write_transport_schema(schema, path):
    path = Path(path)
    path.write_text(json.dumps(transport_schema(schema), ensure_ascii=False, indent=2) + "\n")
    return path


def _findings(value):
    found = []
    def walk(node):
        if isinstance(node, dict):
            if isinstance(node.get("finding_id"), str):
                found.append(node)
            for child in node.values():
                walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)
    walk(value)
    return found


def _review_decisions_preserved(before, after):
    """Allow removal only of already-covered, same-verdict/same-target rows.

    Remaining proposal explanations stay verbatim. A removed row must be covered
    by an original row that survives with the same targets. For this exception,
    require the complete result audit to remain byte-value equivalent as JSON.
    Final-ID bookkeeping without row removal follows the existing guard.
    """
    old, new = before.get("proposal_reviews"), after.get("proposal_reviews")
    if not isinstance(old, list) or not isinstance(new, list):
        return False
    regrouped = regroup_review_rows(before)
    if regrouped != before and new == regrouped.get("proposal_reviews"):
        return _without_local_order(before.get("result_audit")) == _without_local_order(after.get("result_audit"))

    def key(row):
        if not isinstance(row, dict):
            return None
        ids = row.get("candidate_ids")
        if not isinstance(ids, list) or not ids or not all(isinstance(x, str) for x in ids):
            return None
        return json.dumps({"candidate_ids": sorted(set(ids)),
                           "verdict": row.get("verdict"),
                           "explanation": row.get("explanation")}, sort_keys=True)

    old_keys, new_keys = [key(x) for x in old], [key(x) for x in new]
    if None in old_keys or None in new_keys:
        return False
    if Counter(old_keys) == Counter(new_keys):
        return True
    if before.get("result_audit") != after.get("result_audit"):
        return False
    # Retain existing rows; do not synthesize a new grouping or new rationale.
    remaining = list(old)
    survivors = []
    for row, signature in zip(new, new_keys):
        index = next((i for i, prior in enumerate(remaining) if key(prior) == signature), None)
        if index is None:
            return False
        survivors.append((remaining.pop(index), row))

    def targets(row):
        ids = row.get("final_ids")
        return set(ids) if isinstance(ids, list) and all(isinstance(x, str) for x in ids) else None

    for removed in remaining:
        target_ids = targets(removed)
        if target_ids is None:
            return False
        if not any(set(removed["candidate_ids"]) <= set(kept["candidate_ids"])
                   and removed.get("verdict") == kept.get("verdict")
                   and target_ids == targets(prior) == targets(kept)
                   for prior, kept in survivors):
            return False
    return True


def _without_local_order(value, *, strip_identity=False):
    value = copy.deepcopy(value)
    for finding in _findings(value):
        finding.pop("assessed_after_repairing", None)
        if strip_identity: finding.pop("finding_id", None)
    return value


def preservation_errors(before, after):
    """Protect already-parseable scientific decisions during serialization repair."""
    if not isinstance(before, dict) or not isinstance(after, dict):
        return []  # Syntax-invalid originals require review of the retained raw diff.
    errors = []
    old_findings, new_findings = _findings(before), _findings(after)
    old_counts = Counter(x["finding_id"] for x in old_findings)
    remaining = list(new_findings)
    if len(old_findings) != len(new_findings): errors.append("format repair changed finding IDs or finding count")
    for old in old_findings:
        if old_counts[old["finding_id"]] > 1:
            # Repair duplicated identifiers only with exact, one-to-one
            # preservation of each distinct finding's entire scientific body.
            index = next((i for i, new in enumerate(remaining)
                          if _without_local_order(old, strip_identity=True) == _without_local_order(new, strip_identity=True)), None)
        else:
            index = next((i for i, new in enumerate(remaining) if new["finding_id"] == old["finding_id"]), None)
        if index is None:
            errors.append("format repair changed finding IDs or finding count")
            new = {}
        else:
            new = remaining.pop(index)
        for field in ("subtype", "error_statement", "mathematical_reason", "displayed_expression", "correct_recalculation",
                      "extra_conditions", "supported_conclusion", "missing_obligation", "premises", "claimed_inference"):
            if field in old and old[field] != new.get(field):
                errors.append(f"format repair changed {old['finding_id']}.{field}")
        if "repair_assessment" in old and old["repair_assessment"] != new.get("repair_assessment"):
            errors.append(f"format repair changed {old['finding_id']}.repair_assessment")
    old_root = before.get("result_audit", before)
    new_root = after.get("result_audit", after)
    if not isinstance(old_root, dict) or not isinstance(new_root, dict):
        return errors
    for field in ("result_id", "audit_status"):
        if field in old_root and old_root[field] != new_root.get(field):
            errors.append(f"format repair changed {field}")
    if isinstance(old_root.get("theorem_failure"), dict):
        old_failure, new_failure = old_root["theorem_failure"], new_root.get("theorem_failure", {})
        if not isinstance(new_failure, dict):
            errors.append("format repair removed theorem_failure")
        else:
            for field, value in old_failure.items():
                # This array contains findings: its order-ID metadata is subject
                # to the same repair policy as findings in the other dimensions.
                old_value, new_value = value, new_failure.get(field)
                if field == "statement_object_findings":
                    old_value = _without_local_order(value, strip_identity=True)
                    new_value = _without_local_order(new_value, strip_identity=True)
                if old_value != new_value:
                    errors.append(f"format repair changed theorem_failure.{field}")
            for field in ("statement_object_findings", "other_global_counterexamples"):
                if field not in old_failure and new_failure.get(field):
                    errors.append(f"format repair invented theorem_failure.{field}")
    if isinstance(old_root.get("contract"), dict):
        new_contract = new_root.get("contract")
        for field, value in old_root["contract"].items():
            if not isinstance(new_contract, dict) or value != new_contract.get(field):
                errors.append(f"format repair changed contract.{field}")
    for field, keys in (
        ("result_impact_assessment", ("result_impact_level", "revised_result_summary", "impact_explanation")),
        ("paper_impact_assessment", ("paper_impact_level", "impact_summary", "remaining_contribution_summary")),
    ):
        if field not in old_root:
            continue
        old, new = old_root[field], new_root.get(field)
        if old is None:
            if new is not None:
                errors.append(f"format repair changed null {field}")
        elif isinstance(old, dict):
            for key in keys:
                if key in old and (not isinstance(new, dict) or old[key] != new.get(key)):
                    errors.append(f"format repair changed {field}.{key}")
    if isinstance(before.get("proposal_reviews"), list):
        if not _review_decisions_preserved(before, after):
            errors.append("format repair changed reviewer proposal decisions")
    if isinstance(before.get("downstream_assessments"), list):
        candidate_rows = after.get("downstream_assessments", [])
        new_rows = {r.get("downstream_result_id"): r for r in (candidate_rows if isinstance(candidate_rows, list) else []) if isinstance(r, dict)}
        for row in before["downstream_assessments"]:
            if not isinstance(row, dict):
                continue
            updated = new_rows.get(row.get("downstream_result_id"), {})
            for key in ("propagation_status", "affected_interface"):
                if key in row and row[key] != updated.get(key):
                    errors.append(f"format repair changed downstream {key}")
            old = row.get("propagated_result_impact_assessment")
            new = updated.get("propagated_result_impact_assessment")
            if old is None and new is not None:
                errors.append("format repair changed null propagated impact")
            if isinstance(old, dict):
                for key in ("result_impact_level", "revised_result_summary", "impact_explanation"):
                    if key in old and (not isinstance(new, dict) or old[key] != new.get(key)):
                        errors.append(f"format repair changed propagated {key}")
    return errors


def repair_invalid_output(*, runtime, args, output_path, output, errors, turn,
                          schema, wire_schema_path, session_id, environment,
                          workspace, validate, checkpoint):
    """Correct at most N times in the same paper session, retaining every response.

    Returns (accepted_or_last_value, errors, selected_path). Transport failures are
    retained as failures rather than retried here. Session usage stays cumulative.
    """
    limit = getattr(args, "max_output_repairs", 2)
    if not errors or not session_id or limit <= 0:
        return output, errors, output_path
    original, original_path = copy.deepcopy(output), Path(output_path)
    turn["repair_policy_version"] = REPAIR_POLICY_VERSION
    raw = original_path.read_text()
    records = turn.setdefault("output_attempts", [])
    records.append({"attempt": 0, "output_path": str(original_path),
                    "output_sha256": hashlib.sha256(original_path.read_bytes()).hexdigest(),
                    "validation_errors": list(errors), "usage": turn.get("usage"),
                    "status": "invalid_output"})
    turn["repair_preservation_check"] = "parseable_decisions_guarded" if isinstance(original, dict) else "raw_original_retained_for_review"
    checkpoint()
    normalized, actions = normalize_bookkeeping(original)
    if actions:
        normalized_path = original_path.with_name(original_path.stem + ".bookkeeping.json")
        if normalized_path.exists(): raise FileExistsError(normalized_path)
        normalized_path.write_text(json.dumps(normalized, ensure_ascii=False, indent=2) + "\n")
        output, errors = validate(normalized_path)
        errors.extend(preservation_errors(original, output))
        records.append({"attempt": "deterministic_bookkeeping", "status": "invalid_output" if errors else "completed",
                        "output_path": str(normalized_path), "output_sha256": hashlib.sha256(normalized_path.read_bytes()).hexdigest(),
                        "validation_errors": list(errors), "actions": actions, "model_call": False})
        output_path = normalized_path
        checkpoint()
        if not errors: return output, errors, output_path
    for number in range(1, limit + 1):
        candidate = original_path.with_name(original_path.stem + f".repair_{number:02d}.json")
        if candidate.exists():
            raise FileExistsError(f"Refusing to overwrite repair output: {candidate}")
        patch_anchor = output if isinstance(output, dict) and not preservation_errors(original, output) else original
        slots = bookkeeping_slots(patch_anchor)
        patch_mode = bool(slots) and not list(jsonschema.Draft202012Validator(schema).iter_errors(patch_anchor))
        request_path, request_schema = candidate, wire_schema_path
        if patch_mode:
            request_path = candidate.with_suffix(".patch.json")
            request_schema = candidate.with_suffix(".patch.schema.json")
            if request_path.exists() or request_schema.exists(): raise FileExistsError(request_path)
            write_transport_schema(bookkeeping_patch_schema(slots), request_schema)
            payload = (
                "Repair only the bookkeeping of the same assessment. Return an edits array of JSON-pointer "
                "replacements; value_json is a JSON-encoded value, not a mathematical explanation. The host "
                "applies these replacements to the preserved assessment and validates the complete result. "
                "All mathematical claims, classifications, witnesses, levels and rationale stay byte-for-byte "
                "unchanged. Resolve ID/status mistakes using the existing explanation and the session's established "
                "finding ledger. Never invent an upstream finding, delete a substantive blocker, or choose a new "
                "scientific judgment to fit the schema. If the existing assessment cannot support a consistent "
                "bookkeeping repair, return no edits and explain in unresolved_reason. "
                "A finding_id field is editable only when the original accidentally reused that ID for distinct "
                "findings: give each an unambiguous ID and update references without adding/removing any finding. "
                + BOOKKEEPING_RULES + "\n"
                + "<validation_errors>\n" + json.dumps(errors, ensure_ascii=False) + "\n</validation_errors>\n"
                + "<allowed_existing_fields>\n" + json.dumps(slots, ensure_ascii=False) + "\n</allowed_existing_fields>\n"
                + "<assessment_to_patch>\n" + json.dumps(patch_anchor, ensure_ascii=False) + "\n</assessment_to_patch>\n"
            )
        else:
            payload = (
            "Correct the serialization of the same result or paper assessment; do not start a new audit. "
            "The complete paper and preceding reasoning remain in this session. The prior response failed "
            "the exact output contract. Return the entire corrected JSON object, not a patch.\n"
            "Preserve every finding, finding ID, counterexample, mathematical claim, repair choice, level, "
            "and rationale. Copy existing error_statement, mathematical_reason, repair_assessment, and impact "
            "prose verbatim. Correct JSON punctuation/escaping, required fields, field placement, exact enum "
            "spelling and referenced-ID bookkeeping only. Missing explanatory fields must restate existing "
            "reasoning; do not invent evidence. A calculation already described as calculation may be moved "
            "from a misplaced inference array to calculation without altering its substance. If an impact "
            "level is null, set its primary-driver field to null; do not change the level. Never delete a "
            "finding or regrade an assessment merely to pass validation. In proposal_reviews, copy retained "
            "rows' explanations verbatim when correcting final_ids. You may delete a redundant proposal row "
            "only when an existing retained row covers all its candidate_ids with the same verdict and "
            "exact same set of final_ids; preserve that covering row and the entire result_audit unchanged. "
            "Do not delete a distinct or conflicting decision, or invent a new grouping or explanation. "
            "If consistency would require a new "
            "mathematical judgment, preserve that judgment rather than fabricate a compliant answer.\n"
            "<validation_errors>\n" + json.dumps(errors, ensure_ascii=False) + "\n</validation_errors>\n"
            "<exact_output_schema>\n" + json.dumps(schema, ensure_ascii=False) + "\n</exact_output_schema>\n"
            "<original_response_data>\n" + raw + "\n</original_response_data>\n"
            ) + "\n" + BOOKKEEPING_RULES
        prompt_path = candidate.with_suffix(".input.txt")
        prompt_path.write_text(payload)
        record = {"attempt": number, "started_at": runtime.utc_now(), "status": "running",
                  "input_path": str(prompt_path), "model_input_sha256": hashlib.sha256(payload.encode()).hexdigest(),
                  "output_path": str(candidate), "session_id": session_id,
                  "model_call": True,
                  "repair_mode": "bookkeeping_patch" if patch_mode else "full_serialization",
                  "model_response_path": str(request_path)}
        records.append(record)
        checkpoint()
        try:
            proc = runtime.run_codex(
                command=runtime.resume_command(args, session_id, request_path, request_schema),
                model_input=payload, environment=environment,
                timeout_seconds=args.timeout_seconds, cwd=workspace)
        except subprocess.TimeoutExpired:
            errors = ["format correction timed out"]
            record.update(status="timeout", completed_at=runtime.utc_now(), validation_errors=errors)
            turn["completed_at"] = runtime.utc_now()
            checkpoint()
            return output, errors, output_path
        usage, observed = runtime.extract_event_metadata(proc.stdout)
        record.update(getattr(proc, "transport_metadata", {}))
        record.update(returncode=proc.returncode, usage=usage, observed_session_id=observed,
                      completed_at=runtime.utc_now())
        # Include failed corrections in the most recent observed cumulative usage.
        if usage and observed == session_id:
            turn["usage"] = usage
        elif usage:
            turn.setdefault("unmerged_correction_usage", []).append({"session_id": observed, "usage": usage})
        errors = []
        if observed != session_id:
            errors.append("format correction changed or lost the persistent session ID")
        if proc.returncode:
            errors.append(f"format correction CLI returned {proc.returncode}")
        if not request_path.is_file():
            errors.append("format correction produced no output file")
        transport_failed = bool(errors)
        if not errors and patch_mode:
            record["model_response_sha256"] = hashlib.sha256(request_path.read_bytes()).hexdigest()
            try:
                patch = json.loads(request_path.read_text())
                patched = apply_bookkeeping_patch(patch_anchor, patch, slots)
                candidate.write_text(json.dumps(patched, ensure_ascii=False, indent=2) + "\n")
                record["patch"] = patch
            except (ValueError, KeyError, TypeError) as exc:
                errors.append(str(exc))
        if not errors:
            output, errors = validate(candidate)
            errors.extend(preservation_errors(original, output))
            output_path = candidate
            record["output_sha256"] = hashlib.sha256(candidate.read_bytes()).hexdigest()
        record.update(status="invalid_output" if errors else "completed", validation_errors=errors)
        turn["completed_at"] = runtime.utc_now()
        checkpoint()
        if not errors or transport_failed:
            return output, errors, output_path
    return output, errors, output_path
