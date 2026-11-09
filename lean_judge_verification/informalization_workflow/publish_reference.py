#!/usr/bin/env python3
"""Publish an independently accepted staged reference as six flat data files.

No model calls, source changes, overwrites of existing cases, or cleanup. The
private index retains compact cited-state evidence and construction receipts.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import shutil

import pipeline as p
import validation as v
from io_utils import read, write, sha


def retained_trace(trace, requested, original_hash):
    nodes = {item["id"]: item for item in trace["tactics"]}
    keep = set(requested)
    pending = list(keep)
    while pending:
        name = pending.pop()
        if name not in nodes:
            raise ValueError(f"Missing cited tactic: {name}")
        parent = nodes[name]["parent_id"]
        if parent is not None and parent not in keep:
            keep.add(parent)
            pending.append(parent)
    result = deepcopy(trace)
    result["tactics"] = [item for item in trace["tactics"] if item["id"] in keep]
    result["retention"] = {
        "original_trace_sha256": original_hash,
        "original_tactic_count": len(trace["tactics"]),
        "retained_tactic_count": len(result["tactics"]),
        "policy": "Final alignment references and their actual InfoTree ancestors only.",
    }
    return result


def publish(job, selection_flag, selection_note):
    checked = v.validate_job(job, "final", with_review=True)
    review = checked["review"]["data"]
    if review["verdict"] not in ("accepted_unchanged", "accepted_with_corrections"):
        raise ValueError("Only independently accepted references may be published")
    boundary, _, _ = p.check_plan(job)
    source = job["case_id"].split("/")[0]
    destination = v.PROJECT / "data" / source / job["key"]
    index_path = v.PROJECT / ".runtime/reference_evidence/index.json"
    config_path = v.PROJECT / "research/case_pipeline/case_config.json"
    index, config = read(index_path), read(config_path)
    if destination.exists() or any(c["case_id"] == job["case_id"] for c in index["cases"]):
        raise ValueError("Publication never overwrites an existing package or index entry")
    if any(c["id"] == job["case_id"] or (c["source"] == source and c["target"] == job["target"])
           for c in config["cases"]):
        raise ValueError("Case or target already configured")
    out = v.read_path(job["output"])
    bundle = v.read_path(job["case_root"])
    receipt_dir = bundle / "construction"
    if receipt_dir.exists():
        raise ValueError("Construction receipt directory already exists")

    trace_ids = {}
    for block in checked["alignment"]["proof_blocks"]:
        for ref in block["trace_refs"]:
            trace_ids.setdefault(ref["trace_file"], set()).add(ref["tactic_id"])
    compact = []
    for old, ids in trace_ids.items():
        trace = read(v.read_path(old))
        original_hash = sha(v.read_path(old))
        path = bundle / "cited_states" / Path(trace["source_file"]).with_suffix(".json")
        if path.exists() or old in index["traces"]:
            raise ValueError("Cited-state destination or alias already exists")
        compact.append((old, path, retained_trace(trace, ids, original_hash), original_hash))

    # All acceptance and collision checks precede new publication writes.
    receipt_dir.mkdir(parents=True)
    for name in ("review.json", "plan_freeze.json", "freeze.json"):
        shutil.copyfile(out / name, receipt_dir / name)
    shutil.copyfile(out / "plan/boundary.json", receipt_dir / "boundary.json")
    for name in ("trace_reuse.md", "trace_reuse.json"):
        trace_provenance = v.read_path(job["run_root"]) / name
        if trace_provenance.is_file():
            shutil.copyfile(trace_provenance, receipt_dir / name)
    run_manifest = read(v.read_path(job["run_root"]) / "manifest.json")
    write(receipt_dir / "execution.json", {
        "case_id": job["case_id"], "agents": run_manifest["agents"],
        "turns": run_manifest["turns"], "frozen_inputs": run_manifest["frozen_inputs"],
        "context_isolation": run_manifest.get("context_isolation", "See the run's declared case-input allowlists and recorded role IDs; blank history is not inferred from distinct role IDs."),
        "identity_limit": "runner_observed_invocation IDs identify actual observed tool invocations, not hidden provider turn IDs.",
        "retention_limit": "Historical read hashes are audit records; redundant intermediate prose need not be retained.",
    })
    for old, path, trace, original_hash in compact:
        write(path, trace)
        index["traces"][old] = {"path": v.relative(path), "sha256": sha(path),
                                "original_trace_sha256": original_hash}
    destination.mkdir(parents=True)
    for name in v.ARTIFACTS:
        shutil.copyfile(out / "final" / name, destination / name)
    index["cases"].append({
        "case_id": job["case_id"], "package": v.relative(destination),
        "selection": selection_flag, "selection_note": selection_note,
        "source_bundle": job["case_root"],
        "scope": {"id": job["case_id"], "key": job["key"], "target": job["target"],
                  "module": job["module"], "expanded": boundary["expanded_obligations"]},
        "final_sha256": {name: sha(destination / name) for name in v.ARTIFACTS},
        "draft_sha256": {name: sha(out / "draft" / name) for name in v.ARTIFACTS},
        "historical_translation_review": review["verdict"],
        "construction_receipts": v.relative(receipt_dir),
    })
    config["cases"].append({"id": job["case_id"], "source": source,
                             "target": job["target"], "module": job["module"]})
    write(config_path, config)
    write(index_path, index)
    print(f"Published {job['case_id']}: {selection_flag}; {review['verdict']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument("--case", required=True)
    parser.add_argument("--selection", required=True, choices=("retained", "borderline"))
    parser.add_argument("--note", required=True)
    args = parser.parse_args()
    jobs = [j for j in p.get_jobs(p.checked_run_path(args.run)) if args.case in (j["case_id"], j["key"])]
    if len(jobs) != 1 or not args.note.strip():
        parser.error("Select one known case and explain the screening decision")
    publish(jobs[0], args.selection, args.note)


if __name__ == "__main__":
    main()
