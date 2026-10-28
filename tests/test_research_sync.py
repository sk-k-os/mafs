from __future__ import annotations

import fcntl
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import ModuleType
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT = ROOT / ".agents/skills/mathforge/scripts/checkpoint.py"
LAUNCHER = ROOT / ".agents/skills/mathforge/scripts/mathforge"
GIT = shutil.which("git")


@unittest.skipUnless(GIT, "Git is required for local checkpoint integration tests")
class ResearchSyncTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="mafs-research-sync-")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.remote = self.directory / "remote.git"
        self.repo = self.directory / "research checkout"
        self.env = {
            key: value for key, value in os.environ.items()
            if not key.startswith("GIT_")
        }
        global_config = self.directory / "empty-gitconfig"
        global_config.write_text("", encoding="utf-8")
        self.env.update({
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": str(global_config),
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_ALLOW_PROTOCOL": "file",
        })
        self.git("init", "--bare", "--initial-branch=main", str(self.remote), cwd=self.directory)
        self.git("clone", str(self.remote), str(self.repo), cwd=self.directory)
        self.configure_author(self.repo)
        (self.repo / "README.md").write_text("Checkpoint test repository.\n", encoding="utf-8")
        (self.repo / "research").mkdir()
        (self.repo / "research/STATE.md").write_text(
            "# State\n\nThe target remains unresolved. Next: inspect the hypotheses.\n",
            encoding="utf-8",
        )
        self.config: dict[str, object] = {
            "version": 1,
            "enabled": True,
            "remote": "origin",
            "expectedRemote": str(self.remote),
            "scope": "research/",
        }
        self.write_config()
        self.git("add", "README.md", "research-sync.json", "research/STATE.md")
        self.git("commit", "-m", "Seed research checkpoint repository")
        self.git("push", "-u", "origin", "main")
        self.seed_commit = self.head()

    def git(self, *arguments: str, cwd: Path | None = None) -> str:
        assert GIT is not None
        result = subprocess.run(
            [GIT, *arguments], cwd=cwd or self.repo, env=self.env,
            capture_output=True, text=True, check=False, timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def configure_author(self, path: Path) -> None:
        self.git("config", "user.name", "Mathforge Test", cwd=path)
        self.git("config", "user.email", "mathforge-test@example.invalid", cwd=path)
        self.git("config", "commit.gpgsign", "false", cwd=path)
        self.git("config", "core.autocrlf", "false", cwd=path)

    def write_config(self) -> None:
        (self.repo / "research-sync.json").write_text(
            json.dumps(self.config) + "\n", encoding="utf-8",
        )

    def head(self) -> str:
        return self.git("rev-parse", "HEAD")

    def remote_head(self) -> str:
        return self.git("--git-dir", str(self.remote), "rev-parse", "refs/heads/main")

    def write_note(self, name: str = "lemma.md", text: str | None = None) -> Path:
        note = self.repo / "research" / name
        note.parent.mkdir(parents=True, exist_ok=True)
        note.write_text(
            text or "# Candidate lemma\n\nThis argument is incomplete and requires review.\n",
            encoding="utf-8",
        )
        return note

    def checkpoint(self, message: str = "Preserve bounded research progress") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CHECKPOINT), "-C", str(self.repo), message],
            cwd=self.repo, env=self.env, capture_output=True, text=True,
            check=False, timeout=20,
        )

    def fake_research_session(self, exit_code: int) -> subprocess.CompletedProcess[str]:
        fake_codex = self.directory / "fakeCodex"
        fake_codex.write_text(
            "#!/usr/bin/env python3\n"
            "from pathlib import Path\n"
            "import sys\n"
            "assert sys.argv[1] == '-C'\n"
            "workspace = Path(sys.argv[2])\n"
            "(workspace / 'research/session.md').write_text("
            "'A simulated session preserved an unresolved research observation.\\n', encoding='utf-8')\n"
            f"sys.exit({exit_code})\n",
            encoding="utf-8",
        )
        fake_codex.chmod(0o755)
        return subprocess.run(
            [sys.executable, str(LAUNCHER), "-C", str(self.repo), "research", "Record a bounded observation"],
            cwd=self.repo, env=dict(self.env, MATHFORGE_CODEX=str(fake_codex)),
            capture_output=True, text=True, check=False, timeout=20,
        )

    def checkpoint_module(self) -> ModuleType:
        spec = importlib.util.spec_from_file_location("mathforge_checkpoint_race_test", CHECKPOINT)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def assert_blocked_without_commits(self) -> subprocess.CompletedProcess[str]:
        before = self.head()
        remote_before = self.remote_head()
        result = self.checkpoint()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.head(), before)
        self.assertEqual(self.remote_head(), remote_before)
        return result

    def assert_synced(self, result: subprocess.CompletedProcess[str]) -> dict[str, object]:
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertIs(report.get("synced"), True)
        self.assertEqual(report.get("commit"), self.head())
        self.assertEqual(self.remote_head(), self.head())
        return report

    def test_research_changes_are_committed_and_pushed(self) -> None:
        self.write_note()
        state = self.repo / "research/STATE.md"
        state.write_text(state.read_text(encoding="utf-8") + "A candidate was recorded.\n", encoding="utf-8")

        self.assert_synced(self.checkpoint("Record lemma candidate and next obligation"))

        self.assertNotEqual(self.head(), self.seed_commit)
        changed = set(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines())
        self.assertEqual(changed, {"research/STATE.md", "research/lemma.md"})
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_push_follow_tags_cannot_publish_unrequested_annotated_tag(self) -> None:
        self.git("config", "push.followTags", "true")
        self.git("tag", "-a", "unpublished-local-note", "-m", "Local tag remains unpublished")
        self.write_note()

        self.assert_synced(self.checkpoint())

        self.assertEqual(self.git("tag", "--list"), "unpublished-local-note")
        self.assertEqual(self.git("--git-dir", str(self.remote), "tag", "--list"), "")

    def test_commit_added_after_inspection_is_never_published(self) -> None:
        self.write_note()
        module = self.checkpoint_module()
        original_inspector = module.inspect_pending_history
        inspected_heads: list[str] = []
        concurrent_heads: list[str] = []

        def inspect_then_add_commit(root: Path, remote_head: str, *heads: str) -> None:
            original_inspector(root, remote_head, *heads)
            inspected_heads.append(heads[0] if heads else self.head())
            (self.repo / "README.md").write_text("Concurrent unrelated work must stay local.\n", encoding="utf-8")
            self.git("add", "README.md")
            self.git("commit", "-m", "Concurrent unrelated local commit")
            concurrent_heads.append(self.head())

        with mock.patch.dict(os.environ, self.env, clear=True):
            with mock.patch.object(module, "inspect_pending_history", inspect_then_add_commit):
                with self.assertRaises(module.SyncError):
                    module.checkpoint(self.repo, "Checkpoint with a concurrent local commit")

        self.assertEqual(len(inspected_heads), 1)
        self.assertEqual(len(concurrent_heads), 1)
        self.assertNotEqual(inspected_heads[0], concurrent_heads[0])
        self.assertEqual(self.head(), concurrent_heads[0])
        self.assertIn(self.remote_head(), {self.seed_commit, inspected_heads[0]})
        self.assertEqual(
            self.git("--git-dir", str(self.remote), "show", "refs/heads/main:README.md"),
            "Checkpoint test repository.",
        )

    def test_origin_change_after_validation_cannot_redirect_publication(self) -> None:
        self.write_note()
        redirected_remote = self.directory / "redirected.git"
        self.git("clone", "--bare", str(self.remote), str(redirected_remote), cwd=self.directory)
        module = self.checkpoint_module()
        original_git = module.git
        changed = False

        def change_origin_after_validation(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
            nonlocal changed
            result = original_git(root, *args, check=check)
            if args and args[0] == "symbolic-ref" and not changed:
                self.git("remote", "set-url", "origin", str(redirected_remote))
                changed = True
            return result

        with mock.patch.dict(os.environ, self.env, clear=True):
            with mock.patch.object(module, "git", change_origin_after_validation):
                result = module.checkpoint(self.repo, "Publish to the validated repository")

        self.assertTrue(changed)
        self.assertIs(result.get("synced"), True)
        self.assertEqual(result.get("commit"), self.head())
        self.assertNotEqual(self.head(), self.seed_commit)
        self.assertEqual(self.remote_head(), self.head())
        self.assertEqual(
            self.git("--git-dir", str(redirected_remote), "rev-parse", "refs/heads/main"),
            self.seed_commit,
        )

    def test_unrelated_unstaged_work_is_not_committed(self) -> None:
        self.write_note()
        readme = self.repo / "README.md"
        private_work = "Unrelated work stays local.\n"
        readme.write_text(private_work, encoding="utf-8")

        self.assert_synced(self.checkpoint())

        self.assertEqual(readme.read_text(encoding="utf-8"), private_work)
        self.assertEqual(self.git("show", "HEAD:README.md"), "Checkpoint test repository.")
        self.assertEqual(self.git("diff", "--name-only"), "README.md")

    def test_unrelated_staged_work_is_rejected_and_index_preserved(self) -> None:
        self.write_note()
        (self.repo / "README.md").write_text("Already staged unrelated change.\n", encoding="utf-8")
        self.git("add", "README.md")
        index_before = self.git("write-tree")

        self.assert_blocked_without_commits()

        self.assertEqual(self.git("write-tree"), index_before)
        self.assertEqual(self.git("diff", "--cached", "--name-only"), "README.md")
        self.assertTrue((self.repo / "research/lemma.md").is_file())

    def test_empty_state_is_rejected(self) -> None:
        self.write_note()
        (self.repo / "research/STATE.md").write_text(" \n\t", encoding="utf-8")

        self.assert_blocked_without_commits()

    def test_disabled_configuration_is_rejected(self) -> None:
        self.write_note()
        self.config["enabled"] = False
        self.write_config()

        self.assert_blocked_without_commits()

    def test_expected_remote_mismatch_is_rejected(self) -> None:
        self.write_note()
        other_remote = self.directory / "other.git"
        self.git("init", "--bare", "--initial-branch=main", str(other_remote), cwd=self.directory)
        self.config["expectedRemote"] = str(other_remote)
        self.write_config()

        self.assert_blocked_without_commits()

    def test_symlink_in_research_is_rejected(self) -> None:
        outside = self.directory / "outside-note.md"
        outside.write_text("Do not follow a link outside the research tree.\n", encoding="utf-8")
        (self.repo / "research/linked.md").symlink_to(outside)

        self.assert_blocked_without_commits()

        self.assertEqual(outside.read_text(encoding="utf-8"), "Do not follow a link outside the research tree.\n")

    def test_private_key_material_is_rejected(self) -> None:
        self.write_note("private-note.md", "-----BEGIN PRIVATE KEY-----\nFAKE_TEST_ONLY\n-----END PRIVATE KEY-----\n")

        self.assert_blocked_without_commits()

    def test_api_secret_pattern_is_rejected(self) -> None:
        self.write_note("secret-note.md", "Synthetic test token: sk-proj-" + "a" * 64 + "\n")

        self.assert_blocked_without_commits()

    def test_unsupported_file_is_rejected(self) -> None:
        (self.repo / "research/result.bin").write_bytes(b"\x00\x01\x02\xff")

        self.assert_blocked_without_commits()

    def test_research_deletion_is_rejected(self) -> None:
        note = self.write_note("prior-result.md")
        self.git("add", "research/prior-result.md")
        self.git("commit", "-m", "Preserve a previous result")
        self.git("push", "origin", "main")
        note.unlink()

        self.assert_blocked_without_commits()

    def test_unpushed_nonresearch_commit_is_not_published(self) -> None:
        (self.repo / "README.md").write_text("A local unrelated commit must remain local.\n", encoding="utf-8")
        self.git("add", "README.md")
        self.git("commit", "-m", "Local unrelated work")
        local_commit = self.head()
        self.write_note()

        result = self.checkpoint()

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.git("merge-base", "--is-ancestor", local_commit, "HEAD")
        self.assertEqual(self.git("rev-list", "--min-parents=2", local_commit + "..HEAD"), "")
        self.assertEqual(self.remote_head(), self.seed_commit)

    def test_secret_removed_from_pending_history_still_blocks_publication(self) -> None:
        token = "sk-proj-" + "b" * 64
        note = self.write_note("history.md", "Synthetic secret fixture: " + token + "\n")
        self.git("add", "research/history.md")
        self.git("commit", "-m", "Record a local research revision")
        note.write_text("The current revision contains no secret fixture.\n", encoding="utf-8")
        self.git("add", "research/history.md")
        self.git("commit", "-m", "Revise the local research note")

        result = self.assert_blocked_without_commits()

        self.assertEqual(self.remote_head(), self.seed_commit)
        self.assertNotIn(token, result.stdout + result.stderr)

    def test_push_failure_preserves_local_research_commit(self) -> None:
        self.write_note()
        hook = self.remote / "hooks/pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
        hook.chmod(0o755)

        result = self.checkpoint()

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertNotEqual(self.head(), self.seed_commit)
        self.assertEqual(self.remote_head(), self.seed_commit)
        self.assertEqual(self.git("show", "HEAD:research/lemma.md"), (self.repo / "research/lemma.md").read_text(encoding="utf-8").strip())
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.assertEqual(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"), "research/lemma.md")

    def test_retry_after_push_rejection_publishes_the_same_commit(self) -> None:
        self.write_note()
        hook = self.remote / "hooks/pre-receive"
        hook.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
        hook.chmod(0o755)

        rejected = self.checkpoint()

        self.assertNotEqual(rejected.returncode, 0, rejected.stdout)
        retained_commit = self.head()
        self.assertNotEqual(retained_commit, self.seed_commit)
        self.assertEqual(self.remote_head(), self.seed_commit)
        hook.unlink()

        self.assert_synced(self.checkpoint("Retry publication of the saved checkpoint"))

        self.assertEqual(self.head(), retained_commit)
        self.assertEqual(self.remote_head(), retained_commit)
        self.assertEqual(self.git("rev-list", "--count", self.seed_commit + "..HEAD"), "1")

    def test_successful_research_session_automatically_checkpoints(self) -> None:
        result = self.fake_research_session(0)

        self.assert_synced(result)

        self.assertNotEqual(self.head(), self.seed_commit)
        self.assertEqual(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"), "research/session.md")
        self.assertEqual(self.git("show", "HEAD:research/session.md"), (self.repo / "research/session.md").read_text(encoding="utf-8").strip())
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_failed_research_session_keeps_records_local_without_checkpointing(self) -> None:
        result = self.fake_research_session(7)

        self.assertEqual(result.returncode, 7, result.stderr)
        self.assertEqual(self.head(), self.seed_commit)
        self.assertEqual(self.remote_head(), self.seed_commit)
        self.assertTrue((self.repo / "research/session.md").is_file())
        self.assertEqual(self.git("ls-files", "--others", "--exclude-standard"), "research/session.md")

    def test_divergence_neither_forces_remote_nor_merges(self) -> None:
        self.write_note("local.md")
        self.git("add", "research/local.md")
        self.git("commit", "-m", "Local research branch")
        local_commit = self.head()
        peer = self.directory / "peer"
        self.git("clone", str(self.remote), str(peer), cwd=self.directory)
        self.configure_author(peer)
        (peer / "research/peer.md").write_text("Independent remote research.\n", encoding="utf-8")
        self.git("add", "research/peer.md", cwd=peer)
        self.git("commit", "-m", "Remote research branch", cwd=peer)
        self.git("push", "origin", "main", cwd=peer)
        remote_commit = self.remote_head()
        self.write_note("pending.md")

        result = self.checkpoint()

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.remote_head(), remote_commit)
        self.git("merge-base", "--is-ancestor", local_commit, "HEAD")
        self.assertEqual(self.git("rev-list", "--min-parents=2", local_commit + "..HEAD"), "")

    def test_shared_fcntl_lock_prevents_commit_or_push_while_held(self) -> None:
        self.write_note()
        lock = self.repo / ".git/mathforge-checkpoint.lock"
        with lock.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            process = subprocess.Popen(
                [sys.executable, str(CHECKPOINT), "-C", str(self.repo), "Locked checkpoint"],
                cwd=self.repo, env=self.env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            )
            completed_while_locked = False
            try:
                try:
                    stdout, stderr = process.communicate(timeout=2)
                    completed_while_locked = True
                except subprocess.TimeoutExpired:
                    pass
                self.assertEqual(self.head(), self.seed_commit)
                self.assertEqual(self.remote_head(), self.seed_commit)
                if completed_while_locked:
                    self.assertNotEqual(process.returncode, 0, stdout)
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
                if not completed_while_locked:
                    try:
                        stdout, stderr = process.communicate(timeout=15)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.communicate()
                        self.fail("Checkpoint did not finish after the shared lock was released")
            if not completed_while_locked and process.returncode == 0:
                self.assert_synced(subprocess.CompletedProcess(process.args, process.returncode, stdout, stderr))


if __name__ == "__main__":
    unittest.main(verbosity=2)
