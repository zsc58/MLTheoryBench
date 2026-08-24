from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


PIPELINE = Path(__file__).resolve().parents[1] / "pipeline"
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

from prepare_stage3_corpus import prepare_corpus  # noqa: E402


class PrepareStage3CorpusTests(unittest.TestCase):
    def _paper(
        self,
        root: Path,
        sequence: int,
        collection: str,
        admission: str,
        *,
        year: int = 2026,
        targets: int = 1,
    ) -> str:
        paper_id = f"paper_{year}_{sequence}"
        private = root / paper_id / "private_source"
        private.mkdir(parents=True)
        (private / "metadata.json").write_text(
            json.dumps(
                {
                    "paper_id": paper_id,
                    "year": year,
                    "collection_id": collection,
                    "admission_decision": admission,
                    "content_source_file": "source.html",
                    "n_formal_targets": targets,
                }
            ),
            encoding="utf-8",
        )
        (private / "source.html").write_text("paper", encoding="utf-8")
        return paper_id

    def test_prepare_corpus_uses_the_three_collection_rules_without_ge6_filter(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "papers"
            output = root / "selection"
            stat = self._paper(
                source, 10, "stat_ml_2026", "accepted_by_category", targets=9
            )
            cross = self._paper(
                source, 2, "cs_lg_cross_stat_ml_2026", "accepted_by_category"
            )
            accepted_math = self._paper(
                source, 8, "math_oc_ml_2026", "accepted"
            )
            self._paper(source, 3, "math_oc_ml_2026", "rejected")
            self._paper(
                source, 1, "stat_ml_2026", "accepted_by_category", year=2025
            )

            manifest = prepare_corpus(source, output)

            self.assertEqual(manifest["paper_count"], 3)
            self.assertEqual(manifest["legacy_n_formal_targets_ge6_count"], 1)
            self.assertEqual(
                (output / "paper_ids.txt").read_text(encoding="utf-8").splitlines(),
                [cross, accepted_math, stat],
            )
            self.assertFalse(
                manifest["selection_policy"]["legacy_theorem_count_filter_applied"]
            )


if __name__ == "__main__":
    unittest.main()
