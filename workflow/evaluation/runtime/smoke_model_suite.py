#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import tempfile
import time
from dataclasses import replace
from pathlib import Path

import agent_call
import bare_model
from agent_call import AgentConfig, run_json_agent
from bare_model import ProviderConfig, build_payload, extract_output_text, public_config, send_one_request
from model_profiles import DEFAULT_PROFILES_DIR, load_suite, solver_profiles
from support import atomic_write_json, merged_environment


def main() -> int:
    parser = argparse.ArgumentParser(description="Bounded connection tests only; no dataset inputs.")
    parser.add_argument("--profiles-dir", type=Path, default=DEFAULT_PROFILES_DIR)
    parser.add_argument("--mode", choices=["formal", "test"], default="test")
    parser.add_argument("--label", action="append", default=[])
    parser.add_argument("--agent", action="store_true")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    # Fail fast during configuration checks; production retry policy is unchanged.
    bare_model.TRANSIENT_RETRY_DELAYS_SECONDS = ()
    agent_call.TRANSIENT_CODEX_RETRY_DELAYS_SECONDS = ()
    selected = solver_profiles(args.mode, args.profiles_dir)
    unknown = set(args.label) - {label for label, _ in selected}
    if unknown:
        parser.error(f"labels not in selected mode: {sorted(unknown)}")
    results = []
    for label, path in selected:
        if args.label and label not in args.label:
            continue
        config = ProviderConfig.from_environment(merged_environment(path), base_dir=path.parent)
        probe = replace(config, timeout_seconds=120)
        start = time.monotonic()
        result = {"label": label, "config": public_config(probe)}
        try:
            response = send_one_request(probe, build_payload(probe, "Answer directly without tools or retrieval.", "What is 17 * 19? Reply with only the integer."))
            output = extract_output_text(response, config.wire_api).strip()
            reasoning = (response.get("choices") or [{}])[0].get("message", {}).get("reasoning_content", "")
            if config.wire_api == "anthropic_messages":
                reasoning = "".join(block.get("thinking", "") for block in response.get("content", []))
            result.update(status="passed" if output == "323" else "unexpected_answer", output=output, usage=response.get("usage"), reasoning_chars=len(reasoning or ""))
        except Exception as error:
            result.update(status="failed", error=str(error).replace(config.api_key, "[REDACTED]")[:1500])
        result["seconds"] = round(time.monotonic() - start, 2)
        results.append(result)
        atomic_write_json(args.output, {"purpose": "configuration_smoke_not_experiment", "results": results})
        print(json.dumps(result, ensure_ascii=False), flush=True)
    if args.agent:
        spec = load_suite()["agent"]
        start = time.monotonic()
        result = {"label": "non_solver_agent", "model": spec["model"], "reasoning_effort": spec["reasoning_effort"]}
        try:
            with tempfile.TemporaryDirectory() as temporary:
                schema = Path(temporary) / "smoke.schema.json"
                atomic_write_json(schema, {"type": "object", "additionalProperties": False, "properties": {"answer": {"type": "integer"}}, "required": ["answer"]})
                answer, usage, audit = run_json_agent(instructions="Calculate the requested integer. Do not use tools.", inputs="17 * 19", schema_path=schema, config=AgentConfig(args.profiles_dir / spec["provider"], args.codex_bin, spec["model"], spec["reasoning_effort"], 180), output_label="configuration_smoke")
                result.update(status="passed" if answer == {"answer": 323} else "unexpected_answer", output=answer, usage=usage, audit=audit)
        except Exception as error:
            key = (args.profiles_dir / spec["provider"] / "openai_api_key").read_text().strip()
            result.update(status="failed", error=str(error).replace(key, "[REDACTED]")[:1500])
        result["seconds"] = round(time.monotonic() - start, 2)
        results.append(result)
        atomic_write_json(args.output, {"purpose": "configuration_smoke_not_experiment", "results": results})
        print(json.dumps(result, ensure_ascii=False), flush=True)
    return 0 if results and all(item["status"] == "passed" for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
