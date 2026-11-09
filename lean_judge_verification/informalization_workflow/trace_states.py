#!/usr/bin/env python3
"""Re-elaborate retained Lean source and export file-local tactic states offline."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time
from datetime import datetime, timezone


BASE = Path(__file__).resolve().parents[1]
WORKSPACE = BASE.parent
CONFIG_PATH = BASE / "research/case_pipeline/case_config.json"
DRIVER = Path(__file__).resolve().parent / "lean_trace/ExtractTactics.lean"
SCHEMA_VERSION = "1.0"
LIMITATIONS = [
    "Goals are local to this InfoTree tactic scope; an empty after.goals list is not global theorem completion.",
    "Nested, overlapping, macro-generated, and backtracking tactic nodes are retained, not filtered into a proof script.",
    "InfoTree parentage is execution/elaboration nesting, not a mathematical dependency graph.",
    "Goal pretty text contains local context and target using Lean's source-context pretty printer; it is not a serialized proof term.",
    "Term-style proofs may produce no tactic nodes. Missing traces are not fabricated.",
    "Imports use the retained local build artifacts; this extraction re-elaborates the requested source file, not every imported file.",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def finalize_tactics(raw: list[dict], source_bytes: bytes) -> list[dict]:
    """Assign stable run-local IDs and recover exactly the anchored UTF-8 bytes."""
    # Parser.mkInputContext normalizes CRLF on both supported Lean versions.
    # InfoTree byte offsets therefore address normalized input, not original bytes.
    # Preserve original source/line numbers and translate only byte offsets back.
    offsets = [0]
    position = 0
    while position < len(source_bytes):
        position += 2 if source_bytes[position:position + 2] == b"\r\n" else 1
        offsets.append(position)

    def original_span(span):
        if span is None:
            return None
        converted = {}
        for side in ("start", "end"):
            point = dict(span[side])
            normalized = point["byte"]
            if not 0 <= normalized < len(offsets):
                raise ValueError("tactic span is outside normalized Lean input")
            point["byte"] = offsets[normalized]
            converted[side] = point
        return converted

    result = []
    for expected, item in enumerate(raw):
        record = dict(item)
        if record.pop("index") != expected:
            raise ValueError("driver tactic indices must be consecutive preorder indices")
        parent_index = record.pop("parent_index")
        if parent_index is not None and not 0 <= parent_index < expected:
            raise ValueError("parent must precede its child")
        record["source_span"] = original_span(record["source_span"])
        if "command_span" in record:
            record["command_span"] = original_span(record["command_span"])
        start = record["source_span"]["start"]["byte"]
        end = record["source_span"]["end"]["byte"]
        if not 0 <= start <= end <= len(source_bytes):
            raise ValueError("tactic source span is outside the original source bytes")
        record["id"] = f"t{expected + 1:06d}"
        record["parent_id"] = None if parent_index is None else f"t{parent_index + 1:06d}"
        record["tactic"] = source_bytes[start:end].decode("utf-8")
        result.append(record)
    return result


def run_command(command: list[str], cwd: Path, env: dict[str, str], timeout: float) -> dict:
    """Bound a whole subprocess group, including any child spawned by lake."""
    started = time.monotonic()
    proc = subprocess.Popen(command, cwd=cwd, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, start_new_session=True)
    timed_out = False
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(proc.pid, signal.SIGKILL)
        stdout, stderr = proc.communicate()
    return {"command": command, "working_directory": str(cwd),
            "exit_status": proc.returncode, "timed_out": timed_out,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            "stdout": stdout, "stderr": stderr}


def source_configuration(source: str, filename: str) -> dict:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))["sources"][source]
    relative = Path(filename)
    if relative.is_absolute() or ".." in relative.parts or relative.suffix != ".lean":
        raise ValueError("--file must be a project-relative .lean path without '..'")
    if not relative.parts or relative.parts[0] != config["module_prefix"]:
        raise ValueError("--file must be inside the configured project's module prefix")
    snapshot = (BASE / config["root"]).resolve()
    build = (BASE / ".tools/builds" / source).resolve()
    retained_file = snapshot / relative
    build_file = build / relative
    for root, path in ((snapshot, retained_file), (build, build_file)):
        if not path.resolve().is_relative_to(root) or not path.is_file():
            raise ValueError(f"source file does not exist within retained project: {path}")
    if sha256(retained_file) != sha256(build_file):
        raise ValueError("build source differs from retained snapshot; refusing trace")
    fingerprints = {}
    for name in ("lean-toolchain", "lake-manifest.json"):
        old, current = snapshot / name, build / name
        if not old.is_file() or not current.is_file() or sha256(old) != sha256(current):
            raise ValueError(f"build {name} differs from retained snapshot")
        fingerprints[name] = sha256(old)
    toolchain = BASE / ".tools/toolchains" / config["toolchain_folder"]
    lean, lake = toolchain / "bin/lean", toolchain / "bin/lake"
    if not lean.is_file() or not lake.is_file():
        raise ValueError(f"retained toolchain missing: {toolchain}; no installation is attempted")
    return {**config, "filename": relative.as_posix(), "snapshot": snapshot,
            "build": build, "retained_file": retained_file, "build_file": build_file,
            "lean": lean, "lake": lake, "fingerprints": fingerprints,
            "pinned_toolchain": (snapshot / "lean-toolchain").read_text().strip()}


def extract(source: str, filename: str, timeout: float, original_only: bool = True) -> dict:
    config = source_configuration(source, filename)
    source_bytes = config["retained_file"].read_bytes()
    env = dict(os.environ)
    env["PATH"] = str(config["lean"].parent) + os.pathsep + env.get("PATH", "")
    env["LEAN_NUM_THREADS"] = "2"
    env["LEAN_IMPORT_WORKERS"] = "2"
    version = run_command([str(config["lean"]), "--version"], config["build"], env, 20)
    if version["exit_status"] != 0:
        raise ValueError(f"could not read retained Lean version: {version}")
    pinned = config["pinned_toolchain"].split(":")[-1].removeprefix("v")
    if f"version {pinned}," not in version["stdout"] and f"version {pinned} " not in version["stdout"]:
        raise ValueError("Lean executable version does not match retained lean-toolchain")
    result = {"schema_version": SCHEMA_VERSION, "status": "pending", "source": source,
              "source_file": config["filename"], "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
              "revision": config["revision"], "pinned_toolchain": config["pinned_toolchain"],
              "lean_version": version["stdout"].strip(), "driver_sha256": sha256(DRIVER),
              "launcher_sha256": sha256(Path(__file__)),
              "parser_input_normalization": "CRLF to LF; exported byte offsets mapped back to original source",
              "tactic_selection": "original_source_nodes" if original_only else "all_anchored_infotree_nodes",
              "build_source_matches_retained": True, "build_configuration_sha256": config["fingerprints"],
              "created_at": datetime.now(timezone.utc).isoformat(),
              "extraction_method": "original_file_reelaboration_lean_infotree",
              "source_span_convention": "1-based lines; 0-based Unicode columns; UTF-8 byte offsets; end exclusive",
              "state_format": "Lean ppGoal (local context plus goal target)",
              "limitations": [
                  ("Synthetic macro-helper nodes are excluded; original source nodes can still overlap, nest, or belong to backtracking elaboration."
                   if original_only and item.startswith("Nested, overlapping") else item)
                  for item in LIMITATIONS
              ], "tactics": []}
    # Keep generated drivers outside the source tree so concurrent source-hash
    # audits cannot mistake an in-flight extraction driver for edited project code.
    # Lake still runs with the pinned build directory as its working directory.
    scratch_root = BASE / ".runtime/trace_work"
    scratch_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="informalization_trace_", dir=scratch_root) as tmp:
        temporary = Path(tmp)
        driver = temporary / "ExtractTactics.lean"
        raw_output = temporary / "raw.json"
        shutil.copyfile(DRIVER, driver)
        module = config["filename"][:-5].replace("/", ".")
        command = [str(config["lake"]), "env", str(config["lean"]), "--run", str(driver),
                   config["filename"], str(raw_output), module]
        if original_only:
            command.append("original_only")
        process = run_command(command, config["build"], env, timeout)
        result.update(process)
        progress = Path(str(raw_output) + ".progress")
        result["last_processing_phase"] = progress.read_text().strip() if progress.exists() else "before_imports_processed"
        if process["timed_out"]:
            result["status"] = "timeout"
        elif raw_output.is_file():
            raw = json.loads(raw_output.read_text(encoding="utf-8"))
            result.update({key: value for key, value in raw.items() if key != "tactics"})
            result["tactics"] = finalize_tactics(raw["tactics"], source_bytes)
            result["status"] = ("elaboration_error" if raw["has_errors"] or process["exit_status"] != 0
                                else "success" if result["tactics"] else "no_tactic_traces")
            if result["status"] == "success" and (raw["unresolved_info_tree_holes"]
                                                    or raw["unanchored_tactic_nodes"]):
                result["status"] = "partial_trace"
        else:
            result["status"] = "driver_error"
    if sha256(config["retained_file"]) != result["source_sha256"] or sha256(config["build_file"]) != result["source_sha256"]:
        result["status"] = "source_changed_during_extraction"
    result["tactic_count"] = len(result["tactics"])
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, choices=("ai4slt", "tlb"))
    parser.add_argument("--file", required=True, help="original source path relative to the source project")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--timeout", type=float, default=600)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--original-only", dest="original_only", action="store_true", help="Export original source nodes, excluding synthetic macro helper nodes (default)")
    selection.add_argument("--all-nodes", dest="original_only", action="store_false", help="Also format synthetic helper nodes; may be substantially slower")
    parser.set_defaults(original_only=True)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    output = args.output.expanduser().resolve()
    protected = [BASE / ".tools", BASE / "research/source_pilot_20260908"]
    if output.suffix != ".json" or any(output.is_relative_to(path.resolve()) for path in protected):
        parser.error("--output must be a .json file outside retained source and .tools")
    try:
        result = extract(args.source, args.file, args.timeout, args.original_only)
    except (OSError, ValueError, KeyError) as error:
        result = {"schema_version": SCHEMA_VERSION, "status": "configuration_error",
                  "source": args.source, "source_file": args.file, "source_sha256": None,
                  "exit_status": None, "error": str(error), "tactics": [], "tactic_count": 0}
    output.parent.mkdir(parents=True, exist_ok=True)
    # Replace any previous success with the current receipt, including failed attempts.
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "tactic_count": result["tactic_count"],
                      "output": str(output)}, ensure_ascii=False))
    return 0 if result["status"] in ("success", "no_tactic_traces") else 1


if __name__ == "__main__":
    raise SystemExit(main())
