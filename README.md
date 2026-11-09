<div align="center">

# MLTheoryBench

**Evaluating Proofs in Machine Learning Theory**

[Blog](https://openmltheory.com/blog/MLtheorybench) · [Dataset](data/README.md) · [Quick Start](#quick-start) · [Repository Structure](#repository-structure)

</div>

MLTheoryBench turns the principal theoretical contributions of recent machine learning papers into closed-book proof tasks. It measures proof completion and gives partial credit for valid mathematical progress.

The benchmark contains **885 tasks**, reference proofs, 10-point rubrics, and code for task construction and model evaluation. The [project blog](https://openmltheory.com/blog/MLtheorybench) presents the motivation, results, and case studies.

## Evaluation Design

- **One theoretical contribution per task.** A flagship chain can combine matching upper and lower bounds, necessary and sufficient conditions, or a general result and its key application. The task states the target and assumptions; the reference proof retains the intermediate results that the Solver must discover and prove.
- **Complexity assessed before solving.** Proof Reconstruction Complexity (PRC) evaluates strategy discovery, subgoal structure, technical execution, and tool integration, assigning each task a level from PRC0 to PRC4.
- **Audited, frozen tasks.** A full-source Audit and an independent Task+GT Checker verify the task and reference proof before the evaluation version is frozen.
- **Independent validity review and stepwise scoring.** The Validity Reviewer reads the task and answer. The Reference Evaluator adds the reference proof (GT) and rubric, awards credit for valid partial progress, and accepts correct alternative proofs. Scores of 8 or above indicate a substantially complete proof.

<p align="center">
  <img src="https://openmltheory.com/blog/assets/figures/fig1_pipeline_en.png" alt="MLTheoryBench task construction and closed-book evaluation pipeline" width="960">
</p>

## Dataset

Tasks come from arXiv papers submitted between January 1 and July 27, 2026: primary `stat.ML`, ML-related primary `math.OC`, and primary `cs.LG` cross-listed in `stat.ML`. Recent papers, de-identified tasks, and closed-book solving reduce opportunities to recall or retrieve the original proofs.

| PRC0 | PRC1 | PRC2 | PRC3 | PRC4 | Total |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 61 | 324 | 242 | 111 | 147 | **885** |

```text
data/
├── manifest.json                         # Task IDs, PRC, paths, and SHA-256 hashes
├── tasks/<paper_id>/task.md               # Solver input
└── references/<paper_id>/
    ├── proof_ground_truth.md             # Reference proof (GT)
    └── rubric.md                         # Scoring rubric
```

The manifest identifies each task's final frozen version by file hash. During evaluation, the Solver receives the task and common instructions; reference proofs and rubrics are inputs to the judges.

## Quick Start

### 1. Install and Validate

Use Python 3.11 or later and install Codex CLI for agent-based judging.

```bash
git clone https://github.com/zsc58/MLTheoryBench.git
cd MLTheoryBench
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Validate all dataset files and preview the selected task offline
.venv/bin/python workflow/run.py evaluate \
  --data-root data --paper-id paper_2026_001 --dry-run
```

### 2. Configure Models

Model definitions and request parameters are in [`model_suite.json`](workflow/evaluation/config/model_suite.json). Generate local profiles from protected key files. See [model configuration](workflow/evaluation/README.md#model-configuration) for profile settings and custom models.

```bash
.venv/bin/python workflow/run.py profiles \
  --get-key-file /absolute/protected/path/get_api_key \
  --novita-key-file /absolute/protected/path/novita_api_key
```

### 3. Solve and Score

```bash
.venv/bin/python workflow/run.py evaluate \
  --data-root data --paper-id paper_2026_001 \
  --mode test --run-id example_001 --run-root .runtime/example_001 \
  --profiles-dir .venv/paperproof-config/model-suite
```

Test mode runs the two configured GPT Solvers; `--mode formal` selects the full model suite. Repeat `--paper-id` to select several tasks, use `--all` for the entire dataset, and set `--paper-workers` to control concurrency across complete task pipelines.

Each Solver independently receives a 48,000-token completion budget. Answers to the same task are anonymized and jointly reviewed, with a separate score for each answer. An attempt with no final answer receives zero credit; API failures are recorded separately. Results are saved under the specified run directory, and the task version remains frozen throughout evaluation.

## Repository Structure

| Module | Purpose |
| --- | --- |
| [`workflow/`](workflow/README.md) | Paper screening, flagship-chain selection, task construction and calibration, closed-book solving, and joint judging. |
| [`error_taxonomy/`](error_taxonomy/README.md) | Source-paper error classification, repair difficulty, Result Impact, and Paper Impact. |
| [`lean_judge_verification/`](lean_judge_verification/README.md) | Lean-backed natural-language proof construction, fidelity review, and controlled error detection. |

The main entry point is `workflow/run.py`: use `build` to construct tasks, `calibrate` for source-aware revision, and `evaluate` for the released dataset. `workflow/legacy_comparison/` preserves the earlier protocol for compatibility and regression testing.

<details>
<summary><b>Regression Tests</b></summary>

```bash
.venv/bin/python -m unittest discover -s workflow/data_preparation/tests -p 'test_*.py'
.venv/bin/python -m unittest discover -s workflow/runtime_support/tests -p 'test_*.py'
.venv/bin/python -m unittest discover -s workflow/evaluation/tests -p 'test_*.py'
.venv/bin/python -m unittest discover -s error_taxonomy/tests -p 'test_*.py'
.venv/bin/python -m unittest discover -s workflow/legacy_comparison/tests -p 'test_*.py'
```

</details>
