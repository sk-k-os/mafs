#!/usr/bin/env python3
"""Install this package without replacing an existing skill or command."""
from pathlib import Path
import os
import shutil
import sys


def main() -> int:
    source = Path(__file__).resolve().parent.parent
    codex_root = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser().resolve()
    destination = codex_root / "skills" / "mathforge"
    command = Path.home() / ".local" / "bin" / "mathforge"
    if destination.exists() or destination.is_symlink() or command.exists() or command.is_symlink():
        print("Existing skill or command found. Inspect it before updating; nothing was changed.", file=sys.stderr)
        return 2
    required = ["SKILL.md", "scripts/mathforge", "references/architecture.md", "references/verification-and-lifecycle.md", "hud.html"]
    if any(not (source / name).is_file() for name in required):
        print("Source package is incomplete.", file=sys.stderr)
        return 2
    destination.parent.mkdir(parents=True, exist_ok=True)
    command.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    launcher = destination / "scripts" / "mathforge"
    launcher.chmod(0o755)
    command.symlink_to(launcher)
    print("Installed skill: " + str(destination))
    print("Installed command: " + str(command))
    print("No model call, service, schedule, or research campaign was started.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
