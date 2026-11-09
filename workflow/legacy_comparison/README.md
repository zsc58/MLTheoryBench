# Fixed-Task Model Comparison

This earlier comparison protocol varies the Solver while keeping the Reviewer, Evaluator, Task, GT, and Rubric fixed. Task versions remain frozen during evaluation.

The current joint-judging implementation is in [`workflow/evaluation/`](../evaluation/README.md). This module preserves the earlier prompts, schemas, and regression tests.

## Protocol

`freeze_selection.py` freezes the source construction package's file manifest and SHA-256 hashes. `run_model_comparison.py` reads that manifest and runs a bare-model Solver, reference-blind Validity Reviewer, and Reference Evaluator. The earlier judge defaults to `gpt-5.6-sol` with `high` reasoning effort.

The Solver receives the Task and common instructions. The Reviewer produces a validity report from the Task and answer. The Evaluator uses GT, Rubric, and the validity report to assign a 0–10 score.

## Run

```bash
python workflow/legacy_comparison/freeze_selection.py \
  --source-run-root /absolute/private/formal_run \
  --output /absolute/private/selection.json

python workflow/legacy_comparison/run_model_comparison.py \
  --selection /absolute/private/selection.json \
  --run-root /absolute/private/new_run \
  --solver-env-file /absolute/protected/solver.env \
  --judge-api-profile /absolute/protected/judge_profile \
  --codex-bin /absolute/path/to/codex \
  --judge-model gpt-5.6-sol --judge-reasoning-effort high \
  --workers 5
```

Repeat `--paper-id` to select tasks. `--resume` retries missing or failed items and skips completed items. Run records preserve the input manifest and prompt/schema hashes, with outputs saved under the specified run directory.

See [model configuration](../evaluation/README.md#model-configuration) for profile settings. This module takes manifests in the source construction package format.

## Tests

```bash
python -m unittest discover -s workflow/legacy_comparison/tests -p 'test_*.py'
```
