<div align="center">

# MLTheoryBench

**Evaluating Proofs in Machine Learning Theory**

[Blog](https://openmltheory.com/blog/MLtheorybench) · [Dataset](data/README.md) · [Quick Start](#quick-start) · [External Agents](#bring-your-own-agent) · [Repository Structure](#repository-structure)

</div>

MLTheoryBench turns the principal theoretical contributions of recent machine learning papers into closed-book proof tasks. It measures proof completion and gives partial credit for valid mathematical progress.

The benchmark contains **885 tasks**, reference proofs, 10-point rubrics, and code for task construction and model evaluation. Read the [MLTheoryBench blog](https://openmltheory.com/blog/MLtheorybench) for the motivation, experimental results, and case studies.

## Choose Your Route

| What you have | Command | What the benchmark does |
| --- | --- | --- |
| A model exposed through a supported API | `evaluate --solver LABEL=profile.env` | Calls the model to produce an answer, then reviews and scores it. |
| An agent or other system that already writes answer Markdown | `evaluate-answers --answer LABEL=PATH` | Reads your answer files, then runs the same review and scoring stages. It does not call your agent. |

Both routes need a separately configured **Codex CLI judge** for the Validity Reviewer and Reference Evaluator. The judge is independent of the Solver being tested. The answer-import route is the simplest way to evaluate an agent with its own runtime or multi-step reasoning loop.

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

Use Python 3.11 or later. Installing the requirements provides the Python dependencies and the pinned Codex CLI used by the judges.

```bash
git clone https://github.com/zsc58/MLTheoryBench.git
cd MLTheoryBench
python3.11 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Locate the pinned Codex CLI bundled by the Python package
CODEX_BIN="$(.venv/bin/python -c 'from codex_cli_bin import bundled_codex_path; print(bundled_codex_path())')"
"$CODEX_BIN" --version

# Verify all 885 frozen Task/GT/Rubric file hashes, without model calls
.venv/bin/python workflow/run.py evaluate \
  --data-root data --paper-id paper_2026_001 --dry-run
```

The dry run reports `validated_tasks: 885` and `model_requests: 0`. Choose task IDs from [`data/manifest.json`](data/manifest.json). Each task has a public `data/tasks/<paper_id>/task.md`, a reference proof, and a rubric. Keep the `CODEX_BIN` variable in the same shell for the commands below, or set it again in a new shell.

### 2. Configure the Judge

Real scoring requires a judge API profile, even when your agent generated the answer elsewhere. The profile is a protected directory containing `config.toml` and a one-line `openai_api_key` file. For the repository's default judge (`gpt-6-astra`, high reasoning effort), use a Responses-compatible provider that serves that model. The judge runs through Codex CLI in an isolated workspace; your interactive Codex login is not used.

Create the profile directory and `.venv/paperproof-config/model-suite/get-api/config.toml`, replacing the base URL if necessary:

```bash
mkdir -p .venv/paperproof-config/model-suite/get-api
chmod 700 .venv/paperproof-config/model-suite/get-api
```

```toml
model = "gpt-6-astra"
model_reasoning_effort = "high"
model_provider = "get-api"

[model_providers.get-api]
name = "Get API"
env_key = "OPENAI_API_KEY"
base_url = "https://api.get-apikey.com/v1"
wire_api = "responses"
requires_openai_auth = true
```

Copy the one-line provider key into the profile and set both files to mode `600`:

```bash
install -m 600 /absolute/protected/path/get_api_key \
  .venv/paperproof-config/model-suite/get-api/openai_api_key
chmod 600 .venv/paperproof-config/model-suite/get-api/config.toml \
  .venv/paperproof-config/model-suite/get-api/openai_api_key
```

Keep credentials under `.venv/`, which Git ignores. Pass `--judge-api-profile .venv/paperproof-config/model-suite/get-api` and `--codex-bin "$CODEX_BIN"` in scoring commands. If you use another Codex-compatible judge model, set `--judge-model` explicitly; changing the judge can change scores.

If you have both keys used by the built-in model suite, the profile generator creates the judge profile and all built-in Solver profiles instead:

```bash
.venv/bin/python workflow/run.py profiles \
  --get-key-file /absolute/protected/path/get_api_key \
  --novita-key-file /absolute/protected/path/novita_api_key
```

The input key files must be regular files with mode `600`. See [model configuration](workflow/evaluation/README.md#model-configuration) for provider-specific settings.

## Bring Your Own Agent

Your agent's input is the public [`task.md`](data/tasks/paper_2026_001/task.md), the common [Solver instructions](workflow/evaluation/prompts/frozen_solver_system_prompt.md), and the [answer template](workflow/evaluation/prompts/frozen_solver_answer_template.md). Supply these to your agent in its own runtime. Its Markdown answer should follow this structure:

```markdown
# Solution

## Proof Framework

...proof obligations and dependencies...

## Full Proof

...the mathematical proof or rigorously established partial results...

## Self-Assessment

...claimed score, completed components, and remaining gaps...
```

Put the mathematical argument in `Full Proof`, before `Self-Assessment`. The template is supplied as a prompt, not enforced by a strict Markdown parser. The scorer removes the `Self-Assessment` section and everything after it before judging, and ignores any self-reported score.

For one task, write the answer to any Markdown file outside `data/`, then run:

```bash
.venv/bin/python workflow/run.py evaluate-answers \
  --data-root data --paper-id paper_2026_001 \
  --answer my_agent=/absolute/path/answer.md \
  --judge-api-profile .venv/paperproof-config/model-suite/get-api \
  --codex-bin "$CODEX_BIN" \
  --run-id my_agent_001 --run-root .runtime/my_agent_001
```

Run the same command with `--dry-run` first to check the task and answer path without any model calls; `--run-id` and `--run-root` are not needed for a dry run. A new `--run-root` directory is required for every real run.

For multiple tasks, place one file per task in a directory, named exactly `<paper_id>.md`. For example, `/absolute/path/agent_answers/paper_2026_001.md`. Point `--answer` at the **directory**, then select tasks with repeated `--paper-id` arguments or `--all`:

```bash
.venv/bin/python workflow/run.py evaluate-answers \
  --data-root data \
  --paper-id paper_2026_001 --paper-id paper_2026_002 \
  --answer agent_a=/absolute/path/agent_a_answers \
  --answer agent_b=/absolute/path/agent_b_answers \
  --judge-api-profile .venv/paperproof-config/model-suite/get-api \
  --codex-bin "$CODEX_BIN" \
  --run-id comparison_001 --run-root .runtime/comparison_001
```

You may submit one to eight distinct answer labels in a run. Every selected task must have a file for every label. `--paper-workers N` controls how many task pipelines run concurrently. The imported answer's source hash is recorded, but its model calls, token use, and input exposure cannot be verified by this runner. To make results comparable, enforce the shared 48,000-token completion budget and closed-book rules in your agent runtime: do not give it `data/references/`, source papers, retrieval, network tools, or other task-specific hints. Reference files are present in this public repository for the judges, so agent isolation is your responsibility.

## Use a Model API Directly

If your Solver is a model endpoint, create a protected `.env` profile and let `evaluate` call it. The current client supports Responses, Chat Completions, and Anthropic Messages. For example, a Chat Completions-compatible model profile contains:

```text
ML_THEORY_LLM_BASE_URL=https://provider.example/v1
ML_THEORY_LLM_API_KEY_FILE=/absolute/protected/path/api_key
ML_THEORY_LLM_MODEL=model-name
ML_THEORY_LLM_WIRE_API=chat_completions
ML_THEORY_LLM_MAX_OUTPUT_TOKENS=48000
ML_THEORY_LLM_STREAM=true
```

The API key file must have mode `600`. The completion limit must be exactly `48000`; some providers also need `ML_THEORY_LLM_CHAT_TOKEN_LIMIT_PARAMETER=max_completion_tokens`. See the [provider configuration](workflow/evaluation/README.md#model-configuration) for optional reasoning settings.

```bash
.venv/bin/python workflow/run.py evaluate \
  --data-root data --paper-id paper_2026_001 \
  --solver my_model=/absolute/path/my_model.env \
  --judge-api-profile .venv/paperproof-config/model-suite/get-api \
  --codex-bin "$CODEX_BIN" \
  --run-id model_001 --run-root .runtime/model_001
```

Repeat `--solver` to evaluate up to eight models together. Alternatively, `--mode test` selects the two built-in GPT Solver profiles and `--mode formal` selects the full configured suite in [`model_suite.json`](workflow/evaluation/config/model_suite.json); these modes require profiles generated for their providers. `--mode`, `--solver`, and `--answer` are alternative input modes, not options to combine in one command.

## Read the Results

Both routes use the same scoring pipeline. Answers to a task are anonymized, then the reference-blind Validity Reviewer checks each proof. The Reference Evaluator receives the public task, anonymized proofs, validity reports, reference proof, and 10-point rubric. It awards step-level credit and accepts mathematically valid alternative proofs. An empty answer receives zero; an unscorable target stops that task and flags it for human review. Scores are judgments by configured models, not formal proof certificates.

```text
.runtime/<run-id>/
├── run.json                                  # Run configuration and status
├── summary.json                              # Per-label counts, mean, distribution
└── papers/<paper_id>/
    ├── result.json                           # Task status and scores by label
    └── rounds/round_0/models/<label>/
        ├── answer.md                         # Submitted answer, Markdown-normalized
        ├── answer_for_evaluator.md           # Proof without Self-Assessment
        ├── validity_report.json              # Reference-blind review
        └── evaluation.json                   # Step-level scoring report
```

The runner checks the frozen Task/GT/Rubric hashes before and after evaluation. Keep each run directory fresh and separate from `data/`. `--dry-run` verifies inputs only; it does not test provider connectivity or produce a score.

## Repository Structure

| Module | Purpose |
| --- | --- |
| [`workflow/`](workflow/README.md) | Paper screening, flagship-chain selection, task construction and calibration, closed-book solving, and joint judging. |
| [`error_taxonomy/`](error_taxonomy/README.md) | Source-paper error classification, repair difficulty, Result Impact, and Paper Impact. |
| [`lean_judge_verification/`](lean_judge_verification/README.md) | Lean-backed natural-language proof construction, fidelity review, and controlled error detection. |

The main entry point is `workflow/run.py`: use `build` to construct tasks, `calibrate` for source-aware revision, `evaluate` for API Solvers, and `evaluate-answers` for submitted answers. `workflow/legacy_comparison/` preserves the earlier protocol for compatibility and regression testing.

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
