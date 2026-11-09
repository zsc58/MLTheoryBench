#!/usr/bin/env python3
"""Copy exact full-module trace receipts from explicit local cache roots.

This never substitutes compact cited-state subsets or claims fresh compilation.
Run after freeze-plan and before WRITE; the ordinary check-traces gate remains
mandatory. Sources, pinned build metadata and extractor identity must match.
"""
import argparse
import json
from pathlib import Path
import shutil

import pipeline as p
import validation as v
import trace_states as ts
from io_utils import read, write, sha


def matches(trace, source, filename, cfg, original_only=True):
    return (
        trace.get("status") in ("success", "no_tactic_traces")
        and trace.get("exit_status") == 0
        and not trace.get("timed_out", False)
        and not trace.get("has_errors", False)
        and "retention" not in trace
        and trace.get("source") == source
        and trace.get("source_file") == filename
        and trace.get("source_sha256") == ts.sha256(cfg["retained_file"])
        and trace.get("revision") == cfg["revision"]
        and trace.get("pinned_toolchain") == cfg["pinned_toolchain"]
        and trace.get("build_source_matches_retained") is True
        and trace.get("build_configuration_sha256") == cfg["fingerprints"]
        and trace.get("driver_sha256") == ts.sha256(ts.DRIVER)
        and trace.get("launcher_sha256") == ts.sha256(Path(ts.__file__))
        and trace.get("extraction_method") == "original_file_reelaboration_lean_infotree"
        and trace.get("tactic_selection") == (
            "original_source_nodes" if original_only else "all_anchored_infotree_nodes")
        and trace.get("tactic_count") == len(trace.get("tactics", []))
    )


def reuse(job, roots):
    p.check_plan(job)
    run, out = v.read_path(job["run_root"]), v.read_path(job["output"])
    if (out / "freeze.json").exists():
        raise ValueError("Cannot add cache provenance after draft freeze")
    if any(t["phase"] == "write" for t in p.turns_for(job)):
        raise ValueError("Prepare cache provenance before the writing turn")
    report_path = run / "trace_reuse.json"
    if report_path.exists() or (run / "trace_reuse.md").exists():
        raise ValueError("Existing cache provenance must not be overwritten")
    plan = read(out / "trace_plan.json")
    pending = []
    records = []
    copies = []
    for item in plan:
        source, filename = item["source"], item["file"]
        cfg = ts.source_configuration(source, filename)
        suffix = Path("traces") / source / Path(filename).with_suffix(".json")
        destination = v.in_tree(run, suffix)
        if destination.exists():
            if not matches(read(destination), source, filename, cfg, item.get("original_only", True)):
                raise ValueError(f"Existing trace does not match strict cache rules: {destination}")
            records.append({"file": filename, "action": "already_present", "sha256": sha(destination)})
            continue
        found = None
        for root in roots:
            candidates = sorted(root.rglob(Path(filename).with_suffix(".json").name))
            for candidate in candidates:
                if not candidate.as_posix().endswith(suffix.as_posix()) or not candidate.is_file():
                    continue
                trace = read(candidate)
                if matches(trace, source, filename, cfg, item.get("original_only", True)):
                    found = candidate, trace
                    break
            if found:
                break
        if not found:
            pending.append(item)
            continue
        origin, trace = found
        copies.append((origin, destination))
        records.append({"file": filename, "action": "copied_full_original_receipt",
                        "from": v.relative(origin), "to": v.relative(destination),
                        "sha256": sha(origin), "source_sha256": trace["source_sha256"],
                        "tactic_count": trace["tactic_count"],
                        "created_at": trace.get("created_at"),
                        "build_configuration_sha256": trace["build_configuration_sha256"]})
    for origin, destination in copies:
        destination.parent.mkdir(parents=True, exist_ok=True)
        # No overwrite, even if another process raced the preflight.
        with destination.open("xb") as output, origin.open("rb") as input_stream:
            shutil.copyfileobj(input_stream, output)
        if sha(destination) != sha(origin):
            raise ValueError("Trace copy failed byte verification")
    report = {"case_id": job["case_id"], "records": records, "missing_modules": pending,
              "policy": "Exact full original-source trace reuse only. No fresh compilation is claimed; required missing modules need extraction and the ordinary check-traces gate remains mandatory."}
    write(report_path, report)
    lines = ["# Exact full-module trace reuse", "", report["policy"], "",
             "Source revision, source bytes, pinned toolchain/build manifests and extractor hashes were matched. Receipts remain byte-identical, retaining original commands and timestamps.", ""]
    for item in records:
        lines.append(f"- `{item['file']}`: {item['action']}; SHA-256 `{item['sha256']}`.")
    for item in pending:
        lines.append(f"- `{item['file']}`: not reused; fresh extraction remains required.")
    (run / "trace_reuse.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument("--case", required=True)
    parser.add_argument("--cache-root", required=True, action="append", type=Path)
    args = parser.parse_args()
    roots = []
    for root in args.cache_root:
        root = root.resolve()
        root.relative_to((v.PROJECT / ".runtime").resolve())
        if not root.is_dir() or root == (v.PROJECT / ".runtime").resolve():
            parser.error("Use specific existing trace cache roots within .runtime")
        roots.append(root)
    jobs = [j for j in p.get_jobs(p.checked_run_path(args.run)) if args.case in (j["case_id"], j["key"])]
    if len(jobs) != 1:
        parser.error("Select exactly one known case")
    reuse(jobs[0], roots)


if __name__ == "__main__":
    main()
