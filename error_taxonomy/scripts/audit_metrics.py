"""Common counting rules; no historical datasets or model-price assumptions."""
from collections import Counter


def last_cumulative_usage(turns):
    """CLI usage is cumulative within one session, not additive across turns.

    Preserve missing usage as unknown. Reasoning tokens are already included in
    output tokens. Recheck this adapter assumption when upgrading the CLI.
    """
    rows = [t["usage"] for t in turns if isinstance(t.get("usage"), dict) and t["usage"]]
    errors = []
    for earlier, later in zip(rows, rows[1:]):
        if any(later.get(k, 0) < earlier.get(k, 0) for k in ("input_tokens", "output_tokens")):
            errors.append("usage counter decreased; cumulative interpretation needs review")
    return (rows[-1] if rows else None), errors


def assessment_level(value, key):
    return "unaffected" if value is None else ("undetermined" if value[key] is None else str(value[key]))


def audit_counts(audit):
    from validate_result_node_audits import rejected_missing_proof_source, result_findings
    counts = {key: Counter() for key in (
        "repair_levels", "dimensions", "subtypes", "repair_ge2_dimensions", "repair_ge2_subtypes",
        "result_levels", "result_primary_driver_dimensions", "result_primary_driver_subtypes")}
    all_findings = {fid: value for r in audit["result_audits"] for fid, value in result_findings(r).items()}
    rows = []
    for result in audit["result_audits"]:
        if rejected_missing_proof_source(result):
            counts["result_levels"]["excluded_missing_proof_source"] += 1
            continue
        impact = result["result_impact_assessment"]
        counts["result_levels"][assessment_level(impact, "result_impact_level")] += 1
        if impact and impact.get("primary_driver_finding_id") in all_findings:
            dim, finding = all_findings[impact["primary_driver_finding_id"]]
            counts["result_primary_driver_dimensions"][dim] += 1
            counts["result_primary_driver_subtypes"][finding["subtype"]] += 1
        for fid, (dim, finding) in result_findings(result).items():
            lev = finding["repair_assessment"]["repair_difficulty_level"]
            counts["repair_levels"]["undetermined" if lev is None else str(lev)] += 1
            counts["dimensions"][dim] += 1
            counts["subtypes"][finding["subtype"]] += 1
            if lev is not None and lev >= 2:
                counts["repair_ge2_dimensions"][dim] += 1
                counts["repair_ge2_subtypes"][finding["subtype"]] += 1
            rows.append({"result_id": result["result_id"], "finding_id": fid, "dimension": dim,
                         "subtype": finding["subtype"], "repair_level": lev})
    return {**{key: dict(value) for key, value in counts.items()}, "findings": len(rows),
            "repair_ge2": sum(counts["repair_ge2_dimensions"].values()), "finding_rows": rows,
            "paper_level": assessment_level(audit["paper_impact_assessment"], "paper_impact_level"),
            "paper_impact_eligible": not any(rejected_missing_proof_source(r) for r in audit["result_audits"]),
            "paper_primary_driver_result_id": (audit["paper_impact_assessment"] or {}).get("primary_driver_result_id")}
