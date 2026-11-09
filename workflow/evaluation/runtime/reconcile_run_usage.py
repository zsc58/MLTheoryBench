"""Rebuild usage summaries from saved responses without rerunning any model."""
from __future__ import annotations

import argparse
from pathlib import Path

from run_comparison import build_summary, load_json, recover_recorded_usage
from support import atomic_write_json


def reconcile(run_root: Path) -> dict:
    results = []
    for path in sorted((run_root / "papers").glob("*/result.json")):
        result = load_json(path)
        original = path.with_name("result_before_usage_reconciliation.json")
        if not original.exists():
            atomic_write_json(original, result)
        result.update(recover_recorded_usage(path.parent))
        result["usage_accounting_basis"] = "last_reported_cumulative_per_codex_session_plus_bare_api_calls"
        atomic_write_json(path, result)
        results.append(result)
    return build_summary(run_root, results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_root", type=Path)
    args = parser.parse_args()
    print(reconcile(args.run_root.resolve()))
