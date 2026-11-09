"""Small dependency-free JSON, hashing and source-receipt utilities."""
import hashlib
import json
from pathlib import Path
import re


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_schema(value, schema, root=None, location="$",):
    """Validate the deliberately small keyword subset used by the workflow schemas."""
    root = root or schema
    if "$ref" in schema:
        node = root
        for part in schema["$ref"].removeprefix("#/").split("/"):
            node = node[part]
        return check_schema(value, node, root, location)
    types = {"object": dict, "array": list, "string": str, "integer": int, "boolean": bool}
    if "type" in schema and type(value) is not types[schema["type"]]:
        raise ValueError(f"{location}: expected {schema['type']}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(f"{location}: invalid enum {value!r}")
    if "const" in schema and value != schema["const"]:
        raise ValueError(f"{location}: invalid constant")
    if "minimum" in schema and value < schema["minimum"]:
        raise ValueError(f"{location}: below minimum")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                raise ValueError(f"{location}: missing {key}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False and set(value) - set(props):
            raise ValueError(f"{location}: unexpected fields {set(value) - set(props)}")
        for key, spec in props.items():
            if key in value:
                check_schema(value[key], spec, root, f"{location}.{key}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            raise ValueError(f"{location}: too few items")
        for i, item in enumerate(value):
            check_schema(item, schema.get("items", {}), root, f"{location}[{i}]")


def check_receipt(case, manifest):
    evidence = case / "evidence"
    receipt = read(evidence / "verification_receipt.json")
    expected = {"case_id": manifest["case_id"], "target": manifest["target"], "source_revision": manifest["source_revision"], "lean_toolchain": manifest["lean_toolchain"], "exit_code": 0}
    if any(receipt.get(k) != v for k, v in expected.items()):
        raise ValueError(f"Receipt contract mismatch: {case}")
    files = {"trace_sha256": "lean_dependencies.json", "driver_sha256": "export_driver.lean", "build_log_sha256": "target_build.log", "check_log_sha256": "lean_check.log"}
    for field, name in files.items():
        if sha(evidence / name) != receipt[field]:
            raise ValueError(f"Receipt hash mismatch: {name}")
    return [evidence / name for name in files.values()]


def validate_markdown(path):
    text = path.read_text(encoding="utf-8")
    if not text.strip() or re.search(r"(?<!\\)\\(?:\(|\[)", text):
        raise ValueError(f"Empty text or unsupported math delimiters: {path}")
    if re.search(r"(?m)^[ \t]*\$[ \t]*$", text):
        raise ValueError(f"Use double-dollar delimiters for display math: {path}")
    if text.count("$$") % 2 or text.replace("$$", "").replace("\\$", "").count("$") % 2:
        raise ValueError(f"Unbalanced math delimiters: {path}")
    if "/Users/" in text or "private_gt/" in text or "private_source/" in text:
        raise ValueError(f"Non-standalone/private path in mathematical output: {path}")
