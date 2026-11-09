"""Wait for the real-paper smoke test, then run and monitor both judge cohorts."""
import argparse
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import subprocess
import sys
import time


def load(p):
    return json.loads(p.read_text())


def save(p, v):
    temp = p.with_suffix('.tmp')
    temp.write_text(json.dumps(v, indent=2) + '\n')
    temp.replace(p)


def stamp():
    return datetime.now(timezone.utc).isoformat()


def main():
    a = argparse.ArgumentParser()
    a.add_argument('--root', type=Path, required=True)
    a.add_argument('--credentials', type=Path, required=True)
    a.add_argument('--resume', action='store_true')
    a.add_argument('--cooldown-seconds', type=int, default=0)
    args = a.parse_args()
    root = args.root
    lock = (root / 'supervisor.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    runner = root / 'code/run_crosscheck.py'
    smoke = load(root / 'smoke_launch.json')['paper_id']
    status_path = root / 'supervisor_status.json'
    deadline = time.monotonic() + 8 * 3600
    judges = ['deepseek', 'qwen']
    run_tag = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')

    def launch(label, more):
        command = [sys.executable, '-u', '-B', str(runner), 'run', '--root', str(root),
                   '--credentials', str(args.credentials), '--workers-per-judge', '10', '--response-format', 'plain'] + more
        with (root / (label + '_' + run_tag + '.log')).open('x') as log:
            child = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                     stdin=subprocess.DEVNULL)
            while child.poll() is None:
                save(status_path, {'phase': label, 'updated_at': stamp(), 'child_pid': child.pid})
                time.sleep(20)
            return child.returncode

    if args.cooldown_seconds:
        save(status_path, {'phase': 'cooldown', 'updated_at': stamp(), 'seconds': args.cooldown_seconds})
        time.sleep(args.cooldown_seconds)
    while not args.resume:
        states = {j: load(root / 'judges' / j / 'papers' / smoke / 'result.json')['status'] for j in judges}
        save(status_path, {'phase': 'waiting_for_smoke', 'updated_at': stamp(), 'states': states})
        if all(v in {'completed', 'unscorable', 'failed'} for v in states.values()):
            break
        if time.monotonic() >= deadline:
            save(status_path, {'phase': 'blocked', 'reason': 'smoke_wait_timeout', 'updated_at': stamp()})
            return
        time.sleep(20)
    time.sleep(5)
    failed = [] if args.resume else [j for j, v in states.items() if v == 'failed']
    if failed:
        launch('smoke_retry', ['--paper-ids', smoke, '--judges', *failed])
        states = {j: load(root / 'judges' / j / 'papers' / smoke / 'result.json')['status'] for j in judges}
        if any(v == 'failed' for v in states.values()):
            save(status_path, {'phase': 'blocked', 'reason': 'smoke_failed_twice', 'states': states, 'updated_at': stamp()})
            return
    code = launch('batch', [])
    if code:
        save(status_path, {'phase': 'blocked', 'reason': 'batch_process_error', 'returncode': code, 'updated_at': stamp()})
        return
    for judge in judges:
        failed_ids = [p.parent.name for p in (root / 'judges' / judge / 'papers').glob('*/result.json')
                      if load(p)['status'] == 'failed']
        if failed_ids:
            launch('retry_' + judge, ['--judges', judge, '--paper-ids', *failed_ids])
    subprocess.run([sys.executable, '-B', str(runner), 'summarize', '--root', str(root)], check=True)
    comparison = load(root / 'comparison.json')
    save(status_path, {'phase': 'finished', 'updated_at': stamp(),
                       'outcomes': {j: v['status_counts'] for j, v in comparison['judges'].items()}})


if __name__ == '__main__':
    main()
