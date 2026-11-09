# MLTheoryBench Lean Judge

This module constructs natural-language proofs from verified Lean sources and evaluates mathematical error detection.

## Structure

| Path | Purpose |
| --- | --- |
| [`informalization_workflow/`](informalization_workflow/README.md) | Proof boundaries, state alignment, planning, translation, independent fidelity review, and package validation. |
| `informalization_workflow/prompts/` | Construction and checking prompts. |
| `informalization_workflow/schemas/` | Structured output schemas for each stage. |
| [`research/case_pipeline/`](research/case_pipeline/README.md) | Lean source preparation, dependency extraction, and build tools. |
| [`data/reviewer.md`](data/reviewer.md) | Error-detection prompt for submitted proofs. |
| [`data/reviewer.schema.json`](data/reviewer.schema.json) | Error-detection output schema. |
| [`boundary_policy.json`](informalization_workflow/boundary_policy.json) | Translation boundaries and verification constraints. |

Prepare pinned source material for source verification, translation, and judging. Runtime records are stored under `.runtime/`.

The proof-validity Reviewer receives the problem statement, allowed background, and submitted proof. Reference proofs and mutation labels remain separate from blind-review inputs.
