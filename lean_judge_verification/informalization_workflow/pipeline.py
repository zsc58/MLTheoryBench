#!/usr/bin/env python3
"""Offline staged informalization: prepare, author plan, author write, independent review."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil

import validation as v
from io_utils import read, write, sha, check_receipt
from boundary import PLAN_FILES, registry, validate_plan, trace_plan


def prepare(run, case_roots):
    if run.exists() and any(run.iterdir()):
        raise ValueError("Run directory already exists and is not empty")
    if not case_roots:
        raise ValueError("Supply at least one --case-root; no per-case scope is prewritten")
    prepared, keys, frozen = [], set(), []
    for case in case_roots:
        case = case.resolve()
        case.relative_to(v.PROJECT.resolve())
        metadata = read(case / "evidence/manifest.json")
        case_id = metadata["case_id"]
        if not re.fullmatch(r"[a-z0-9_]+/[a-z0-9_]+", case_id):
            raise ValueError("Case IDs must be source/ASCII_snake_case")
        key = case_id.replace("/", "_")
        if key in keys:
            raise ValueError("Duplicate case or filename key")
        keys.add(key)
        if metadata.get("lean_locally_verified") is not True or metadata.get("standard_axioms_only") is not True:
            raise ValueError("Source target needs a successful local check and the allowed axiom audit")
        source_files = v.sources(case)
        receipts = check_receipt(case, metadata)
        inputs = [case / "evidence" / name for name in (
            "manifest.json", "source_files.json", "background_source_files.json",
            "lean_dependencies.json", "verification_receipt.json")]
        frozen.extend(inputs + receipts + [case / name for name in source_files])
        prepared.append((case, metadata, key, source_files, inputs))
    run.mkdir(parents=True, exist_ok=True)
    for name in v.SNAPSHOT_FILES:
        target = run / "snapshot" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(v.WORKFLOW / name, target)
        frozen.append(target)
    jobs = []
    for case, metadata, key, source_files, inputs in prepared:
        source = metadata["case_id"].split("/")[0]
        trace_root = run / "traces" / source
        mapping = {
            v.relative(trace_root / Path(name.removeprefix("sources/project/")).with_suffix(".json")): name
            for name in source_files if name.startswith("sources/project/")
        }
        module_file = metadata["target_module"].replace(".", "/") + ".lean"
        initial = v.relative(trace_root / Path(module_file).with_suffix(".json"))
        if initial not in mapping:
            raise ValueError("Target module is not retained")
        out, snapshot = run / key, run / "snapshot"
        job_path = run / "jobs" / (key + ".json")
        job = {
            "version": "1.0", "boundary_mode": "author_selected",
            "case_id": metadata["case_id"], "key": key, "target": metadata["target"],
            "module": metadata["target_module"], "case_root": v.relative(case),
            "job_file": v.relative(job_path), "run_root": v.relative(run),
            "evidence_inputs": [v.relative(p) for p in inputs],
            "source_read_roots": [v.relative(case / "sources")],
            "translation_prompt": v.relative(snapshot / "prompts/author.md"),
            "plan_prompt": v.relative(snapshot / "prompts/plan.md"),
            "write_prompt": v.relative(snapshot / "prompts/write.md"),
            "review_prompt": v.relative(snapshot / "prompts/review.md"),
            "alignment_schema": v.relative(snapshot / "schemas/alignment.schema.json"),
            "sketch_schema": v.relative(snapshot / "schemas/sketch.schema.json"),
            "boundary_schema": v.relative(snapshot / "schemas/boundary.schema.json"),
            "review_schema": v.relative(snapshot / "schemas/review.schema.json"),
            "scope_file": v.relative(snapshot / "boundary_policy.json"),
            "declaration_index": v.relative(out / "declaration_index.json"),
            "trace_files": [initial], "trace_read_root": v.relative(trace_root),
            "trace_source_files": mapping, "output": v.relative(out),
            "draft_output": v.relative(out / "draft"), "final_output": v.relative(out / "final"),
            "artifacts": list(v.ARTIFACTS),
            "source_path_convention": "source_refs are relative to case_root; files_read and trace references are relative to lean_judge_verification.",
            "provenance": {k: metadata[k] for k in ("source_revision", "source_repository", "lean_toolchain")},
        }
        project, external = registry(job)
        # Facts only: no preselected mathematical boundary, blueprint prose or old translation.
        write(v.read_path(job["declaration_index"]), {
            "target": job["target"],
            "project": [{k: n.get(k) for k in (
                "name", "kind", "module", "range", "elaborated_statement",
                "type_dependencies", "value_dependencies", "declaration_metadata_dependencies")}
                for n in project.values()],
            "external": list(external.values()),
            "warning": "Raw declaration edges include definitions and implementation details; not a mathematical proof tree.",
        })
        for stage in ("plan", "draft", "final"):
            (out / stage).mkdir(parents=True, exist_ok=True)
        trace_root.mkdir(parents=True, exist_ok=True)
        write(job_path, job)
        jobs.append(v.relative(job_path))
        frozen.extend([job_path, v.read_path(job["declaration_index"])])
    write(run / "manifest.json", {
        "version": "1.0", "mode": "author_selected_boundary", "created_at_utc": v.now(),
        "jobs": jobs, "frozen_inputs": v.fingerprint(frozen), "agents": [], "turns": [],
        "execution": "Offline lifecycle controller; an external agent runner supplies real thread and turn IDs. No model calls are made here.",
        "isolation": "Declared case-local input allowlists and distinct reviewer thread; not an OS access audit.",
    })
    print(f"Prepared {len(jobs)} case(s); authors select the boundaries.")


def get_jobs(run):
    manifest = read(run / "manifest.json")
    if manifest.get("mode") != "author_selected_boundary" or manifest.get("version") != "1.0":
        raise ValueError("Not a formal staged run; use check_data.py for the retained flat reference packages")
    v.check_hashes(manifest["frozen_inputs"])
    jobs = [read(v.read_path(name)) for name in manifest["jobs"]]
    for job in jobs:
        case = v.read_path(job["case_root"])
        check_receipt(case, read(case / "evidence/manifest.json"))
    return jobs


def turns_for(job):
    manifest = read(v.read_path(job["run_root"]) / "manifest.json")
    return [x for x in manifest["turns"] if x["case_id"] == job["case_id"]]


def record_turn(job, phase, thread_id, turn_id, turn_id_source="provider"):
    if not thread_id.strip() or not turn_id.strip():
        raise ValueError("Use real, nonempty thread and turn IDs")
    if turn_id_source not in ("provider", "runner_observed_invocation"):
        raise ValueError("Unknown turn identity source")
    run = v.read_path(job["run_root"])
    manifest = read(run / "manifest.json")
    entries = turns_for(job)
    entry = {"case_id": job["case_id"], "phase": phase, "thread_id": thread_id, "turn_id": turn_id}
    if turn_id_source != "provider":
        entry["turn_id_source"] = turn_id_source
    previous = next((x for x in entries if all(x.get(k) == value for k, value in entry.items())), None)
    if previous is not None:
        if phase == "write" and previous.get("plan_sha256") != sha(v.read_path(job["output"]) / "plan_freeze.json"):
            raise ValueError("This writing turn belongs to an earlier plan; record a new actual turn")
        return
    if any(x["thread_id"] == thread_id and x["turn_id"] == turn_id for x in manifest["turns"]):
        raise ValueError("One actual turn cannot be claimed as multiple stages")
    authors = [x for x in entries if x["phase"] in ("plan", "write")]
    if phase in ("plan", "write"):
        if authors and any(x["thread_id"] != thread_id for x in authors):
            raise ValueError("Author planning and writing must share the same thread")
        if phase == "plan" and (v.read_path(job["output"]) / "plan_freeze.json").exists():
            raise ValueError("Planning is frozen; use reopen-plan before revising")
        if phase == "write":
            check_plan(job)
            check_traces(job, require_ready=True)
            if (v.read_path(job["output"]) / "freeze.json").exists():
                raise ValueError("Draft is already frozen")
            entry["plan_sha256"] = sha(v.read_path(job["output"]) / "plan_freeze.json")
        v.record_agent(run, job, "translator", thread_id)
    elif phase == "review":
        if not any(x["phase"] == "write" for x in entries):
            raise ValueError("Review must follow an actual author writing turn")
        v.record_agent(run, job, "reviewer", thread_id)
    else:
        raise ValueError("Unknown phase")
    manifest = read(run / "manifest.json")  # record_agent may have added a role
    manifest["turns"].append(entry)
    write(run / "manifest.json", manifest)


def freeze_plan(job):
    out = v.read_path(job["output"])
    if (out / "plan_freeze.json").exists():
        return check_plan(job)
    plans = [x for x in turns_for(job) if x["phase"] == "plan"]
    if not plans:
        raise ValueError("Record the author planning turn first")
    previous_turns = {read(path)["planning_turn_id"] for path in
                      (out / "plan_history").glob("revision_*/plan_freeze.json")}
    if plans[-1]["turn_id"] in previous_turns:
        raise ValueError("A reopened plan needs a new actual planning turn")
    boundary, sketch, coverage = validate_plan(job)
    write(out / "trace_plan.json", trace_plan(job, sketch))
    write(out / "plan_freeze.json", {
        "case_id": job["case_id"], "frozen_at_utc": v.now(),
        "author_thread_id": plans[-1]["thread_id"], "planning_turn_id": plans[-1]["turn_id"],
        "outputs": v.fingerprint([out / "plan" / name for name in PLAN_FILES]),
        "reads": v.fingerprint([v.read_path(name) for name in boundary["files_read"]]),
        "trace_plan": v.fingerprint([out / "trace_plan.json"]),
        "dependency_coverage": coverage,
        "limitation": "Code checks accounting and provenance, not the semantic suitability of stopping points.",
    })
    snapshot_plan_navigation(job)
    return boundary, sketch, coverage


def snapshot_plan_navigation(job):
    """Archive read-time utilities without changing the frozen plan identity."""
    out = v.read_path(job["output"])
    receipt = read(out / "plan_freeze.json")
    pinned = {}
    navigation = v.navigation_paths(job)
    for name, digest in receipt["reads"].items():
        if name not in navigation:
            continue
        source = v.read_path(name)
        if sha(source) != digest:
            raise ValueError("Cannot archive changed read-time navigation bytes")
        archive = v.read_path(job["run_root"]) / "snapshot/navigation" / (digest + source.suffix)
        archive.parent.mkdir(parents=True, exist_ok=True)
        if archive.exists() and sha(archive) != digest:
            raise ValueError("Navigation archive collision")
        if not archive.exists():
            shutil.copyfile(source, archive)
        pinned[name] = v.relative(archive)
    write(out / "plan_navigation.json", {
        "plan_freeze_sha256": sha(out / "plan_freeze.json"), "snapshots": pinned,
    })


def check_plan(job):
    out = v.read_path(job["output"])
    receipt = read(out / "plan_freeze.json")
    if receipt["case_id"] != job["case_id"]:
        raise ValueError("Frozen plan case mismatch")
    if receipt["author_thread_id"] != v.roles_for(job).get("translator"):
        raise ValueError("Frozen plan belongs to a different author")
    expected = {v.relative(out / "plan" / name) for name in PLAN_FILES}
    if set(receipt["outputs"]) != expected:
        raise ValueError("Plan freeze must contain exactly four planning artifacts")
    for field in ("outputs", "trace_plan"):
        v.check_hashes(receipt[field])
    pinned = {}
    archive_receipt = out / "plan_navigation.json"
    if archive_receipt.exists():
        archived = read(archive_receipt)
        if archived["plan_freeze_sha256"] != sha(out / "plan_freeze.json"):
            raise ValueError("Navigation receipt belongs to a different frozen plan")
        pinned = archived["snapshots"]
        navigation = v.navigation_paths(job)
        for name, destination in pinned.items():
            if name not in navigation or name not in receipt["reads"]:
                raise ValueError("Only actually read navigation utilities may use archived bytes")
            archive = v.read_path(destination)
            archive.relative_to((v.read_path(job["run_root"]) / "snapshot").resolve())
            if sha(archive) != receipt["reads"][name]:
                raise ValueError("Frozen planning navigation snapshot changed")
    v.check_hashes({name: digest for name, digest in receipt["reads"].items() if name not in pinned})
    boundary, sketch, coverage = validate_plan(job)
    if set(receipt["reads"]) != set(boundary["files_read"]):
        raise ValueError("Frozen planning reading log changed")
    return boundary, sketch, coverage


def reopen_plan(job):
    out = v.read_path(job["output"])
    if (out / "freeze.json").exists():
        raise ValueError("Draft already frozen: create a new run for a boundary revision")
    check_plan(job)
    archive_root = out / "plan_history"
    number = len(list(archive_root.glob("revision_*"))) + 1
    destination = archive_root / f"revision_{number:03d}"
    destination.mkdir(parents=True)
    shutil.copytree(out / "plan", destination / "plan")
    for name in ("plan_freeze.json", "plan_navigation.json", "trace_plan.json", "trace_readiness.json"):
        if (out / name).exists():
            shutil.move(str(out / name), str(destination / name))
    # A partially written draft must never silently survive a changed boundary.
    if any((out / "draft").iterdir()):
        shutil.move(str(out / "draft"), str(destination / "draft"))
        (out / "draft").mkdir()
    print(f"Plan reopened; previous plan/draft preserved at {destination}")


def check_traces(job, require_ready=False, save=False):
    _, sketch, _ = check_plan(job)
    entries = []
    for item in trace_plan(job, sketch):
        path = v.read_path(job["run_root"]) / "traces" / item["source"] / Path(item["file"]).with_suffix(".json")
        if not path.exists():
            entries.append({**item, "status": "missing"})
            continue
        trace, _, _ = v.validate_trace(job, v.relative(path))
        entries.append({**item, "status": trace["status"], "sha256": sha(path)})
    ready = all(x["status"] in ("success", "partial_trace", "no_tactic_traces") for x in entries)
    result = {"case_id": job["case_id"], "ready": ready, "files": entries}
    if save:
        write(v.read_path(job["output"]) / "trace_readiness.json", result)
    if require_ready and not ready:
        raise ValueError("Expanded-file traces are missing; extract the recorded trace plan before writing")
    return result


def task(job, phase):
    out = v.read_path(job["output"])
    if phase == "write":
        check_traces(job, require_ready=True)
    elif phase == "review":
        v.check_frozen(job)
    prompt = job[{"plan": "plan_prompt", "write": "write_prompt", "review": "review_prompt"}[phase]]
    return (
        f"Case: {job['case_id']}\nJob: {job['job_file']}\n"
        f"Read the common mathematical standard: {job['translation_prompt']}\n"
        f"Read and execute the stage instruction: {prompt}\n"
        f"Read the boundary policy and schemas named in the job. Record actual reads.\n"
        + ("Use a fresh author thread; do not inherit old case prose.\n" if phase == "plan" else
           "Continue the SAME author thread used for planning. Use the frozen plan and new trace results.\n" if phase == "write" else
           "Use a DIFFERENT, fresh reviewer thread; do not inherit the author's conversation history.\n")
        + f"Output directory: {v.relative(out / ('plan' if phase == 'plan' else 'draft' if phase == 'write' else 'final'))}\n"
        "The external runner records the actual thread/turn IDs; do not invent them or edit administrative receipts."
    )


def freeze_draft(job):
    plan_digest = sha(v.read_path(job["output"]) / "plan_freeze.json")
    if not any(x["phase"] == "write" and x.get("plan_sha256") == plan_digest for x in turns_for(job)):
        raise ValueError("Record an actual writing turn before freezing the draft")
    check_traces(job, require_ready=True)
    return v.freeze(job)


def checked_run_path(path):
    """Keep generated runs in a dedicated private runtime subdirectory."""
    run = Path(path).resolve()
    runtime = (v.PROJECT / ".runtime").resolve()
    run.relative_to(runtime)
    if run == runtime:
        raise ValueError("Use a dedicated run directory beneath .runtime")
    return run


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=("prepare", "task", "record-turn", "check-plan",
        "freeze-plan", "reopen-plan", "check-traces", "freeze", "validate", "summarize"))
    p.add_argument("--run", required=True, type=Path)
    p.add_argument("--case-root", action="append", type=Path, default=[])
    p.add_argument("--case")
    p.add_argument("--phase", choices=("plan", "write", "review"))
    p.add_argument("--thread")
    p.add_argument("--turn")
    p.add_argument("--turn-id-source", choices=("provider", "runner_observed_invocation"), default="provider",
                   help="Use runner_observed_invocation only when the transport exposes no native turn ID; record the actual observed invocation, not a fabricated provider ID")
    p.add_argument("--stage", choices=("draft", "final"), default="draft")
    p.add_argument("--with-review", action="store_true")
    args = p.parse_args()
    try:
        run = checked_run_path(args.run)
    except ValueError as exc:
        p.error(str(exc))
    if args.command == "prepare":
        return prepare(run, args.case_root)
    jobs = get_jobs(run)
    if args.case:
        jobs = [j for j in jobs if args.case in (j["case_id"], j["key"])]
        if not jobs:
            p.error("Unknown case")
    if args.command in ("task", "record-turn") and (len(jobs) != 1 or not args.phase):
        p.error("task/record-turn require one --case and --phase")
    if args.command == "record-turn":
        if not args.thread or not args.turn:
            p.error("record-turn requires actual --thread and --turn IDs")
        return record_turn(jobs[0], args.phase, args.thread, args.turn, args.turn_id_source)
    if args.command == "task":
        print(task(jobs[0], args.phase))
        return
    if args.command == "summarize":
        return v.summarize(run, jobs)
    for job in jobs:
        if args.command == "check-plan":
            validate_plan(job)
        elif args.command == "freeze-plan":
            freeze_plan(job)
        elif args.command == "reopen-plan":
            reopen_plan(job)
        elif args.command == "check-traces":
            print(json.dumps(check_traces(job, save=True), ensure_ascii=False))
            continue
        elif args.command == "freeze":
            freeze_draft(job)
        else:
            if args.with_review and not any(x["phase"] == "review" for x in turns_for(job)):
                raise ValueError("Record the independent reviewer turn")
            v.validate_job(job, args.stage, args.with_review)
        print(f"Valid: {job['case_id']} ({args.command}; structure/provenance, not mathematical certification)")


if __name__ == "__main__":
    main()
