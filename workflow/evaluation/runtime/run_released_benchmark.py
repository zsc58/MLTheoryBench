#!/usr/bin/env python3
"""Run frozen released tasks with the existing Solver and joint judging contracts."""
from __future__ import annotations

import argparse
import concurrent.futures
import json
from pathlib import Path
import re
import shutil
import time

from agent_call import AgentConfig
from bare_model import ProviderConfig, public_config
from model_profiles import DEFAULT_PROFILES_DIR, load_suite, solver_profiles
from paired_pipeline import (
    ArtifactBundle, SolverSpec, anonymous_assignment, run_all_solvers,
    run_paired_reviewer, run_paired_evaluator,
)
from run_comparison import build_summary, recover_recorded_usage, solver_spec
from support import atomic_write_json, merged_environment, sha256_file


DATA_ROOT = Path(__file__).resolve().parents[3] / 'data'
FILES = {'task_file': ('task.md', 'tasks'),
         'proof_ground_truth_file': ('proof_ground_truth.md', 'references'),
         'rubric_file': ('rubric.md', 'references')}


def validate_dataset(root: Path) -> dict[str, dict]:
    root = root.resolve()
    manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    tasks = manifest['tasks']
    if manifest['name'] != 'MLTheoryBench' or manifest['task_count'] != len(tasks):
        raise ValueError('invalid dataset manifest')
    selected = {}
    for item in tasks:
        paper_id = item['paper_id']
        if not re.fullmatch(r'paper_2026_\d+', paper_id) or paper_id in selected:
            raise ValueError('invalid or duplicate paper ID')
        if item['prc'] not in {f'PRC{i}' for i in range(5)}:
            raise ValueError('invalid PRC label')
        for field, (name, directory) in FILES.items():
            expected = f'{directory}/{paper_id}/{name}'
            if item[field] != expected:
                raise ValueError('unexpected artifact path')
            path = root / expected
            if path.is_symlink() or not path.resolve().is_relative_to(root):
                raise ValueError('artifact escapes dataset')
            if not path.is_file() or sha256_file(path) != item['sha256'][name]:
                raise ValueError(f'changed or missing artifact: {paper_id}/{name}')
        selected[paper_id] = item
    return selected


def copy_bundle(root: Path, item: dict, destination: Path) -> ArtifactBundle:
    destination.mkdir(parents=True, exist_ok=False)
    for field, (name, _) in FILES.items():
        source = root / item[field]
        if sha256_file(source) != item['sha256'][name]:
            raise ValueError(f'changed dataset file: {source.name}')
        shutil.copyfile(source, destination / name)
        if sha256_file(destination / name) != item['sha256'][name]:
            raise ValueError('artifact copy mismatch')
    # The evaluator accepts provenance, but raw source mappings are not released.
    atomic_write_json(destination / 'provenance.json', {
        'dataset': 'MLTheoryBench', 'paper_id': item['paper_id'],
        'reference_basis': 'released_task_ground_truth_and_rubric',
    })
    return ArtifactBundle(revision=0, root=destination)


def run_task(root: Path, item: dict, output: Path, run_id: str,
             specs: list[SolverSpec], judge: AgentConfig) -> dict:
    started = time.monotonic()
    output.mkdir(parents=True, exist_ok=False)
    state = {'paper_id': item['paper_id'], 'prc': item['prc'], 'status': 'running',
             'stop_reason': None, 'scores': {}, 'formal_feedback_enabled': False,
             'source_sha256': item['sha256']}
    try:
        bundle = copy_bundle(root, item, output / 'artifacts')
        round_dir = output / 'rounds/round_0'
        round_dir.mkdir(parents=True)
        results = run_all_solvers(specs, bundle, round_dir, frozen_task=True)
        active = [s.label for s in specs if results[s.label]['solver_outcome'] != 'no_final_answer']
        assignment = anonymous_assignment(item['paper_id'], run_id, 0, active)
        atomic_write_json(round_dir / 'anonymous_assignment.json', assignment)
        scores = {s.label: 0 for s in specs if s.label not in active}
        if assignment:
            reviews, _ = run_paired_reviewer(bundle, assignment, results, round_dir, judge)
            evaluations, _ = run_paired_evaluator(bundle, assignment, results, reviews, round_dir, judge)
            unscorable = [assignment[k] for k, v in evaluations.items()
                          if v['evaluation_status'] == 'unscorable']
            if unscorable:
                state.update(status='stopped', stop_reason='evaluator_unscorable',
                             unscorable_models=unscorable)
            else:
                scores.update({assignment[k]: v['score'] for k, v in evaluations.items()})
        for _, (name, _) in FILES.items():
            if sha256_file(bundle.root / name) != item['sha256'][name]:
                raise ValueError('frozen artifact changed during evaluation')
        if state['status'] != 'stopped':
            state.update(status='completed', scores=scores)
    except Exception as error:
        state.update(status='failed', scores={}, error=f'{type(error).__name__}: {error}')
    state.update(recover_recorded_usage(output))
    state['wall_time_seconds'] = time.monotonic() - started
    atomic_write_json(output / 'result.json', state)
    return state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-root', type=Path, default=DATA_ROOT)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--paper-id', action='append', default=[])
    selection.add_argument('--all', action='store_true')
    models = parser.add_mutually_exclusive_group()
    models.add_argument('--mode', choices=['test', 'formal'])
    models.add_argument('--solver', type=solver_spec, action='append')
    parser.add_argument('--profiles-dir', type=Path, default=DEFAULT_PROFILES_DIR)
    parser.add_argument('--judge-api-profile', type=Path)
    parser.add_argument('--judge-model', default=load_suite()['agent']['model'])
    parser.add_argument('--judge-reasoning-effort', default='high')
    parser.add_argument('--judge-timeout-seconds', type=int, default=3600)
    parser.add_argument('--codex-bin', default='codex')
    parser.add_argument('--run-id')
    parser.add_argument('--run-root', type=Path)
    parser.add_argument('--paper-workers', type=int, default=1)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if args.paper_workers < 1:
        parser.error('paper-workers must be positive')
    if not args.dry_run and (not args.run_root or not args.run_id):
        parser.error('run-root and run-id are required unless dry-run')
    return args


def main() -> int:
    args = parse_args()
    root = args.data_root.resolve()
    tasks = validate_dataset(root)
    paper_ids = list(tasks) if args.all else args.paper_id
    if len(set(paper_ids)) != len(paper_ids) or set(paper_ids) - tasks.keys():
        raise ValueError('duplicate or unknown requested task')
    if args.dry_run:
        print(json.dumps({'validated_tasks': len(tasks), 'selected_tasks': paper_ids,
                          'solver_exposure': ['task.md', 'frozen_solver_instructions'],
                          'model_requests': 0}, indent=2))
        return 0
    output = args.run_root.resolve()
    if output == root or output.is_relative_to(root) or root.is_relative_to(output):
        raise ValueError('output must be disjoint from the dataset')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.run_id):
        raise ValueError('invalid run ID')
    profiles = args.solver or solver_profiles(args.mode or 'test', args.profiles_dir.resolve())
    if not profiles or len(profiles) > 8 or len({p[0] for p in profiles}) != len(profiles):
        raise ValueError('choose one to eight uniquely labeled solvers')
    specs = []
    for label, profile in profiles:
        profile = profile.resolve()
        config = ProviderConfig.from_environment(merged_environment(profile), base_dir=profile.parent)
        specs.append(SolverSpec(label, config))
    judge = AgentConfig((args.judge_api_profile or args.profiles_dir / 'get-api').resolve(),
                        args.codex_bin, args.judge_model, args.judge_reasoning_effort,
                        args.judge_timeout_seconds)
    output.mkdir(parents=True, exist_ok=False)
    record = {'name': 'MLTheoryBench', 'run_id': args.run_id, 'status': 'running',
              'protocol': 'released_frozen_tasks_joint_judging', 'paper_ids': paper_ids,
              'formal_feedback_enabled': False,
              'solvers': {s.label: public_config(s.config) for s in specs},
              'judge': {'model': judge.model, 'reasoning_effort': judge.reasoning_effort}}
    atomic_write_json(output / 'run.json', record)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.paper_workers) as executor:
        futures = [executor.submit(run_task, root, tasks[pid], output / 'papers' / pid,
                                   args.run_id, specs, judge) for pid in paper_ids]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            build_summary(output, results)
            print(json.dumps({'paper_id': result['paper_id'], 'status': result['status'],
                              'finished': len(results)}), flush=True)
    failed = any(r['status'] == 'failed' for r in results)
    record['status'] = 'completed_with_failures' if failed else 'completed'
    atomic_write_json(output / 'run.json', record)
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
