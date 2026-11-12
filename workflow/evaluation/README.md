# MLTheoryBench: Calibration and Evaluation

This module provides full-source task auditing, independent checking, task freezing, and anonymized joint evaluation of multiple Solvers. Evaluation of released tasks starts at the Solver stage.

## Evaluate Released Tasks

```text
Frozen Task → independent Solvers → joint Validity Reviewer
                                 → joint Reference Evaluator → one score per answer
```

[`run_released_benchmark.py`](runtime/run_released_benchmark.py) reads [`data/manifest.json`](../../data/manifest.json) and runs the Solver, Reviewer, and Evaluator with their prompts, schemas, and semantic validators.

```bash
# Validate the entire dataset offline
python workflow/evaluation/runtime/run_released_benchmark.py \
  --data-root data --paper-id paper_2026_001 --dry-run

# Solve and score one task
python workflow/evaluation/runtime/run_released_benchmark.py \
  --data-root data --paper-id paper_2026_001 \
  --mode test --run-id trial_001 --run-root .runtime/trial_001 \
  --profiles-dir .venv/paperproof-config/model-suite
```

Repeat `--paper-id` to select tasks, use `--all` for the full dataset, and set `--paper-workers` to control concurrency across complete pipelines. `--mode formal` runs the full model suite; the default `test` mode runs two GPT Solvers. To select custom models, supply repeated `--solver LABEL=/absolute/path/profile.env` arguments in place of `--mode`.

Use a fresh output directory for each run. The runner verifies Task, GT, and Rubric hashes before solving and keeps these files frozen. Runtime provenance records the dataset and task ID; the released Task, GT, and Rubric define the mathematical scoring inputs.

## Evaluate External Answers

Run your agent separately on `data/tasks/<paper_id>/task.md`, using the shared [Solver instructions](prompts/frozen_solver_system_prompt.md) and [answer template](prompts/frozen_solver_answer_template.md). Save its Markdown answer outside `data/`. Then score it without invoking a Solver:

```bash
python workflow/run.py evaluate-answers \
  --data-root data --paper-id paper_2026_001 \
  --answer my_agent=/absolute/path/answer.md \
  --judge-api-profile /absolute/path/codex-judge-profile \
  --run-id my_agent_001 --run-root .runtime/my_agent_001
```

Repeat `--answer` to compare up to eight submissions on the same tasks. For multiple `--paper-id` values or `--all`, each `--answer LABEL=PATH` must point to a directory containing one `<paper_id>.md` file per selected task. `--dry-run` validates the dataset and answer paths without calling a model. The command uses the existing anonymous Reviewer and Reference Evaluator and writes the same score reports as `evaluate`. An empty proof receives zero; `Self-Assessment` is saved but excluded from judging.

External answer provenance and token usage cannot be verified by this runner. To preserve the benchmark's closed-book protocol, the external agent must see only the public task and common instructions, with no access to `data/references/`, source papers, retrieval, or network tools. The 48,000-token completion limit must be enforced by the external agent. The scoring stages still require a configured Codex CLI judge.

## Model Configuration

[`config/model_suite.json`](config/model_suite.json) defines the seven Solver profiles used in the experiments. Agent stages use `gpt-6-astra` with `high` reasoning effort. Edit the model configuration or supply custom profiles to select models and providers.

Generate protected profiles from external key files with permissions set to `600`:

```bash
python workflow/evaluation/runtime/model_profiles.py \
  --get-key-file /absolute/protected/path/get_api_key \
  --novita-key-file /absolute/protected/path/novita_api_key
```

Profiles are generated under `.venv/paperproof-config/model-suite/`, with authentication isolated from interactive Codex login. A custom Solver profile has this format:

```text
ML_THEORY_LLM_BASE_URL=https://provider.example/v1
ML_THEORY_LLM_API_KEY_FILE=/absolute/protected/path/api_key
ML_THEORY_LLM_MODEL=model-name
ML_THEORY_LLM_WIRE_API=chat_completions
ML_THEORY_LLM_REASONING_EFFORT=high
ML_THEORY_LLM_MAX_OUTPUT_TOKENS=48000
ML_THEORY_LLM_STREAM=true
```

The client supports Responses, Chat Completions, and Anthropic Messages, with provider-specific parameter mapping and stream parsing. The completion budget is 48,000 tokens. Usage and finish reasons are recorded for each request.

## Input Isolation and Scoring

| Stage | Inputs | Output |
| --- | --- | --- |
| Solver | Task, common system prompt, and answer template | Independent proof. |
| Validity Reviewer | Task and anonymized answers | Proof-validity report and specific findings. |
| Reference Evaluator | Task, anonymized answers, validity report, GT, and rubric | A 0–10 score and step-level credit for each answer. |

Answers to the same task share Reviewer and Evaluator calls, with separate reports for each submission. Judging uses each answer's mathematical content independently. Correct alternative proofs can receive full credit, and valid partial progress earns partial credit.

Attempts with no final answer receive zero credit and skip judging. Transport and format failures receive separate statuses. An unscorable judgment stops the task. The run directory stores request usage, hashes, input-exposure records, and per-model outputs.

## Calibrate New Tasks

After construction through Thread A/B in [`workflow/`](../README.md), use [`run_comparison.py`](runtime/run_comparison.py) with `--calibrate-once`:

1. The Audit reads the full paper and latest Task, GT, and Rubric, then repairs extraction or formalization errors.
2. A fresh Checker session receives Task+GT and examines key gaps and counterexamples.
3. Checker findings return to the same Audit session for revision, followed by another fresh Checker session.
4. Up to two feedback revisions and three Checker passes are allowed. A passing version is frozen for solving and scoring.

Prepare the input manifest with [`freeze_selection.py`](runtime/freeze_selection.py) using source construction packages. Earlier feedback entry points remain covered by regression tests. Each CLI's `--help` lists its full options.

## Prompts and Tests

Frozen solving uses [`frozen_solver_system_prompt.md`](prompts/frozen_solver_system_prompt.md) and [`frozen_solver_answer_template.md`](prompts/frozen_solver_answer_template.md). Joint judging uses [`reviewer_system_prompt.md`](prompts/reviewer_system_prompt.md), [`evaluator_system_prompt.md`](prompts/evaluator_system_prompt.md), and the two `paired_*_protocol.md` files. Calibration uses [`task_audit.md`](prompts/task_audit.md) and [`task_checker.md`](prompts/task_checker.md).

```bash
python -m unittest discover -s workflow/evaluation/tests -p 'test_*.py'
```
