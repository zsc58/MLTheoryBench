"""Codex SDK adapter with isolated per-thread workspaces."""

from __future__ import annotations

import asyncio
import hashlib
import importlib.util
import json
import os
import shlex
import shutil
import sys
import tempfile
from dataclasses import asdict, dataclass, is_dataclass
from pathlib import Path
from typing import Any

from openai_codex import (
    ApprovalMode,
    AsyncCodex,
    CodexConfig,
    is_retryable_error,
)

from pipeline_contracts import parse_and_validate, schema_for


SCRIPT_DIR = Path(__file__).resolve().parent
WORKFLOW_ROOT = SCRIPT_DIR.parents[1]
LOCAL_RUNTIME_DIR = WORKFLOW_ROOT / ".runtime"

PHASE_TASKS = {
    "adapter_smoke_test": (
        "Run `python3` on the staged command_probe_script from request context; "
        "the script must create the declared output file from the input file. Do not "
        "create that output by another method. Then try to read the absolute "
        "forbidden_probe_path from request context. Return `blocked` with an empty "
        "outside_observed_text if the sandbox denies access; otherwise return "
        "`readable` and the exact observed text. Report whether command execution "
        "completed or was aborted."
    ),
    "screen_paper": (
        "Screen the admission packet, which contains only the title/front matter, "
        "abstract when available, and complete introduction. Return the paper-admission "
        "contract; the central runner persists the validated decision."
    ),
    "screen_math_oc_title_abstract": (
        "Using only the supplied title and abstract, decide whether this math.OC "
        "paper's central research object or main theoretical result belongs to "
        "machine learning. Accept papers centrally about learning models, training "
        "or learning algorithms, statistical learning, reinforcement learning, "
        "federated learning, or another explicit ML problem. Reject generic "
        "optimization, stochastic approximation, control, PDE, operations research, "
        "or probability work when ML appears only as motivation, a possible "
        "application, an experiment, or an example. Applicability to ML alone is not "
        "enough. Return `undetermined` rather than rejecting when the title and "
        "abstract do not provide enough evidence to decide whether the central "
        "contribution belongs to ML. In the reason, identify the concrete central ML "
        "object and result, explain why the ML mention is incidental, or state what "
        "information is missing for a decision. Return the three-way math.OC "
        "admission contract."
    ),
    "prepare_coarse_paper": (
        "Create the private paper metadata and compact full-paper proof DAG from the "
        "complete line-numbered paper source supplied in request context. It may come "
        "from arXiv HTML, TeX, or MinerU. Inventory every formal "
        "Theorem and Proposition in the main text, appendices, and supplementary "
        "material, but exclude informal summaries. Preserve the original result type "
        "in the DAG while treating both as equal formal targets. Do not screen, rank, "
        "or group formal targets. "
        "Return the complete bundle directly; do not call tools or edit files."
    ),
    "review_coarse_paper_dag": (
        "Review the most recent coarse paper bundle in this same thread against the "
        "complete paper source already in context. Check the formal Theorem and "
        "Proposition inventory, source grounding, proof coverage, dependency semantics, "
        "and global DAG consistency. Use deterministic validation errors from request context as "
        "diagnostics, but repair the underlying graph rather than deleting an edge only "
        "to silence an error. Return pass with a null corrected bundle only when no "
        "change is needed; otherwise return the complete corrected bundle."
    ),
    "prepare_and_map_paper": (
        "Continue the accepted paper workflow: create and fill the paper scaffold, "
        "extract or install the provided extracted text, read the full paper once, "
        "inventory formal theorem statements from the main text, appendices, and "
        "supplementary material, and build the compact paper-level proof DAG. Use "
        "the abstract and Introduction to identify the small set of core result "
        "groups; group parallel theorem variants and exclude overview-only informal "
        "restatements. Do not create theorem scaffolds or formalize core results."
    ),
    "formalize_selected_theorem": (
        "Complete the core result group's private ground truth from the extracted "
        "source context and code-derived proof DAG. Check the subgraph. For difficulty "
        "1, apply the key-lemma benchmark normally. For deeper targets, preserve "
        "automatically selected upstream core results, ignore their covered ancestors, "
        "and choose at most three additional ladder results without exhaustive numeric "
        "scoring. Formalize selected steps and finish the ground-truth derivation. "
        "Do not rebuild the DAG or read the full paper."
    ),
    "formalize_coarse_theorem": (
        "Convert the supplied theorem packet into the seven requested Markdown files. "
        "Preserve the complete source proof in ground truth, make inherited assumptions "
        "explicit, sanitize the direct public task, and create its direct-proof rubric. "
        "Do not select key lemmas, create a ladder task, call tools, or edit files. "
        "Return every complete file in the structured bundle."
    ),
    "build_and_review_theorem_tasks": (
        "Build both rubrics and both public tasks from the completed private ground "
        "truth. Review each task as a standalone solver input, repair format and "
        "anti-leakage problems, run deterministic validation, and return the final "
        "theorem-agent result."
    ),
    "review_theorem_outputs": (
        "Review all theorem-agent outputs for this paper. Read each public task first "
        "without relying on private context, then compare it against private ground truth. "
        "Check completeness, anti-leakage, and cross-file consistency, update task "
        "metadata, record unresolved issues, and return the final paper-review contract."
    ),
}


@dataclass
class SessionWorkspace:
    root: Path
    thread: Any


def _source_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = WORKSPACE_ROOT / path
    if path.is_symlink():
        raise ValueError(f"symlinked path is not allowed: {path}")
    return path.resolve()


def _stage_relative(source: Path) -> Path:
    try:
        return source.relative_to(WORKSPACE_ROOT.resolve())
    except ValueError:
        digest = hashlib.sha256(str(source).encode("utf-8")).hexdigest()[:12]
        return Path("_external_sources") / digest / source.name


def _copy_into_stage(source: Path, target: Path) -> None:
    if source.is_symlink():
        raise ValueError(f"symlinked input is not allowed: {source}")
    if source.is_dir():
        nested_symlinks = [path for path in source.rglob("*") if path.is_symlink()]
        if nested_symlinks:
            raise ValueError(
                "symlinks inside allowed read directories are not allowed: "
                + ", ".join(str(path) for path in nested_symlinks[:10])
            )
        if target.exists() or target.is_symlink():
            if target.is_symlink():
                target.unlink()
            elif target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink()
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target, symlinks=False)
        return
    if source.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        return
    raise FileNotFoundError(f"allowed read path does not exist: {source}")


def _fingerprint(root: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            values[relative] = "symlink"
        elif path.is_dir():
            values[relative] = "directory"
        elif path.is_file():
            digest = hashlib.sha256()
            with path.open("rb") as file:
                for chunk in iter(lambda: file.read(1024 * 1024), b""):
                    digest.update(chunk)
            values[relative] = f"file:{digest.hexdigest()}"
        else:
            values[relative] = "special"
    return values


def _snapshot_path(path: Path) -> str | None:
    if not path.exists():
        return None
    if path.is_symlink():
        raise ValueError(f"symlinked output path is not allowed: {path}")
    if path.is_dir():
        return "directory:" + json.dumps(
            _fingerprint(path), sort_keys=True, separators=(",", ":")
        )
    if path.is_file():
        digest = hashlib.sha256()
        with path.open("rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                digest.update(chunk)
        return f"file:{digest.hexdigest()}"
    raise ValueError(f"unsupported output path type: {path}")


def _is_within(path: Path, allowed: Path) -> bool:
    return path == allowed or allowed in path.parents


def _is_discardable_python_cache(path: Path) -> bool:
    return "__pycache__" in path.parts and path.suffix in {".pyc", ".pyo"}


def _verify_changes(
    root: Path,
    before: dict[str, str],
    allowed_write_paths: tuple[Path, ...],
) -> None:
    after = _fingerprint(root)
    changed = {
        Path(name)
        for name in before.keys() | after.keys()
        if before.get(name) != after.get(name)
        and not ({before.get(name), after.get(name)} <= {None, "directory"})
    }
    illegal = sorted(
        path.as_posix()
        for path in changed
        if not _is_discardable_python_cache(path)
        if not any(_is_within(path, allowed) for allowed in allowed_write_paths)
    )
    if illegal:
        raise PermissionError(
            "agent modified paths outside write allowlist: " + ", ".join(illegal[:10])
        )
    symlinks = [path for path in root.rglob("*") if path.is_symlink()]
    if symlinks:
        raise PermissionError(
            "agent workspace contains forbidden symlinks: "
            + ", ".join(path.relative_to(root).as_posix() for path in symlinks[:10])
        )


def _atomic_copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(f".{target.name}.pipeline-tmp")
    shutil.copy2(source, temporary)
    temporary.replace(target)


def _sync_write_path(
    staged: Path,
    destination: Path,
    expected_destination_snapshot: str | None,
) -> None:
    if _snapshot_path(destination) != expected_destination_snapshot:
        raise RuntimeError(
            f"write destination changed while the agent was running: {destination}"
        )
    if not staged.exists():
        if destination.exists():
            raise RuntimeError(f"agent removed an existing write path: {destination}")
        return
    if staged.is_symlink():
        raise PermissionError(f"refusing to sync symlink: {staged}")
    if staged.is_file():
        _atomic_copy_file(staged, destination)
        return
    if staged.is_dir():
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary_root = Path(
            tempfile.mkdtemp(
                prefix=f".{destination.name}.pipeline-tmp-",
                dir=destination.parent,
            )
        )
        backup_root = Path(
            tempfile.mkdtemp(
                prefix=f".{destination.name}.pipeline-backup-",
                dir=destination.parent,
            )
        )
        replacement = temporary_root / "replacement"
        backup = backup_root / "previous"
        shutil.copytree(staged, replacement, symlinks=False)
        try:
            if destination.exists():
                destination.replace(backup)
            replacement.replace(destination)
        except Exception:
            if backup.exists() and not destination.exists():
                backup.replace(destination)
            raise
        finally:
            shutil.rmtree(temporary_root, ignore_errors=True)
            shutil.rmtree(backup_root, ignore_errors=True)
        return
    raise RuntimeError(f"unsupported staged output type: {staged}")


def _usage_dict(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if is_dataclass(value):
        return asdict(value)
    if hasattr(value, "__dict__"):
        return dict(value.__dict__)
    return {"value": str(value)}


def _retry_delay_seconds(error: Exception, attempt: int) -> float:
    message = str(error).lower()
    if "429" in message or "too many requests" in message:
        return min(300.0, 60.0 * (2**attempt))
    return min(30.0, 2.0 * (2**attempt))


def _is_transient_transport_error(error: Exception) -> bool:
    message = str(error).lower()
    return any(
        marker in message
        for marker in (
            "429",
            "502",
            "503",
            "504",
            "too many requests",
            "bad gateway",
            "service unavailable",
            "gateway timeout",
            "connection reset",
            "temporarily unavailable",
        )
    )


def _codex_binary() -> Path:
    configured = os.environ.get("ML_THEORY_CODEX_BIN")
    candidate = configured or shutil.which("codex")
    if not candidate:
        package = importlib.util.find_spec("codex_cli_bin")
        if package is not None and package.origin is not None:
            bundled = Path(package.origin).resolve().parent / "bin/codex"
            if bundled.is_file():
                candidate = str(bundled)
    if not candidate:
        raise RuntimeError(
            "Codex CLI was not found; install it or set ML_THEORY_CODEX_BIN"
        )
    path = Path(candidate).expanduser().resolve()
    if not path.is_file() or not os.access(path, os.X_OK):
        raise RuntimeError(f"Codex CLI is not executable: {path}")
    return path


def _utf8_subprocess_env() -> dict[str, str]:
    clean: dict[str, str] = {}
    for key, value in os.environ.items():
        try:
            key.encode("utf-8")
            value.encode("utf-8")
        except UnicodeEncodeError:
            continue
        clean[key] = value
    return clean


def _app_server_launch_args(
    codex_bin: Path, config_overrides: tuple[str, ...] = ()
) -> tuple[str, ...]:
    config_args = ["--config", "features.hooks=false"]
    for override in config_overrides:
        config_args.extend(["--config", override])
    quoted_config = " ".join(shlex.quote(value) for value in config_args)
    command = (
        f"{shlex.quote(str(codex_bin))} {quoted_config} app-server --listen stdio://"
    )
    # Keeping /bin/sh as the app-server parent avoids a current macOS runner
    # failure when the calling Python executable has a non-ASCII path.
    return ("/bin/sh", "-c", command)


def _permission_config(profile_config: str | None = None) -> str:
    python_runtime = Path(sys.base_prefix).resolve()
    codex_runtime = _codex_binary().parent
    profile = ""
    if profile_config is not None:
        profile = "\n" + profile_config.strip() + "\n"
    return (
        'default_permissions = "pipeline-isolated"\n'
        'web_search = "disabled"\n'
        f"{profile}\n"
        "[permissions.pipeline-isolated.filesystem]\n"
        '":minimal" = "read"\n'
        f'{json.dumps(str(python_runtime))} = "read"\n'
        f'{json.dumps(str(codex_runtime))} = "read"\n'
        '":workspace_roots" = { "." = "write" }\n'
        "\n"
        "[permissions.pipeline-isolated.network]\n"
        "enabled = false\n"
        "\n"
        "[shell_environment_policy]\n"
        'inherit = "core"\n'
    )


def _private_file(path: Path, label: str) -> Path:
    if path.is_symlink():
        raise ValueError(f"{label} must not be a symlink: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"{label} not found: {path}")
    if path.stat().st_mode & 0o077:
        raise PermissionError(f"{label} must have mode 600: {path}")
    return path


def _load_api_profile(profile_dir: Path) -> tuple[str, str]:
    profile_source = profile_dir.expanduser()
    if profile_source.is_symlink():
        raise ValueError(
            f"Codex API profile directory must not be a symlink: {profile_source}"
        )
    profile = profile_source.resolve()
    if not profile.is_dir():
        raise ValueError(f"invalid Codex API profile directory: {profile}")
    if profile.stat().st_mode & 0o077:
        raise PermissionError(
            f"Codex API profile directory must have mode 700: {profile}"
        )
    profile_config = _private_file(profile / "config.toml", "Codex API profile config")
    key_file = _private_file(profile / "openai_api_key", "Codex API key file")
    api_key = key_file.read_text(encoding="utf-8").strip()
    if not api_key or "\n" in api_key or "\r" in api_key:
        raise ValueError("Codex API key file must contain exactly one non-empty line")
    return profile_config.read_text(encoding="utf-8"), api_key


def _new_adapter_root(prefix: str) -> Path:
    session_root = LOCAL_RUNTIME_DIR / "agent-sessions"
    session_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    session_root.chmod(0o700)
    return Path(tempfile.mkdtemp(prefix=prefix, dir=session_root))


class CodexAPIAdapter:
    """Translate AgentRequest objects into isolated Codex SDK threads."""

    def __init__(self, profile_dir: Path | None = None) -> None:
        reasoning_effort = os.environ.get("ML_THEORY_CODEX_REASONING_EFFORT")
        if reasoning_effort not in {
            None,
            "none",
            "low",
            "medium",
            "high",
            "xhigh",
            "max",
        }:
            raise ValueError(
                "ML_THEORY_CODEX_REASONING_EFFORT must be one of "
                "none, low, medium, high, xhigh, max"
            )
        self._config_overrides = (
            ()
            if reasoning_effort is None
            else (f'model_reasoning_effort="{reasoning_effort}"',)
        )
        loaded_profile = (
            _load_api_profile(profile_dir) if profile_dir is not None else None
        )
        self._codex: AsyncCodex | None = None
        self._sessions: dict[str, SessionWorkspace] = {}
        self._temporary_root = _new_adapter_root("ml-theory-codex-")
        self._codex_bin = _codex_binary()
        self._codex_home = self._temporary_root / "codex_home"
        self._codex_home.mkdir()
        self._client_env = {
            "CODEX_HOME": str(self._codex_home),
            "PYTHONDONTWRITEBYTECODE": "1",
        }

        if profile_dir is None:
            config_text = _permission_config()
            source_home = Path(
                os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))
            ).expanduser()
            source_auth = source_home / "auth.json"
            if source_auth.is_file():
                shutil.copy2(source_auth, self._codex_home / "auth.json")
        else:
            assert loaded_profile is not None
            profile_config, api_key = loaded_profile
            config_text = _permission_config(profile_config)
            self._client_env["OPENAI_API_KEY"] = api_key

        (self._codex_home / "config.toml").write_text(
            config_text,
            encoding="utf-8",
        )
        self._model = os.environ.get("ML_THEORY_CODEX_MODEL") or None

    async def _client(self) -> AsyncCodex:
        if self._codex is None:
            self._codex = AsyncCodex(
                CodexConfig(
                    cwd=str(self._temporary_root),
                    env=self._client_env,
                    launch_args_override=_app_server_launch_args(
                        self._codex_bin, self._config_overrides
                    ),
                )
            )
            await self._codex.__aenter__()
        return self._codex

    def _new_workspace(self) -> Path:
        return Path(tempfile.mkdtemp(prefix="thread-", dir=self._temporary_root))

    def _hydrate(
        self,
        root: Path,
        read_paths: tuple[str, ...],
        write_paths: tuple[str, ...],
    ) -> tuple[
        dict[str, str],
        tuple[Path, ...],
        list[tuple[Path, Path, str | None]],
    ]:
        path_map: dict[str, str] = {}
        for value in read_paths:
            source = _source_path(value)
            staged_relative = _stage_relative(source)
            _copy_into_stage(source, root / staged_relative)
            path_map[value] = staged_relative.as_posix()

        staged_writes: list[Path] = []
        sync_pairs: list[tuple[Path, Path, str | None]] = []
        for value in write_paths:
            destination = _source_path(value)
            try:
                staged_relative = destination.relative_to(WORKSPACE_ROOT.resolve())
            except ValueError as error:
                raise PermissionError(
                    f"write path must be inside the repository workspace: {value}"
                ) from error
            staged_writes.append(staged_relative)
            sync_pairs.append(
                (root / staged_relative, destination, _snapshot_path(destination))
            )
            path_map[value] = staged_relative.as_posix()
        return path_map, tuple(staged_writes), sync_pairs

    def _instructions(self, request: Any) -> str:
        sections: list[str] = []
        for value in request.instructions_files:
            path = _source_path(value)
            if not path.is_file():
                raise FileNotFoundError(f"instruction file not found: {path}")
            sections.append(
                f"## Instructions from {value}\n\n{path.read_text(encoding='utf-8')}"
            )
        return "\n\n".join(sections)

    def _base_instructions(self, request: Any) -> str:
        agents_path = WORKSPACE_ROOT / "AGENTS.md"
        repository_rules = (
            agents_path.read_text(encoding="utf-8") if agents_path.is_file() else ""
        )
        return (
            f"You are the isolated {request.role} for the ML-theory data-construction "
            "pipeline. Follow the repository rules below. You have no conversation "
            "history other than turns created for this pipeline thread.\n\n"
            f"{repository_rules}"
        )

    def _prompt(
        self,
        request: Any,
        path_map: dict[str, str],
        contract_name: str,
        retry_reason: str | None = None,
    ) -> str:
        task = PHASE_TASKS.get(request.phase)
        if task is None:
            raise ValueError(f"unknown agent phase: {request.phase}")
        readable = [path_map[value] for value in request.read_paths]
        writable = [path_map[value] for value in request.write_paths]
        retry = ""
        if retry_reason:
            retry = (
                "\n\nThis is a bounded recovery turn. Do not repeat destructive setup. "
                "Inspect the files already present, finish missing work if needed, and "
                f"correct the final response. Previous problem: {retry_reason}"
            )
        if request.context.get("inline_no_tools"):
            workspace_section = (
                "# Execution boundary\n\n"
                "All task data is included inline below. Do not call tools, inspect the "
                "filesystem, or access the network. Return the structured response "
                "directly.\n\n"
            )
            final_instruction = (
                f"Return only one JSON object satisfying the `{contract_name}` schema. "
                "Do not wrap it in a Markdown fence."
            )
        else:
            workspace_section = (
                "# Isolated workspace\n\n"
                "The current working directory is an isolated staging workspace. Original "
                "paths have been copied to the mapped paths below. Read only the declared "
                "read paths. Modify only the declared write paths. Do not use network access.\n\n"
                f"Read paths:\n{json.dumps(readable, ensure_ascii=False, indent=2)}\n\n"
                f"Write paths:\n{json.dumps(writable, ensure_ascii=False, indent=2)}\n\n"
                "Original-to-staged path map:\n"
                f"{json.dumps(path_map, ensure_ascii=False, indent=2)}\n\n"
            )
            final_instruction = (
                f"Return only one JSON object satisfying the `{contract_name}` schema. "
                "Do not wrap it in a Markdown fence. File edits must be complete before "
                "returning the object."
            )
        return (
            "# Assignment\n\n"
            f"Role: `{request.role}`\n\n"
            f"Phase: `{request.phase}`\n\n"
            f"Paper ID: `{request.paper_id}`\n\n"
            f"Theorem ID: `{request.theorem_id or 'not_applicable'}`\n\n"
            f"# Task\n\n{task}{retry}\n\n"
            f"# Role references\n\n{self._instructions(request)}\n\n"
            f"{workspace_section}"
            f"# Request context\n\n{json.dumps(request.context, ensure_ascii=False, indent=2)}\n\n"
            "# Final response\n\n"
            f"{final_instruction}"
        )

    async def _run_turn(
        self,
        thread: Any,
        prompt: str,
        contract_name: str,
        timeout_seconds: int,
    ) -> Any:
        handle = await thread.turn(
            prompt,
            cwd=str(self._sessions[thread.id].root),
            model=self._model,
            output_schema=schema_for(contract_name),
        )
        try:
            return await asyncio.wait_for(handle.run(), timeout=timeout_seconds)
        except TimeoutError:
            try:
                await handle.interrupt()
            except Exception:
                pass
            raise TimeoutError(
                f"Codex turn exceeded {timeout_seconds} seconds"
            ) from None

    async def run(self, request: Any) -> dict[str, Any]:
        contract_name = str(request.context.get("output_contract", ""))
        schema_for(contract_name)
        client = await self._client()

        if request.resume_session_id:
            session = self._sessions.get(request.resume_session_id)
            if session is None:
                raise RuntimeError(
                    "cannot resume an unknown pipeline thread: "
                    f"{request.resume_session_id}"
                )
        else:
            root = self._new_workspace()
            thread = await client.thread_start(
                approval_mode=ApprovalMode.auto_review,
                base_instructions=self._base_instructions(request),
                cwd=str(root),
                ephemeral=True,
                model=self._model,
            )
            if not thread.id:
                raise RuntimeError("Codex SDK created a thread without an ID")
            session = SessionWorkspace(root=root, thread=thread)
            self._sessions[thread.id] = session

        path_map, staged_writes, sync_pairs = self._hydrate(
            session.root, request.read_paths, request.write_paths
        )
        before = _fingerprint(session.root)
        retry_reason: str | None = None
        last_error: Exception | None = None

        transport_retry_limit = int(
            os.environ.get("ML_THEORY_TRANSPORT_RETRIES", "4")
        )
        semantic_attempt = 0
        transport_attempt = 0
        total_attempts = 0
        while True:
            total_attempts += 1
            prompt = self._prompt(
                request,
                path_map,
                contract_name,
                retry_reason=retry_reason,
            )
            try:
                result = await self._run_turn(
                    session.thread,
                    prompt,
                    contract_name,
                    request.timeout_seconds,
                )
                status = getattr(result.status, "value", str(result.status))
                if status != "completed":
                    raise RuntimeError(
                        f"Codex turn {result.id} ended with status {status}: {result.error}"
                    )
                payload = parse_and_validate(contract_name, result.final_response)
                _verify_changes(session.root, before, staged_writes)
                for staged, destination, destination_snapshot in sync_pairs:
                    _sync_write_path(staged, destination, destination_snapshot)
                return {
                    "status": payload["status"],
                    "payload": payload,
                    "session_id": session.thread.id,
                    "turn_id": result.id,
                    "usage": _usage_dict(result.usage),
                    "attempts": total_attempts,
                }
            except Exception as error:
                last_error = error
                if _is_transient_transport_error(error):
                    if transport_attempt >= transport_retry_limit:
                        break
                    await asyncio.sleep(
                        _retry_delay_seconds(error, transport_attempt)
                    )
                    transport_attempt += 1
                    continue
                retryable = isinstance(
                    error, (TimeoutError, ValueError)
                ) or is_retryable_error(error)
                if semantic_attempt >= request.max_retries or not retryable:
                    break
                retry_reason = str(error)
                await asyncio.sleep(
                    _retry_delay_seconds(error, semantic_attempt)
                )
                semantic_attempt += 1

        assert last_error is not None
        raise RuntimeError(
            f"Codex phase {request.phase} failed after "
            f"{total_attempts} attempt(s): {last_error}"
        ) from last_error

    async def aclose(self) -> None:
        if self._codex is not None:
            await self._codex.close()
            self._codex = None
        shutil.rmtree(self._temporary_root, ignore_errors=True)


class CodexCLIAdapter:
    """Run the same isolated contract through `codex exec` and HTTPS fallback."""

    def __init__(self, profile_dir: Path | None = None) -> None:
        reasoning_effort = os.environ.get("ML_THEORY_CODEX_REASONING_EFFORT")
        if reasoning_effort not in {
            None,
            "none",
            "low",
            "medium",
            "high",
            "xhigh",
            "max",
        }:
            raise ValueError(
                "ML_THEORY_CODEX_REASONING_EFFORT must be one of "
                "none, low, medium, high, xhigh, max"
            )
        self._config_overrides = (
            ()
            if reasoning_effort is None
            else (f'model_reasoning_effort="{reasoning_effort}"',)
        )
        loaded_profile = (
            _load_api_profile(profile_dir) if profile_dir is not None else None
        )
        self._temporary_root = _new_adapter_root("ml-theory-codex-cli-")
        self._codex_home = self._temporary_root / "codex_home"
        self._codex_home.mkdir()
        self._codex_bin = _codex_binary()
        self._sessions: dict[str, Path] = {}
        diagnostics = os.environ.get("ML_THEORY_CODEX_DIAGNOSTICS_DIR")
        self._diagnostics_dir = (
            Path(diagnostics).expanduser().resolve() if diagnostics else None
        )
        if self._diagnostics_dir is not None:
            self._diagnostics_dir.mkdir(parents=True, exist_ok=True)
        self._client_env = {
            **_utf8_subprocess_env(),
            "CODEX_HOME": str(self._codex_home),
            "PYTHONDONTWRITEBYTECODE": "1",
        }
        if profile_dir is None:
            config_text = _permission_config()
            source_home = Path(
                os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))
            ).expanduser()
            source_auth = source_home / "auth.json"
            if source_auth.is_file():
                shutil.copy2(source_auth, self._codex_home / "auth.json")
        else:
            assert loaded_profile is not None
            profile_config, api_key = loaded_profile
            config_text = _permission_config(profile_config)
            self._client_env["OPENAI_API_KEY"] = api_key
        (self._codex_home / "config.toml").write_text(
            config_text,
            encoding="utf-8",
        )
        self._model = os.environ.get("ML_THEORY_CODEX_MODEL") or None

    def _new_workspace(self) -> Path:
        return Path(tempfile.mkdtemp(prefix="thread-", dir=self._temporary_root))

    @staticmethod
    def _event_session_id(events: list[dict[str, Any]]) -> str | None:
        for event in events:
            for key in ("thread_id", "session_id"):
                value = event.get(key)
                if isinstance(value, str) and value:
                    return value
            thread = event.get("thread")
            if isinstance(thread, dict):
                value = thread.get("id")
                if isinstance(value, str) and value:
                    return value
        return None

    @staticmethod
    def _event_usage(events: list[dict[str, Any]]) -> dict[str, Any] | None:
        for event in reversed(events):
            usage = event.get("usage")
            if isinstance(usage, dict):
                return usage
        return None

    def _redact_diagnostics(self, text: str) -> str:
        api_key = self._client_env.get("OPENAI_API_KEY")
        if api_key:
            text = text.replace(api_key, "[REDACTED_API_KEY]")
        return text

    def _write_diagnostics(
        self,
        call_id: str,
        request: Any,
        command: list[str],
        stdout: bytes,
        stderr: bytes,
    ) -> None:
        if self._diagnostics_dir is None:
            return
        prefix = self._diagnostics_dir / f"{request.phase}_{call_id}"
        metadata = {
            "paper_id": request.paper_id,
            "phase": request.phase,
            "resume_session_id": request.resume_session_id,
            "command": command,
        }
        prefix.with_suffix(".metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        prefix.with_suffix(".stdout.jsonl").write_text(
            self._redact_diagnostics(stdout.decode("utf-8", errors="replace")),
            encoding="utf-8",
        )
        prefix.with_suffix(".stderr.log").write_text(
            self._redact_diagnostics(stderr.decode("utf-8", errors="replace")),
            encoding="utf-8",
        )

    async def _run_cli(
        self,
        request: Any,
        root: Path,
        prompt: str,
        contract_name: str,
    ) -> tuple[dict[str, Any], str, str | None, dict[str, Any] | None]:
        call_root = self._temporary_root / "cli_calls"
        call_root.mkdir(exist_ok=True)
        call_id = hashlib.sha256(
            f"{request.paper_id}:{request.phase}:{os.urandom(8).hex()}".encode()
        ).hexdigest()[:16]
        schema_path = call_root / f"{call_id}.schema.json"
        output_path = call_root / f"{call_id}.response.json"
        schema_path.write_text(
            json.dumps(schema_for(contract_name), ensure_ascii=False),
            encoding="utf-8",
        )

        config_args = ["--config", "features.hooks=false"]
        for override in self._config_overrides:
            config_args.extend(["--config", override])
        common = [
            "--skip-git-repo-check",
            "--ignore-rules",
            "--json",
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
        ]
        if self._model:
            common.extend(["--model", self._model])
        if request.resume_session_id:
            command = [
                str(self._codex_bin),
                *config_args,
                "exec",
                "resume",
                *common,
                request.resume_session_id,
                "-",
            ]
        else:
            command = [
                str(self._codex_bin),
                *config_args,
                "exec",
                *common,
                "--cd",
                str(root),
                "-",
            ]

        process = await asyncio.create_subprocess_exec(
            *command,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(root),
            env=self._client_env,
        )
        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(prompt.encode("utf-8")),
                timeout=request.timeout_seconds,
            )
        except TimeoutError:
            process.terminate()
            stdout, stderr = await process.communicate()
            self._write_diagnostics(call_id, request, command, stdout, stderr)
            raise TimeoutError(
                f"Codex CLI turn exceeded {request.timeout_seconds} seconds"
            ) from None
        self._write_diagnostics(call_id, request, command, stdout, stderr)
        if process.returncode != 0:
            error_text = stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(
                f"Codex CLI exited {process.returncode}: {error_text[-12000:]}"
            )
        if not output_path.is_file():
            raise RuntimeError("Codex CLI did not write its final response")
        payload = parse_and_validate(
            contract_name,
            output_path.read_text(encoding="utf-8"),
        )
        events: list[dict[str, Any]] = []
        for line in stdout.decode("utf-8", errors="replace").splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(event, dict):
                events.append(event)
        session_id = request.resume_session_id or self._event_session_id(events)
        if not session_id:
            raise RuntimeError("Codex CLI returned no thread ID")
        turn_id = next(
            (
                str(event["id"])
                for event in reversed(events)
                if isinstance(event.get("id"), str)
                and "turn" in str(event.get("type", ""))
            ),
            None,
        )
        return payload, session_id, turn_id, self._event_usage(events)

    async def run(self, request: Any) -> dict[str, Any]:
        contract_name = str(request.context.get("output_contract", ""))
        schema_for(contract_name)
        if request.resume_session_id:
            root = self._sessions.get(request.resume_session_id)
            if root is None:
                raise RuntimeError(
                    "cannot resume an unknown CLI pipeline thread: "
                    f"{request.resume_session_id}"
                )
        else:
            root = self._new_workspace()

        staging = CodexAPIAdapter.__new__(CodexAPIAdapter)
        path_map, staged_writes, sync_pairs = CodexAPIAdapter._hydrate(
            staging,
            root,
            request.read_paths,
            request.write_paths,
        )
        before = _fingerprint(root)
        prompt = CodexAPIAdapter._prompt(
            staging,
            request,
            path_map,
            contract_name,
        )
        if not request.resume_session_id:
            prompt = (
                CodexAPIAdapter._base_instructions(staging, request) + "\n\n" + prompt
            )

        last_error: Exception | None = None
        for attempt in range(request.max_retries + 1):
            try:
                payload, session_id, turn_id, usage = await self._run_cli(
                    request,
                    root,
                    prompt,
                    contract_name,
                )
                _verify_changes(root, before, staged_writes)
                for staged, destination, destination_snapshot in sync_pairs:
                    _sync_write_path(staged, destination, destination_snapshot)
                self._sessions[session_id] = root
                return {
                    "status": payload["status"],
                    "payload": payload,
                    "session_id": session_id,
                    "turn_id": turn_id,
                    "usage": usage,
                    "attempts": attempt + 1,
                }
            except Exception as error:
                last_error = error
                if attempt >= request.max_retries:
                    break
                await asyncio.sleep(_retry_delay_seconds(error, attempt))
        assert last_error is not None
        raise RuntimeError(
            f"Codex CLI phase {request.phase} failed after "
            f"{request.max_retries + 1} attempt(s): {last_error}"
        ) from last_error

    async def aclose(self) -> None:
        shutil.rmtree(self._temporary_root, ignore_errors=True)


def create_adapter() -> CodexAPIAdapter:
    return CodexAPIAdapter()


def create_cli_adapter() -> CodexCLIAdapter:
    return CodexCLIAdapter()


def create_get_codex_adapter() -> CodexAPIAdapter:
    """Create the isolated adapter backed by the ignored local API profile."""

    configured = os.environ.get("ML_THEORY_CODEX_PROFILE_DIR")
    profile_dir = (
        Path(configured).expanduser() if configured else LOCAL_RUNTIME_DIR / "get-codex"
    )
    return CodexAPIAdapter(profile_dir=profile_dir)


def create_get_codex_cli_adapter() -> CodexCLIAdapter:
    configured = os.environ.get("ML_THEORY_CODEX_PROFILE_DIR")
    profile_dir = (
        Path(configured).expanduser() if configured else LOCAL_RUNTIME_DIR / "get-codex"
    )
    return CodexCLIAdapter(profile_dir=profile_dir)
