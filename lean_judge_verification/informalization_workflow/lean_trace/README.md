# Export Tactic States from Original Lean Files

[`trace_states.py`](../trace_states.py) re-elaborates a complete original file using its pinned toolchain and build environment, preserving imports, namespaces, variables, definitions, and proofs. A Lean driver runs from a temporary directory under `.tools/builds/<source>/`, which is removed after completion or timeout.

Prepare the source-specific `cache` and `build` stages described in [source preparation](../../research/case_pipeline/README.md), then run from the repository root:

```bash
python3 -B lean_judge_verification/informalization_workflow/trace_states.py \
  --source tlb --file TestingLowerBounds/Testing/Risk.lean \
  --output lean_judge_verification/.runtime/runs/example_next/traces/tlb/TestingLowerBounds/Testing/Risk.json \
  --timeout 600
```

`--source` supports `ai4slt` (Lean 4.32.0) and `tlb` (Lean 4.13.0-rc3). `--file` is relative to the selected Lean project. Output paths can be absolute or relative to the working directory. Before execution, the tool compares the target file, `lean-toolchain`, and `lake-manifest.json` against snapshot hashes and checks the executable version. The case pipeline verifies source and build-dependency consistency.

## Receipts and Extraction Modes

Each receipt records `source_sha256`, pinned `revision` and `pinned_toolchain`, actual `lean_version`, `driver_sha256`, `launcher_sha256`, the full `command`, working directory, exit code, elapsed time, Lean messages, and tactic states.

`success` means the file elaborated successfully and the anchored tactic nodes in the selected scope were exported. `no_tactic_traces` means elaboration succeeded with no tactic nodes. Errors, timeouts, and missing tree nodes have separate statuses and nonzero exit codes. Existing output files are replaced; use a fresh output path to retain earlier attempts.

The default `--original-only` mode elaborates the full file and exports states for original source nodes, filtering synthetic macro nodes. `--all-nodes` includes those auxiliary nodes. Receipts record `tactic_selection` and filtering counts; earlier receipts may omit this field. `last_processing_phase` identifies whether execution reached imports, command elaboration, or state extraction. CRLF parser offsets are normalized to Lean's LF representation and mapped back to original UTF-8 bytes.

## Tactic Records

- `id`: an InfoTree preorder identifier, such as `t000123`, unique within the trace.
- `parent_id`: the closest source-anchored tactic parent; `null` at the top level.
- `source_span`: `start/end` positions containing `line`, `column`, and `byte`; lines are 1-based, Unicode columns are 0-based, and UTF-8 byte ranges are end-exclusive.
- `tactic`: the source slice at that span. `source_kind`, `syntax_kind`, and `elaborator` describe macro, repeated-span, and nested nodes.
- `before/after`: `goal_count` and a `goals` array. Each goal contains Lean's pretty-printed context and target in `pretty`, plus its metavariable name in `goal_id`.
- `declaration_name`, `namespace`, and `command_span`: source anchors for the declaration and surrounding command.

InfoTree follows elaboration nesting, including macro expansion and backtracking. An empty `after.goals` array describes the focused block; whole-theorem completion is established by successful elaboration. The viewer retains enclosing scopes that intersect the selected lines.

## Inspect States

```bash
python3 -B lean_judge_verification/informalization_workflow/lean_trace/trace_view.py \
  lean_judge_verification/.runtime/reference_evidence/traces/tlb/TestingLowerBounds/Testing/Risk.json \
  --lines 269:270

python3 -B lean_judge_verification/informalization_workflow/lean_trace/trace_view.py \
  lean_judge_verification/.runtime/reference_evidence/traces/tlb/TestingLowerBounds/Testing/Risk.json \
  --id t002586
```

Repeat `--id` to select nodes. `--index` emits one compact JSON line per record with anchors, origin, and goal counts. The viewer's `--original-only` filters display, while `--limit 40` bounds the displayed records and reports truncation. Locate nodes with `--index --original-only`, inspect their actual states, then cite `{trace_file, tactic_id}`. Evidence subsets describe retained nodes and ancestors in their `retention` metadata; extract a fresh trace for additional states.

## Tests

```bash
python3 -B lean_judge_verification/informalization_workflow/test_trace_states.py
```

Offline tests cover Unicode byte slicing, nested parent nodes, bounds and path checks, subset overlap and end-position rules, and pinned-version file matching. Lean smoke tests use `SLT/MatrixInfra/EYM.lean` and `TestingLowerBounds/Testing/Risk.lean`, with outcomes recorded in JSON receipts.
