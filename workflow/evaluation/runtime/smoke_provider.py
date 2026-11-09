#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from bare_model import (
    ProviderConfig,
    build_payload,
    extract_output_text,
    public_config,
    send_one_request,
)
from support import merged_environment, normalize_usage


def main() -> int:
    parser = argparse.ArgumentParser(description="Send one tiny bare-model smoke request.")
    parser.add_argument("--env-file", required=True, type=Path)
    args = parser.parse_args()
    config = ProviderConfig.from_environment(
        merged_environment(args.env_file.resolve()),
        require_credentials=True,
        base_dir=args.env_file.resolve().parent,
    )
    response = send_one_request(
        config,
        build_payload(
            config,
            "Return a direct answer without tools or external retrieval.",
            "Reply with exactly: OK",
        ),
    )
    output = extract_output_text(response, config.wire_api).strip()
    print(
        json.dumps(
            {
                "config": public_config(config),
                "output": output,
                "usage": normalize_usage(response.get("usage")),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if output != "OK":
        raise ValueError(f"unexpected smoke output: {output!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
