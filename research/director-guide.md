# Working with the Mathforge research team

Recorded October 29, 2026. The operator is the human scientific director. The coordinator turns direction into finite assignments, shares evidence among specialists, arranges separate review, and preserves the research record.

The currently available mode is an interactive Codex session with specialist agents within its actual host limit. The six account broker, live HUD, protected benchmark service and formal verification service are still design proposals. A session prompt does not supply durable scheduling or enforced resource accounting.

## The research conversation

Give the coordinator an objective, a time limit and a desired output. At each meaningful decision, ask for the exact question, strongest evidence, unresolved step, competing next moves and recommendation. Choose the next experiment by what it could teach us about a named BSD obligation.

Useful messages to enter directly in the active MAFS Codex session:

| Purpose | Message |
| :--- | :--- |
| Understand progress | Explain the strongest supported result, the exact remaining obstruction, the evidence that could change your view, and the next decision you need from me. Link the records. |
| Contribute an idea | My idea is: [idea]. Preserve it as a research suggestion, translate it into a precise hypothesis, identify the missing bridge to BSD, and propose the cheapest test and a possible falsifier. |
| Select a branch | Pursue [named route] for one 30 minute supervised assignment. Name the precise obligation and expected output. Share findings, obtain separate review, checkpoint, and stop with the next decision. |
| Challenge a result | Give a fresh referee the exact claim, proof and sources before showing other reviewers' verdicts. Find the weakest inference and either justify it or record a concrete objection. Share the completed review with the team. |
| Change direction | Explain what failed and which new premise or test would justify revisiting it. Preserve that record, then compare two alternatives with different mechanisms. |
| Save | Run `./bin/mathforge checkpoint 'Save research progress and next steps'` and verify the returned synced status. |
| Replace an agent | Check whether the problem is context loss, source access, a failed approach or measured errors. Preserve the handoff, validate the successor's understanding, and keep unresolved objections visible. |
| Save and stop | Stop new assignments. Reconcile active workers, save findings and open obligations, update research/STATE.md, checkpoint to GitHub, verify synced is true, and then stop. |

A save and stop message is a coordination request processed by the active session. It is not a guaranteed immediate termination mechanism.

Creative ideas are welcome. Their value is whether they suggest a new structure, a useful obstruction or a discriminating test. Intuition generates candidates; explicit arguments and evidence determine what can be used in a proof. Catching a mistake is shared progress. Slow progress on a hard question alone is not evidence that an agent should be replaced.

## Resume and inspect

Continue in the existing terminal while its session is open. If that session has ended, run this from the repository root:

```bash
./bin/mathforge --check
./bin/mathforge resume 'Read research/STATE.md and research/director-guide.md. Continue the next ready assignment for one supervised run of at most 30 minutes. Use collaborating specialists within the host limit, preserve independent review, checkpoint the records, and stop with a focused director decision.'
```

Inside Codex, invoke the skill with `$mathforge` or select it through `/skills`. The launcher does not register a custom `/mathforge` command.

Read [STATE.md](STATE.md) for the current scientific state. Follow its links to exact claims, sources, experiments, reviews and the latest handoff. The terminal displays live work. The packaged HUD is a synthetic preview and does not display this team's activity.

Only one coordinator owns Git writes. It runs `./bin/mathforge checkpoint 'Research milestone'` at meaningful milestones and completion. A successful checkpoint reports `synced: true` and the confirmed commit. Keep credentials, account details and raw conversations outside public research records.

## Completion standard

The selected positive target covers every elliptic curve over the rational numbers: rank equality, finiteness of Sha, and the full leading coefficient formula. A result for one curve, a restricted family or one prime retains that limited scope.

The [solution contract](../.agents/skills/mathforge/references/solution-contract.md) requires an exact proof bundle, closed dependencies, resolved objections, reproducible computational ingredients and independent qualified human mathematical review before final acceptance. Formal coverage is reported separately. The director chooses research priorities; agent agreement or a direction decision cannot certify a proof.
