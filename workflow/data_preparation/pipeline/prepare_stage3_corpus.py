#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from run_stage3_batch import atomic_write_json, validate_private_source


PAPER_ID = re.compile(r"^paper_(\d{4})_(\d+)$")
UNCONDITIONAL_COLLECTIONS = {
    "stat_ml_2026",
    "cs_lg_cross_stat_ml_2026",
}
SCREENED_COLLECTION = "math_oc_ml_2026"


def paper_sort_key(paper_id: str) -> tuple[int, int]:
    match = PAPER_ID.fullmatch(paper_id)
    if match is None:
        raise ValueError(f"invalid paper ID: {paper_id}")
    return int(match.group(1)), int(match.group(2))


def include_metadata(metadata: dict[str, Any]) -> bool:
    if metadata.get("year") != 2026:
        return False
    collection = metadata.get("collection_id")
    if collection in UNCONDITIONAL_COLLECTIONS:
        return True
    return (
        collection == SCREENED_COLLECTION
        and metadata.get("admission_decision") == "accepted"
    )


def prepare_corpus(source_papers_root: Path, output_dir: Path) -> dict[str, Any]:
    selected: list[tuple[str, dict[str, Any]]] = []
    for paper_dir in source_papers_root.glob("paper_*"):
        metadata_path = paper_dir / "private_source/metadata.json"
        if not metadata_path.is_file():
            continue
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if not include_metadata(metadata):
            continue
        paper_id = paper_dir.name
        if metadata.get("paper_id") != paper_id:
            raise ValueError(f"metadata paper_id mismatch for {paper_id}")
        validate_private_source(paper_dir / "private_source", paper_id)
        selected.append((paper_id, metadata))

    selected.sort(key=lambda item: paper_sort_key(item[0]))
    paper_ids = [paper_id for paper_id, _ in selected]
    if len(paper_ids) != len(set(paper_ids)):
        raise ValueError("selected corpus contains duplicate paper IDs")

    collection_counts = Counter(
        metadata["collection_id"] for _, metadata in selected
    )
    source_kind_counts: Counter[str] = Counter()
    legacy_ge6 = 0
    for paper_id, metadata in selected:
        private_source = source_papers_root / paper_id / "private_source"
        declared = metadata.get("content_source_file")
        if declared is not None:
            source_kind_counts[declared] += 1
        else:
            for candidate in (
                "source.html", "source.tex", "extracted_text.md", "source.pdf"
            ):
                if (private_source / candidate).is_file():
                    source_kind_counts[candidate] += 1
                    break
        if (metadata.get("n_formal_targets") or 0) >= 6:
            legacy_ge6 += 1

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "paper_ids.txt").write_text(
        "".join(f"{paper_id}\n" for paper_id in paper_ids), encoding="utf-8"
    )
    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_papers_root": str(source_papers_root.resolve()),
        "selection_policy": {
            "year": 2026,
            "unconditional_collections": sorted(UNCONDITIONAL_COLLECTIONS),
            "screened_collection": SCREENED_COLLECTION,
            "screened_admission_decision": "accepted",
            "legacy_theorem_count_filter_applied": False,
        },
        "paper_count": len(paper_ids),
        "collection_counts": dict(sorted(collection_counts.items())),
        "source_kind_counts": dict(sorted(source_kind_counts.items())),
        "legacy_n_formal_targets_ge6_count": legacy_ge6,
        "paper_ids_file": "paper_ids.txt",
    }
    atomic_write_json(output_dir / "selection_manifest.json", manifest)
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare the deterministic 2026 Stage 3 corpus manifest."
    )
    parser.add_argument("--source-papers-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = prepare_corpus(
        args.source_papers_root.resolve(), args.output_dir.resolve()
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
