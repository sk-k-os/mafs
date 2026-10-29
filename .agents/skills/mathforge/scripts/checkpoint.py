#!/usr/bin/env python3
"""Commit research records and verify their push to the configured origin branch."""
from __future__ import annotations

import argparse
import fcntl
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit


class SyncError(Exception):
    pass


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    try:
        result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SyncError("Git unavailable or timed out; local records are retained.") from error
    if check and result.returncode:
        # Git diagnostics may contain a credential-bearing URL. Do not echo them.
        raise SyncError(f"Git {args[0]} failed; local records are retained. Check Git status and connectivity.")
    return result


def output(root: Path, *args: str) -> str:
    return git(root, *args).stdout.decode("utf-8").strip()


def names(data: bytes) -> list[str]:
    return [item.decode("utf-8") for item in data.split(b"\0") if item]


def remote_identity(value: str) -> str:
    value = value.rstrip("/")
    if value.startswith("git@github.com:"):
        value = "https://github.com/" + value.split(":", 1)[1]
    if value.startswith("https://"):
        parsed = urlsplit(value)
        if parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise SyncError("Credential-bearing or parameterized remote URLs are not supported.")
        return value.removesuffix(".git")
    if Path(value).is_absolute():
        return str(Path(value).resolve())
    raise SyncError("Use an HTTPS origin, GitHub SSH origin, or an absolute local test remote.")


ALLOWED_EXTENSIONS = {".md", ".txt", ".json", ".csv", ".tsv", ".py", ".sage", ".lean",
                      ".toml", ".yaml", ".yml", ".bib", ".tex", ".svg", ".ipynb"}
PRIVATE_PARTS = {"private", "raw", "cache", "accounts", "credentials", "secrets"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?im)\b(?:OPENAI_API_KEY|GITHUB_TOKEN|GH_TOKEN|access_token|refresh_token)\s*[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9_./+-]{12,}"),
]


def scan_text(data: bytes, label: str) -> None:
    if len(data) > 5 * 1024 * 1024:
        raise SyncError(f"Artifact too large for research checkpoint: {label}. Store a reference and hash instead.")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise SyncError(f"Only UTF-8 research artifacts are supported: {label}") from error
    if "\0" in text or any(pattern.search(text) for pattern in SECRET_PATTERNS):
        raise SyncError(f"Potential credential or binary content blocked in {label}; nothing was pushed.")


def check_path(path: str) -> None:
    parts = Path(path).parts
    if not parts or parts[0] != "research" or len(parts) < 2:
        raise SyncError("A pending commit includes content outside research/; publish code separately first.")
    if any(part.startswith(".") or part.lower() in PRIVATE_PARTS for part in parts[1:]):
        raise SyncError(f"Private research path cannot be published: {path}")
    if Path(path).name.lower() in {"auth.json", "credentials.json", "secrets.json"}:
        raise SyncError(f"Credential filename blocked: {path}")
    if Path(path).suffix.lower() not in ALLOWED_EXTENSIONS or any(char in path for char in "\n\r\t"):
        raise SyncError(f"Unsupported research artifact path: {path}")


def scan_index(root: Path) -> None:
    for entry in git(root, "ls-files", "--stage", "-z", "--", "research").stdout.split(b"\0"):
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        mode, oid, stage = metadata.decode().split()
        path = raw_path.decode()
        check_path(path)
        if mode not in {"100644", "100755"} or stage != "0":
            raise SyncError(f"Symlink, submodule or unresolved artifact blocked: {path}")
        scan_text(git(root, "cat-file", "blob", oid).stdout, path)
    state = git(root, "show", ":research/STATE.md", check=False)
    if state.returncode or not state.stdout.strip():
        raise SyncError("A nonempty research/STATE.md is required for a recoverable checkpoint.")


def inspect_pending_history(root: Path, remote_head: str, head: str) -> None:
    if git(root, "merge-base", "--is-ancestor", remote_head, head, check=False).returncode:
        raise SyncError("Origin has new or divergent work. Local checkpoint retained; reconcile explicitly before retrying.")
    for commit in output(root, "rev-list", "--reverse", f"{remote_head}..{head}").splitlines():
        if len(output(root, "rev-list", "--parents", "-n", "1", commit).split()) > 2:
            raise SyncError("An unpublished merge requires explicit review before a research checkpoint push.")
        scan_text(git(root, "show", "-s", "--format=%B", commit).stdout, "commit message")
        changed = names(git(root, "diff-tree", "--root", "--no-commit-id", "--name-only", "--no-renames", "-r", "-z", commit).stdout)
        for path in changed:
            check_path(path)
        deleted = git(root, "diff-tree", "--root", "--no-commit-id", "--name-only", "--no-renames", "--diff-filter=D", "-r", "-z", commit).stdout
        if deleted:
            raise SyncError("Research deletions are not published by checkpoints. Retain records and add corrections.")
        for entry in git(root, "ls-tree", "-r", "-z", commit, "--", "research").stdout.split(b"\0"):
            if not entry:
                continue
            metadata, raw_path = entry.split(b"\t", 1)
            mode, kind, oid = metadata.decode().split()
            path = raw_path.decode()
            check_path(path)
            if mode not in {"100644", "100755"} or kind != "blob":
                raise SyncError(f"Nonregular research artifact in pending history: {path}")
            scan_text(git(root, "cat-file", "blob", oid).stdout, path)


def checkpoint(root: Path, message: str) -> dict[str, object]:
    config_path = root / "research-sync.json"
    if not config_path.is_file() or config_path.is_symlink():
        raise SyncError("This workspace has no research sync configuration.")
    config = json.loads(config_path.read_text())
    if config.get("version") != 1 or config.get("enabled") is not True or config.get("remote") != "origin" or config.get("scope") != "research/":
        raise SyncError("Research sync is disabled or its configuration is unsupported.")
    expected = remote_identity(config["expectedRemote"])
    bound_urls: list[str] = []
    for args in [("remote", "get-url", "--all", "origin"), ("remote", "get-url", "--push", "--all", "origin")]:
        urls = output(root, *args).splitlines()
        if len(urls) != 1 or remote_identity(urls[0]) != expected:
            raise SyncError("Origin does not match the configured research repository; nothing was pushed.")
        bound_urls.append(urls[0])
    fetch_url, push_url = bound_urls
    branch = output(root, "symbolic-ref", "--quiet", "--short", "HEAD")
    for state in ["MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply"]:
        path = Path(output(root, "rev-parse", "--git-path", state))
        if not path.is_absolute():
            path = root / path
        if path.exists():
            raise SyncError("Finish the current Git merge, rebase or replay before checkpointing.")
    if git(root, "ls-files", "--unmerged").stdout:
        raise SyncError("Unresolved Git conflicts block checkpointing.")
    staged = names(git(root, "diff", "--cached", "--name-only", "--no-renames", "-z").stdout)
    if any(not path.startswith("research/") for path in staged):
        raise SyncError("Unrelated staged files are present. Keep code commits separate from research checkpoints.")
    if (root / "research").is_symlink() or not (root / "research").is_dir():
        raise SyncError("research/ must be a real directory.")
    if any(path.is_symlink() for path in (root / "research").rglob("*")):
        raise SyncError("Symlinks are not allowed in research checkpoints.")
    scan_text(message.encode(), "checkpoint message")
    if len(message) > 240 or "\n" in message or "\r" in message:
        raise SyncError("Use a single concise checkpoint message of at most 240 characters.")
    git(root, "add", "--all", "--", "research")
    if git(root, "diff", "--cached", "--name-only", "--no-renames", "--diff-filter=D", "-z", "--", "research").stdout:
        raise SyncError("Research deletions are blocked. Retain the record and document its correction or rejection.")
    scan_index(root)
    # A failed network operation leaves this local commit available for retry.
    if git(root, "diff", "--cached", "--quiet", check=False).returncode:
        git(root, "commit", "-m", message)
    head = output(root, "rev-parse", "HEAD")
    remote_refs = output(root, "ls-remote", "--heads", fetch_url, f"refs/heads/{branch}").split()
    if len(remote_refs) != 2:
        raise SyncError("The current branch must already exist in origin before research checkpointing.")
    remote_head = remote_refs[0]
    git(root, "fetch", "--no-tags", "--no-write-fetch-head", fetch_url, f"refs/heads/{branch}")
    inspect_pending_history(root, remote_head, head)
    if remote_head != head:
        git(root, "push", "--no-follow-tags", push_url, f"{head}:refs/heads/{branch}")
    observed = output(root, "ls-remote", "--heads", push_url, f"refs/heads/{branch}").split()
    if not observed or observed[0] != head:
        raise SyncError("Remote checkpoint could not be confirmed; local records are retained.")
    if output(root, "rev-parse", "HEAD") != head or output(root, "symbolic-ref", "--quiet", "--short", "HEAD") != branch:
        raise SyncError("The inspected checkpoint was pushed, but local HEAD or branch changed during sync. Reconcile before retrying.")
    if git(root, "status", "--porcelain", "--untracked-files=all", "--", "research").stdout:
        raise SyncError("The committed checkpoint was pushed, but research files changed during sync. Run another checkpoint.")
    return {"synced": True, "commit": head, "branch": branch, "remote": "origin", "scope": "research/"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-C", "--directory", default=str(Path.cwd()))
    parser.add_argument("message", nargs="?", default="Save research checkpoint")
    args = parser.parse_args()
    try:
        root = Path(output(Path(args.directory).resolve(), "rev-parse", "--show-toplevel"))
        common = Path(output(root, "rev-parse", "--git-common-dir"))
        if not common.is_absolute():
            common = root / common
        with (common / "mathforge-checkpoint.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                raise SyncError("Another local checkpoint owns the Git writer lock. Retry after it finishes.") from error
            result = checkpoint(root, args.message)
        print(json.dumps(result, indent=2))
        return 0
    except (SyncError, OSError, ValueError, KeyError) as error:
        print(json.dumps({"synced": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
