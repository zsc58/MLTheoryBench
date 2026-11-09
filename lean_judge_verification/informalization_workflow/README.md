# Lean-to-Natural-Language Workflow

This workflow turns verified Lean targets and their dependencies into self-contained English mathematical packages: a problem statement, standard background lemmas, a hierarchical proof sketch, and a natural-language proof. Declaration dependencies define the proof scope, Lean states verify expanded steps, and an independent Reviewer assesses source fidelity.

## Pipeline

```text
Verified source and declarations
  → author PLAN: proof boundary, sketch, background interfaces
  → validate and freeze plan
  → extract or verify matching Lean traces
  → same author WRITE: aligned natural-language proof
  → independent REVIEW: source fidelity and local corrections
  → validate and freeze final package
```

PLAN and WRITE share an author session. The Reviewer uses a separate session. Code validates source versions, dependencies, structure, and hashes; mathematical review assesses proof boundaries and translation fidelity.

## Artifacts

| Stage | Artifacts |
| --- | --- |
| PLAN | `boundary.json`, `sketch.json`, `pf_sketch.md`, and `standard_lemmas.md`. |
| Trace | Actual Lean states and verification records matched to pinned sources, toolchains, and expanded declarations. |
| WRITE | English problem and proof, with declaration/state alignment. |
| REVIEW | Independent source review, corrections, and final validation. |

Background lemmas specify complete interfaces and justify where expansion stops. The boundary policy keeps the target's central proof obligations within the submitted proof. Trace records explicitly identify missing states, partial coverage, and term-style proofs.

## Entry Points

[`pipeline.py`](pipeline.py) prepares stages and task instructions, registers sessions, freezes plans, and validates translated packages. Author and Reviewer sessions follow the generated instructions. Each input case requires pinned sources and verification receipts.

```bash
python lean_judge_verification/informalization_workflow/pipeline.py --help

python lean_judge_verification/informalization_workflow/trace_batch.py \
  --plan /absolute/private/trace_plan.json \
  --run /absolute/private/new_run --workers 2

python -m unittest discover \
  -s lean_judge_verification/informalization_workflow -p 'test_*.py'
```

[`reuse_traces.py`](reuse_traces.py) reuses complete traces with matching source version, toolchain, and build configuration, retaining their original provenance. [`boundary_policy.json`](boundary_policy.json), prompts, and schemas specify mathematical quality and input boundaries.

See [`case_pipeline`](../research/case_pipeline/README.md) for source preparation and [`lean_trace`](lean_trace/README.md) for read-only state inspection. [`data/reviewer.md`](../data/reviewer.md) defines the proof-validity review stage.
