# Lean Source Preparation

This pipeline collects source files from pinned Lean projects, exports declaration dependencies, verifies targets and axioms, and prepares traceable inputs for natural-language proof construction.

## Dependency Records

- `import_closure.json` records the module import closure, a superset of potentially relevant source files.
- `lean_dependencies.json` records dependencies in elaborated types, proof/definition terms, and declaration metadata, preserving these edge types separately.
- `blueprint_dependencies.json` records Blueprint sections and explicit dependencies. Differences from Lean dependencies guide subsequent review.

After compilation, `collectAxioms` checks transitive axioms. Verification uses pinned sources, toolchains, and dependency versions, with hashes and exit statuses stored in receipts. Verified references must satisfy the approved axiom policy, including the exclusion of `sorryAx`.

## Tools

[`build_cases.py`](build_cases.py) provides `setup`, `prepare`, `cache`, `build`, `trace`, and `summarize`. [`ExportDependencies.lean`](ExportDependencies.lean) exports declaration relationships.

[`case_config.json`](case_config.json) contains example source-project and toolchain settings. Restore the selected project's pinned source version and configure local paths before use. Match each Lean version to its corresponding toolchain and Mathlib dependencies.

```bash
python lean_judge_verification/research/case_pipeline/build_cases.py --help

# Offline parser tests
python lean_judge_verification/research/case_pipeline/test_build_cases.py
```

Compilation and trace outputs are saved in the configured evidence directories. Machine verification establishes Lean source validity and tool behavior; independent mathematical review assesses natural-language translation fidelity.
