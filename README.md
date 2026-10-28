# mafs

Mathforge is a research skill and proposed agent system for Birch and Swinnerton Dyer over the rational numbers.

The repository currently contains a working interactive Codex launcher, research instructions, solution criteria, an architecture for six authenticated accounts, candidate evaluations and a synthetic HUD. The persistent coordinator, live HUD, account enrollment and trusted mathematics services are not implemented.

## Start locally

Requirements: Git, Python 3.10 or later, and an installed Codex CLI. Use ChatGPT sign in when working through a subscription. The check command does not inspect authentication or billing.

```bash
git clone https://github.com/sk-k-os/mafs.git
cd mafs
./bin/mathforge --check
codex login status
```

If signed out, run `codex login` and complete native ChatGPT sign in. Existing credentials remain under Codex's control. [Official authentication documentation](https://learn.chatgpt.com/docs/auth)

Start one supervised assignment:

```bash
./bin/mathforge research 'Read the proposed BSD target. Complete one source backed theorem applicability audit. Preserve exact hypotheses, distinguish numerical evidence from proof, and identify one useful next test. Save the dossier under research/bsd-intake. Stop after delivering it.'
```

The terminal remains interactive. This command does not start a service or a long research allocation. The `research/` directory is ignored by Git so generated work is not accidentally published.

The repository skill lives in `.agents/skills/mathforge`. Inside Codex, select it with `/skills` or mention `$mathforge`. `./bin/mathforge` selects this checkout's copy explicitly, even when a global installation also exists. [Official skill discovery documentation](https://learn.chatgpt.com/docs/build-skills)

## Read the design

1. [Six account architecture](.agents/skills/mathforge/references/six-account-architecture.md).
2. [Mathematical target](.agents/skills/mathforge/references/research-target.md) and [solution contract](.agents/skills/mathforge/references/solution-contract.md).
3. [Verification and agent lifecycle](.agents/skills/mathforge/references/verification-and-lifecycle.md).
4. [Runtime implementation manual](.agents/skills/mathforge/references/build-manual.md).
5. [HUD specification](.agents/skills/mathforge/hud-spec.md) and [preview source](.agents/skills/mathforge/hud.html).
6. [Validation evidence and limits](.agents/skills/mathforge/validation.md).

`./bin/mathforge hud` prints the local preview path for manual opening. The preview contains synthetic data. Browser rendering and interaction checks are outstanding.

## Six account rollout

The first implementation milestone is one authenticated worker completing a bounded assignment through the durable coordinator, with evidence in the live HUD and successful restart recovery. After qualification, enroll the remaining accounts individually, validate isolation and usage controls, then run a bounded calibration before sustained research.

The broker is ordinary software. Every model call, including planners, evaluators and summaries, counts toward the proposed six active slots. Account changes preserve budgets, contribution history and review conflicts. Mathematical agreement is not proof.

The public account plan is an unconfigured template. Keep identities, credentials, prices, usage observations and operator decisions outside version control. No source file grants execution or spending authority. No mathematical tools are bundled; their environments must be selected and qualified during implementation.

## Validate

```bash
python3 .agents/skills/mathforge/scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

Tests use a fake Codex executable and do not call models. GitHub Actions runs these package checks. The 80 mathematical, lifecycle and account cases are proposed specifications, not executed benchmark results.

After an intentional change to the skill package, refresh its content manifest and rerun validation:

```bash
python3 scripts/update_manifest.py
```

The embedded Montserrat fonts retain their [SIL Open Font License](.agents/skills/mathforge/assets/Montserrat-LICENSE.txt).
