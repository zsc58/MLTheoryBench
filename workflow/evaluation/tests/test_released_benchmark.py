from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'runtime'))
import run_released_benchmark as release


class ReleasedDatasetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'data'
        self.root.mkdir()
        self.item = {'paper_id': 'paper_2026_001', 'prc': 'PRC4', 'sha256': {}}
        for field, (name, directory) in release.FILES.items():
            path = self.root / directory / 'paper_2026_001' / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('Test ' + name)
            self.item[field] = path.relative_to(self.root).as_posix()
            self.item['sha256'][name] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.write_manifest([self.item])

    def write_manifest(self, items):
        (self.root / 'manifest.json').write_text(json.dumps({
            'name': 'MLTheoryBench', 'task_count': len(items), 'tasks': items}))

    def test_validate_and_copy(self):
        self.assertEqual(len(release.validate_dataset(self.root)), 1)
        bundle = release.copy_bundle(self.root, self.item, Path(self.temp.name) / 'bundle')
        self.assertEqual(bundle.task.read_text(), 'Test task.md')
        self.assertEqual(bundle.proof_ground_truth.read_text(), 'Test proof_ground_truth.md')

    def test_hash_change_rejected(self):
        (self.root / self.item['task_file']).write_text('changed')
        with self.assertRaises(ValueError):
            release.validate_dataset(self.root)

    def test_duplicate_rejected(self):
        self.write_manifest([self.item, self.item])
        with self.assertRaises(ValueError):
            release.validate_dataset(self.root)

    def test_path_escape_rejected(self):
        self.item['task_file'] = '../task.md'
        self.write_manifest([self.item])
        with self.assertRaises(ValueError):
            release.validate_dataset(self.root)

    def test_empty_answer_zero_skips_judges(self):
        spec = release.SolverSpec('test', None)
        with patch.object(release, 'run_all_solvers', return_value={
            'test': {'solver_outcome': 'no_final_answer'}}) as solver, \
             patch.object(release, 'run_paired_reviewer') as reviewer, \
             patch.object(release, 'run_paired_evaluator') as evaluator:
            result = release.run_task(self.root, self.item, Path(self.temp.name) / 'run',
                                      'test', [spec], None)
        self.assertEqual(result['scores'], {'test': 0})
        self.assertEqual(result['status'], 'completed')
        self.assertTrue(solver.call_args.kwargs['frozen_task'])
        reviewer.assert_not_called()
        evaluator.assert_not_called()

    def test_shared_judging(self):
        specs = [release.SolverSpec(k, None) for k in ['a', 'b']]
        results = {k: {'solver_outcome': 'final_answer', 'proof': k} for k in ['a', 'b']}
        def evaluate(bundle, assignment, *args):
            return {aid: {'evaluation_status': 'scored', 'score': 9}
                    for aid in assignment}, None
        with patch.object(release, 'run_all_solvers', return_value=results), \
             patch.object(release, 'run_paired_reviewer', return_value=({}, None)) as reviewer, \
             patch.object(release, 'run_paired_evaluator', side_effect=evaluate) as evaluator:
            result = release.run_task(self.root, self.item, Path(self.temp.name) / 'run',
                                      'test', specs, None)
        self.assertEqual(result['scores'], {'a': 9, 'b': 9})
        reviewer.assert_called_once()
        evaluator.assert_called_once()

    def test_transport_failure_not_zero(self):
        with patch.object(release, 'run_all_solvers', side_effect=RuntimeError('test failure')):
            result = release.run_task(self.root, self.item, Path(self.temp.name) / 'run',
                                      'test', [], None)
        self.assertEqual(result['status'], 'failed')
        self.assertEqual(result['scores'], {})

    def test_unscorable_is_stop(self):
        with patch.object(release, 'run_all_solvers', return_value={
            'a': {'solver_outcome': 'final_answer', 'proof': 'proof'}}), \
             patch.object(release, 'run_paired_reviewer', return_value=({}, None)), \
             patch.object(release, 'run_paired_evaluator', return_value=(
                 {'answer_a': {'evaluation_status': 'unscorable', 'score': None}}, None)):
            result = release.run_task(self.root, self.item, Path(self.temp.name) / 'run',
                                      'test', [release.SolverSpec('a', None)], None)
        self.assertEqual(result['status'], 'stopped')
        self.assertEqual(result['stop_reason'], 'evaluator_unscorable')
        self.assertEqual(result['scores'], {})


if __name__ == '__main__':
    unittest.main()
