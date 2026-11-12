#!/usr/bin/env python3
"""One CLI for construction, calibration, and frozen benchmark evaluation."""
from pathlib import Path
import argparse
import runpy
import sys

ROOT = Path(__file__).resolve().parent
ENTRIES = {
    'build': 'data_preparation/pipeline/run_stage3_batch.py',
    'build-single': 'data_preparation/pipeline/run_stage3_pipeline.py',
    'calibrate': 'evaluation/runtime/run_comparison.py',
    'evaluate': 'evaluation/runtime/run_released_benchmark.py',
    'evaluate-answers': 'evaluation/runtime/run_released_benchmark.py',
    'profiles': 'evaluation/runtime/model_profiles.py',
}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, usage='%(prog)s STAGE [stage arguments]')
    parser.add_argument('stage', choices=ENTRIES)
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    entry = ROOT / ENTRIES[args.stage]
    forwarded = list(args.arguments)
    if forwarded[:1] == ['--']:
        forwarded.pop(0)
    if args.stage == 'calibrate' and '--calibrate-once' not in forwarded:
        forwarded.append('--calibrate-once')
    if args.stage == 'evaluate-answers':
        forwarded.insert(0, '--answers-only')
    sys.path.insert(0, str(entry.parent))
    sys.argv = [str(entry), *forwarded]
    runpy.run_path(str(entry), run_name='__main__')


if __name__ == '__main__':
    main()
