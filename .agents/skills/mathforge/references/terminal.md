# Terminal use

From the repository root, use the checkout's launcher:

```bash
./bin/mathforge --check
./bin/mathforge design
./bin/mathforge research 'Complete one source backed theorem applicability audit for the BSD pilot'
./bin/mathforge review 'Review a specific candidate against its exact statement'
./bin/mathforge resume
./bin/mathforge checkpoint 'Preserve findings and next steps'
./bin/mathforge hud
```

Inside Codex CLI, select Mathforge with `/skills` or use `$mathforge`. Repository skills are discovered from `.agents/skills`. A custom `/mathforge` slash command is not registered. [Official skills documentation](https://learn.chatgpt.com/docs/build-skills)

`bin/mathforge` resolves to `.agents/skills/mathforge/scripts/mathforge`. It reads this checkout's skill directly, even if a user also has an older global Mathforge installation. It preserves model, authentication, sandbox and approval settings. An explicit invalid `MATHFORGE_CODEX` path fails instead of selecting another executable.

Python 3.10 or later and Codex CLI are prerequisites for interactive sessions. The checkpoint helper uses Git and Python on macOS or Linux without invoking Codex. `--check` inspects files, executable paths, CLI version and the presence of a sync policy only. It does not authenticate an account or measure mathematical competence, billing or capacity. `--print-launch` displays the command as data without starting a model or publishing records.

Use `-C /absolute/path/to/workspace` before the mode to select another existing workspace. Task text is passed as one process argument and is never evaluated as shell code.

When this package lives in a repository with `research-sync.json`, its launcher defaults to that repository even when invoked from another directory. Otherwise it defaults to the current directory. A successful research, review or resume session automatically attempts a Git checkpoint if the selected workspace has a sync policy. Design sessions do not automatically publish. Read [research records](research-records.md) for milestone checkpoints, recovery and publication boundaries.

The HUD command prints a path for manual inspection. The preview is synthetic. Browser rendering and interactions have not been qualified.

The optional `scripts/install.py` installs a copy and global `mathforge` command for a user without an existing installation. It deliberately refuses to replace an existing skill or command. Repository use does not require running the installer.

The six account transport is a proposed implementation. There is no `mathforge accounts login`, `mathforge swarm`, background coordinator or live HUD service. Six terminal windows do not establish distinct account identities. Installation and invocation do not start an unattended research campaign.
