# Validation record

Public repository baseline. The package is a skill and design specification with an interactive launcher.

## Available reproducible checks

From the repository root:

```bash
python3 .agents/skills/mathforge/scripts/validate_package.py
python3 -m unittest discover -s tests -v
./bin/mathforge --check
```

The package validator checks local links, syntax, workflow identities, executable permissions, disconnected template state and manifest integrity. Launcher behavior tests use a fake Codex executable and make no model requests. The actual CLI check queries its version, not authentication, quota or model access.

The TypeScript design contracts have also been checked with strict mode and no emit during preparation. That check establishes type consistency only; runtime adapters and permission enforcement are not implemented.

Repository preparation passed eight launcher and artifact integrity tests, the skill frontmatter validator, strict TypeScript contract compilation and static HUD syntax checks. The repository launcher also passed a local version and file check. No model or account operation was used for these checks.

## Inherited design evidence

The original package had an independent design review and one illustrative written rejection of an invalid BSD proof. Those are design observations, not protected benchmark results. Public migration does not turn them into executed mathematical tests.

Local CLI help and generated protocol types were inspected without login, inference or credential inspection. See [account transport evidence](references/account-transport-evidence.md). Regenerate and qualify the selected CLI schema before building a live adapter; the generated inspection workspace is not shipped.

The 42 mathematical and lifecycle cases plus 38 account integrity cases are public candidate specifications. No complete fixture set, adjudicated hidden suite, model accuracy score or productivity measurement has been produced.

## Unverified capabilities

No persistent coordinator, six account connection, mathematics sandbox, trusted proof gateway, billing control or live HUD has been implemented. No mathematical computation or BSD proof was produced by these package checks. Lean, Lake, Sage and PARI were unavailable on the originally inspected PATH; capability discovery is machine specific.

The HUD is a synthetic local preview. Static syntax and fixture checks do not establish browser rendering, responsive layout or interactions. Browser verification remains outstanding.
