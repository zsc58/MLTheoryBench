#!/usr/bin/env python3
"""Explicit VM-only integration smoke: five cold sessions, then one warm session.

No paper is exposed. Test request-schema switching, resume, session markers,
tool-call absence and allocated cache growth using the actual production shim.
Run manually, not as part of unittest discovery. Credentials are never saved.
"""
import argparse
import concurrent.futures
import json
import os
from pathlib import Path
import stat
import sys
from types import SimpleNamespace

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_paper_result_audits as base
import run_paper_dual_review as reviewer
from plugin_cache import prepare_plugin_cache
from provider_runtime import load_profile, stage_environment


def allocation(root):
    size = 0; count = 0; seen = set()
    for directory, _, names in os.walk(root, followlinks=False):
        for name in names:
            info = (Path(directory) / name).lstat()
            if not stat.S_ISREG(info.st_mode) or (info.st_dev, info.st_ino) in seen:
                continue
            seen.add((info.st_dev, info.st_ino))
            size += info.st_blocks * 512; count += 1
    return {"allocated_bytes": size, "regular_files": count}


def one_session(number, args, profile, cache):
    directory = args.output / f"session_{number:02d}"
    directory.mkdir(mode=0o700)
    env = stage_environment(directory, str(args.codex), profile, Path(cache["path"]))
    env.update(PAPERPROOF_TAXONOMY_CODEX_BIN=str(args.codex), PYTHONDONTWRITEBYTECODE="1")
    workspace = directory / "workspace"; workspace.mkdir(mode=0o700)
    # This local sentinel is never supplied to the model.
    (workspace / "do_not_read.txt").write_text("local-file-sentinel-" + os.urandom(12).hex())
    marker = "session-marker-" + os.urandom(12).hex()
    opts = SimpleNamespace(codex_bin=str(ROOT / "scripts/vm_codex_shim.py"),
                           model="gpt-6-astra", reasoning_effort="high")
    result_schema, review_schema = reviewer.schema_bundle()
    impact_schema = base.read_json(ROOT / "schemas/paper_impact_output.schema.json")
    expected = {"result_id": "theory_001", "audit_status": "assessed",
                "contract": {"quantified_domain": [], "assumptions": [],
                             "conclusion": marker, "statement_objects": []},
                "lead_adjudications": [], "theorem_failure": {"status": "undetermined",
                "statement_object_findings": [], "other_global_counterexamples": []},
                "findings": {"proof_obligation": [], "inference": [], "calculation": []},
                "dependencies": [], "result_impact_assessment": None, "open_questions": []}
    tests = [("result", result_schema, expected),
             ("review", review_schema, {"result_audit": expected, "proposal_reviews": []}),
             ("impact", impact_schema, {"paper_impact_assessment": None, "paper_open_questions": []})]
    report = {"session_number": number, "turns": [], "source_papers_exposed": [],
              "plugin_cache": cache, "started_at": base.utc_now()}
    session = None
    for i, (kind, schema, value) in enumerate(tests, 1):
        wire = base.write_transport_schema(schema, directory / f"{kind}_wire.json")
        output = directory / f"{i:03d}_{kind}.json"
        supplied = json.dumps(value)
        if kind == "review":
            supplied = supplied.replace(marker, "RECALL_THE_PREVIOUS_TURN_CONCLUSION")
        prompt = ("This is a serialization and session-continuity test. Do not use tools, read any "
                  "files, or access other sessions. Return exactly the following value. "
                  "If the conclusion is RECALL_THE_PREVIOUS_TURN_CONCLUSION, replace it with the "
                  "exact conclusion from your previous turn. All other fields are literal. " + supplied)
        (directory / f"{i:03d}_input.txt").write_text(prompt)
        command = base.initial_command(opts, workspace, output, wire) if session is None else base.resume_command(opts, session, output, wire)
        proc = base.run_codex(command=command, model_input=prompt, environment=env,
                              timeout_seconds=240, cwd=workspace)
        stdout = proc.stdout.replace(profile[1], "[REDACTED]")
        stderr = proc.stderr.replace(profile[1], "[REDACTED]")
        base.write_json(directory / f"{i:03d}_transport.json",
                        {"returncode": proc.returncode, "stdout": stdout, "stderr": stderr})
        usage, observed = base.extract_event_metadata(stdout)
        errors = []
        if proc.returncode: errors.append("CLI failed")
        if not observed: errors.append("Missing session ID")
        if session is not None and observed != session: errors.append("Session changed")
        session = observed or session
        try:
            got = base.read_json(output)
            errors.extend(e.message for e in jsonschema.Draft202012Validator(schema).iter_errors(got))
            if got != value: errors.append("Output/session-marker mismatch")
        except (ValueError, OSError): errors.append("Invalid or absent JSON")
        report["turns"].append({"kind": kind, "returncode": proc.returncode,
                                 "session_id": observed, "usage": usage, "errors": errors})
        if errors: break
    home = Path(env["CODEX_HOME"])
    tool_calls = []
    for rollout in (home / "sessions").rglob("*.jsonl"):
        for line in rollout.read_text().splitlines():
            event = json.loads(line); payload = event.get("payload", {})
            if event.get("type") == "response_item" and payload.get("type") in (
                    "function_call", "custom_tool_call", "web_search_call", "local_shell_call"):
                tool_calls.append({"type": payload["type"], "name": payload.get("name")})
    report["tool_calls"] = tool_calls
    report["cache_link_ok"] = (home / ".tmp").is_symlink() and (home / ".tmp").resolve() == Path(cache["path"])
    report["usage"], report["usage_errors"] = base.last_cumulative_usage(report["turns"])
    report["status"] = "passed" if (len(report["turns"]) == 3 and
        all(not turn["errors"] for turn in report["turns"]) and not tool_calls and
        report["cache_link_ok"] and not report["usage_errors"]) else "failed"
    report["completed_at"] = base.utc_now()
    base.write_json(directory / "report.json", report)
    print(json.dumps({"session": number, "status": report["status"]}), flush=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--codex", type=Path, required=True)
    args = parser.parse_args()
    if sys.platform != "linux": raise SystemExit("Real API smoke is VM/Linux only")
    args.output = args.output.resolve()
    args.output.mkdir(parents=True, mode=0o700)
    profile = load_profile(args.profile)
    cache = prepare_plugin_cache(args.output / "shared_runtime", str(args.codex))
    report = {"started_at": base.utc_now(), "plugin_cache": cache, "before": allocation(Path(cache["path"]))}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        reports = list(pool.map(lambda n: one_session(n, args, profile, cache), range(1, 6)))
    report["after_cold_five"] = allocation(Path(cache["path"]))
    reports.append(one_session(6, args, profile, cache))
    report["after_warm_six"] = allocation(Path(cache["path"]))
    report["shared_entries"] = sorted(p.name for p in Path(cache["path"]).iterdir())
    report["sessions"] = reports
    ids = {r["turns"][0]["session_id"] for r in reports}
    report["independent_sessions"] = len(ids) == 6 and None not in ids
    report["cache_bytes_added_by_warm_session"] = report["after_warm_six"]["allocated_bytes"] - report["after_cold_five"]["allocated_bytes"]
    report["status"] = "passed" if all(r["status"] == "passed" for r in reports) and report["independent_sessions"] and report["cache_bytes_added_by_warm_session"] == 0 else "failed"
    report["usage"] = {k: sum((r.get("usage") or {}).get(k, 0) for r in reports)
                        for k in {k for r in reports for k in (r.get("usage") or {})}}
    report["completed_at"] = base.utc_now()
    base.write_json(args.output / "report.json", report)
    print(json.dumps({k: v for k, v in report.items() if k != "sessions"}), flush=True)
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
