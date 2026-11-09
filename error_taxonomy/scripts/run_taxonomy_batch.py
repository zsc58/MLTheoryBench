#!/usr/bin/env python3
"""Freeze an explicit private cohort and run independent A/B audits plus reviewer.

No sampling quotas, historical inputs, SSH, automatic model upgrades or API prices.
Each worker runs A, then B, then reviewer, in distinct persistent sessions.
Resume reuses completed stages and preserves every failed stage attempt.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import run_paper_result_audits as base
from provider_runtime import load_profile, stage_environment
from plugin_cache import prepare_plugin_cache

ROOT = Path(__file__).resolve().parents[1]
SAFE_PAPER = re.compile(r"paper_2026_[0-9]{3,}")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    base.write_json(temporary, value)
    temporary.replace(path)


def frozen_assets():
    paths = [p for folder in ("scripts", "prompts", "schemas") for p in (ROOT / folder).iterdir()
             if p.suffix in (".py", ".md", ".json")]
    return {str(p.relative_to(ROOT)): digest(p) for p in sorted(paths)}


def explicit_selection(args):
    if args.selection_file:
        if args.papers_root or args.paper_ids_file:
            raise ValueError("Use either selection-file or papers-root plus paper-ids-file")
        rows = base.read_json(args.selection_file)["papers"]
        for row in rows:
            for name in ("source_file", "source_audit_file", "later_chain_leads_file"):
                if row.get(name) and not Path(row[name]).is_absolute():
                    row[name] = str((args.selection_file.resolve().parent / row[name]).resolve())
        return rows
    if not args.papers_root or not args.paper_ids_file:
        raise ValueError("prepare needs selection-file or papers-root plus paper-ids-file")
    ids = base.read_json(args.paper_ids_file)["paper_ids"]
    rows = []
    for pid in ids:
        if not isinstance(pid, str) or not SAFE_PAPER.fullmatch(pid):
            raise ValueError("Invalid paper ID")
        paper = args.papers_root / pid
        final = paper / "paper_analysis/paper_analysis.json"
        rows.append({"paper_id": pid, "source_file": str(paper / "private_source/extracted_text.md"),
                     "source_audit_file": str(final if final.exists() else paper / "paper_analysis/turn3_source_audit.json")})
    return rows


def select_batch_targets(records, later, issue_scope):
    if issue_scope == "all":
        return base.select_targets(records, later, None)
    if issue_scope != "major":
        raise ValueError("Unknown issue scope")
    ids = [r["item_id"] for r in records if r.get("role") in base.AUDITABLE_ROLES
           and (r.get("statement_status") == "major_issue" or r.get("proof_status") == "major_gap")]
    if not ids:
        raise ValueError("No major-marked theory_candidate/internal_support targets")
    return base.select_targets(records, later, ids)


def prepare(args):
    if args.batch_root.exists():
        raise ValueError("Refusing to overwrite an existing batch root")
    rows = explicit_selection(args)
    if not rows or len({r["paper_id"] for r in rows}) != len(rows):
        raise ValueError("Supply a nonempty, unique paper cohort")
    prepared, exposures = [], []
    # Validate the complete cohort before creating any batch files.
    for row in rows:
        pid = row["paper_id"]
        if not SAFE_PAPER.fullmatch(pid):
            raise ValueError("Invalid paper ID")
        source, audit_path = (Path(row[k]).resolve() for k in ("source_file", "source_audit_file"))
        if source.suffix.lower() not in (".md", ".txt", ".tex", ".html", ".htm"):
            raise ValueError("Supply complete UTF-8 text/TeX/HTML, not a PDF")
        raw = source.read_bytes()
        if not raw.decode("utf-8").strip():
            raise ValueError("Empty source representation")
        audit_raw = base.read_json(audit_path)
        if "material_records" in audit_raw:
            audit = audit_raw
            pointer = ""
        else:
            audit = audit_raw.get("source_audit")
            pointer = "/source_audit"
        if not isinstance(audit, dict):
            raise ValueError(f"No current source audit for {pid}; never silently fall back to stale Turn 3")
        later_path = Path(row["later_chain_leads_file"]).resolve() if row.get("later_chain_leads_file") else None
        later = base.normalize_later_leads(base.read_json(later_path) if later_path else None)
        records = base.material_records(audit)
        targets = select_batch_targets(records, later, args.issue_scope)
        base.build_issue_leads(records, later)
        fidelity = row.get("source_fidelity") or base.infer_source_fidelity(source)
        if fidelity not in base.SOURCE_FIDELITIES:
            raise ValueError("Invalid source fidelity")
        staged = {"source" + source.suffix: raw,
                  "turn3_source_audit.json": (json.dumps(audit, ensure_ascii=False, indent=2) + "\n").encode()}
        if later_path:
            staged["later_chain_leads.json"] = later_path.read_bytes()
        record = {"paper_id": pid, "theory_topic": row.get("theory_topic") or "theoretical_machine_learning",
                  "source_name": "source" + source.suffix, "source_fidelity": fidelity,
                  "target_result_ids": [r["item_id"] for r in targets],
                  "files": {n: base.sha256_bytes(content) for n, content in staged.items()}}
        prepared.append((record, staged))
        for kind, path, at in (("paper_source", source, ""), ("source_audit", audit_path, pointer),
                               ("later_chain_leads", later_path, "")):
            if path:
                exposures.append({"paper_id": pid, "kind": kind, "source_path": str(path),
                                  "sha256": digest(path), "json_pointer": at})
    args.batch_root.mkdir(parents=True, mode=0o700)
    for row, files in prepared:
        dest = args.batch_root / "private_inputs" / row["paper_id"]
        dest.mkdir(parents=True, mode=0o700)
        for name, content in files.items():
            path = dest / name
            path.write_bytes(content)
            path.chmod(0o600)
    manifest = {"schema_version": "taxonomy_production_batch_v1", "prepared_at": base.utc_now(),
                "selection_policy": f"explicit_paper_cohort_{args.issue_scope}_issue_nodes_no_random_substitution",
                "issue_scope": args.issue_scope,
                "model": args.model, "reasoning_effort": args.reasoning_effort,
                "timeout_seconds": args.timeout_seconds, "frozen_assets": frozen_assets(),
                "max_output_repairs": getattr(args, "max_output_repairs", 2),
                "papers": [r for r, _ in prepared], "private_access_manifest": exposures,
                "propagation_policy": "reviewed_dependencies_and_final_paper_turn_no_extra_propagation_turn"}
    save(args.batch_root / "batch_manifest.json", manifest)
    print(json.dumps({"prepared": len(prepared), "result_nodes": sum(len(r["target_result_ids"]) for r, _ in prepared)}))


def verify_batch(root):
    manifest = base.read_json(root / "batch_manifest.json")
    if manifest["frozen_assets"] != frozen_assets():
        raise ValueError("Runtime assets changed after freeze; prepare a new batch")
    for row in manifest["papers"]:
        for name, expected in row["files"].items():
            if digest(root / "private_inputs" / row["paper_id"] / name) != expected:
                raise ValueError("Staged input hash mismatch")
    return manifest


def check(args):
    manifest = verify_batch(args.batch_root)
    # This mode never loads credentials or calls a model.
    print(json.dumps({"checked": len(manifest["papers"]), "model": manifest["model"],
                      "reasoning_effort": manifest["reasoning_effort"], "model_calls": 0}))


def completed_attempt(directory):
    if not directory.exists():
        return None
    for attempt in sorted(directory.iterdir()):
        record = attempt / "attempt.json"
        if not record.is_file():
            continue
        info = base.read_json(record)
        if info.get("status") == "completed":
            path = attempt / info["audit_path"]
            if digest(path) != info["audit_sha256"]:
                raise ValueError("Completed output changed; refusing resume")
            return path
    return None


def one_paper(row, args, manifest, profile):
    pid = row["paper_id"]
    private = args.batch_root / "private_inputs" / pid
    paper = args.batch_root / "papers" / pid
    paper.mkdir(parents=True, exist_ok=True, mode=0o700)
    selected, sessions = {}, set()
    for stage in ("A", "B", "reviewer"):
        directory = paper / stage
        existing = completed_attempt(directory)
        if existing:
            sid = base.read_json(existing.parent / "manifest.json")["session_id"]
            if sid in sessions:
                raise ValueError("A/B/reviewer must have independent sessions")
            sessions.add(sid)
            selected[stage] = str(existing.relative_to(args.batch_root))
            continue
        directory.mkdir(exist_ok=True, mode=0o700)
        number = max([int(p.name) for p in directory.iterdir() if p.is_dir() and p.name.isdigit()], default=0) + 1
        attempt = directory / f"{number:03d}"
        attempt.mkdir(mode=0o700)
        info = {"stage": stage, "started_at": base.utc_now(), "status": "running"}
        save(attempt / "attempt.json", info)
        cache = getattr(args, "plugin_cache", None)
        environment = stage_environment(attempt, args.codex_bin, profile,
                                        Path(cache["path"]) if cache else None) if profile else dict(os.environ)
        if cache:
            info["plugin_cache"] = cache
            save(attempt / "attempt.json", info)
        environment.update(PAPERPROOF_TAXONOMY_CODEX_BIN=args.codex_bin, PYTHONDONTWRITEBYTECODE="1")
        common = ["--runs-root", str(attempt / "runs"), "--codex-bin", str(ROOT / "scripts/vm_codex_shim.py"),
                  "--model", manifest["model"], "--reasoning-effort", manifest["reasoning_effort"],
                  "--timeout-seconds", str(manifest["timeout_seconds"]),
                  "--max-output-repairs", str(manifest.get("max_output_repairs", 0))]
        if stage != "reviewer":
            cmd = [sys.executable, "-B", str(ROOT / "scripts/run_paper_result_audits.py"),
                   "--paper-id", pid, "--theory-topic", row["theory_topic"],
                   "--source-file", str(private / row["source_name"]), "--source-fidelity", row["source_fidelity"],
                   "--turn3-audit", str(private / "turn3_source_audit.json"),
                   "--auth-mode", "isolated_vm_api_profile" if profile else "current_local_codex_login", *common]
            if (private / "later_chain_leads.json").exists():
                cmd.extend(["--later-chain-leads", str(private / "later_chain_leads.json")])
            # Keep the complete source audit as context, but execute only frozen targets.
            for result_id in row["target_result_ids"]:
                cmd.extend(["--result-id", result_id])
        else:
            inputs = attempt / "private_inputs"
            inputs.mkdir(mode=0o700)
            for name in row["files"]:
                shutil.copy2(private / name, inputs / name)
            for arm in ("A", "B"):
                shutil.copy2(args.batch_root / selected[arm], inputs / f"audit_{arm.lower()}.json")
            cmd = [sys.executable, "-B", str(ROOT / "scripts/run_paper_dual_review.py"),
                   "--inputs", str(inputs), "--source-file", str(inputs / row["source_name"]), *common]
        try:
            with (attempt / "stdout.log").open("w") as out, (attempt / "stderr.log").open("w") as err:
                proc = subprocess.run(cmd, env=environment, stdout=out, stderr=err, check=False)
            info["returncode"] = proc.returncode
            runs = list((attempt / "runs").glob("*/manifest.json"))
            if proc.returncode != 0 or len(runs) != 1:
                raise RuntimeError("Stage did not complete; inspect preserved private attempt")
            result = base.read_json(runs[0])
            path = runs[0].parent / "paper_audit.json"
            if result.get("status") != "completed" or not path.is_file():
                raise RuntimeError("Stage has no validated completed audit")
            if base.read_json(path).get("target_result_ids") != row["target_result_ids"]:
                raise ValueError("Stage target queue differs from frozen batch selection")
            sid = result.get("session_id")
            if not sid or sid in sessions:
                raise ValueError("A/B/reviewer must have independent sessions")
            sessions.add(sid)
            info.update(status="completed", session_id=sid, audit_path=str(path.relative_to(attempt)), audit_sha256=digest(path))
            selected[stage] = str(path.relative_to(args.batch_root))
        except Exception as exc:
            info.update(status="failed", error_type=type(exc).__name__)
        info["completed_at"] = base.utc_now()
        save(attempt / "attempt.json", info)
        if info["status"] != "completed":
            return {"paper_id": pid, "status": "failed", "failed_stage": stage, "selected_audits": selected}
    return {"paper_id": pid, "status": "completed", "selected_audits": selected}


def run(args):
    manifest = verify_batch(args.batch_root)
    status_path = args.batch_root / "batch_status.json"
    if status_path.exists() and not args.resume:
        raise ValueError("Batch was started; use --resume to retain successes and retry failed stages")
    binary = shutil.which(args.codex_bin)
    if not binary:
        raise ValueError("Codex executable not found")
    args.codex_bin = str(Path(binary).resolve())
    (ROOT / "scripts/vm_codex_shim.py").chmod(0o700)
    lock = args.batch_root / ".running.lock"
    with lock.open("x") as out:
        out.write(str(os.getpid()))
    try:
        # API profile loading occurs only after an explicit run command.
        profile = load_profile(args.api_profile) if args.api_profile else None
        args.plugin_cache = prepare_plugin_cache(args.batch_root / "shared_runtime", args.codex_bin) if profile else None
        status = {"started_at": base.utc_now(), "status": "running", "workers": args.workers,
                  "auth_mode": "isolated_vm_api_profile" if profile else "current_local_codex_login",
                  "provider": profile[3] if profile else None, "papers": [],
                  "plugin_cache": args.plugin_cache}
        save(status_path, status)
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(one_paper, row, args, manifest, profile): row["paper_id"] for row in manifest["papers"]}
            for future in concurrent.futures.as_completed(futures):
                try:
                    row = future.result()
                except Exception as exc:
                    row = {"paper_id": futures[future], "status": "failed", "error_type": type(exc).__name__}
                status["papers"].append(row)
                save(status_path, status)
                print(json.dumps({"paper_id": row["paper_id"], "status": row["status"]}), flush=True)
        status.update(status="completed" if all(r["status"] == "completed" for r in status["papers"]) else "completed_with_failures",
                      completed_at=base.utc_now())
        save(status_path, status)
        return 0 if status["status"] == "completed" else 1
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "check", "run"))
    parser.add_argument("--batch-root", type=Path, required=True)
    parser.add_argument("--papers-root", type=Path)
    parser.add_argument("--paper-ids-file", type=Path)
    parser.add_argument("--selection-file", type=Path)
    parser.add_argument("--issue-scope", choices=("all", "major"), default="all",
                        help="Prepare-time target filter; major selects major_issue or major_gap nodes only")
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--reasoning-effort", default="high")
    parser.add_argument("--timeout-seconds", type=int, default=2400)
    parser.add_argument("--max-output-repairs", type=int, choices=(0, 1, 2), default=2)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--api-profile", type=Path)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    args.batch_root = args.batch_root.resolve()
    if (args.batch_root == ROOT or ROOT in args.batch_root.parents) and ROOT / ".runtime" not in args.batch_root.parents:
        parser.error("Use a dedicated .runtime batch or an external private output directory")
    if not 1 <= args.workers <= 10 or args.timeout_seconds <= 0:
        parser.error("workers must be 1..10 and timeout positive")
    if args.mode == "prepare":
        prepare(args)
    elif args.mode == "check":
        check(args)
    else:
        return run(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
