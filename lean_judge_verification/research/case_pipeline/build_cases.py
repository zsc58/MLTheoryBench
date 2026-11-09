#!/usr/bin/env python3
"""Reproducible source bundles and Lean/blueprint evidence for configured cases.

No remote writes, model calls, source repairs, or natural-language proof generation.
All generated artifacts stay under this subproject. Original snapshots are read-only.
"""
from __future__ import annotations

import argparse
from collections import deque
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
BUNDLES = BASE / ".runtime/reference_evidence"
CONFIG = json.loads((HERE / "case_config.json").read_text())


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_fingerprint(root: Path) -> str:
    """Hash original project sources and build pins, excluding generated dependencies."""
    paths = sorted(p for p in root.rglob("*.lean") if ".lake" not in p.parts
                   and not p.name.startswith("CaseExport_"))
    paths += [root / n for n in ["lean-toolchain", "lake-manifest.json"] if (root / n).is_file()]
    content = "\n".join(str(p.relative_to(root)) + ":" + digest(p) for p in paths)
    return hashlib.sha256(content.encode()).hexdigest()


def verify_build_sources(source_id: str) -> str:
    source = CONFIG["sources"][source_id]
    expected = source_fingerprint(BASE / source["root"])
    actual = source_fingerprint(BASE / ".tools/builds" / source_id)
    if actual != expected:
        raise ValueError(f"Build source differs from original pinned snapshot: {source_id}")
    return expected


def setup(source_id: str, _cases: list[dict]) -> None:
    source = CONFIG["sources"][source_id]
    target = BASE / ".tools/builds" / source_id
    if not target.exists():
        shutil.copytree(BASE / source["root"], target, ignore=shutil.ignore_patterns(".lake", ".git"))
    verify_build_sources(source_id)
    print(f"{source_id}: isolated build source matches pinned snapshot")


def validate_receipt(evidence: Path, receipt: dict, case: dict, source: dict, fingerprint: str, toolchain: str) -> None:
    expected = {"case_id": case["id"], "target": case["target"],
                "source_revision": source["revision"], "source_fingerprint": fingerprint,
                "lean_toolchain": toolchain, "exit_code": 0}
    if any(receipt.get(key) != value for key, value in expected.items()):
        raise ValueError("Verification receipt contract mismatch")
    files = {"trace_sha256": "lean_dependencies.json", "driver_sha256": "export_driver.lean",
             "build_log_sha256": "target_build.log", "check_log_sha256": "lean_check.log"}
    for key, name in files.items():
        if not (evidence / name).is_file() or receipt.get(key) != digest(evidence / name):
            raise ValueError(f"Verification receipt file mismatch: {name}")


def uncomment(text: str) -> str:
    """Mask nested Lean comments and string contents while preserving source offsets."""
    out = list(text)
    i = depth = 0
    string = False
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                depth += 1
                out[i:i+2] = "  "
                i += 2
            elif text.startswith("-/", i):
                depth -= 1
                out[i:i+2] = "  "
                i += 2
            else:
                if text[i] != "\n":
                    out[i] = " "
                i += 1
        elif string:
            if text[i] == "\\" and i + 1 < len(text):
                out[i:i+2] = "  "
                i += 2
            else:
                if text[i] == '"':
                    string = False
                if text[i] != "\n":
                    out[i] = " "
                i += 1
        elif text.startswith("/-", i):
            depth = 1
            out[i:i+2] = "  "
            i += 2
        elif text.startswith("--", i):
            j = text.find("\n", i)
            if j < 0:
                j = len(text)
            out[i:j] = " " * (j-i)
            i = j
        elif text[i] == '"':
            string = True
            out[i] = " "
            i += 1
        else:
            i += 1
    return "".join(out)


def imports(path: Path) -> list[str]:
    clean = uncomment(path.read_text())
    return re.findall(r"(?m)^\s*(?:(?:public|private|meta)\s+)*import\s+(?:all\s+)?([\w.]+)", clean)


def closure(root: Path, target: str) -> dict:
    if not (root / Path(*target.split(".")).with_suffix(".lean")).is_file():
        raise FileNotFoundError(f"Target module missing: {target} in {root}")
    queue = deque([target])
    files, external, edges = {}, set(), []
    while queue:
        mod = queue.popleft()
        if mod in files:
            continue
        rel = Path(*mod.split(".")).with_suffix(".lean")
        path = root / rel
        if not path.is_file():
            external.add(mod)
            continue
        deps = imports(path)
        files[mod] = str(rel)
        for dep in deps:
            edges.append({"importing_module": mod, "imported_module": dep})
            queue.append(dep)
    return {
        "method": "recursive_project_module_imports",
        "target_module": target,
        "project_modules": dict(sorted(files.items())),
        "external_module_boundary": sorted(external),
        "edges": edges,
        "scope_note": "This is an import-closure source superset, not a theorem-use graph. It contains all project files made available through the target imports, including unused declarations. No depth truncation is applied to file collection.",
    }


def blueprint_nodes(root: Path) -> dict[str, dict]:
    src = root / "blueprint/src"
    if not src.exists():
        return {}
    active, seen = [], set()

    def visit(path: Path) -> None:
        if path in seen:
            return
        seen.add(path)
        text = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text())
        active.append((path, text))
        for ref in re.findall(r"\\input\{([^}]+)\}", text):
            p = src / (ref if ref.endswith(".tex") else ref + ".tex")
            if p.exists():
                visit(p)

    visit(src / "content.tex")
    results = {}
    pattern = re.compile(r"\\begin\{(theorem|lemma|corollary|proposition|definition)\}(.*?)\\end\{\1\}", re.S)
    for path, text in active:
        matches = list(pattern.finditer(text))
        for i, match in enumerate(matches):
            body = match.group(2)
            labels = re.findall(r"\\label\{([^}]+)\}", body)
            if not labels:
                continue
            after = text[match.end():matches[i+1].start() if i+1 < len(matches) else len(text)]
            proof_match = re.search(r"\\begin\{proof\}(.*?)\\end\{proof\}", after, re.S)
            proof = proof_match.group(1) if proof_match else ""
            alltext = body + "\n" + proof
            uses = [v.strip() for group in re.findall(r"\\uses\{([^}]+)\}", alltext) for v in group.split(",") if v.strip()]
            names = [v.strip() for group in re.findall(r"\\lean\{([^}]+)\}", body) for v in group.split(",") if v.strip()]
            item = {
                "label": labels[0], "kind": match.group(1),
                "file": str(path.relative_to(root)),
                "start_line": text.count("\n", 0, match.start()) + 1,
                "lean_declarations": names, "uses": sorted(set(uses)),
                "statement_tex": body.strip(), "proof_tex": proof.strip(),
            }
            results[labels[0]] = item
    return results


def blueprint_closure(root: Path, target: str) -> dict:
    allnodes = blueprint_nodes(root)
    roots = [k for k, v in allnodes.items() if target in v["lean_declarations"]]
    queue, selected, missing = deque(roots), {}, set()
    while queue:
        key = queue.popleft()
        if key in selected:
            continue
        if key not in allnodes:
            missing.add(key)
            continue
        selected[key] = allnodes[key]
        queue.extend(allnodes[key]["uses"])
    return {
        "method": "author_declared_active_blueprint_uses",
        "target": target, "root_labels": roots,
        "nodes": selected, "unresolved_labels": sorted(missing),
        "scope_note": "Author-written blueprint graph, not compiler-extracted proof dependencies. An absent edge is not evidence that Lean omits the mathematical step.",
    }


def tool_env(source: dict) -> dict[str, str]:
    import os
    env = dict(os.environ)
    bindir = BASE / ".tools/toolchains" / source["toolchain_folder"] / "bin"
    env["PATH"] = str(bindir) + ":/opt/homebrew/bin:" + env.get("PATH", "/usr/bin:/bin")
    env["LEAN_NUM_THREADS"] = "3"
    # Avoid storing downloaded Mathlib archives in a user-global cache.
    env["XDG_CACHE_HOME"] = str(BASE / ".tools/cache")
    return env


def background_sources(case: dict, data: dict, dest: Path) -> list[dict]:
    """Copy full source files at the declared external-background stopping boundary."""
    source = CONFIG["sources"][case["source"]]
    buildroot = BASE / ".tools/builds" / case["source"]
    packages = json.loads((buildroot / "lake-manifest.json").read_text())["packages"]
    search = [(str(p["name"]), buildroot / ".lake/packages" / p["name"], p) for p in packages]
    search.append(("lean", BASE / ".tools/toolchains" / source["toolchain_folder"] / "src/lean", {}))
    records = []
    modules = sorted({n["module"] for n in data["external_background_boundary"] if n["module"]})
    for module in modules:
        rel = Path(*module.split(".")).with_suffix(".lean")
        found = next(((name, folder, meta) for name, folder, meta in search if (folder / rel).is_file()), None)
        if found is None:
            records.append({"module": module, "status": "source_not_located"})
            continue
        name, folder, meta = found
        original = folder / rel
        target = dest / "sources/background" / name / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
        url = meta.get("url", "https://github.com/leanprover/lean4").removesuffix(".git")
        rev = meta.get("rev", (BASE / source["root"] / "lean-toolchain").read_text().strip().split(":")[-1])
        uri_path = str(rel) if name != "lean" else "src/lean/" + str(rel)
        records.append({"module": module, "package": name, "path": str(target.relative_to(dest)), "sha256": digest(original), "revision": rev, "url": f"{url}/blob/{rev}/{uri_path}", "status": "copied_at_background_boundary"})
        for license_name in ["LICENSE", "LICENSE.md"]:
            if (folder / license_name).exists():
                shutil.copyfile(folder / license_name, dest / "sources/background" / name / license_name)
    return records


def prepare(case: dict) -> None:
    source = CONFIG["sources"][case["source"]]
    root = BASE / source["root"]
    dest = BUNDLES / case["id"]
    evidence = dest / "evidence"
    bundle = dest / "sources/project"
    info = closure(root, case["module"])
    records = []
    for module, rel in info["project_modules"].items():
        original, copy = root / rel, bundle / rel
        copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, copy)
        records.append({"module": module, "path": str(copy.relative_to(dest)), "sha256": digest(original), "original_snapshot_path": str(original.relative_to(BASE)), "url": f'{source["repository"]}/blob/{source["revision"]}/{rel}'})
    for name in ["LICENSE", "lean-toolchain", "lakefile.lean", "lake-manifest.json"]:
        if (root / name).exists():
            (dest / "sources").mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, dest / "sources" / name)
    dump(evidence / "import_closure.json", info)
    dump(evidence / "source_files.json", records)
    if case["source"] == "tlb":
        bp = blueprint_closure(root, case["target"])
        dump(evidence / "blueprint_dependencies.json", bp)
        for node in bp["nodes"].values():
            original = root / node["file"]
            copy = dest / "sources" / node["file"]
            copy.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, copy)
    trace = evidence / "lean_dependencies.json"
    manifest = {
        "schema_version": "1.0", "case_id": case["id"], "target": case["target"],
        "target_module": case["module"], "source_revision": source["revision"],
        "source_repository": source["repository"],
        "lean_toolchain": (root / "lean-toolchain").read_text().strip(),
        "source_collection": "complete_project_import_closure",
        "project_source_file_count": len(records),
        "lean_locally_verified": False, "proof_term_dependencies_extracted": False,
        "transitive_axioms": None, "standard_axioms_only": None,
        "natural_language_proof": "human_readable_reconstruction_requires_semantic_review",
        "natural_language_expansion": "Up to five project-result layers; standard background is stated explicitly. This depth limit does not truncate the collected source files or the project proof-term closure.",
    }
    receipt_path = evidence / "verification_receipt.json"
    if trace.exists() and receipt_path.exists():
        data = json.loads(trace.read_text())
        receipt = json.loads(receipt_path.read_text())
        if data["target"] != case["target"]:
            raise ValueError("Trace target mismatch")
        validate_receipt(evidence, receipt, case, source, source_fingerprint(root), manifest["lean_toolchain"])
        axioms = data["transitive_axioms"]
        manifest.update({"lean_locally_verified": True, "proof_term_dependencies_extracted": True, "transitive_axioms": axioms, "standard_axioms_only": set(axioms) <= {"propext", "Classical.choice", "Quot.sound"}, "project_declaration_count": len(data["project_declaration_closure"]), "external_boundary_count": len(data["external_background_boundary"]), "trace_sha256": digest(trace)})
        external_files = background_sources(case, data, dest)
        dump(evidence / "background_source_files.json", external_files)
        manifest["background_source_file_count"] = sum(r["status"] == "copied_at_background_boundary" for r in external_files)
        manifest["background_source_missing"] = [r["module"] for r in external_files if r["status"] == "source_not_located"]
        actual = {v["name"] for v in data["project_declaration_closure"]}
        manifest["project_modules_actually_used"] = sorted({v["module"] for v in data["project_declaration_closure"]})
        manifest["verification_receipt"] = "evidence/verification_receipt.json"
        if case["source"] == "tlb":
            bpnodes = bp["nodes"]
            listed = {name for v in bpnodes.values() for name in v["lean_declarations"]}
            dump(evidence / "dependency_comparison.json", {
                "target": case["target"],
                "blueprint_labels": list(bpnodes),
                "blueprint_mapped_names_in_project_proof_closure": sorted(actual & listed),
                "blueprint_mapped_names_not_in_project_proof_closure": sorted(listed - actual),
                "project_proof_names_not_in_blueprint_closure": sorted(actual - listed),
                "interpretation": "Set differences reflect abstraction, alternative proof organization, definitions and formalization glue; they are not automatic errors. Some blueprint-mapped external names are deliberately outside the expanded project closure.",
            })
        index = ["# 实际证明依赖索引", "", "由 Lean 的 elaborated type / proof term 及声明元数据提取；构造子边保留结构字段合同。不是仅靠源码关键词搜索。", "", "| 声明 | 类型 | 原源码 |", "|---|---|---|"]
        for node in sorted(data["project_declaration_closure"], key=lambda n: (n["module"], (n.get("range") or {}).get("start_line", 0), n["name"])):
            rel = node["module"].replace(".", "/") + ".lean"
            line = (node.get("range") or {}).get("start_line", 1)
            url = f'{source["repository"]}/blob/{source["revision"]}/{rel}#L{line}'
            index.append(f'| `{node["name"]}` | {node["kind"]} | [{rel}:{line}]({url}) |')
        (evidence / "dependency_index.md").write_text("\n".join(index) + "\n")
    dump(evidence / "manifest.json", manifest)
    print(f'{case["id"]}: {len(records)} project source files; verified={manifest["lean_locally_verified"]}')


def run_logged(cmd: list[str], source: dict, source_id: str, log: Path) -> None:
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("w") as handle:
        handle.write("COMMAND " + shlex.join(cmd) + "\n")
        handle.flush()
        result = subprocess.run(cmd, cwd=BASE / ".tools/builds" / source_id, env=tool_env(source), stdout=handle, stderr=subprocess.STDOUT)
    print(f'{log.relative_to(BASE)}: exit {result.returncode}', flush=True)
    if result.returncode:
        print(log.read_text()[-9000:])
        raise SystemExit(result.returncode)


def cache(source_id: str, cases: list[dict]) -> None:
    source = CONFIG["sources"][source_id]
    root = BASE / source["root"]
    mods = set()
    for case in cases:
        mods.update(closure(root, case["module"])["external_module_boundary"])
    # Cache CLI conventions differ across the pinned releases.
    mathmods = sorted(m for m in mods if m == "Mathlib" or m.startswith("Mathlib."))
    paths = mathmods if source_id == "ai4slt" else [m.replace(".", "/") + ".lean" for m in mathmods]
    run_logged(["lake", "exe", "cache", "get", *paths], source, source_id, BASE / "research/case_rebuild_20260916" / f"{source_id}_cache.log")


def build(source_id: str, cases: list[dict]) -> None:
    source = CONFIG["sources"][source_id]
    verify_build_sources(source_id)
    run_logged(["lake", "build", *sorted({c["module"] for c in cases})], source, source_id, BASE / "research/case_rebuild_20260916" / f"{source_id}_build.log")


def trace(case: dict) -> None:
    source = CONFIG["sources"][case["source"]]
    fingerprint = verify_build_sources(case["source"])
    buildroot = BASE / ".tools/builds" / case["source"]
    dest = BUNDLES / case["id"] / "evidence"
    dest.mkdir(parents=True, exist_ok=True)
    # A failed rerun must not leave a successful receipt for overwritten evidence.
    (dest / "verification_receipt.json").unlink(missing_ok=True)
    prepare(case)
    summarize()
    run_logged(["lake", "build", case["module"]], source, case["source"], dest / "target_build.log")
    helper = (HERE / "ExportDependencies.lean").read_text()
    driver = f'import {case["module"]}\n' + helper + f'\n#export_case {case["target"]} prefix {json.dumps(source["module_prefix"])} to {json.dumps(str(dest / "lean_dependencies.json"), ensure_ascii=False)}\n'
    name = "CaseExport_" + case["id"].replace("/", "_") + ".lean"
    (buildroot / name).write_text(driver)
    shutil.copyfile(buildroot / name, dest / "export_driver.lean")
    run_logged(["lake", "env", "lean", name], source, case["source"], dest / "lean_check.log")
    dump(dest / "verification_receipt.json", {
        "case_id": case["id"], "target": case["target"], "source_revision": source["revision"],
        "source_fingerprint": fingerprint, "exit_code": 0,
        "trace_sha256": digest(dest / "lean_dependencies.json"),
        "driver_sha256": digest(buildroot / name),
        "build_log_sha256": digest(dest / "target_build.log"),
        "check_log_sha256": digest(dest / "lean_check.log"),
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "lean_toolchain": (buildroot / "lean-toolchain").read_text().strip(),
        "method": "original target rebuilt by lake; exporter elaborated and transitive axioms collected; dependency packages use pinned upstream Mathlib cache",
    })
    prepare(case)


def summarize() -> None:
    rows = []
    for case in CONFIG["cases"]:
        file = BUNDLES / case["id"] / "evidence/manifest.json"
        if not file.exists():
            rows.append({"case_id": case["id"], "target": case["target"], "lean_locally_verified": False})
            continue
        data = json.loads(file.read_text())
        row = {k: data.get(k) for k in ["case_id", "target", "lean_locally_verified", "standard_axioms_only", "transitive_axioms", "project_source_file_count", "project_declaration_count", "external_boundary_count", "background_source_file_count"]}
        row["actual_project_module_count"] = len(data.get("project_modules_actually_used", []))
        bpfile = file.parent / "blueprint_dependencies.json"
        if bpfile.exists():
            bp = json.loads(bpfile.read_text())
            row["blueprint_node_count"] = len(bp["nodes"])
            row["blueprint_unresolved_labels"] = bp["unresolved_labels"]
        rows.append(row)
    dump(BUNDLES / "verification_summary.json", rows)
    lines = ["# 本机核验与依赖回溯汇总", "", "由 `build_cases.py summarize` 从各例清单生成；具体证据以各例的 receipt、日志与源码哈希为准。", "", "| 例子 | 原目标本机核验 | 标准公理范围内 | 项目导入文件数 | 真正用到的项目文件数 | 项目声明数 | 背景源文件数 | Blueprint 节点数 |", "|---|---|---|---:|---:|---:|---:|---:|"]
    for r in rows:
        cells = [f'[{r["case_id"]}]({r["case_id"]}/evidence/manifest.json)', "通过" if r["lean_locally_verified"] else "尚未通过", "是" if r.get("standard_axioms_only") else "待查／否"]
        cells += [str(r[k]) if r.get(k) is not None else "—" for k in ["project_source_file_count", "actual_project_module_count", "project_declaration_count", "background_source_file_count", "blueprint_node_count"]]
        lines.append("| " + " | ".join(cells) + " |")
    lines += ["", "项目声明计数含定义、构造子、实例与自动辅助声明，不是独立大定理数量。导入文件是超集；实际使用关系由 elaborated type/proof term 提取，并补全声明元数据中的结构字段／构造子依赖。背景声明所在文件予以保存，但不把整个 Mathlib 的递归证明无限展开。", "", "标准公理范围为 `propext`、`Classical.choice`、`Quot.sound`。目标的公理检查越过项目／背景边界，若含 `sorryAx` 就不能通过该项。原项目有未被目标引用的占位，不自动污染本目标。", "", "本表不声称自然语言文本经过 Lean 内核认证；译文的完整合同、关键步骤和引用接口另经逐段源码对照。Mathlib 使用原项目固定提交的缓存，不声称本轮重编了整个库。"]
    (BUNDLES / "verification_summary.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["setup", "prepare", "cache", "build", "trace", "summarize"])
    parser.add_argument("--source", choices=list(CONFIG["sources"]))
    parser.add_argument("--case")
    args = parser.parse_args()
    if args.command == "summarize":
        summarize()
        return
    cases = [c for c in CONFIG["cases"] if (not args.source or c["source"] == args.source) and (not args.case or c["id"] == args.case)]
    if not cases:
        parser.error("No matching cases")
    if args.command in {"setup", "cache", "build"}:
        for src in sorted({c["source"] for c in cases}):
            globals()[args.command](src, [c for c in cases if c["source"] == src])
    else:
        for case in cases:
            globals()[args.command](case)
    if args.command in {"prepare", "trace"}:
        summarize()


if __name__ == "__main__":
    main()
