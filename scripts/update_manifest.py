#!/usr/bin/env python3
"""Refresh the repository skill manifest after intentional package changes."""
from pathlib import Path
import hashlib
import json


def main() -> None:
    root = Path(__file__).resolve().parents[1] / ".agents/skills/mathforge"
    files = [path for path in sorted(root.rglob("*")) if path.is_file()
             and path.name != "manifest.json" and not path.name.startswith(".")
             and "__pycache__" not in path.parts and path.suffix != ".pyc"]
    manifest = {
        "package": "mathforge", "version": "3", "scope": "skillAndDesignOnly",
        "runtimeActive": False, "accountsConnected": 0,
        "files": [{"path": path.relative_to(root).as_posix(),
                   "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                   "bytes": path.stat().st_size} for path in files],
    }
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Updated {len(files)} package file records")


if __name__ == "__main__":
    main()
