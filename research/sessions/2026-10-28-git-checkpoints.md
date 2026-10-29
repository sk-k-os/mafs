# Research persistence setup

Date: October 28, 2026. Scope: preserve findings and useful research context in the designated GitHub repository. This was software implementation and verification, not a mathematical research run.

## Decision and implementation

The human director requested that findings and context be pushed to `sk-k-os/mafs`. The authorized public record now includes findings, exact assumptions, source locators, experiments, failed approaches, objections, scientific decisions and successor context. Private account data, credentials and raw conversations remain outside the public record.

Implementation commit `f0211b4` adds a Git checkpoint helper and a tracked research directory. The current state is the resume entry point. The interactive launcher attempts a checkpoint after successful research, review and resume sessions. Agents are instructed to checkpoint meaningful milestones and handoffs explicitly. The terminal launcher on the setup machine now selects this repository; the older personal skill package remains intact separately.

The helper checks research artifacts and pending history, pushes the inspected commit to the configured repository's current branch and verifies the remote commit. Failed publication preserves the local checkpoint. It refuses divergent history and unrelated staged work, and does not force pushes or publish tags. Git publication does not certify a claim or merge the open foundation pull request into `main`.

## Verification evidence

Ran `python3 -m unittest discover -s tests -v`: 30 tests passed, including 22 research persistence integration tests. Fixtures use local bare Git repositories and a fake Codex executable; no model request was made. Tests exercise push rejection and exact commit retry, deletion and secret rejection, unpublished historical secrets, concurrent writer behavior and automatic session completion checkpoints.

Independent code review identified three publication defects during development: mutable HEAD could bypass inspection, Git configuration could add tags, and mutable origin configuration could redirect a push. Each was corrected before this record. Regression tests exercise all three, and a second inspection found no additional substantive blocker. This is bounded review evidence, not a guarantee against every possible defect.

Package structure and manifest validation passed. The skill frontmatter validator passed using an isolated local Python environment with its YAML dependency. The actual launcher passed its file and CLI version check. These checks do not authenticate accounts or measure model competence. The real repository checkpoint command is used to publish this record; the command's returned commit and remote verification are the publication receipt, rather than an assertion embedded before the push.

## Limits and next assignment

No mathematical finding, counterexample, research computation or formal proof receipt was produced. No persistent research service was started. Automatic persistence occurs at checkpoints; it cannot recover context that was never written to disk. Interrupted or unsuccessful interactive sessions need an explicit checkpoint. One coordinator should own Git writes in a shared checkout.

Resume from [STATE.md](../STATE.md). The next scientific assignment remains one bounded source applicability audit with exact hypotheses and a discriminating next test. The next runtime milestone remains one durable worker assignment with live evidence and restart recovery before expansion to six slots. Record actual research only when performed, and preserve its mathematical status separately from publication status.
