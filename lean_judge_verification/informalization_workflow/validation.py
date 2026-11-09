"""Source, trace, package and reviewer validation; not a mathematical oracle."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import re
import shutil
from io_utils import check_receipt, check_schema, read, sha, validate_markdown, write

WORKFLOW = Path(__file__).resolve().parent
PROJECT = WORKFLOW.parent
ARTIFACTS = ("alignment.json", "sketch.json", "problem.md", "proof.md", "standard_lemmas.md", "pf_sketch.md")
SNAPSHOT_FILES = ("prompts/author.md", "prompts/plan.md", "prompts/write.md", "prompts/review.md", "schemas/alignment.schema.json", "schemas/sketch.schema.json", "schemas/review.schema.json", "schemas/boundary.schema.json", "boundary_policy.json")
NAVIGATION_FILES = ("README.md", "pipeline.py", "validation.py", "boundary.py", "expansion_sources.py", "publish_reference.py", "test_pipeline.py", "lean_trace/trace_view.py", "lean_trace/README.md")

def now():
    return datetime.now(timezone.utc).isoformat()


def in_tree(base, name):
    path = (Path(base) / name).resolve()
    path.relative_to(Path(base).resolve())
    return path


def relative(path):
    path = Path(path).resolve()
    if path == PROJECT.parent / "AGENTS.md":
        return "../AGENTS.md"
    return str(path.relative_to(PROJECT.resolve()))


def read_path(name):
    if name == "../AGENTS.md":
        return PROJECT.parent / "AGENTS.md"
    return in_tree(PROJECT, name)


def fingerprint(paths):
    return {relative(path): sha(path) for path in sorted(set(paths))}


def check_hashes(entries):
    for name, digest in entries.items():
        if sha(read_path(name)) != digest:
            raise ValueError(f"Frozen file changed: {name}")


def sources(case):
    result = {}
    for name in ("source_files.json", "background_source_files.json"):
        for entry in read(case / "evidence" / name):
            path = in_tree(case, entry["path"])
            path.relative_to((case / "sources").resolve())
            if sha(path) != entry["sha256"]:
                raise ValueError(f"Source snapshot hash mismatch: {path}")
            result[entry["path"]] = entry["sha256"]
    return result


def unique(values, label):
    if len(values) != len(set(values)):
        raise ValueError(f"Duplicate {label}")


def roles_for(job):
    assignments = read(read_path(job["run_root"]) / "manifest.json")["agents"]
    entries = [entry for entry in assignments if entry["case_id"] == job["case_id"]]
    unique([entry["role"] for entry in entries], "agent role assignments")
    return {entry["role"]: entry["agent_id"] for entry in entries}


def record_agent(run, job, role, agent):
    manifest = read(run / "manifest.json")
    entry = {"case_id": job["case_id"], "role": role, "agent_id": agent}
    roles = roles_for(job)
    if role in roles and roles[role] != agent:
        raise ValueError("Role already assigned; preserve the original assignment")
    if any(value == agent for key, value in roles.items() if key != role):
        raise ValueError("Translator and reviewer must be different agents")
    if role == "reviewer":
        if "translator" not in roles:
            raise ValueError("Record the translator before assigning a reviewer")
        check_frozen(job)
    if role not in roles:
        manifest["agents"].append(entry)
        write(run / "manifest.json", manifest)


def navigation_paths(job):
    """Non-mathematical inputs whose read-time bytes may be archived."""
    return {relative(WORKFLOW / name) for name in NAVIGATION_FILES} | {
        relative(read_path(job["run_root"]) / "manifest.json")
    }


def validate_reads(job, names, role="translator"):
    """Enforce a case-local input allowlist, not merely a prior-text denylist."""
    unique(names, "files_read paths")
    case = read_path(job["case_root"])
    retained = sources(case)
    allowed = {relative(case / name) for name in retained}
    allowed.update(job["evidence_inputs"])
    allowed.update(relative(case / "evidence" / name) for name in ("target_build.log", "lean_check.log", "export_driver.lean", "dependency_index.md"))
    allowed.update(job["trace_source_files"])
    # Optional current-run extraction/cache provenance, never an earlier
    # translation. If actually read, freeze() hashes it with all other inputs.
    allowed.update(relative(read_path(job["run_root"]) / name)
                   for name in ("trace_reuse.md", "trace_reuse.json"))
    allowed.update(job[key] for key in ("job_file", "translation_prompt", "alignment_schema", "sketch_schema", "review_schema", "scope_file"))
    allowed.update(job[key] for key in ("plan_prompt", "write_prompt", "boundary_schema", "declaration_index") if key in job)
    if job.get("boundary_mode") == "author_selected":
        out = read_path(job["output"])
        allowed.update(relative(out / "plan" / name) for name in ("boundary.json", "sketch.json", "pf_sketch.md", "standard_lemmas.md"))
        allowed.update(relative(out / "draft" / name) for name in ARTIFACTS)
        allowed.update(relative(out / name) for name in ("plan_freeze.json", "trace_plan.json", "trace_readiness.json"))
    allowed.add("../AGENTS.md")
    # These case-independent utilities explain navigation/validation only; they
    # contain no previous translations or mathematical comparison judgments.
    allowed.update(relative(WORKFLOW / name) for name in NAVIGATION_FILES)
    run_manifest = relative(read_path(job["run_root"]) / "manifest.json")
    if run_manifest in names and role == "translator":
        # The author may inspect its own administrative receipt, but not a
        # multi-case manifest exposing another case's inputs or assignments.
        metadata = read(read_path(run_manifest))
        if metadata.get("jobs") != [job["job_file"]] or any(
            item.get("case_id") != job["case_id"]
            for group in ("agents", "turns") for item in metadata.get(group, [])
        ):
            raise ValueError("Author manifest read must be single-case administrative metadata")
        allowed.add(run_manifest)
    # Some agents began by reading the live instructions before prepare completed.
    # Preserve those truthful paths, but only while they match the frozen contract.
    live_equivalents = {
        relative(WORKFLOW / name): relative(read_path(job["run_root"]) / "snapshot" / name)
        for name in SNAPSHOT_FILES if name != "prompts/review.md"
    }
    if role == "reviewer":
        allowed.update(job[key] for key in ("review_prompt", "review_schema"))
        # Role/input fingerprints are administrative metadata, not prior prose.
        allowed.add(relative(read_path(job["run_root"]) / "manifest.json"))
        out = read_path(job["output"])
        allowed.add(relative(out / "freeze.json"))
        # A reviewer may revisit its own report for an explicitly requested
        # correction; no other case or earlier-run review is exposed by this rule.
        allowed.update(relative(out / name) for name in (
            "review.json", "review.md", "review_initial.json", "review_initial.md",
        ))
        allowed.update(relative(out / stage / name) for stage in ("draft", "final") for name in ARTIFACTS)
        live_equivalents[relative(WORKFLOW / "prompts/review.md")] = job["review_prompt"]
    for name in names:
        if name in live_equivalents:
            if sha(read_path(name)) != sha(read_path(live_equivalents[name])):
                raise ValueError(f"Live instructions differ from frozen snapshot: {name}")
            allowed.add(name)
        if name not in allowed:
            raise ValueError(f"{role} read outside the declared case allowlist: {name}")
        if not read_path(name).is_file():
            raise ValueError(f"Read file does not exist: {name}")
    return [read_path(name) for name in names]


def source_refs(alignment, sketch):
    yield from alignment["contract"]["source_refs"]
    for group in ("definitions", "background_lemmas", "proof_blocks"):
        for item in alignment[group]:
            yield from item["source_refs"]
    for node in sketch["nodes"]:
        yield from node["source_refs"]


def validate_source_refs(job, refs, files_read):
    case = read_path(job["case_root"])
    retained = sources(case)
    counts = {}
    for ref in refs:
        if ref["file"] not in retained:
            raise ValueError(f"Anchor is not a retained source file: {ref['file']}")
        path = in_tree(case, ref["file"])
        if path not in counts:
            counts[path] = len(path.read_text(encoding="utf-8").splitlines())
        if not 1 <= ref["start_line"] <= ref["end_line"] <= counts[path]:
            raise ValueError(f"Out-of-range source anchor: {ref}")
        if not ref["declaration"].strip():
            raise ValueError("Source anchor needs a declaration")
        if relative(path) not in files_read:
            raise ValueError(f"Cited source missing from actual read log: {ref['file']}")


def validate_sketch(job, sketch, alignment, require_blocks=True):
    if sketch["case_id"] != job["case_id"]:
        raise ValueError("Sketch case mismatch")
    ids = [node["id"] for node in sketch["nodes"]]
    backgrounds = sketch["background_ids"]
    unique(ids, "sketch node IDs")
    unique(backgrounds, "sketch background IDs")
    expected_backgrounds = [item["id"] for item in alignment["background_lemmas"]]
    if set(backgrounds) != set(expected_backgrounds) or set(ids) & set(backgrounds):
        raise ValueError("Sketch background closure differs from the declared B-lemmas")
    if set(expected_backgrounds) != {f"B{i}" for i in range(1, len(expected_backgrounds) + 1)}:
        raise ValueError("Background lemmas must use stable consecutive B1, B2, ... IDs")
    nodes = {node["id"]: node for node in sketch["nodes"]}
    target = sketch["target_node"]
    if target not in nodes or [node["id"] for node in sketch["nodes"] if node["role"] == "target"] != [target]:
        raise ValueError("Sketch must have exactly its declared target node")
    if job["scope"]["target"] not in nodes[target]["lean_declarations"]:
        raise ValueError("Target node does not name the target declaration")
    for node in sketch["nodes"]:
        if not node["id"].strip() or not node["summary"].strip() or not node["lean_declarations"]:
            raise ValueError("Sketch nodes need stable IDs, summaries and source declarations")
        unique(node["depends_on"], "node dependencies")
        if not set(node["depends_on"]) <= set(ids) | set(backgrounds):
            raise ValueError(f"Unknown/free background dependency at {node['id']}")
    visited, active = set(), set()

    def visit(node_id):
        if node_id in active:
            raise ValueError("Sketch dependency cycle")
        if node_id in visited or node_id in backgrounds:
            return
        active.add(node_id)
        for dependency in nodes[node_id]["depends_on"]:
            visit(dependency)
        active.remove(node_id)
        visited.add(node_id)

    visit(target)
    if visited != set(ids):
        raise ValueError("Sketch has nodes unreachable from the target")
    obligations = job["scope"]["expanded"]
    covered = set()
    for item in sketch["scope_coverage"]:
        name = item["obligation"]
        if name in obligations:
            index = obligations.index(name)
        elif re.fullmatch(r"[1-9][0-9]*", name) and int(name) <= len(obligations):
            index = int(name) - 1
        else:
            raise ValueError(f"Unknown scope obligation (use exact string or 1-based index): {name}")
        if index in covered:
            raise ValueError("Scope obligation covered more than once")
        covered.add(index)
        if not item["node_ids"] or not set(item["node_ids"]) <= set(ids):
            raise ValueError("Scope coverage must point to nonempty proved sketch nodes")
        unique(item["node_ids"], "scope coverage node IDs")
    if covered != set(range(len(obligations))):
        raise ValueError("Sketch omits expanded scope obligations")
    if require_blocks:
        block_nodes = {block["node_id"] for block in alignment["proof_blocks"]}
        if block_nodes != set(ids):
            raise ValueError("Every sketch node needs aligned proof blocks; all block nodes must exist")


def validate_trace(job, name):
    if name not in job["trace_source_files"]:
        raise ValueError(f"Trace is not for a retained case project source: {name}")
    path = read_path(name)
    trace = read(path)
    retained = job["trace_source_files"][name]
    source_path = in_tree(read_path(job["case_root"]), retained)
    raw = source_path.read_bytes()
    if trace.get("source_sha256") != sha(source_path):
        raise ValueError(f"Trace source hash mismatch: {name}")
    if trace.get("source_file") != retained.removeprefix("sources/project/") or trace.get("source") != job["case_id"].split("/", 1)[0]:
        raise ValueError(f"Trace source identity mismatch: {name}")
    provenance = job["provenance"]
    if trace.get("revision") != provenance["source_revision"] or trace.get("pinned_toolchain") != provenance["lean_toolchain"]:
        raise ValueError(f"Trace revision or toolchain mismatch: {name}")
    if not isinstance(trace.get("lean_version"), str) or not trace["lean_version"].strip() or not trace.get("command"):
        raise ValueError(f"Trace lacks actual version/command provenance: {name}")
    if trace.get("status") not in ("success", "no_tactic_traces", "partial_trace") or type(trace.get("exit_status")) is not int or trace["exit_status"] != 0:
        raise ValueError(f"Trace is not from successful source elaboration: {name}")
    tactics = trace.get("tactics")
    if not isinstance(tactics, list):
        raise ValueError("Trace tactics must be an array")
    if (trace["status"] == "no_tactic_traces") != (not tactics):
        # A partial trace can have no anchored records; it cannot supply references.
        if not (trace["status"] == "partial_trace" and not tactics):
            raise ValueError("Trace status and tactic count disagree")
    indexed = {}
    for tactic in tactics:
        identifier = tactic.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"t[0-9]{6,}", identifier) or identifier in indexed:
            raise ValueError("Invalid or duplicate tactic ID")
        if "parent_id" not in tactic or tactic["parent_id"] is not None and tactic["parent_id"] not in indexed:
            raise ValueError("Tactic parent must precede its child")
        span = tactic.get("source_span", {})
        for endpoint in ("start", "end"):
            point = span.get(endpoint, {})
            if any(type(point.get(key)) is not int for key in ("line", "column", "byte")):
                raise ValueError("Trace coordinates must be integers")
            if point["line"] < 1 or point["column"] < 0 or not 0 <= point["byte"] <= len(raw):
                raise ValueError("Trace coordinate is out of bounds")
            if point["line"] != raw[:point["byte"]].count(b"\n") + 1:
                raise ValueError("Trace byte position and line disagree")
        start, end = span["start"]["byte"], span["end"]["byte"]
        if start > end or tactic.get("tactic") != raw[start:end].decode("utf-8"):
            raise ValueError("Tactic text is not the retained source byte slice")
        for side in ("before", "after"):
            state = tactic.get(side, {})
            goals = state.get("goals")
            if not isinstance(goals, list) or type(state.get("goal_count")) is not int or state["goal_count"] != len(goals):
                raise ValueError("Trace goal count disagrees with actual goals")
            for goal in goals:
                if not isinstance(goal.get("goal_id"), str) or not isinstance(goal.get("pretty"), str):
                    raise ValueError("Trace goal lacks its ID or pretty-printed state")
        indexed[identifier] = tactic
    return trace, indexed, retained


def validate_blocks(job, alignment):
    cache = {}
    statuses = Counter()
    for block in alignment["proof_blocks"]:
        if not block["trace_note"].strip():
            raise ValueError("Every block needs an explicit trace coverage note")
        refs = block["trace_refs"]
        unique([(ref["trace_file"], ref["tactic_id"]) for ref in refs], "block trace references")
        if block["trace_coverage"] == "source_only":
            if refs:
                raise ValueError("source_only cannot contain claimed compiler-state references")
            statuses["source_only"] += 1
            continue
        if not refs:
            raise ValueError("states_attached needs actual trace references")
        partial = False
        for ref in refs:
            name = ref["trace_file"]
            if name not in alignment["files_read"]:
                raise ValueError(f"Cited trace missing from actual read log: {name}")
            if name not in cache:
                cache[name] = validate_trace(job, name)
            trace, tactics, retained = cache[name]
            if ref["tactic_id"] not in tactics:
                raise ValueError(f"Unknown tactic ID: {ref}")
            span = tactics[ref["tactic_id"]]["source_span"]
            # A span ending at column zero excludes that ending line.
            start = span["start"]["line"]
            end = span["end"]["line"] - int(span["end"]["column"] == 0 and span["end"]["line"] > start)
            if not any(anchor["file"] == retained and anchor["start_line"] <= end and start <= anchor["end_line"] for anchor in block["source_refs"]):
                raise ValueError(f"Trace tactic does not overlap the block's source anchors: {ref}")
            partial |= trace["status"] == "partial_trace"
        if partial and not re.search(r"partial|unanchored|hole|incomplete", block["trace_note"], flags=re.IGNORECASE):
            raise ValueError("Partially extracted traces require an explicit partial-coverage note")
        statuses["states_attached_partial_trace" if partial else "states_attached_success"] += 1
    return {"proof_blocks": len(alignment["proof_blocks"]), "block_coverage": dict(statuses), "referenced_trace_files": {name: value[0]["status"] for name, value in cache.items()}}


def validate_job(job, stage="draft", with_review=False):
    if stage not in ("draft", "final"):
        raise ValueError("Unknown artifact stage")
    out = read_path(job["output"])
    if job.get("boundary_mode") == "author_selected":
        from pipeline import check_plan
        from boundary import interfaces, scope_job
        selected, planned, _ = check_plan(job)
        job = scope_job(job, selected)
    if (out / "freeze.json").exists() or stage == "final" or with_review:
        check_frozen(job)
    package = out / stage
    alignment, sketch = read(package / "alignment.json"), read(package / "sketch.json")
    if job.get("boundary_mode") == "author_selected":
        if alignment["background_lemmas"] != interfaces(selected):
            raise ValueError("Background interfaces differ from the frozen author plan")
        if sketch != planned:
            raise ValueError("Proof sketch differs from the frozen plan; revise the plan explicitly")
        if stage == "draft" and (package / "standard_lemmas.md").read_bytes() != (out / "plan/standard_lemmas.md").read_bytes():
            raise ValueError("Standard-lemma text differs from the frozen plan")
    check_schema(alignment, read(read_path(job["alignment_schema"])))
    check_schema(sketch, read(read_path(job["sketch_schema"])))
    if alignment["case_id"] != job["case_id"] or alignment["target"] != job["scope"]["target"]:
        raise ValueError("Alignment target or case mismatch")
    for name in ARTIFACTS[2:]:
        validate_markdown(package / name)
    validate_reads(job, alignment["files_read"], "translator" if stage == "draft" else "reviewer")
    for group in ("background_lemmas", "proof_blocks"):
        unique([item["id"] for item in alignment[group]], group + " IDs")
    validate_source_refs(job, source_refs(alignment, sketch), alignment["files_read"])
    validate_sketch(job, sketch, alignment)
    coverage = validate_blocks(job, alignment)
    result = {"alignment": alignment, "sketch": sketch, "coverage": coverage}
    if with_review:
        result["review"] = validate_review(job)
    return result


def check_frozen(job):
    out = read_path(job["output"])
    receipt = read(out / "freeze.json")
    if receipt.get("case_id") != job["case_id"]:
        raise ValueError("Frozen draft case mismatch")
    expected = {relative(out / "draft" / name) for name in ARTIFACTS}
    if set(receipt["outputs"]) != expected:
        raise ValueError("Frozen draft must include exactly all six artifacts")
    check_hashes(receipt["outputs"])
    reads = receipt["actual_read_files_self_reported"]
    pinned = receipt.get("navigation_snapshots", {})
    navigation = navigation_paths(job)
    for name, archived in pinned.items():
        if name not in navigation or name not in reads:
            raise ValueError("Only actually read navigation utilities may use archived bytes")
        archive = read_path(archived)
        archive.relative_to((read_path(job["run_root"]) / "snapshot").resolve())
        if sha(archive) != reads[name]:
            raise ValueError(f"Frozen navigation snapshot changed: {name}")
    check_hashes({name: digest for name, digest in reads.items() if name not in pinned})
    alignment = read(out / "draft/alignment.json")
    if set(receipt["actual_read_files_self_reported"]) != set(alignment["files_read"]):
        raise ValueError("Frozen reading log differs from the translator's actual-read list")
    roles = roles_for(job)
    if receipt.get("translator_agent_id") != roles.get("translator") or "translator" not in roles:
        raise ValueError("Frozen translator assignment differs from run manifest")
    return receipt


def freeze(job):
    out = read_path(job["output"])
    if (out / "freeze.json").exists():
        return check_frozen(job)
    roles = roles_for(job)
    if "translator" not in roles:
        raise ValueError("Record the translator agent before freezing")
    validated = validate_job(job)
    receipt = {
        "version": "1.0", "case_id": job["case_id"], "frozen_at_utc": now(), "translator_agent_id": roles["translator"],
        "outputs": fingerprint([out / "draft" / name for name in ARTIFACTS]),
        "actual_read_files_self_reported": fingerprint([read_path(name) for name in validated["alignment"]["files_read"]]),
        "read_log_limitations": "Self-reported actual reads; not a sandbox or process access log", "coverage": validated["coverage"],
        "unresolved_issues": validated["alignment"]["unresolved_issues"],
    }
    # Utilities can evolve during a pilot; preserve their exact read-time bytes
    # separately. Mathematical sources, traces, prompts and drafts stay strict.
    receipt["navigation_snapshots"] = {}
    for name, digest in receipt["actual_read_files_self_reported"].items():
        if name in navigation_paths(job):
            destination = read_path(job["run_root"]) / "snapshot/navigation" / (digest + Path(name).suffix)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() and sha(destination) != digest:
                raise ValueError("Existing navigation snapshot does not match its digest")
            if not destination.exists():
                shutil.copyfile(read_path(name), destination)
            receipt["navigation_snapshots"][name] = relative(destination)
    write(out / "freeze.json", receipt)
    return receipt


def validate_review(job):
    frozen = check_frozen(job)
    roles = roles_for(job)
    if set(roles) != {"translator", "reviewer"} or roles["translator"] == roles["reviewer"]:
        raise ValueError("Review requires independent recorded translator/reviewer agents")
    if job.get("boundary_mode") == "author_selected":
        from pipeline import turns_for
        if not any(entry["phase"] == "review" and entry["thread_id"] == roles["reviewer"] for entry in turns_for(job)):
            raise ValueError("Record the actual independent review turn before validation")
    out = read_path(job["output"])
    review = read(out / "review.json")
    check_schema(review, read(read_path(job["review_schema"])))
    if review["case_id"] != job["case_id"]:
        raise ValueError("Review case mismatch")
    validate_markdown(out / "review.md")
    validate_reads(job, review["files_read"], "reviewer")
    if not set(frozen["outputs"]) <= set(review["files_read"]):
        raise ValueError("Reviewer must record reading all six frozen draft files")
    unique([issue["id"] for issue in review["issues"]], "review issue IDs")
    for issue in review["issues"]:
        if any(not issue[key].strip() for key in ("draft_passage", "reason")) or not issue["source_evidence"]:
            raise ValueError("Review defect needs exact passage, source evidence and mathematical reason")
        if issue["resolved"] and not issue["correction"].strip():
            raise ValueError("Resolved review issue needs its correction")
    final = validate_job(job, "final")
    changed = [name for name in ARTIFACTS if sha(out / "draft" / name) != sha(out / "final" / name)]
    unresolved = any(not issue["resolved"] for issue in review["issues"]) or any(check["outcome"] == "unresolved" for check in review["checks"])
    verdict = review["verdict"]
    if verdict == "accepted_unchanged" and (changed or review["issues"] or any(check["outcome"] != "satisfied" for check in review["checks"])):
        raise ValueError("accepted_unchanged must preserve every draft byte and have no corrections/issues")
    if verdict == "accepted_with_corrections" and (not changed or not review["issues"] or not any(issue["resolved"] for issue in review["issues"])):
        raise ValueError("accepted_with_corrections needs actual changed artifacts and a resolved issue")
    if verdict != "needs_followup" and unresolved:
        raise ValueError("Unresolved review findings require needs_followup")
    if verdict == "needs_followup" and not unresolved and not review["limitations"] and not final["alignment"]["unresolved_issues"]:
        raise ValueError("needs_followup requires an explicit unresolved finding or limitation")
    return {"data": review, "changed_artifacts": changed, "final_coverage": final["coverage"]}


def summarize(run, jobs):
    manifest = read(run / "manifest.json")
    results = []
    for job in jobs:
        draft = validate_job(job, "draft", with_review=True)
        reviewed = draft["review"]
        review = reviewed["data"]
        out = read_path(job["output"])
        final_sketch = read(out / "final/sketch.json")
        expanded_sources = {ref["file"] for sketch in (draft["sketch"], final_sketch) for node in sketch["nodes"] for ref in node["source_refs"]}
        required = {name for name, source in job["trace_source_files"].items() if source in expanded_sources}
        candidates = set(job["trace_files"]) - required
        inspected = ((set(draft["alignment"]["files_read"]) | set(review["files_read"])) & set(job["trace_source_files"])) | set(reviewed["final_coverage"]["referenced_trace_files"])
        trace_inventory = {}
        for category, names in (("expanded_source_files", required), ("initial_candidates_only", candidates), ("other_inspected_files", inspected - required - candidates)):
            trace_inventory[category] = {}
            for name in sorted(names):
                path = read_path(name)
                absent = "candidate_not_requested" if category == "initial_candidates_only" else "not_extracted"
                trace_inventory[category][name] = read(path).get("status", "unknown") if path.exists() else absent
        results.append({
            "case_id": job["case_id"], "verdict": review["verdict"], "changed_artifacts": reviewed["changed_artifacts"],
            "review_checks": len(review["checks"]), "issue_counts": dict(Counter(issue["kind"] for issue in review["issues"])),
            "substantive_issues": sum(issue["importance"] == "substantive" for issue in review["issues"]),
            "unresolved_issues": sum(not issue["resolved"] for issue in review["issues"]),
            "draft_coverage": draft["coverage"], "final_coverage": reviewed["final_coverage"], "trace_inventory": trace_inventory,
            "trace_inventory_counts": {category: dict(Counter(files.values())) for category, files in trace_inventory.items()},
            "review_receipt": {"outputs": fingerprint([out / "review.json", out / "review.md"] + [out / "final" / name for name in ARTIFACTS]), "actual_read_files_self_reported": fingerprint([read_path(name) for name in review["files_read"]])},
        })
    write(run / "review_summary.json", {
        "version": "1.0", "created_at_utc": now(), "cases": results, "verdict_counts": dict(Counter(result["verdict"] for result in results)),
        "interpretation": "Independent AI review and trace-coverage counts, not formal English equivalence certificates or estimated translation accuracy. Source-only and partial traces are explicit limitations.",
    })
    print(f"Summarized {len(results)} independent reviews; counts are not mathematical accuracy estimates.")
