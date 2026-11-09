# MLTheoryBench Workflow

This directory covers task construction from source papers, independent calibration, frozen closed-book solving, and anonymized joint judging. [`run.py`](run.py) dispatches each stage to its implementation.

```text
Paper → Thread A → Thread B → full-source Audit ↔ independent Checker
                           → frozen Task → Solvers → Reviewer → Evaluator
```

## Layout

```text
workflow/
├── run.py                         # Unified CLI
├── data_preparation/               # Thread A/B: selection, construction, audit, PRC
├── evaluation/                    # Calibration, freezing, and multi-model judging
│   ├── runtime/
│   ├── prompts/
│   ├── schemas/
│   ├── config/
│   └── tests/
├── proof_experiment/               # Bare-model interface used by construction
├── reviewer_and_evaluator/         # Original single-answer judging contracts
├── runtime_support/               # Construction support and file contracts
└── legacy_comparison/              # Earlier protocol and regression tests
```

Use `evaluate` for released tasks. For new tasks, run `build` or `build-single`, followed by `calibrate`. The compatibility module `legacy_comparison/` retains the earlier scoring fields and feedback behavior.

## Evaluate Released Tasks

```bash
# Validate every task hash offline
python workflow/run.py evaluate \
  --data-root data --paper-id paper_2026_001 --dry-run

# Generate local profiles from protected key files
python workflow/run.py profiles \
  --get-key-file /absolute/protected/path/get_api_key \
  --novita-key-file /absolute/protected/path/novita_api_key

# Independently solve a task and jointly judge the anonymized answers
python workflow/run.py evaluate \
  --data-root data --paper-id paper_2026_001 \
  --mode test --run-id trial_001 --run-root .runtime/trial_001 \
  --profiles-dir .venv/paperproof-config/model-suite
```

See [`evaluation/README.md`](evaluation/README.md) for models and evaluation options. Released-task evaluation uses the frozen task, reference proof, and rubric.

## Construct New Tasks

Thread A inventories theoretical material by mathematical role, ranks flagship chains, then reconstructs source proofs and checks correctness. Thread B produces the Task, GT, Rubric, and Provenance, audits consistency and leakage, and assigns PRC before solving.

| Stage | Prompts |
| --- | --- |
| A1: Contribution Triage | [Triage](data_preparation/prompts/thread_a_turn1_triage.md), [independent filtering audit](data_preparation/prompts/thread_a_triage_audit.md) |
| A2: Flagship Target Selection | [Target Selection](data_preparation/prompts/thread_a_turn2_target_selection.md) |
| A3: Source Recovery and Audit | [Source Audit](data_preparation/prompts/thread_a_turn3_source_audit.md) |
| B1: Formalization Compile | [Compile](data_preparation/prompts/thread_b_turn1_compile.md) |
| B2: Artifact Audit | [Audit](data_preparation/prompts/thread_b_turn2_artifact_audit.md), [Source Check](data_preparation/prompts/thread_b_local_source_check.md), [Revision](data_preparation/prompts/thread_b_revision.md) |
| B3: PRC Assessment | [PRC](data_preparation/prompts/thread_b_turn3_prc_assessment.md) |

Store each paper under `<paper_dir>/private_source/`, with `metadata.json` and the complete HTML, TeX, or extracted text.

```bash
python workflow/run.py build-single \
  --paper-dir /absolute/private/paper_2026_001 \
  --api-profile .venv/paperproof-config/model-suite/get-api \
  --model gpt-6-astra --reasoning-effort high \
  --codex-bin "$(command -v codex)"
```

The batch entry point `build` accepts `--source-papers-root`, `--paper-ids-file`, `--run-root`, and `--workers`. `calibrate` takes a frozen manifest of source construction packages, runs the full-source Audit and independent Checker with bounded feedback, then proceeds to solving and scoring.

## Tests

```bash
python -m unittest discover -s workflow/data_preparation/tests -p 'test_*.py'
python -m unittest discover -s workflow/runtime_support/tests -p 'test_*.py'
python -m unittest discover -s workflow/evaluation/tests -p 'test_*.py'
python -m unittest discover -s workflow/legacy_comparison/tests -p 'test_*.py'
```
