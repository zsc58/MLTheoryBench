"""Rejudge frozen submissions using the production judging functions unchanged."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import concurrent.futures
from dataclasses import dataclass, field
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib
import json
import os
from pathlib import Path
import random
import re
import shutil
import statistics
import sys
import threading
import time

MODELS = {'deepseek': 'deepseek-flash', 'qwen': 'qwen3.8-reasoner'}
CORE = ('gpt6', 'gpt56', 'kimi_k3', 'claude_fable', 'qwen38_max', 'deepseek_pro')
ALL_MODELS = (*CORE, 'glm53')
ARTIFACTS = ('task.md', 'proof_ground_truth.md', 'rubric.md', 'provenance.json')
LOCAL = threading.local()


def now():
    return datetime.now(timezone.utc).isoformat()


def load(path):
    return json.loads(path.read_text())


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def emit(**value):
    print(json.dumps({'time': now(), **value}, ensure_ascii=False), flush=True)


def stratified_sample(eligible, seed=20261103):
    rng = random.Random(seed)
    chosen = {}
    for level in range(5):
        key = f'PRC{level}'
        population = sorted(eligible[key])
        count = 6 if level == 4 else 10
        if len(population) < count:
            raise ValueError(f'{key}: only {len(population)} eligible papers for {count} slots')
        chosen[key] = sorted(rng.sample(population, count))
    return chosen


def prepare(root, base):
    manifest = root / 'selection.json'
    if manifest.exists():
        return load(manifest)
    index = load(base / 'experiments/main/index.json')
    eligible = defaultdict(list)
    by_id = {}
    for row in index:
        if not row['completed_task']:
            continue
        pid = row['paper_id']
        directory = Path(row['directory'])
        model_rows = {m: load(directory / 'models' / m / 'solver_result.json') for m in CORE}
        if not all(v.get('solver_outcome') == 'final_answer' for v in model_rows.values()):
            continue
        prc = load(base / 'data/source_and_construction/papers' / pid /
                   'formalization/proof_reconstruction_complexity.json')['proof_reconstruction_complexity_level']
        eligible[prc].append(pid)
        by_id[pid] = row
    sample = stratified_sample(eligible)
    root.mkdir(parents=True, exist_ok=True)
    os.chmod(root, 0o700)
    frozen = root / 'frozen_framework'
    original_framework = base / 'framework/revised_workflow'
    shutil.copytree(original_framework, frozen, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns('__pycache__', '.runtime', '.venv', '*.pyc'))
    hashes = {}
    for file in frozen.rglob('*'):
        if file.is_file():
            relative = file.relative_to(frozen)
            assert digest(file) == digest(original_framework / relative)
            hashes[str(relative)] = digest(file)
    save(root / 'framework_hashes.json', hashes)
    papers = []
    for prc, ids in sample.items():
        for pid in ids:
            row = by_id[pid]
            source = Path(row['directory'])
            dest = root / 'inputs' / pid
            frozen_artifacts = load(source / 'frozen_artifacts.json')
            revision = source / 'task_versions' / f"revision_{frozen_artifacts['task_revision']}"
            (dest / 'artifacts').mkdir(parents=True, exist_ok=True)
            files = {}
            for name in ARTIFACTS:
                assert digest(revision / name) == frozen_artifacts['sha256'][name]
                shutil.copy2(revision / name, dest / 'artifacts' / name)
                files['artifacts/' + name] = digest(dest / 'artifacts' / name)
            assignment = load(source / 'rounds/round_0/anonymous_assignment.json')
            assert set(assignment.values()) == set(CORE), (pid, assignment)
            outcomes = {}
            for model in ALL_MODELS:
                src = source / 'models' / model
                record = load(src / 'solver_result.json') if (src / 'solver_result.json').exists() else {}
                outcome = record.get('solver_outcome', 'missing')
                outcomes[model] = outcome
                if outcome not in {'final_answer', 'no_final_answer'}:
                    raise ValueError(f'{pid}/{model}: unresolved solver outcome {outcome}; not zero-imputed')
                dst = dest / 'answers' / model
                dst.mkdir(parents=True, exist_ok=True)
                for name in ('solver_result.json', 'answer_for_evaluator.md', 'evaluation.json'):
                    if (src / name).exists():
                        shutil.copy2(src / name, dst / name)
                        files[f'answers/{model}/{name}'] = digest(dst / name)
                if outcome == 'final_answer':
                    assert (dst / 'answer_for_evaluator.md').read_text().strip(), (pid, model)
                    assert digest(dst / 'answer_for_evaluator.md') == record['proof_sha256'], (pid, model)
            if outcomes['glm53'] == 'final_answer':
                unused = next(f'answer_{c}' for c in 'abcdefgh' if f'answer_{c}' not in assignment)
                assignment[unused] = 'glm53'
            entry = {'paper_id': pid, 'prc': prc, 'source_directory': str(source),
                     'revision': frozen_artifacts['task_revision'], 'assignment': assignment,
                     'solver_outcomes': outcomes, 'baseline_scores': row['combined_scores'],
                     'input_sha256': files}
            save(dest / 'manifest.json', entry)
            papers.append(entry)
    result = {'created_at': now(), 'seed': 20261103, 'eligible_by_prc': {k: len(v) for k, v in eligible.items()},
              'sample_by_prc': sample, 'judges': MODELS, 'papers': papers,
              'selection_rule': 'All six non-GLM solvers submitted answers; sample without using scores.',
              'baseline_grouping': 'Six-model joint production judging; GLM was judged separately.',
              'new_grouping': 'Joint anonymous judging of all existing answers, including GLM when present.',
              'zero_rule': 'Only recorded no_final_answer solver outcomes receive automatic zero.'}
    save(manifest, result)
    emit(event='prepared', counts={k: len(v) for k, v in sample.items()})
    return result


@dataclass
class ChatThread:
    root: Path
    config: object
    messages: list = field(default_factory=list)
    turn_count: int = 0

    def close(self):
        pass


def parse_json(text):
    text = text.strip()
    if text.startswith('```') and text.endswith('```'):
        lines = text.splitlines()
        text = '\n'.join(lines[1:-1])
    value = json.loads(text)
    if not isinstance(value, dict):
        raise ValueError('Judge must return a JSON object')
    return value


def reduced_output_budget(error, current):
    message = str(error)
    if 'HTTP 400' not in message:
        return None
    limit = re.search(r'at most (\d+) combined input and output tokens', message)
    used = re.search(r'request has (\d+) input tokens', message)
    if not limit or not used:
        return None
    available = int(limit.group(1)) - int(used.group(1)) - 1024
    return available if 4096 <= available < current else None


def install_transport(root, credential_file, max_tokens, response_format):
    runtime = root / 'frozen_framework/runtime'
    sys.path.insert(0, str(runtime))
    pipeline = importlib.import_module('paired_pipeline')
    bare = importlib.import_module('bare_model')
    support = importlib.import_module('support')
    credentials = dict(line.split('=', 1) for line in credential_file.read_text().splitlines() if '=' in line)
    key = credentials['API_KEY']
    if credential_file.stat().st_mode & 0o077:
        raise PermissionError('Credential file must have mode 600')
    original_reader = bare._read_chat_completions_stream

    def tracked_reader(response):
        start = time.monotonic()
        last_write = 0.0
        events = size = 0

        def tracked_lines():
            nonlocal last_write, events, size
            for line in response:
                events += 1
                size += len(line)
                elapsed = time.monotonic() - start
                if elapsed > 10800:
                    raise RuntimeError('Judge stream exceeded three-hour safety limit')
                if elapsed - last_write >= 5:
                    save(LOCAL.call_dir / 'stream_progress.json', {
                        'updated_at': now(), 'elapsed_seconds': elapsed,
                        'lines_received': events, 'bytes_received': size})
                    last_write = elapsed
                yield line
        return original_reader(tracked_lines())

    bare._read_chat_completions_stream = tracked_reader

    def create_thread(config, label):
        return ChatThread(LOCAL.run_dir / 'calls' / label, config)

    def run_json_agent(*, instructions, inputs, schema_path, config, output_label, thread=None):
        active = thread or create_thread(config, output_label)
        active.turn_count += 1
        call_dir = active.root / f'turn_{active.turn_count}'
        LOCAL.call_dir = call_dir
        call_dir.mkdir(parents=True, exist_ok=True)
        full_input = (f'{instructions.rstrip()}\n\n{inputs.rstrip()}\n\n'
                      '# Exact Output Contract\n\n'
                      'Return exactly one JSON object matching the supplied output schema. '
                      'Do not add prose or Markdown fences.\n')
        schema = load(schema_path)
        if response_format in {'json_object', 'plain'}:
            full_input += '\n# Supplied Output Schema\n\n' + json.dumps(schema, ensure_ascii=False)
        active.messages.append({'role': 'user', 'content': full_input})
        payload = {'model': config.model, 'messages': active.messages,
                   'max_tokens': max_tokens, 'stream': True, 'stream_options': {'include_usage': True},
                   'reasoning_effort': 'high', 'thinking': {'type': 'enabled'}}
        if response_format == 'json_schema':
            payload['response_format'] = {'type': 'json_schema', 'json_schema': {
                'name': output_label, 'strict': True, 'schema': schema}}
        elif response_format == 'json_object':
            payload['response_format'] = {'type': 'json_object'}
        save(call_dir / 'request.json', payload)
        save(call_dir / 'output_schema.json', schema)
        provider = bare.ProviderConfig(credentials['BASE_URL'], key, config.model,
                                       'chat_completions', 'high', max_tokens, 1200, True)
        attempts = []

        def on_attempt(value):
            attempts.append(value)
            save(call_dir / 'transport_attempts.json', attempts)

        start = time.monotonic()
        try:
            try:
                response = bare.send_one_request(provider, payload, attempt_callback=on_attempt)
            except Exception as error:
                budget = reduced_output_budget(error, payload['max_tokens'])
                if budget is None:
                    raise
                save(call_dir / 'context_budget_adjustment.json', {
                    'at': now(), 'old_max_tokens': payload['max_tokens'],
                    'new_max_tokens': budget, 'reason': str(error).replace(key, '[REDACTED_API_KEY]'),
                    'messages_unchanged': True})
                save(call_dir / 'request_before_budget_adjustment.json', payload)
                payload['max_tokens'] = budget
                save(call_dir / 'request.json', payload)
                response = bare.send_one_request(provider, payload, attempt_callback=on_attempt)
            save(call_dir / 'response.json', response)
            choice = response['choices'][0]
            message = choice['message']
            usage = support.normalize_usage(response.get('usage'))
            audit = {'model': config.model, 'base_url': credentials['BASE_URL'], 'requested_reasoning_effort': 'high',
                     'usage': usage, 'raw_usage': response.get('usage'),
                     'wall_time_seconds': time.monotonic() - start, 'finish_reason': choice.get('finish_reason'),
                     'schema_sha256': digest(schema_path), 'input_sha256': hashlib.sha256(full_input.encode()).hexdigest(),
                     'tools': [], 'network_tools': 'disabled', 'request': str(call_dir / 'request.json'),
                     'turn_count': active.turn_count, 'transport_attempts': len(attempts)}
            save(call_dir / 'audit.json', audit)
            if choice.get('finish_reason') == 'length':
                raise ValueError('Judge exhausted output budget; not a zero-score solver outcome')
            content = message.get('content', '')
            value = parse_json(content)
            active.messages.append({'role': 'assistant', 'content': content,
                                    **({'reasoning_content': message['reasoning_content']} if message.get('reasoning_content') else {})})
            save(call_dir / 'parsed.json', value)
            return value, usage, audit
        except Exception as error:
            safe = str(error).replace(key, '[REDACTED_API_KEY]')
            save(call_dir / 'error.json', {'error': safe, 'at': now(), 'elapsed_seconds': time.monotonic() - start})
            raise RuntimeError(safe) from None

    pipeline.create_agent_thread = create_thread
    pipeline.run_json_agent = run_json_agent
    return pipeline


def rejudge(root, entry, judge, pipeline):
    pid = entry['paper_id']
    directory = root / 'judges' / judge / 'papers' / pid
    result_path = directory / 'result.json'
    if result_path.exists() and load(result_path)['status'] in {'completed', 'unscorable'}:
        return load(result_path)
    attempts = directory / 'attempts'
    number = len(list(attempts.glob('attempt_*'))) + 1
    run_dir = attempts / f'attempt_{number}'
    LOCAL.run_dir = run_dir
    inputs = root / 'inputs' / pid
    for file, expected in entry['input_sha256'].items():
        assert digest(inputs / file) == expected, str(inputs / file)
    results = {m: {'proof': (inputs / 'answers' / m / 'answer_for_evaluator.md').read_text()}
               for m in entry['assignment'].values()}
    terminal = {m: 0 for m, outcome in entry['solver_outcomes'].items() if outcome == 'no_final_answer'}
    bundle = pipeline.ArtifactBundle(entry['revision'], inputs / 'artifacts')
    agent = pipeline.AgentConfig(Path('unused-by-chat-transport'), 'unused', MODELS[judge], 'high', 1200)
    state = {'paper_id': pid, 'prc': entry['prc'], 'judge': judge, 'model': MODELS[judge],
             'started_at': now(), 'status': 'running', 'stage': 'reviewer', 'attempt': number,
             'baseline_scores': entry['baseline_scores'], 'scores': terminal, 'usage': {}}
    save(result_path, state)
    save(run_dir / 'exposure.json', {'assignment': entry['assignment'],
         'reviewer': ['artifacts/task.md'] + [f'answers/{m}/answer_for_evaluator.md' for m in entry['assignment'].values()],
         'evaluator_additional': ['artifacts/proof_ground_truth.md', 'artifacts/rubric.md', 'artifacts/provenance.json', 'new_judge_reviewer_reports'],
         'input_sha256': entry['input_sha256'], 'original_gpt_scores_exposed': False, 'source_paper_exposed': False})
    emit(event='started', paper_id=pid, judge=judge, attempt=number)
    try:
        prior_review = next((d / 'paired_reviewer.json' for d in sorted(attempts.glob('attempt_*'), reverse=True)
                            if d != run_dir and (d / 'paired_reviewer.json').is_file()), None)
        if prior_review is not None:
            envelope = load(prior_review)
            pipeline.validate_schema(envelope, load(pipeline.SCHEMAS / 'paired_reviewer.schema.json'))
            reviews = pipeline._reports_by_id(envelope, 'report', set(entry['assignment']))
            for aid, report in reviews.items():
                pipeline.validate_reviewer_report(report, load(pipeline.SCHEMAS / 'reviewer.schema.json'))
                save(run_dir / 'models' / entry['assignment'][aid] / 'validity_report.json', report)
            save(run_dir / 'paired_reviewer.json', envelope)
            save(run_dir / 'reviewer_reuse.json', {'source': str(prior_review), 'sha256': digest(prior_review)})
            usage = None
        else:
            reviews, usage = pipeline.run_paired_reviewer(bundle, entry['assignment'], results, run_dir, agent)
        state.update(stage='evaluator', reviewer_completed_at=now())
        state['usage']['reviewer'] = usage
        save(result_path, state)
        evaluations, usage = pipeline.run_paired_evaluator(bundle, entry['assignment'], results, reviews, run_dir, agent)
        state['usage']['evaluator'] = usage
        state['scores'].update({entry['assignment'][aid]: ev['score'] for aid, ev in evaluations.items()})
        unscorable = {entry['assignment'][aid]: ev['evaluation_status'] for aid, ev in evaluations.items()
                      if ev['evaluation_status'] == 'unscorable'}
        state.update(status='unscorable' if unscorable else 'completed', unscorable=unscorable, stage='finished')
    except Exception as error:
        state.update(status='failed', error=str(error))
    state['finished_at'] = now()
    save(result_path, state)
    save(run_dir / 'result.json', state)
    emit(event='finished', paper_id=pid, judge=judge, status=state['status'], scores=state['scores'])
    return state


def metrics(pairs):
    if not pairs:
        return {'n': 0}
    old, new = zip(*pairs)
    return {'n': len(pairs), 'gpt_judge_mean': statistics.mean(old), 'new_judge_mean': statistics.mean(new),
            'mean_delta': statistics.mean(b-a for a, b in pairs),
            'mean_absolute_difference': statistics.mean(abs(b-a) for a, b in pairs),
            'gpt_ge8_rate': sum(a >= 8 for a in old)/len(old),
            'new_ge8_rate': sum(b >= 8 for b in new)/len(new),
            'exact_agreement': sum(a == b for a, b in pairs)/len(pairs)}


def summarize(root):
    selection = load(root / 'selection.json')
    report = {'updated_at': now(), 'expected_per_judge': len(selection['papers']), 'judges': {}}
    for judge in MODELS:
        records = [load(p) for p in (root / 'judges' / judge / 'papers').glob('*/result.json')]
        completed = [r for r in records if r['status'] == 'completed']
        groups = {}
        for prc in ['all', 'PRC0', 'PRC1', 'PRC2', 'PRC3', 'PRC4']:
            subset = [r for r in completed if prc == 'all' or r['prc'] == prc]
            groups[prc] = {m: metrics([(r['baseline_scores'][m], r['scores'][m]) for r in subset
                                       if isinstance(r['baseline_scores'].get(m), (int, float))
                                       and isinstance(r['scores'].get(m), (int, float))]) for m in ALL_MODELS}
        contrasts = []
        for r in completed:
            if all(isinstance(r['scores'].get(m), (int, float)) and isinstance(r['baseline_scores'].get(m), (int, float)) for m in CORE):
                delta = {m: r['scores'][m] - r['baseline_scores'][m] for m in CORE}
                contrasts.append(statistics.mean(delta[m] for m in ('gpt6', 'gpt56')) -
                                 statistics.mean(delta[m] for m in CORE if m not in ('gpt6', 'gpt56')))
        usage_totals = Counter()
        returned_calls = 0
        for audit_path in (root / 'judges' / judge).glob('papers/*/attempts/*/calls/*/*/audit.json'):
            audit = load(audit_path)
            returned_calls += 1
            for key, value in (audit.get('usage') or {}).items():
                if isinstance(value, (int, float)):
                    usage_totals[key] += value
        report['judges'][judge] = {'status_counts': dict(Counter(r['status'] for r in records)),
            'not_started': len(selection['papers']) - len(records),
            'usage_all_returned_calls_including_retries': dict(usage_totals), 'returned_calls': returned_calls,
            'metrics': groups, 'gpt_vs_non_gpt_delta_contrast': statistics.mean(contrasts) if contrasts else None,
            'contrast_n': len(contrasts), 'records': records}
    save(root / 'comparison.json', report)
    lines = ['# 交叉模型评分测试', '', f"更新：{report['updated_at']}（UTC）", '',
             '固定抽样 46 篇：PRC0–3 各 10 篇，PRC4 全部 6 篇。六个非 GLM 模型均提交过答案。',
             '每个新评审模型使用原冻结 Task、答案、GT、rubric、匿名顺序及生产评分规则；不运行 Solver，不修改任务。',
             'GLM 无答案的记录保留为 0 分。调用或校验失败不计为 0 分。以下均为新评分已完成篇目与其原 GPT 评分的配对比较。', '']
    for judge, value in report['judges'].items():
        lines += [f'## {MODELS[judge]}', '', f"执行状态：`{json.dumps(value['status_counts'], ensure_ascii=False)}`。", '',
                  '| Solver | 配对篇数 | 原 GPT 均分 | 新评审均分 | 平均变化 | 原 ≥8 比例 | 新 ≥8 比例 |',
                  '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
        for model, row in value['metrics']['all'].items():
            if not row['n']:
                continue
            lines.append(f"| {model} | {row['n']} | {row['gpt_judge_mean']:.2f} | {row['new_judge_mean']:.2f} | {row['mean_delta']:+.2f} | {row['gpt_ge8_rate']:.1%} | {row['new_ge8_rate']:.1%} |")
        if value['gpt_vs_non_gpt_delta_contrast'] is not None:
            lines += ['', '逐篇计算 GPT 两个 Solver 的平均分数变化，再减去其他四个 Solver 的平均分数变化。',
                      f"该差值的平均值为 **{value['gpt_vs_non_gpt_delta_contrast']:+.3f}**，配对篇数 {value['contrast_n']}。负值表示新评审对 GPT 答案的相对评分更低；这是一项评分差异指标，需要结合具体判分理由判断。"]
        lines += ['', '### 按 PRC 的分数变化', '', '| PRC | Solver | 配对篇数 | 原均分 | 新均分 | 变化 |',
                  '| --- | --- | ---: | ---: | ---: | ---: |']
        for prc in ['PRC0', 'PRC1', 'PRC2', 'PRC3', 'PRC4']:
            for model, row in value['metrics'][prc].items():
                if row['n']:
                    lines.append(f"| {prc} | {model} | {row['n']} | {row['gpt_judge_mean']:.2f} | {row['new_judge_mean']:.2f} | {row['mean_delta']:+.2f} |")
        lines += ['']
    temp = root / 'comparison.md.tmp'
    temp.write_text('\n'.join(lines) + '\n')
    temp.replace(root / 'comparison.md')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'run', 'summarize'])
    parser.add_argument('--base', type=Path, default=Path('/home/ubuntu/ml-theory-run'))
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--credentials', type=Path)
    parser.add_argument('--judges', nargs='+', choices=list(MODELS), default=list(MODELS))
    parser.add_argument('--workers-per-judge', type=int, default=10)
    parser.add_argument('--max-tokens', type=int, default=131072)
    parser.add_argument('--response-format', choices=['json_schema', 'json_object', 'plain'], default='plain')
    parser.add_argument('--paper-ids', nargs='*')
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare(args.root, args.base)
        return
    if args.command == 'summarize':
        report = summarize(args.root)
        emit(event='summary', statuses={k:v['status_counts'] for k,v in report['judges'].items()})
        return
    assert 1 <= args.workers_per_judge <= 10
    assert args.credentials is not None
    concurrency_file = args.root / 'concurrency.json'
    if concurrency_file.exists():
        worker_limit = load(concurrency_file)['workers_per_judge']
        if type(worker_limit) is not int or not 1 <= worker_limit <= 10:
            raise ValueError('workers_per_judge must be an integer between 1 and 10')
        args.workers_per_judge = min(args.workers_per_judge, worker_limit)
    with (args.root / 'runner.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        pipeline = install_transport(args.root, args.credentials, args.max_tokens, args.response_format)
        papers = [p for p in load(args.root / 'selection.json')['papers'] if not args.paper_ids or p['paper_id'] in args.paper_ids]
        save(args.root / 'latest_launch.json', {'at': now(), 'pid': os.getpid(), 'judges': args.judges,
             'workers_per_judge': args.workers_per_judge, 'paper_count': len(papers),
             'max_tokens': args.max_tokens, 'response_format': args.response_format})
        pools = {j: concurrent.futures.ThreadPoolExecutor(max_workers=args.workers_per_judge) for j in args.judges}
        futures = [pools[j].submit(rejudge, args.root, p, j, pipeline) for j in args.judges for p in papers]
        try:
            for future in concurrent.futures.as_completed(futures):
                future.result()
                summarize(args.root)
        finally:
            for pool in pools.values():
                pool.shutdown(wait=True)
        summarize(args.root)
        emit(event='batch_finished')


if __name__ == '__main__':
    main()
