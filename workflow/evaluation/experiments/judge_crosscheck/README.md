# Cross-Judge Evaluation

This experiment changes the Reviewer and Evaluator models while keeping the Task, Solver answers, GT, and Rubric fixed to measure scoring stability.

## Protocol

The Reviewer reads the Task and anonymized answers. The Evaluator receives the new validity report, GT, and Rubric. Baseline scores are used for post-hoc comparison. Prompts, schemas, and semantic validation reuse the main evaluation implementation.

Requests use streaming Chat Completions. Reviewer and Evaluator run in separate conversations, with bounded format-correction turns. Successful scores and API failures receive separate records.

## Tools

- [`run_crosscheck.py`](run_crosscheck.py): freeze inputs, run judging, and summarize score differences.
- [`supervise.py`](supervise.py): schedule work and resume failed items.
- [`test_crosscheck.py`](test_crosscheck.py): offline tests for request and scoring adapters.

Set the main-experiment and frozen-framework paths to the experiment packages being rescored. Inputs include existing Solver answers alongside their Task, GT, and Rubric.

```bash
python workflow/evaluation/experiments/judge_crosscheck/run_crosscheck.py --help
python -m unittest discover \
  -s workflow/evaluation/experiments/judge_crosscheck -p 'test_*.py'
```

Supply credentials through an external protected key file. The run directory stores frozen inputs, selections, logs, rescoring outputs, and summary statistics.
