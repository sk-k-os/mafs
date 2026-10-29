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

## Standing director relay rule

Added October 29, 2026 after Run 003 closed, at Sean's explicit instruction. This is an administrative communication update, not a new assignment or an extension of Run 003.

Relay every question, decision request, required action and material blocker intended for Sean. Keep a concise director packet under `research/` with a stable identifier for each question, its open or answered status, the exact decision needed, and the recorded answer when supplied. Distinguish recommendations from Sean's decisions. Preserve previous questions and answers rather than silently replacing them. The coordinator surfaces urgent blockers promptly in terminal commentary and includes outstanding director items in the final handoff. Do not assume that a record update alone means Sean has seen it.

Sean reports that the desktop chat has a five minute director relay reading this session and these research records. This is operator supplied context, not a locally verified delivery service or permission for the team to create another scheduler or send external correspondence. The terminal and concise packet remain the team's relay surfaces.

All workers share the same scientific objective. They must promptly share useful sources, findings, objections, failed approaches and corrections, including evidence that changes another worker's assumptions. A separate skeptical referee remains essential. Give that referee exact claims and evidence before other reviewers' conclusions; record shared sources and model lineage. Agreement is not proof.

The desktop is investigating reported hook failures. Do not disable hooks, alter permissions or infer that no hook error occurred merely because none appears in the model context. If an actual hook error becomes visible, record its event name, exact error text and effect on the task, omitting private payloads. If the event name or error is unavailable, mark it unknown rather than inventing it. Clearly distinguish a hook failure from a CLI environment warning or a sandbox denial.

Visibility correction: the Run 003 final reply said, “No hook failure occurred.” That was too broad. No hook error was visible in the coordinator's available tool results or model context. This does not establish whether Sean saw hook errors elsewhere. No exact hook event or error payload is available to this coordinator as of this amendment.

Operational relay amendment after Run 004: surface every Git approval wait immediately as an action needed from Sean. State the exact checkpoint action and why approval is required; distinguish publication waiting from scientific work. Do not use a wait as permission to extend an assignment or start another one. If terminal compatibility errors continue and are actually visible, report the exact event and error without private payloads, then request a normal session restart after a verified checkpoint. Do not bypass hook trust or change security policy.

The [public operations summary](sessions/2026-10-29-operations-update.md) records the desktop's reported version 15.5.0 service repair and its limits. Healthy complete capture and repair of historical gaps remain unverified; use versioned evidence and verified checkpoints for mathematical continuity.
