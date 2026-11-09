# MLTheoryBench

## Layout
- `workflow/`: the complete construction, calibration, and evaluation workflow.
- `workflow/run.py`: stage dispatcher for build, calibrate, evaluate, and profiles.
- `workflow/data_preparation/`: Thread A/B paper-level task construction.
- `workflow/evaluation/`: calibration, frozen multi-model solving, and joint judging.
- `workflow/legacy_comparison/`: preserved earlier comparison protocol and tests.
- `data/tasks/`: released public tasks; Solver may see only the selected task file.
- `data/references/`: released GT and Rubric for evaluators, not Solver input.
- `error_taxonomy/`: classification code and prompts, without experiment data.
- `lean_judge_verification/`: construction/checking code, without auxiliary datasets.

## Invariants
- Keep Solver closed-book: task and common instructions only, with no reference proof,
  rubric, source paper, search, tools, or retrieval.
- Treat published references as evaluator-only material during experiments.
- Do not commit credentials, raw source papers, Solver answers, grading outputs,
  taxonomy records, local reports, or runtime logs.
- Do not modify released task/reference files during evaluation. Verify manifest hashes.
- Preserve prompt and scoring contracts when adapting packaging or paths.
- Keep one paper in one task unit and in one data split.
- Git commits and pushes are normally performed by the user. Execute them only
  when the user explicitly grants permission for the current operation.

## Publication
The user authorized publication of final Task, GT and Rubric on 2026-11-09.
Raw papers, original provenance/source mappings and experimental outputs remain excluded.
