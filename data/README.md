# MLTheoryBench Dataset

**885 closed-book proof tasks, each organized around a principal theoretical contribution.** Each task includes a de-identified problem statement, reference proof, 10-point rubric, and PRC label assessed before solving.

| PRC0 | PRC1 | PRC2 | PRC3 | PRC4 | Total |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 61 | 324 | 242 | 111 | 147 | **885** |

## File Layout

```text
data/
├── manifest.json
├── tasks/<paper_id>/task.md
└── references/<paper_id>/
    ├── proof_ground_truth.md
    └── rubric.md
```

`manifest.json` records each task's internal `paper_id`, `prc`, relative file paths, and SHA-256 hashes. Files contain the final frozen task versions, with PRC labels from the construction stage.

## Read a Task

```python
import json
from pathlib import Path

root = Path("data")
manifest = json.loads((root / "manifest.json").read_text())
item = manifest["tasks"][0]
task = (root / item["task_file"]).read_text()
```

Validate every file and hash:

```bash
python workflow/run.py evaluate \
  --data-root data --paper-id paper_2026_001 --dry-run
```

## Evaluation Inputs

| Stage | Inputs |
| --- | --- |
| Solver | Task and common solving instructions. |
| Validity Reviewer | Task and anonymized Solver answers. |
| Reference Evaluator | Task, anonymized answers, validity report, GT, and rubric. |

See the [project README](../README.md) for running the benchmark and the [blog](https://openmltheory.com/blog/MLtheorybench) for dataset construction.
