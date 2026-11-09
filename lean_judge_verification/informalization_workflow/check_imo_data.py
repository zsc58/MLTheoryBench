#!/usr/bin/env python3
"""Validate the informal IMO package layout and optional private hash receipts."""
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from io_utils import validate_markdown

PROJECT = Path(__file__).resolve().parents[1]
CORE = {'problem.md', 'proof.md', 'gt.md'}
GUIDE = 'reading_guide_zh.md'
FIGURE = 'reading_figure.svg'
# Retained after the 2026-10-15 selection: official mean score / 7 < 60%.
EXPECTED_BY_YEAR = {
    2022: (3, 5, 6),
    2023: (2, 3, 5, 6),
    2024: (2, 3, 5, 6),
    2025: (2, 3, 5, 6),
    2026: (2, 3, 5, 6),
}
EXPECTED = {f'imo_{year}_p{number:02d}'
            for year, numbers in EXPECTED_BY_YEAR.items() for number in numbers}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_imo_data():
    root = PROJECT / 'data/imo'
    packages = {p.name: p for p in root.glob('imo_*') if p.is_dir()}
    if set(packages) != EXPECTED:
        raise ValueError(f'IMO inventory mismatch: {set(packages) ^ EXPECTED}')
    note_count = submission_count = mutation_count = guide_count = figure_count = 0
    for case_id, folder in sorted(packages.items()):
        names = {p.name for p in folder.iterdir()}
        submissions = {name for name in names if re.fullmatch(r'pf\d{2}\.md', name)}
        mutations = {name for name in names if re.fullmatch(r'proof_0[1-4]\.md', name)}
        allowed = CORE | {GUIDE, FIGURE, 'error_directions.md'} | submissions | mutations
        if not (CORE | {GUIDE}) <= names or names - allowed:
            raise ValueError(f'Unexpected or missing files in {case_id}: {names}')
        for path in folder.iterdir():
            if not path.is_file():
                raise ValueError(f'IMO packages must be flat: {path}')
            if path.name == FIGURE:
                drawing = ET.parse(path).getroot()
                if drawing.tag != '{http://www.w3.org/2000/svg}svg':
                    raise ValueError(f'Expected SVG teaching figure: {path}')
                guide_text = (folder / GUIDE).read_text(encoding='utf-8')
                if f']({FIGURE})' not in guide_text:
                    raise ValueError(f'Teaching figure is not linked from guide: {path}')
                continue
            validate_markdown(path)
            text = path.read_text(encoding='utf-8')
            if path.name != GUIDE and re.search(r'[\u3400-\u9fff]', text):
                raise ValueError(f'Expected English package content: {path}')
            if re.search(r'\b(?:TODO|FIXME|TBD)\b', text):
                raise ValueError(f'Unfinished package content: {path}')
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if not target.startswith(('http:', 'https:', '#')):
                    if not (folder / target.split('#', 1)[0]).is_file():
                        raise ValueError(f'Broken link in {path}: {target}')
        gt = (folder / 'gt.md').read_text(encoding='utf-8')
        rows = re.findall(r'^\| \[([^]]+)\]\(([^)]+)\) \| `([^`]+)` \|', gt, re.M)
        if {label for label, _, _ in rows} != {'proof.md'} | submissions | mutations:
            raise ValueError(f'Submission/GT mismatch: {case_id}')
        if any(label != target or verdict not in {'no_error_found', 'error_found'}
               for label, target, verdict in rows):
            raise ValueError(f'Invalid GT row: {case_id}')
        if '[proof.md](proof.md) | `no_error_found`' not in gt:
            raise ValueError(f'Missing correct-reference verdict: {case_id}')
        note_count += 'error_directions.md' in names
        guide_count += GUIDE in names
        figure_count += FIGURE in names
        submission_count += len(submissions)
        mutation_count += len(mutations)

    receipt = PROJECT / '.runtime/imo_sources/manifest.json'
    if receipt.exists():
        manifest = json.loads(receipt.read_text(encoding='utf-8'))
        if {c['case_id'] for c in manifest['cases']} != EXPECTED:
            raise ValueError('IMO receipt inventory mismatch')
        for case in manifest['cases']:
            folder = packages[case['case_id']]
            if set(case['artifact_sha256']) != {p.name for p in folder.iterdir()}:
                raise ValueError(f'Incomplete artifact receipt: {case["case_id"]}')
            for name, digest in case['artifact_sha256'].items():
                if sha(folder / name) != digest:
                    raise ValueError(f'Changed IMO artifact: {folder / name}')
        for source in manifest['downloaded_files']:
            path = receipt.parent / source['file']
            if sha(path) != source['sha256']:
                raise ValueError(f'Changed retained source: {path}')
        evidence = 'local source and artifact hashes checked'
    else:
        evidence = 'structure only; local source receipt unavailable'
    print(f'IMO: {len(packages)} packages, {len(packages) * 3} core files, '
          f'{guide_count} Chinese reading guides, {figure_count} teaching figures, '
          f'{note_count} source-based authoring notes, '
          f'{submission_count} contestant submissions, {mutation_count} controlled variants; {evidence}.')
    print('IMO checks cover packaging and receipts; mathematical proofs are informal references.')


if __name__ == '__main__':
    check_imo_data()
