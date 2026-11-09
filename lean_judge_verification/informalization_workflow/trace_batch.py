#!/usr/bin/env python3
"""Run an explicit, bounded module trace plan; never follow imports automatically."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import sys

from trace_states import source_configuration, sha256


def one(item, run, timeout):
    source, file = item["source"], item["file"]
    cfg = source_configuration(source, file)
    output = run / "traces" / source / Path(file).with_suffix(".json")
    if output.exists():
        old = json.loads(output.read_text())
        if (old.get("status") in ("success", "partial_trace", "no_tactic_traces")
                and old.get("source_sha256") == sha256(cfg["retained_file"])
                and old.get("revision") == cfg["revision"]):
            return {"source": source, "file": file, "status": old["status"], "reused": True}
        raise ValueError(f"Existing unsuccessful/mismatched trace: {output}; inspect before retry")
    command = [sys.executable, "-B", str(Path(__file__).with_name("trace_states.py")),
               "--source", source, "--file", file, "--output", str(output),
               "--timeout", str(item.get("timeout", timeout))]
    if item.get("original_only", True):
        command.append("--original-only")
    else:
        command.append("--all-nodes")
    result = subprocess.run(command, text=True, capture_output=True)
    receipt = json.loads(output.read_text()) if output.is_file() else {}
    return {"source": source, "file": file, "status": receipt.get("status", "missing_receipt"), "exit_code": result.returncode,
            "output": result.stdout.strip(), "stderr": result.stderr.strip()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument("--workers", type=int, default=2, choices=(1, 2, 3))
    parser.add_argument("--timeout", type=float, default=900)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    keys = [(p["source"], p["file"]) for p in plan]
    if len(set(keys)) != len(keys):
        parser.error("Duplicate modules in plan")
    failed = False
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(one, p, args.run.resolve(), args.timeout): p for p in plan}
        for future in as_completed(futures):
            try:
                outcome = future.result()
                failed |= outcome.get("status") not in ("success", "partial_trace", "no_tactic_traces")
                print(json.dumps(outcome, ensure_ascii=False), flush=True)
            except Exception as exc:
                failed = True
                print(json.dumps({**futures[future], "error": str(exc)}, ensure_ascii=False), flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
