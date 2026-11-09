#!/usr/bin/env python3
"""Offline, sequential source verification for expansion candidates (04 through 99).

Selections use {source, preferred: [{id, source, target, module, ...}], alternates: [...]}.
The legacy ``cases`` key is accepted in place of ``preferred``. Alternates are never
automatically substituted. This helper does not select mathematical boundaries,
translate proofs, edit source snapshots, or promote cases into the public dataset.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parents[1]
MIN_FREE_BYTES = 8 * 1024 ** 3
SUBPROCESS_TIMEOUT_SECONDS = 1800
TERMINATION_GRACE_SECONDS = 5
STANDARD_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
ID_PATTERN = re.compile(r"([a-z][a-z0-9]*)/(\d{2})_([a-z][a-z0-9_]*)\Z")
MODULE_PATTERN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*\Z")
STATUS_NAME = "expansion_source_status.json"
# The pinned TLB lakefile loads doc-gen4 only for `-Kenv=dev`.
# Mathematical builds below do not enable that configuration.
TLB_OPTIONAL_DOC_PACKAGES = {"MD4Lean", "UnicodeBasic", "BibtexQuery", "«doc-gen4»"}


def load_builder():
    path = BASE / "research/case_pipeline/build_cases.py"
    spec = importlib.util.spec_from_file_location("expansion_source_builder", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_json(path: Path):
    return json.loads(path.read_text())


def slot(case_id: str) -> tuple[str, str]:
    match = ID_PATTERN.fullmatch(case_id)
    if not match or not 4 <= int(match[2]) <= 99:
        raise ValueError(f"Expected source/04_slug through source/99_slug: {case_id}")
    return match[1], match[2]


def validate_selections(documents: list[dict], builder) -> list[dict]:
    """Validate every preferred record before filtering or making any writes."""
    result, ids, slots, targets = [], set(), set(), set()
    for document in documents:
        source_id = document.get("source")
        if source_id not in builder.CONFIG["sources"]:
            raise ValueError(f"Unknown selection source: {source_id}")
        if "preferred" in document and "cases" in document:
            raise ValueError("Selection must use preferred or cases, not both")
        candidates = document.get("preferred", document.get("cases"))
        if not isinstance(candidates, list) or not isinstance(document.get("alternates", []), list):
            raise ValueError("Selection preferred and alternates must be lists")
        for candidate in candidates:
            if not isinstance(candidate, dict) or any(
                not isinstance(candidate.get(key), str) or not candidate[key]
                for key in ("id", "source", "target", "module")
            ):
                raise ValueError("Every preferred candidate requires id, source, target, module")
            case = dict(candidate)
            case_slot = slot(case["id"])
            if case["source"] != source_id or case_slot[0] != source_id:
                raise ValueError(f"Source/ID mismatch: {case['id']}")
            if not MODULE_PATTERN.fullmatch(case["module"]):
                raise ValueError(f"Invalid module name: {case['module']}")
            # Target names may contain Unicode and Lean primes, but not commands,
            # whitespace, quoted identifiers, or punctuation used by our exporter.
            if any(not part or not all(c.isalnum() or c in "_'" for c in part)
                   for part in case["target"].split(".")):
                raise ValueError(f"Invalid target name: {case['target']}")
            key = (source_id, case["target"])
            if case["id"] in ids or case_slot in slots or key in targets:
                raise ValueError(f"Duplicate ID, numeric slot, or target: {case['id']}")
            ids.add(case["id"])
            slots.add(case_slot)
            targets.add(key)
            result.append(case)
    return result


def check_collisions(case: dict, builder) -> None:
    """Reject accepted/configured cases, including renamed IDs in the same slot."""
    source_id, number = slot(case["id"])
    for old in builder.CONFIG["cases"]:
        old_slot = re.match(r"([^/]+)/(\d{2})(?:_|$)", old["id"])
        if (old["id"] == case["id"]
            or (old.get("source"), old.get("target")) == (source_id, case["target"])
            or (old_slot and (old_slot[1], old_slot[2]) == (source_id, number))):
            raise ValueError(f"Candidate collides with case_config: {case['id']}")
    data = builder.BASE / "data"
    if data.exists():
        for directory in data.rglob("*"):
            if not directory.is_dir():
                continue
            prefixed = re.match(rf"{re.escape(source_id)}_{number}(?:_|$)", directory.name)
            short = re.match(rf"{number}(?:_|$)", directory.name)
            if prefixed or (short and source_id in directory.relative_to(data).parts[:-1]):
                raise ValueError(f"Candidate collides with data directory: {directory}")
    source_bundles = builder.BUNDLES / source_id
    if source_bundles.exists():
        for directory in source_bundles.iterdir():
            if (re.match(rf"{number}(?:_|$)", directory.name)
                and directory.name != Path(case["id"]).name):
                raise ValueError(f"Candidate collides with existing evidence slot: {directory}")


def require_space(path: Path) -> int:
    free = shutil.disk_usage(path).free
    if free <= MIN_FREE_BYTES:
        raise ValueError(f"More than 8 GiB free required; available {free / 1024 ** 3:.3f} GiB")
    return free


def checked_child(root: Path, relative: str) -> Path:
    path = root / relative
    if Path(relative).is_absolute() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Source record escapes bundle: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing source file: {path}")
    return path


def validate_bundle(case: dict, builder) -> dict:
    """Read-only validation using the original receipt contract and source pins."""
    bundle = builder.BUNDLES / case["id"]
    evidence = bundle / "evidence"
    source = builder.CONFIG["sources"][case["source"]]
    root = builder.BASE / source["root"]
    metadata = read_json(evidence / "manifest.json")
    receipt = read_json(evidence / "verification_receipt.json")
    trace = read_json(evidence / "lean_dependencies.json")
    builder.validate_receipt(evidence, receipt, case, source,
                             builder.source_fingerprint(root),
                             (root / "lean-toolchain").read_text().strip())
    contract = {"case_id": case["id"], "target": case["target"],
                "target_module": case["module"], "source_revision": source["revision"],
                "source_repository": source["repository"], "lean_toolchain": receipt["lean_toolchain"],
                "lean_locally_verified": True, "proof_term_dependencies_extracted": True,
                "standard_axioms_only": True, "trace_sha256": builder.digest(evidence / "lean_dependencies.json")}
    if any(metadata.get(key) != value for key, value in contract.items()):
        raise ValueError("Completed bundle manifest contract mismatch")
    axioms = trace.get("transitive_axioms")
    if (trace.get("target") != case["target"] or not isinstance(axioms, list)
        or any(not isinstance(a, str) for a in axioms)
        or not set(axioms) <= STANDARD_AXIOMS or metadata.get("transitive_axioms") != axioms):
        raise ValueError("Target or axiom check failed (sorry/nonstandard axioms are not admitted)")
    if not any(node.get("name") == case["target"] and node.get("module") == case["module"]
               for node in trace.get("project_declaration_closure", [])):
        raise ValueError("Target declaration is absent from compiled project dependencies")
    modules = builder.closure(root, case["module"])["project_modules"]
    records = read_json(evidence / "source_files.json")
    if len(records) != len(modules) or {r.get("module") for r in records} != set(modules):
        raise ValueError("Project source collection is incomplete or duplicated")
    for record in records:
        relative = modules[record["module"]]
        if record["path"] != "sources/project/" + relative:
            raise ValueError("Project source path mismatch")
        path = checked_child(bundle, record["path"])
        if builder.digest(path) != record["sha256"] or builder.digest(root / relative) != record["sha256"]:
            raise ValueError(f"Project source hash mismatch: {record['path']}")
    background = read_json(evidence / "background_source_files.json")
    expected_background = {node["module"] for node in trace["external_background_boundary"] if node["module"]}
    if len(background) != len(expected_background) or {r.get("module") for r in background} != expected_background:
        raise ValueError("Background source collection is incomplete or duplicated")
    for record in background:
        if record.get("status") != "copied_at_background_boundary":
            raise ValueError(f"Missing background source: {record.get('module')}")
        if not record["path"].startswith("sources/background/"):
            raise ValueError("Background source path mismatch")
        if builder.digest(checked_child(bundle, record["path"])) != record["sha256"]:
            raise ValueError(f"Background source hash mismatch: {record['path']}")
    if metadata.get("background_source_missing"):
        raise ValueError("Manifest reports missing background sources")
    return {"receipt_sha256": builder.digest(evidence / "verification_receipt.json"),
            "trace_sha256": receipt["trace_sha256"], "transitive_axioms": axioms}


def resume_decision(case: dict, builder) -> tuple[str, dict]:
    bundle = builder.BUNDLES / case["id"]
    if bundle.is_symlink() or not bundle.resolve().is_relative_to(builder.BUNDLES.resolve()):
        raise ValueError("Evidence path is a symlink or escapes its root")
    if not bundle.exists():
        return "build", {}
    # Any incomplete, invalid, or already accepted bundle is never overwritten.
    return "resume", validate_bundle(case, builder)


def preflight(case: dict, builder) -> None:
    source = builder.CONFIG["sources"][case["source"]]
    buildroot = builder.BASE / ".tools/builds" / case["source"]
    builder.verify_build_sources(case["source"])
    driver = buildroot / ("CaseExport_" + case["id"].replace("/", "_") + ".lean")
    if driver.exists():
        raise ValueError(f"Existing export driver is preserved: {driver}")
    bindir = builder.BASE / ".tools/toolchains" / source["toolchain_folder"] / "bin"
    for name in ("lake", "lean"):
        if not (bindir / name).is_file():
            raise ValueError(f"Missing local pinned executable: {bindir / name}")
    manifest = read_json(buildroot / "lake-manifest.json")
    packages = buildroot / manifest.get("packagesDir", ".lake/packages")
    for package in manifest["packages"]:
        folder = packages / package["name"]
        if not folder.is_dir():
            if (case["source"] == "tlb" and package["name"] in TLB_OPTIONAL_DOC_PACKAGES
                    and 'meta if get_config? env = some "dev" then' in (buildroot / "lakefile.lean").read_text()):
                continue
            raise ValueError(f"Missing local dependency; downloads disabled: {folder}")
        if package.get("type") == "git":
            result = subprocess.run(["git", "-C", str(folder), "rev-parse", "HEAD"],
                                    text=True, capture_output=True, check=False)
            if result.returncode or result.stdout.strip() != package["rev"]:
                raise ValueError(f"Local dependency differs from pinned revision: {folder}")


def offline_prefix() -> list[str]:
    """Fail closed if the platform cannot isolate subprocess networking."""
    if sys.platform == "darwin" and Path("/usr/bin/sandbox-exec").is_file():
        return ["/usr/bin/sandbox-exec", "-p", "(version 1) (allow default) (deny network*)"]
    if sys.platform.startswith("linux") and shutil.which("unshare"):
        return [shutil.which("unshare"), "--net", "--"]
    raise RuntimeError("Offline build requires macOS sandbox-exec or Linux unshare --net")


def stop_process_group(process) -> None:
    """Stop only the new session created for this exact build/export subprocess."""
    if process.returncode is not None:
        return  # A reaped PID could have been reused; never signal it.
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        process.wait(timeout=TERMINATION_GRACE_SECONDS)
        return
    # Do not reap the leader between TERM and KILL: retaining its PID prevents
    # an unrelated process group from acquiring that same ID during shutdown.
    time.sleep(TERMINATION_GRACE_SECONDS)
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=TERMINATION_GRACE_SECONDS)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"Build process group {process.pid} did not exit after SIGKILL") from exc


@contextmanager
def guarded_builder(builder):
    old_summary, old_run = builder.summarize, builder.run_logged

    def run_logged(command, source, source_id, log):
        if not (command[:2] == ["lake", "build"] or command[:3] == ["lake", "env", "lean"]):
            raise ValueError(f"Unexpected build command: {command}")
        lake = builder.BASE / ".tools/toolchains" / source["toolchain_folder"] / "bin/lake"
        command = offline_prefix() + [str(lake), *command[1:]]
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("w") as handle:
            handle.write("COMMAND " + shlex.join(command) + "\n")
            handle.flush()
            process = subprocess.Popen(command, cwd=builder.BASE / ".tools/builds" / source_id,
                                       env=builder.tool_env(source), stdout=handle,
                                       stderr=subprocess.STDOUT, start_new_session=True)
            try:
                returncode = process.wait(timeout=SUBPROCESS_TIMEOUT_SECONDS)
            except subprocess.TimeoutExpired as exc:
                handle.write(f"\nTIMEOUT after {SUBPROCESS_TIMEOUT_SECONDS}s; terminating build process group\n")
                handle.flush()
                stop_process_group(process)
                raise TimeoutError(f"Build/export exceeded {SUBPROCESS_TIMEOUT_SECONDS}s; log: {log}") from exc
            except BaseException:
                stop_process_group(process)
                raise
        print(f"{log.relative_to(builder.BASE)}: exit {returncode}", flush=True)
        if returncode:
            print(log.read_text()[-9000:])
            raise SystemExit(returncode)

    builder.summarize = lambda: None
    builder.run_logged = run_logged
    try:
        yield
    finally:
        builder.summarize, builder.run_logged = old_summary, old_run


def process_case(case: dict, builder) -> dict:
    row = {key: case[key] for key in ("id", "source", "target", "module")}
    row["checked_at_utc"] = datetime.now(timezone.utc).isoformat()
    try:
        row["free_bytes_before"] = require_space(builder.BASE)
        check_collisions(case, builder)
        decision, proof = resume_decision(case, builder)
        if decision == "resume":
            row.update(status="resumed", **proof)
        else:
            preflight(case, builder)
            offline_prefix()
            # Exclusive creation prevents two invocations from claiming one bundle.
            (builder.BUNDLES / case["id"]).mkdir(parents=True, exist_ok=False)
            with guarded_builder(builder):
                builder.trace(case)
            row.update(status="verified", **validate_bundle(case, builder))
    except (Exception, SystemExit) as exc:
        row.update(status="failed", error=f"{type(exc).__name__}: {exc}")
    return row


def validate_run(run: Path, builder) -> Path:
    run = run.resolve()
    runtime = (builder.BASE / ".runtime").resolve()
    if (run == runtime or not run.is_relative_to(runtime)
        or run.is_relative_to(builder.BUNDLES.resolve())):
        raise ValueError("--run must be a dedicated directory inside .runtime, outside reference_evidence")
    return run


def main(argv=None) -> int:
    builder = load_builder()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selection", type=Path, action="append", required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--source", choices=sorted(builder.CONFIG["sources"]))
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--limit", type=int)
    args = parser.parse_args(argv)
    try:
        if args.limit is not None and args.limit < 1:
            raise ValueError("--limit must be positive")
        cases = validate_selections([read_json(p) for p in args.selection], builder)
        unknown = set(args.case) - {c["id"] for c in cases}
        if unknown:
            raise ValueError(f"Unknown --case IDs: {sorted(unknown)}")
        cases = [c for c in cases if (not args.source or c["source"] == args.source)
                 and (not args.case or c["id"] in args.case)]
        if args.limit is not None:
            cases = cases[:args.limit]
        if not cases:
            raise ValueError("No matching preferred candidates")
        run = validate_run(args.run, builder)
        runtime = builder.BASE / ".runtime"
        runtime.mkdir(exist_ok=True)
        # One build at a time across helper invocations; retain the lock file.
        with (runtime / "expansion_source_build.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise ValueError("Another expansion source batch holds the build lock") from exc
            run.mkdir(parents=True, exist_ok=True)
            status_path = run / STATUS_NAME
            if status_path.is_symlink():
                raise ValueError("Expansion status must not be a symlink")
            state = read_json(status_path) if status_path.exists() else {"schema_version": "1.0", "cases": {}}
            if state.get("schema_version") != "1.0" or not isinstance(state.get("cases"), dict):
                raise ValueError("Invalid existing expansion status file")
            state["selection_files"] = [{"path": str(p.resolve()), "sha256": builder.digest(p)} for p in args.selection]
            state["policy"] = {"network": "disabled_for_build_subprocesses", "workers": 1,
                               "minimum_free_bytes_exclusive": MIN_FREE_BYTES,
                               "subprocess_timeout_seconds": SUBPROCESS_TIMEOUT_SECONDS,
                               "alternates_scheduled": False}
            failed = False
            for case in cases:
                previous = state["cases"].get(case["id"])
                if previous and any(previous.get(k) != case[k] for k in ("source", "target", "module")):
                    raise ValueError(f"Run already assigns this ID to another target: {case['id']}")
                row = process_case(case, builder)
                state["cases"][case["id"]] = row
                state["updated_at_utc"] = datetime.now(timezone.utc).isoformat()
                builder.dump(status_path, state)
                print(f"{case['id']}: {row['status']}" + (f" — {row['error']}" if "error" in row else ""), flush=True)
                failed |= row["status"] == "failed"
            return 1 if failed else 0
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
