#!/usr/bin/env python3
"""Validate selected A/B/reviewer audits and summarize final reviewer findings.

All failed attempts remain visible. Only the selected completed reviewer output
counts as a paper's final decision. No hard-coded paper list or billing rate.
"""
import argparse
from collections import Counter
from pathlib import Path

import run_paper_result_audits as base
from audit_metrics import audit_counts, last_cumulative_usage
from run_paper_dual_review import candidates, validate_review
from run_taxonomy_batch import digest
from validate_result_node_audits import make_paper_validator, paper_semantic_errors


def validate_run(path):
    run = path.parent
    manifest = base.read_json(run / "manifest.json")
    reviewer = (run / "snapshots/review_schema.json").is_file()
    schema = run / ("snapshots/paper_schema.json" if reviewer else "paper_schema_snapshot.json")
    result_schema = run / ("snapshots/result_schema.json" if reviewer else "result_schema_snapshot.json")
    audit = base.read_json(path)
    validator = make_paper_validator(base.read_json(schema), base.read_json(result_schema))
    errors = [e.message for e in validator.iter_errors(audit)] + paper_semantic_errors(audit)
    if manifest.get("status") != "completed":
        errors.append("Selected run is incomplete")
    if digest(path) != manifest.get("paper_audit_sha256"):
        errors.append("Final audit hash mismatch")
    for turn in manifest["turns"]:
        output = run / "outputs" / Path(turn["output_path"]).name
        if turn["status"] != "completed" or digest(output) != turn.get("output_sha256"):
            errors.append("Invalid or modified output turn")
    if reviewer:
        inputs = run.parents[1] / "private_inputs"
        originals = [{r["result_id"]: r for r in base.read_json(inputs / f"audit_{arm}.json")["result_audits"]}
                     for arm in ("a", "b")]
        schema = base.read_json(run / "snapshots/review_schema.json")
        source_ids = {s["source_id"] for s in audit["paper_context"]["sources"]}
        prior, results = [], []
        for turn in manifest["turns"]:
            rid = turn["result_id"]
            if rid is None:
                continue
            value = base.read_json(run / "outputs" / Path(turn["output_path"]).name)
            errors.extend(validate_review(value, schema, rid, candidates(originals[0][rid], originals[1][rid]),
                                          base.leads_for_result(audit["issue_leads"], rid), prior, source_ids))
            results.append(value["result_audit"])
            prior.extend(base.finding_ledger_entries(value["result_audit"]))
        if results != audit["result_audits"]:
            errors.append("Assembled reviewer ledger differs from output turns")
    return audit, manifest, errors


def summarize(root):
    bm = base.read_json(root / "batch_manifest.json")
    status = base.read_json(root / "batch_status.json")
    rows, errors, sessions = [], [], set()
    counts = {arm: {} for arm in ("A", "B", "reviewer")}
    completed = [r for r in status["papers"] if r["status"] == "completed"]
    for paper in completed:
        row = {"paper_id": paper["paper_id"], "audits": {}}
        for arm, relative in paper["selected_audits"].items():
            audit, manifest, qa = validate_run(root / relative)
            errors.extend({"paper_id": paper["paper_id"], "stage": arm, "error": e} for e in qa)
            sid = manifest["session_id"]
            if sid in sessions:
                errors.append({"paper_id": paper["paper_id"], "error": "Repeated session ID"})
            sessions.add(sid)
            row["audits"][arm] = audit_counts(audit)
        rows.append(row)
    for arm in counts:
        arm_rows = [r["audits"][arm] for r in rows]
        counts[arm] = {"findings": sum(r["findings"] for r in arm_rows),
                       "repair_ge2": sum(r["repair_ge2"] for r in arm_rows)}
        for name in ("repair_levels", "dimensions", "subtypes", "repair_ge2_dimensions", "repair_ge2_subtypes",
                     "result_levels", "result_primary_driver_dimensions", "result_primary_driver_subtypes"):
            total = Counter()
            for r in arm_rows:
                total.update(r[name])
            counts[arm][name] = dict(total)
        counts[arm]["eligible_paper_levels"] = dict(Counter(r["paper_level"] for r in arm_rows if r["paper_impact_eligible"]))
        counts[arm]["incomplete_proof_coverage_papers"] = sum(not r["paper_impact_eligible"] for r in arm_rows)
    usage = {"successful_attempts": Counter(), "failed_or_partial_attempts": Counter()}
    attempts = Counter()
    unknown_usage = 0
    for record in sorted((root / "papers").glob("*/*/*/attempt.json")):
        info = base.read_json(record)
        attempts[info["status"]] += 1
        run_manifests = list((record.parent / "runs").glob("*/manifest.json"))
        observed = False
        for path in run_manifests:
            m = base.read_json(path)
            counter, qa = last_cumulative_usage(m["turns"])
            errors.extend({"attempt": str(record.relative_to(root)), "error": e} for e in qa)
            if counter is not None:
                observed = True
                usage["successful_attempts" if info["status"] == "completed" else "failed_or_partial_attempts"].update(counter)
        unknown_usage += not observed
    return {"schema_version": "taxonomy_production_summary_v1", "requested_papers": len(bm["papers"]),
            "completed_papers": len(completed), "uncompleted_papers": len(bm["papers"]) - len(completed),
            "counting_basis": "paired completed papers; reviewer is final, A/B are comparative only",
            "totals": counts, "papers": rows, "attempt_statuses": dict(attempts),
            "observed_usage": {k: dict(v) for k, v in usage.items()}, "attempts_without_usage": unknown_usage,
            "usage_basis": "last observed cumulative counter per session, summed across attempts; unknown is not zero",
            "qa_errors": errors}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite an existing summary")
    report = summarize(args.batch.resolve())
    base.write_json(args.output, report)
    print({k: report[k] for k in ("requested_papers", "completed_papers", "uncompleted_papers", "qa_errors")})
    raise SystemExit(bool(report["qa_errors"]))
