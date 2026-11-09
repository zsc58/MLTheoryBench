#!/usr/bin/env python3
"""Check flat reference packages and their minimal, local provenance.

This checks retained artifact hashes, source receipts, anchors, and actual cited
states. It does not replay historical agent inputs or certify English semantics.
Drafts are optional historical material and need not pass final alignment checks.
"""
from copy import deepcopy
import validation as v
from io_utils import check_receipt, check_schema, read, sha, validate_markdown
from check_imo_data import check_imo_data


def relocate_reads(value, case, aliases):
    if isinstance(value, str):
        if value in aliases:
            return aliases[value]
        prefix = 'cases/' + case['case_id'] + '/'
        if value.startswith(prefix):
            return case['source_bundle'] + '/' + value[len(prefix):]
    elif isinstance(value, list):
        return [relocate_reads(x, case, aliases) for x in value]
    elif isinstance(value, dict):
        return {k: relocate_reads(x, case, aliases) for k, x in value.items()}
    return value


def main():
    index = read(v.PROJECT / '.runtime/reference_evidence/index.json')
    aliases = {old: item['path'] for old, item in index['traces'].items()}
    for item in index['traces'].values():
        trace_path = v.read_path(item['path'])
        if sha(trace_path) != item['sha256']:
            raise ValueError(f'Retained trace changed: {trace_path}')
        trace = read(trace_path)
        if trace['retention']['original_trace_sha256'] != item['original_trace_sha256']:
            raise ValueError('Original trace identity mismatch')
        if trace['retention']['retained_tactic_count'] != len(trace['tactics']):
            raise ValueError('Retained trace count mismatch')

    for case in index['cases']:
        package = v.read_path(case['package'])
        bundle = v.read_path(case['source_bundle'])
        manifest = read(bundle / 'evidence/manifest.json')
        check_receipt(bundle, manifest)
        v.sources(bundle)
        if not manifest['lean_locally_verified'] or not manifest['standard_axioms_only']:
            raise ValueError(f'Unverified source: {case["case_id"]}')
        if (package / 'final').exists():
            raise ValueError(f'Package is not flat: {package}')
        for stage in ('final', 'draft'):
            folder = package if stage == 'final' else package / 'draft'
            if stage == 'draft' and not folder.exists():
                continue
            expected = case[stage + '_sha256']
            if set(expected) != set(v.ARTIFACTS):
                raise ValueError('Incomplete retained artifact receipt')
            for name, digest in expected.items():
                path = folder / name
                if sha(path) != digest:
                    raise ValueError(f'Historical artifact changed: {path}')
                if path.suffix == '.md':
                    validate_markdown(path)
                else:
                    check_schema(read(path), read(v.WORKFLOW / 'schemas' / (path.stem + '.schema.json')))

        alignment = read(package / 'alignment.json')
        sketch = read(package / 'sketch.json')
        if alignment['case_id'] != case['case_id'] or alignment['target'] != manifest['target']:
            raise ValueError('Package/source identity mismatch')
        job = {'case_id': case['case_id'], 'scope': case['scope'],
               'case_root': case['source_bundle'], 'provenance': manifest,
               'trace_source_files': {}}
        v.validate_sketch(job, sketch, alignment)
        # Relocate only in memory; final JSON remains byte-identical to its receipt.
        resolved = relocate_reads(deepcopy(alignment), case, aliases)
        v.validate_source_refs(job, v.source_refs(alignment, sketch), resolved['files_read'])
        for block in resolved['proof_blocks']:
            for ref in block['trace_refs']:
                trace = read(v.read_path(ref['trace_file']))
                job['trace_source_files'][ref['trace_file']] = 'sources/project/' + trace['source_file']
        coverage = v.validate_blocks(job, resolved)
        print(f"{case['case_id']}: unchanged package; source, schema, graph, anchors and {coverage['proof_blocks']} proof blocks checked")
    discovered = {str(p.parent.relative_to(v.PROJECT)) for group in ('ai4slt', 'tlb')
                  for p in (v.PROJECT / 'data' / group).glob('*/problem.md')}
    if discovered != {case['package'] for case in index['cases']}:
        raise ValueError('Data inventory differs from provenance index')
    check_imo_data()
    print('No model calls or Lean recompilation. Historical read-list replay and English equivalence are not claimed.')


if __name__ == '__main__':
    main()
