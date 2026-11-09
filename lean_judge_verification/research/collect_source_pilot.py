#!/usr/bin/env python3
"""Fetch bounded public research assets with hashes; never execute downloads."""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent / "source_pilot_20260908"
MAX_BYTES = 25_000_000


def fetch(source, name, url):
    destination = ROOT / source / name
    if destination.resolve().is_relative_to(ROOT.resolve()) is False:
        raise ValueError("Destination must stay inside this research snapshot")
    meta = destination.with_name(destination.name + ".provenance.json")
    if destination.exists():
        if not meta.exists():
            raise ValueError("Existing asset lacks provenance")
        record = json.loads(meta.read_text())
        if record["url"] != url or record["sha256"] != hashlib.sha256(destination.read_bytes()).hexdigest():
            raise ValueError("Refusing to overwrite mismatched snapshot")
        return destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    error = None
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={"User-Agent": "PaperProof-public-research/1.0"}), timeout=40) as response:
                data = response.read(MAX_BYTES + 1)
                final_url = response.url
                content_type = response.headers.get("Content-Type")
            if len(data) > MAX_BYTES:
                raise ValueError("Asset exceeds bounded download size")
            destination.write_bytes(data)
            meta.write_text(json.dumps({"url": url, "resolved_url": final_url,
                "retrieved_at": datetime.now(timezone.utc).isoformat(),
                "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                "content_type": content_type, "executed": False}, indent=2) + "\n")
            print(json.dumps({"source": source, "path": name, "bytes": len(data)}), flush=True)
            return destination
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            error = exc
            if isinstance(exc, ValueError):
                break
            if isinstance(exc, HTTPError) and exc.code in (400, 401, 403, 404):
                break
            time.sleep(1)
    failure = destination.with_name(destination.name + ".unavailable.json")
    failure.write_text(json.dumps({"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat(),
                                   "error_type": type(error).__name__,
                                   "http_status": getattr(error, "code", None)}, indent=2) + "\n")
    print(json.dumps({"source": source, "path": name, "status": "unavailable",
                      "error_type": type(error).__name__, "http_status": getattr(error, "code", None)}), flush=True)
    return None


def discover():
    for source, repo in [("ai4slt", "YuanheZ/lean-stat-learning-theory"),
                         ("rlmeval", "augustepoiroux/RLMEval")]:
        tree_path = fetch(source, "catalog/github_tree.json", f"https://api.github.com/repos/{repo}/git/trees/main?recursive=1")
        if tree_path:
            tree = json.loads(tree_path.read_text())
            commit = tree["sha"]
            print(json.dumps({"source": source, "tree_sha": commit, "files": len(tree.get("tree", [])),
                              "truncated": tree.get("truncated", False)}))
            fetch(source, "README.md", f"https://raw.githubusercontent.com/{repo}/{commit}/README.md")
        if source == "rlmeval":
            fetch(source, "catalog/releases.json", f"https://api.github.com/repos/{repo}/releases")
            fetch(source, "catalog/hf_search.json", "https://huggingface.co/api/datasets?search=RLMEval")
    fetch("arxiv_math_grading", "catalog/hf_info.json", "https://huggingface.co/api/datasets/LukeBailey181Pub/ArxivMathGradingBench")
    fetch("arxiv_math_grading", "README.md", "https://huggingface.co/datasets/LukeBailey181Pub/ArxivMathGradingBench/raw/main/README.md")
    fetch("arxiv_math_grading", "raw/arxiv_grading_bench.jsonl", "https://huggingface.co/datasets/LukeBailey181Pub/ArxivMathGradingBench/resolve/main/arxiv_grading_bench.jsonl")
    fetch("ai4slt", "catalog/hf_novel_info.json", "https://huggingface.co/api/datasets/yuanhezhang/lean4-stat-learning-theory-novel")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--source")
    parser.add_argument("--name")
    parser.add_argument("--url")
    args = parser.parse_args()
    if args.discover:
        discover()
    elif all([args.source, args.name, args.url]):
        fetch(args.source, args.name, args.url)
    else:
        parser.error("Use --discover or supply source, name and url")


if __name__ == "__main__":
    main()
