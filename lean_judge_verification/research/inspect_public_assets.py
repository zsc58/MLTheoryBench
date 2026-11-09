"""Snapshot small public source assets; does not install or execute Lean code."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
COMMIT = "d0f506f0a695018265dccb33bcb05e2f5ca1c876"
PATHS = [
    "lean-toolchain", "lake-manifest.json", "LICENSE",
    "SLT/LeastSquares/BasicInequality.lean", "SLT/LeastSquares/Defs.lean",
    "SLT/LeastSquares/LinearRegression/MinimaxRate.lean",
    "SLT/SubGaussian.lean",
]


def main() -> None:
    target = ROOT / "public_snapshot_20260907"
    target.mkdir(exist_ok=False)
    manifest = {"retrieved_at": datetime.now(timezone.utc).isoformat(),
                "repository": "https://github.com/YuanheZ/lean-stat-learning-theory",
                "commit": COMMIT, "executed_downloaded_code": False,
                "lean_build_performed": False, "files": []}
    try:
        for path in PATHS:
            url = f"https://raw.githubusercontent.com/YuanheZ/lean-stat-learning-theory/{COMMIT}/{path}"
            request = Request(url, headers={"User-Agent": "PaperProof-research/1.0"})
            with urlopen(request, timeout=30) as response:
                content = response.read(2_000_001)
            if len(content) > 2_000_000:
                raise ValueError(f"Unexpectedly large source asset: {path}")
            local = target / path
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_bytes(content)
            manifest["files"].append({"path": path, "url": url, "bytes": len(content),
                                      "sha256": hashlib.sha256(content).hexdigest()})
            print(path, len(content), flush=True)
    finally:
        (target / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
