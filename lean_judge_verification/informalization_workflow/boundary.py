"""Validate an author-selected proof boundary against compiled declaration edges."""
from collections import Counter, deque
from io_utils import read, check_schema
import validation as v

PLAN_FILES = ("boundary.json", "sketch.json", "pf_sketch.md", "standard_lemmas.md")


def registry(job):
    export = read(v.read_path(job["case_root"]) / "evidence/lean_dependencies.json")
    if export.get("target") != job["target"]:
        raise ValueError("Dependency export target mismatch")
    project = {n["name"]: n for n in export["project_declaration_closure"]}
    external = {n["name"]: n for n in export["external_background_boundary"]}
    if len(project) != len(export["project_declaration_closure"]) or set(project) & set(external):
        raise ValueError("Ambiguous declaration registry")
    if job["target"] not in project:
        raise ValueError("Target missing from compiled project declarations")
    return project, external


def interfaces(boundary):
    return [{k: item[k] for k in ("id", "interface", "kind", "source_refs")}
            for item in boundary["background_lemmas"]]


def scope_job(job, boundary):
    return {**job, "scope": {"target": job["target"], "expanded": boundary["expanded_obligations"]}}


def dependency_coverage(job, boundary, sketch):
    project, external = registry(job)
    known = set(project) | set(external)
    assignment = {}
    for role, groups in (
        ("expanded", sketch["nodes"]),
        ("background", boundary["background_lemmas"]),
        ("context", boundary["context_groups"]),
    ):
        for group in groups:
            if role != "expanded" and not group["reason"].strip():
                raise ValueError("Every stopping/context decision needs a reason")
            v.unique(group["lean_declarations"], "group declarations")
            for name in group["lean_declarations"]:
                if name not in known:
                    raise ValueError(f"Declaration not in compiled dependency registry: {name}")
                if role == "expanded" and name not in project:
                    raise ValueError("External proof bodies are outside this source export")
                if name in assignment:
                    raise ValueError(f"Declaration assigned to multiple boundary groups: {name}")
                assignment[name] = role
    if assignment.get(job["target"]) != "expanded":
        raise ValueError("The target must be expanded, never granted as background")
    pending = deque([job["target"]])
    # Internal source nodes used for an explicitly grouped proof must be checked
    # even if the raw direct-call route reaches them through a different wrapper.
    pending.extend(n for n, role in assignment.items() if role == "expanded")
    visited, uncovered, implicit_context, external_used = set(), set(), set(), set()
    while pending:
        name = pending.popleft()
        if name in visited:
            continue
        visited.add(name)
        if name in external:
            external_used.add(name)
            continue  # external proof bodies were not exported
        if name not in project:
            raise ValueError(f"Compiled dependency edge has no declaration: {name}")
        node = project[name]
        role = assignment.get(name)
        if role is None:
            if node["kind"] == "theorem":
                uncovered.add(name)
                continue
            # Definitions/constructors/instances are not free theorem lemmas.
            # Traverse all their edges so grouping cannot conceal a theorem.
            implicit_context.add(name)
            role = "context"
        dependencies = list(node.get("type_dependencies", []))
        dependencies += node.get("declaration_metadata_dependencies", [])
        if role != "background":
            dependencies += node.get("value_dependencies", [])
        pending.extend(dependencies)
    return {
        "uncovered_project_theorems": sorted(uncovered),
        "implicit_definition_context": sorted(implicit_context),
        "external_interfaces_encountered": sorted(external_used),
        "visited_project_declarations": sorted(visited & set(project)),
        "explicit_decision_counts": dict(Counter(assignment.values())),
        "interpretation": "Mechanical dependency accounting, not approval of the mathematical boundary.",
    }


def validate_plan(job, directory=None):
    directory = directory or v.read_path(job["output"]) / "plan"
    boundary, sketch = read(directory / "boundary.json"), read(directory / "sketch.json")
    check_schema(boundary, read(v.read_path(job["boundary_schema"])))
    check_schema(sketch, read(v.read_path(job["sketch_schema"])))
    if (boundary["case_id"], boundary["target"]) != (job["case_id"], job["target"]):
        raise ValueError("Boundary target or case mismatch")
    if any(not s.strip() for s in boundary["expanded_obligations"]):
        raise ValueError("Expanded obligations cannot be empty")
    v.unique(boundary["expanded_obligations"], "expanded obligations")
    for filename in ("pf_sketch.md", "standard_lemmas.md"):
        v.validate_markdown(directory / filename)
    v.validate_reads(job, boundary["files_read"])
    fake_alignment = {"background_lemmas": interfaces(boundary)}
    v.validate_sketch(scope_job(job, boundary), sketch, fake_alignment, require_blocks=False)
    refs = [r for n in sketch["nodes"] for r in n["source_refs"]]
    refs += [r for b in boundary["background_lemmas"] for r in b["source_refs"]]
    v.validate_source_refs(job, refs, boundary["files_read"])
    project, _ = registry(job)
    # The anchors must actually cover the expanded declaration, not merely be
    # valid line numbers elsewhere in a retained source file.
    for node in sketch["nodes"]:
        for name in node["lean_declarations"]:
            item = project.get(name)
            if item is None:
                raise ValueError(f"Expanded declaration missing: {name}")
            expected_file = "sources/project/" + item["module"].replace(".", "/") + ".lean"
            span = item.get("range")
            if not any(r["file"] == expected_file and (not span or
                       r["start_line"] <= span["end_line"] and span["start_line"] <= r["end_line"])
                       for r in node["source_refs"]):
                raise ValueError(f"Expanded declaration source module mismatch: {name}")
    coverage = dependency_coverage(job, boundary, sketch)
    if coverage["uncovered_project_theorems"]:
        raise ValueError("Unclassified reachable project theorems: " +
                         ", ".join(coverage["uncovered_project_theorems"]))
    return boundary, sketch, coverage


def trace_plan(job, sketch):
    needed = {r["file"] for n in sketch["nodes"] for r in n["source_refs"]}
    return [{"source": job["case_id"].split("/", 1)[0],
             "file": name.removeprefix("sources/project/"), "original_only": True}
            for name in sorted(needed) if name.startswith("sources/project/")]
