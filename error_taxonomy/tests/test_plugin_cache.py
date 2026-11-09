import concurrent.futures
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from plugin_cache import attach_plugin_cache, prepare_plugin_cache
from provider_runtime import stage_environment


class PluginCacheTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        # macOS aliases /var and /tmp; production passes resolved batch paths.
        self.root = Path(self.tmp.name).resolve()
        self.cache = self.root / "shared" / "plugin_tmp"
        self.profile = ('model_provider="synthetic"\n', "synthetic-not-a-key", "TEST_ONLY_KEY", {})

    def stage(self, number):
        attempt = self.root / f"attempt_{number}"
        attempt.mkdir(mode=0o700)
        return stage_environment(attempt, sys.executable, self.profile, self.cache)

    def test_concurrent_homes_share_cache_not_sessions_or_config(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            envs = list(pool.map(self.stage, range(5)))
        homes = [Path(env["CODEX_HOME"]) for env in envs]
        self.assertEqual(len(set(homes)), 5)
        (self.cache / "plugins").mkdir()
        (self.cache / "plugins" / "asset").write_text("public plugin asset")
        for home in homes:
            self.assertEqual((home / ".tmp").resolve(), self.cache)
            self.assertEqual((home / ".tmp/plugins/asset").stat().st_ino,
                             (self.cache / "plugins/asset").stat().st_ino)
            self.assertFalse((home / "config.toml").is_symlink())
            self.assertNotIn(self.profile[1], (home / "config.toml").read_text())
        (homes[0] / "sessions").mkdir()
        (homes[0] / "sessions/private").write_text("private marker")
        self.assertFalse((homes[1] / "sessions/private").exists())
        self.assertFalse((self.cache / "sessions").exists())

    def test_refresh_replace_is_seen_by_all_homes(self):
        homes = [Path(self.stage(i)["CODEX_HOME"]) for i in range(2)]
        (self.cache / "plugins.sha").write_text("old")
        (self.cache / "new.sha").write_text("new")
        (self.cache / "new.sha").replace(self.cache / "plugins.sha")
        self.assertEqual([(h / ".tmp/plugins.sha").read_text() for h in homes], ["new", "new"])

    def test_existing_scratch_not_replaced(self):
        home = self.root / "home"; home.mkdir()
        (home / ".tmp").mkdir()
        (home / ".tmp/keep").write_text("unchanged")
        with self.assertRaises(ValueError): attach_plugin_cache(home, self.cache)
        self.assertEqual((home / ".tmp/keep").read_text(), "unchanged")

    def test_aliased_cache_rejected(self):
        target = self.root / "target"; target.mkdir(mode=0o700)
        alias = self.root / "alias"; alias.symlink_to(target, target_is_directory=True)
        home = self.root / "home"; home.mkdir()
        with self.assertRaises(ValueError): attach_plugin_cache(home, alias / "new")
        self.assertFalse((target / "new").exists())

    def test_world_accessible_cache_rejected(self):
        self.cache.mkdir(parents=True, mode=0o755); self.cache.chmod(0o755)
        with self.assertRaises(ValueError): self.stage(0)

    def test_cache_cannot_contain_session_home(self):
        self.cache.mkdir(parents=True, mode=0o700)
        home = self.cache / "home"; home.mkdir()
        with self.assertRaises(ValueError): attach_plugin_cache(home, self.cache)

    def test_version_namespaces_reuse_without_reading_credentials(self):
        with patch("plugin_cache.subprocess.run") as run:
            run.return_value.stdout = "codex-cli 0.146.0\n"
            a = prepare_plugin_cache(self.root / "versions", "/bin/codex")
            b = prepare_plugin_cache(self.root / "versions", "/bin/codex")
            run.return_value.stdout = "codex-cli 0.147.0\n"
            c = prepare_plugin_cache(self.root / "versions", "/bin/codex")
        self.assertEqual(a["path"], b["path"])
        self.assertNotEqual(a["path"], c["path"])
        self.assertEqual(a["session_state"], "per_attempt_codex_home")

    def test_no_cache_keeps_previous_direct_runner_behavior(self):
        attempt = self.root / "plain"; attempt.mkdir()
        env = stage_environment(attempt, sys.executable, self.profile)
        self.assertFalse((Path(env["CODEX_HOME"]) / ".tmp").exists())


if __name__ == "__main__":
    unittest.main()
