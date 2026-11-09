#!/usr/bin/env python3
"""Run one explicit real paper in a new VM batch, without importing old outputs."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-batch", type=Path, required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--codex", type=Path, required=True)
    args = parser.parse_args()
    if sys.platform != "linux": raise SystemExit("Real API smoke is VM/Linux only")
    original = json.loads((args.source_batch / "batch_manifest.json").read_text())
    row, = [p for p in original["papers"] if p["paper_id"] == args.paper_id]
    if len(row["target_result_ids"]) != 1:
        raise ValueError("This bounded smoke requires a paper with one selected result")
    args.output.mkdir(parents=True, mode=0o700)
    source = (args.source_batch / "private_inputs" / args.paper_id).resolve()
    selection = args.output / "selection.json"
    selection.write_text(json.dumps({"papers": [{
        "paper_id": args.paper_id, "theory_topic": row["theory_topic"],
        "source_file": str(source / row["source_name"]),
        "source_fidelity": row["source_fidelity"],
        "source_audit_file": str(source / "turn3_source_audit.json")
    }]}, indent=2) + "\n")
    selection.chmod(0o600)
    common = [sys.executable, "-B", str(ROOT / "scripts/run_taxonomy_batch.py")]
    batch = args.output / "batch"
    subprocess.run([*common, "prepare", "--selection-file", str(selection),
                    "--batch-root", str(batch), "--issue-scope", original["issue_scope"],
                    "--model", original["model"], "--reasoning-effort", original["reasoning_effort"],
                    "--timeout-seconds", "1200", "--max-output-repairs", "2"], check=True)
    frozen = json.loads((batch / "batch_manifest.json").read_text())
    if frozen["papers"][0]["target_result_ids"] != row["target_result_ids"]:
        raise ValueError("Smoke selection must preserve the original target queue")
    subprocess.run([*common, "check", "--batch-root", str(batch)], check=True)
    return subprocess.run([*common, "run", "--batch-root", str(batch), "--workers", "1",
                           "--api-profile", str(args.profile), "--codex-bin", str(args.codex)]).returncode


if __name__ == "__main__":
    raise SystemExit(main())
