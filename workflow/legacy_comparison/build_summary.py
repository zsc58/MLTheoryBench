#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import statistics
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


from support import atomic_write_json


USAGE_KEYS = (
    "input_tokens",
    "cached_input_tokens",
    "non_cached_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
)


def _blank_usage() -> dict[str, int]:
    return {key: 0 for key in USAGE_KEYS}


def build_summary(run_root: Path) -> dict[str, Any]:
    run_root = run_root.resolve()
    run = json.loads((run_root / "run.json").read_text(encoding="utf-8"))
    expected = list(run["paper_ids"])
    status_counts: Counter[str] = Counter()
    validity_counts: Counter[str] = Counter()
    score_counts: Counter[int] = Counter()
    usage = {
        "solver": _blank_usage(),
        "validity_reviewer": _blank_usage(),
        "evaluator": _blank_usage(),
        "total": _blank_usage(),
    }
    scores: list[int] = []
    wall_times: list[float] = []
    failures: list[dict[str, str]] = []

    for paper_id in expected:
        result_path = run_root / "papers" / paper_id / "result.json"
        if not result_path.is_file():
            status_counts["pending"] += 1
            continue
        result = json.loads(result_path.read_text(encoding="utf-8"))
        status = str(result.get("status", "unknown"))
        status_counts[status] += 1
        if isinstance(result.get("wall_time_seconds"), (int, float)):
            wall_times.append(float(result["wall_time_seconds"]))
        if status == "failed":
            failures.append(
                {
                    "paper_id": paper_id,
                    "stage": str(result.get("failed_stage", "unknown")),
                    "error": str(result.get("error", "")),
                }
            )
        evaluation_path = run_root / "papers" / paper_id / "evaluation.json"
        validity_path = run_root / "papers" / paper_id / "validity_report.json"
        if evaluation_path.is_file():
            evaluation = json.loads(evaluation_path.read_text(encoding="utf-8"))
            score = int(evaluation["score"])
            scores.append(score)
            score_counts[score] += 1
        if validity_path.is_file():
            validity = json.loads(validity_path.read_text(encoding="utf-8"))
            validity_counts[str(validity["validity_status"])] += 1

        for stage_name in ("solver", "validity_reviewer", "evaluator"):
            stage = result.get("stages", {}).get(stage_name, {})
            for attempt in stage.get("attempts", []):
                attempt_usage = attempt.get("usage")
                if not isinstance(attempt_usage, dict):
                    continue
                for key in USAGE_KEYS:
                    value = int(attempt_usage.get(key, 0) or 0)
                    usage[stage_name][key] += value
                    usage["total"][key] += value

    summary: dict[str, Any] = {
        "schema_version": "1.0",
        "run_id": run["run_id"],
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "expected_paper_count": len(expected),
        "status_counts": dict(sorted(status_counts.items())),
        "evaluated_paper_count": len(scores),
        "score_distribution": {str(key): score_counts[key] for key in range(11)},
        "mean_score": round(statistics.fmean(scores), 4) if scores else None,
        "median_score": statistics.median(scores) if scores else None,
        "validity_distribution": dict(sorted(validity_counts.items())),
        "usage": usage,
        "wall_time_seconds": {
            "sum_per_paper": round(sum(wall_times), 3),
            "mean_per_paper": round(statistics.fmean(wall_times), 3)
            if wall_times
            else None,
            "max_per_paper": round(max(wall_times), 3) if wall_times else None,
        },
        "failures": failures,
    }
    atomic_write_json(run_root / "summary.json", summary)
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize a model-comparison run.")
    parser.add_argument("--run-root", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    summary = build_summary(parse_args().run_root)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
