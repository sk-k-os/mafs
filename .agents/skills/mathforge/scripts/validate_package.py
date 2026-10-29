#!/usr/bin/env python3
"""Validate package structure only; this is not a mathematical verifier."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import re
import sys


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    skill = (root / "SKILL.md").read_text()
    if not skill.startswith("---\nname: mathforge\ndescription: "):
        failures.append("Missing expected skill frontmatter")
    if not (root / "scripts/mathforge").stat().st_mode & 0o111:
        failures.append("Terminal launcher must retain executable permissions")
    for document in root.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            location = target.split("#", 1)[0]
            if not (document.parent / location).exists():
                failures.append(str(document.relative_to(root)) + ": missing link " + target)
    for script in list((root / "scripts").glob("*.py")) + [root / "scripts/mathforge"]:
        ast.parse(script.read_text(), filename=str(script))
    for artifact in root.rglob("*.json"):
        json.loads(artifact.read_text())
    graph = json.loads((root / "workflow.json").read_text())
    node_ids = [node["id"] for node in graph["nodes"]]
    if len(set(node_ids)) != len(node_ids):
        failures.append("Duplicate workflow node")
    for edge in graph["edges"]:
        if edge["from"] not in node_ids or edge["to"] not in node_ids or not edge.get("when"):
            failures.append("Invalid workflow edge: " + str(edge))
    for join in graph["joins"]:
        references = [join["at"]] + join["required"] + list(join.get("conditionalRequired", {}))
        if any(ref not in node_ids for ref in references):
            failures.append("Invalid workflow join: " + join["id"])
    policy = json.loads((root / "campaign-policy.json").read_text())
    if policy["status"] != "proposedNotEnforced" or policy["longDurationAllocationActive"]:
        failures.append("Package must not imply an active runtime allocation")
    accounts = json.loads((root / "account-plan.json").read_text())
    slot_ids = [slot["id"] for slot in accounts["slots"]]
    if slot_ids != [f"{index:02}" for index in range(1, 7)]:
        failures.append("Expected six uniquely identified account slots")
    if accounts["reportedMonthlyTotal"] is not None and (any(slot["reportedMonthlyPrice"] is None for slot in accounts["slots"]) or sum(slot["reportedMonthlyPrice"] for slot in accounts["slots"]) != accounts["reportedMonthlyTotal"]):
        failures.append("Reported subscription arithmetic is inconsistent")
    if policy["maximumActiveModelSessions"] != accounts["maximumConcurrentModelTurns"]:
        failures.append("Concurrency policies disagree")
    if accounts["accountsConnected"] != 0 or any(slot["connectionStatus"] != "notConnected" for slot in accounts["slots"]):
        failures.append("Design package must not imply connected accounts")
    if policy["runtimeImplementationAuthorized"] or policy["providerFundingBoundaryVerified"]:
        failures.append("Design package must preserve pending runtime and funding qualification")
    if accounts["billingVerified"] or any(slot["priceVerified"] for slot in accounts["slots"]):
        failures.append("Reported prices have not been verified")
    cases = json.loads((root / "evals/acceptanceCases.json").read_text())["cases"]
    if len({case["id"] for case in cases}) != len(cases):
        failures.append("Duplicate benchmark case")
    if any(case["labelStatus"] != "candidateSpecification" for case in cases):
        failures.append("No benchmark labels have been adjudicated in this package")
    manifest = json.loads((root / "manifest.json").read_text())
    recorded: set[str] = set()
    for entry in manifest["files"]:
        relative = entry["path"]
        target = (root / relative).resolve()
        if relative in recorded or not target.is_relative_to(root.resolve()):
            failures.append("Invalid or duplicate manifest path: " + relative)
            continue
        recorded.add(relative)
        if not target.is_file():
            failures.append("Missing manifest artifact: " + relative)
            continue
        data = target.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"] or len(data) != entry["bytes"]:
            failures.append("Manifest mismatch: " + relative)
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*")
              if path.is_file() and path.name != "manifest.json"
              and not path.name.startswith(".") and "__pycache__" not in path.parts
              and path.suffix != ".pyc"}
    if actual != recorded:
        failures.append("Manifest does not match package file inventory")
    return failures


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    failures = validate(root)
    print(json.dumps({"scope": "packageStructureOnly", "passed": not failures, "failures": failures}, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
