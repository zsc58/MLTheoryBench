# AGENTS.md

ML Theory Agent Evaluation

## Goal
Test whether AI agents (Codex-based harness) can solve ML-theory problems, and build a
reproducible benchmark to measure it. Method: "reverse evaluation" — use published 2026
ML-theory papers as ground truth; a solver agent reproduces proofs closed-book, a separate
evaluator agent scores them against human-written rubrics.

Three parts:
1. Data preparation (`data_preparation/`): triage, source recovery, target selection,
   formalization, artifact audit, and proof-reconstruction-complexity assessment.
2. Proof experiment (`proof_experiment/`): the solver generates proofs closed-book.
3. Review and evaluation (`reviewer_and_evaluator/`): an independent reviewer checks proof
   validity, then a reference evaluator scores the proof.

## ⚠️ Hard invariants (never violate)
- **Anti-leakage**: in closed-book eval the solver sees ONLY one file under `public_tasks/`.
  Never expose `private_source/` or `private_gt/`, paper title, authors, arXiv id,
  theorem number, or unique method names.
- **Network OFF** for closed-book runs. For retrieval runs, use a local corpus that EXCLUDES
  the target paper; save retrieval logs.
- Every run records exactly which files were exposed to the agent.
- Split by **PAPER**, never by theorem (theorems from one paper stay in one split).
- `private_source/` and `private_gt/` must never reach a public/remote git or a
  solver-agent prompt. Isolated data-construction and evaluator agents may receive
  only the private files required for their declared task; every such exposure must
  be recorded in the run manifest.
- Dataset-level tracking tables such as `data/_tracking/papers_index.csv` must stay
  de-identified; true title/authors/arXiv/source URL fields belong only in
  `private_source/metadata.json`.

## Directory map
- `data_preparation/` — Thread A/B prompts, schemas, templates, pipeline code, and tests.
- `proof_experiment/` — the single-request bare-model solver and its prompts.
- `reviewer_and_evaluator/` — the validity reviewer and reference evaluator.
- `runtime_support/` — Codex integration, formalization I/O, experiment orchestration, and tests.
- `.runtime/` — local credentials, isolated sessions, temporary files, and run outputs; never commit it.

## Conventions (full version in docs/conventions.md)
- IDs: `paper_<year>_<sequence>` with a sequence of at least three digits
  (`001`, ..., `3000`), and `theorem_<NNN>`; snake_case; ASCII only for
  script-touched paths.
- Language: English for AGENTS.md / code / conventions / schemas / data field names; Chinese for
  README files and human-facing docs/notes.

## Working agreements
- Keep THIS file lean (invariants + map + conventions only); never log day-to-day progress here.
- Update AGENTS.md only when structure, a convention, a command, or a hard constraint changes
  — i.e. only when a future session would be misled without the change.
- **Git commits are always run by the user.** Codex may explain/teach git commands (incl.
  `git commit`, `git commit --amend`, `git push`) but must NEVER execute them itself. Codex may
  run read-only git (status, diff, log) and stage edits via the file tools, then hand the user
  the exact commit command to run.
- VM experiments use Get-Codex with `gpt-5.6-sol` and `high` reasoning by default. Use a
  different VM model or reasoning effort only when the user explicitly requests an override.
- Reproduction commands are documented in `README.md`.
