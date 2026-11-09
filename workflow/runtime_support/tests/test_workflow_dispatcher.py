from pathlib import Path
import subprocess
import sys
import unittest

WORKFLOW = Path(__file__).resolve().parents[2]


class WorkflowDispatcherTests(unittest.TestCase):
    def help_for(self, stage):
        result = subprocess.run([sys.executable, '-B', str(WORKFLOW / 'run.py'), stage, '--help'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_build_help(self):
        self.assertIn('--source-papers-root', self.help_for('build'))

    def test_single_help(self):
        self.assertIn('--paper-dir', self.help_for('build-single'))

    def test_calibrate_help(self):
        self.assertIn('--calibrate-once', self.help_for('calibrate'))

    def test_evaluate_help(self):
        self.assertIn('--data-root', self.help_for('evaluate'))

    def test_profiles_help(self):
        self.assertIn('--get-key-file', self.help_for('profiles'))


if __name__ == '__main__':
    unittest.main()
