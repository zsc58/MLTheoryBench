# MLTheoryBench: Source Error Audit

This module analyzes mathematical errors in source papers, recording error type, repair difficulty, Result Impact, and Paper Impact.

## Method

```text
Full paper + source-audit leads
  → independent audit A
  → independent audit B
  → source-aware reviewer
  → retained findings, repair difficulty, result/paper impact
```

Audits A and B run independently. The Reviewer checks the full assumptions and candidate errors, merges duplicate descriptions, excludes typos and unsupported findings, and assigns classifications and ratings. Counterfactual non-propagation counts a downstream error separately when it remains after assuming the upstream error has been repaired.

Repair difficulty measures the mathematical work needed to fix an argument. Impact measures how much of the original result and principal contribution survives that repair.

Method documentation: [design](docs/design.md) · [error taxonomy](docs/error_taxonomy.md) · [repair and impact](docs/repair_and_impact.md) · [references](docs/references.md).

## Inputs

Each paper requires the complete UTF-8 source, including relevant appendices, and a Thread A Source Audit identifying `theory_candidate` and `internal_support` nodes. The default layout is:

```text
<papers_root>/<paper_id>/
  private_source/extracted_text.md
  paper_analysis/paper_analysis.json
```

`paper_analysis.json` contains the latest `source_audit`. Use `--selection-file` for compatible standalone files or custom layouts. Auditing covers the registered result nodes.

## Run

```bash
# Freeze and validate inputs offline
python error_taxonomy/scripts/run_taxonomy_batch.py prepare \
  --papers-root /absolute/private/papers \
  --paper-ids-file /absolute/private/paper_ids.json \
  --batch-root /absolute/private/audit_run \
  --model gpt-6-astra --reasoning-effort high

python error_taxonomy/scripts/run_taxonomy_batch.py check \
  --batch-root /absolute/private/audit_run

# Run independent audits and the Reviewer
python error_taxonomy/scripts/run_taxonomy_batch.py run \
  --batch-root /absolute/private/audit_run --workers 5 \
  --codex-bin /absolute/path/to/codex \
  --api-profile /absolute/protected/judge_profile
```

`paper_ids.json` has the format `{"paper_ids": ["paper_2026_001"]}`. `--issue-scope major` selects nodes already marked major, retaining the full paper and inventory as context. Model calls require Codex CLI and a protected API profile.

`--resume` skips completed stages and creates a new attempt for failed stages. Records distinguish original judgments, format corrections, transport retries, and usage. Format correction preserves findings and mathematical judgments; structural and transport failures receive explicit failure statuses.

## Validation and Summaries

```bash
python error_taxonomy/scripts/validate_result_node_audits.py \
  /absolute/private/paper_audit.json

python error_taxonomy/scripts/summarize_taxonomy_batch.py \
  /absolute/private/audit_run \
  --output /absolute/private/audit_summary.json

python -m unittest discover -s error_taxonomy/tests -p 'test_*.py'
```

Final classifications and ratings come from the Reviewer, with A/B supplying independent candidate evidence. The batch CLI's full options are listed in [`run_taxonomy_batch.py`](scripts/run_taxonomy_batch.py) under `--help`.
