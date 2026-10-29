from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / ".agents/skills/mathforge/scripts/mathforge"


class LauncherTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="mafs-launcher-test-")
        self.path = Path(self.temp.name)
        self.fake = self.path / "fake-codex"
        self.fake.write_text("#!/usr/bin/env python3\nimport json,sys\nprint(json.dumps(sys.argv[1:]))\n")
        self.fake.chmod(0o755)
        self.env = dict(os.environ, MATHFORGE_CODEX=str(self.fake))

    def tearDown(self):
        self.temp.cleanup()

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(LAUNCHER), *args], env=self.env, capture_output=True, text=True, check=False)

    def test_literal_task_and_workspace_are_preserved(self):
        workspace = self.path / "workspace with spaces"
        workspace.mkdir()
        marker = self.path / "should_not_exist"
        task = "Inspect $(touch " + str(marker) + ") and `touch " + str(marker) + "`; preserve $VALUE\nnext line"
        result = self.run_cli("-C", str(workspace), "research", task)
        self.assertEqual(result.returncode, 0, result.stderr)
        actual = json.loads(result.stdout)
        self.assertEqual(actual[:2], ["-C", str(workspace.resolve())])
        self.assertEqual(len(actual), 3)
        self.assertIn(task, actual[2])
        self.assertIn("Use $mathforge", actual[2])
        self.assertFalse(marker.exists())
        self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", actual)

    def test_missing_workspace_fails_before_launch(self):
        result = self.run_cli("-C", str(self.path / "missing"), "design")
        self.assertEqual(result.returncode, 2)
        self.assertIn("does not exist", result.stderr)

    def test_invalid_override_does_not_fall_back(self):
        self.env["MATHFORGE_CODEX"] = str(self.path / "missing-codex")
        result = self.run_cli("design")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unavailable", result.stderr)

    def test_inspection_does_not_launch_session(self):
        result = self.run_cli("--check")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(json.loads(report["codexVersion"]), ["--version"])
        self.assertEqual(report["persistentRuntime"], "notProvided")

    def test_print_launch_is_only_data(self):
        result = self.run_cli("--print-launch", "review", "proof.md")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)[0], str(self.fake))

    def test_hud_does_not_launch_browser(self):
        result = self.run_cli("hud")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Open this file manually", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
