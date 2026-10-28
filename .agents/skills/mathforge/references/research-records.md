# Research records

A research campaign needs durable evidence and a concise entry point for the next agent. In a workspace configured for Git checkpoints, read `research/README.md` for the record layout and `research/STATE.md` for the current target, verified results, unresolved obligations and next assignment. The repository's root instructions and current human authorization determine what may be published.

For each finding, preserve its exact statement, quantifiers, assumptions, input revisions, source locations, evidence, status, objections and next discriminating test. Keep numerical observations separate from exact results. Save experiment code with inputs and tool versions. Store rejected routes and why they failed. Preserve scientific direction as concise decisions with provenance; do not copy private conversations into a public repository.

Before handoff, record what actually happened, what remains unknown, artifacts to inspect, blocked dependencies and a bounded next step. Update the current state. A replacement agent checks the cited artifacts and their revisions before continuing. A context summary cannot replace a proof, source or execution receipt.

Run the workspace launcher:

```bash
./bin/mathforge checkpoint 'Record findings and successor context'
```

The helper reads `research-sync.json`, stages only `research/`, requires a nonempty state record and checks pending history before publishing. It binds the destination to the configured origin, pins the inspected commit and verifies the remote branch after pushing. It rejects unrelated staged files, pending code commits, unpublished merges, research deletions, symlinks, unsupported artifacts and common credential patterns. It does not force a push, merge, rebase or publish tags. The current branch must already exist remotely.

Records must be UTF8 text in supported formats and no larger than 5 MiB each. For large artifacts, retain a durable authorized location, content hash and reproduction instructions. Local paths alone do not back up external evidence. Sensitive account records, raw transcripts and credentials stay outside tracked research. Pattern checks cannot detect all sensitive content.

The JSON response reports `synced: true` only after remote verification. If publication fails, the local records and any checkpoint commit remain available. Diagnose the cause, reconcile divergence explicitly and retry. Repeated successful checkpoints with unchanged records do not create duplicate commits. Report missing remote persistence honestly.

The launcher automatically attempts this operation after successful research, review and resume sessions when a sync policy exists. Milestone checkpoints are still needed during long sessions. Interrupted or unsuccessful sessions do not automatically publish. Direct Codex sessions follow the same record instructions but must call the checkpoint command themselves. This is not a background backup daemon.

Use one Git writer per shared checkout. The helper lock serializes other helper invocations; it cannot block ordinary Git commands. A detected concurrent change requires reconciliation. Mathematical acceptance remains governed by the solution and verification contracts, independent of Git publication.
