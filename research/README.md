# Public research record

Read [STATE.md](STATE.md) first, then the latest session linked there. This directory preserves useful findings, failed approaches, evidence and enough context to resume work. It is public. Keep credentials, account identities, private operator details, private paths and raw conversations outside it.

## What to record

| Location | Required content |
| :--- | :--- |
| `findings/<id>.md` | Exact claim and hypotheses; target obligation; status and assumptions; argument or evidence links; unresolved objections; negative results; next discriminating test. |
| `experiments/<id>/` | Reproducible code and inputs, tool versions and configuration, random seed when relevant, finite search scope, precision or certified bounds, output and a receipt identifying what actually ran. Remove secrets from public receipts without changing the mathematical result. |
| `sources/<id>.md` | Source title, stable citation link, version or access date, exact theorem or page locator, relevant hypotheses and a concise applicability note. Link to papers; do not upload bulk copyrighted papers. |
| `reviews/<id>.md` | Reviewed claim revision, method, precise objections with locators, verdict and remaining obligations. Preserve the first review before adding a dated correction. |
| `sessions/<date>-<id>.md` | Bounded objective, inputs, decisions, actual work, accepted or rejected outcomes, unknowns and the next assignment. Record public decision summaries rather than raw chat. |
| `STATE.md` | Current target, supported results, active obstruction, implementation state, open decisions and next actions. Link to the detailed records. |

Create a directory only when it has an actual record. Use stable IDs and relative links. A summary points to evidence; it does not replace a proof, computation receipt or source statement.

Label speculation, numerical evidence, conditional results and mathematical arguments explicitly. Record review and formal checking separately. A failed proof attempt does not disprove its conclusion. A finite experiment does not establish a universal theorem. Retain failed routes and explain what would justify revisiting them. Apply the [verification policy](../.agents/skills/mathforge/references/verification-and-lifecycle.md) and [solution contract](../.agents/skills/mathforge/references/solution-contract.md) before promoting any mathematical claim.

## Checkpoint and publish

From the repository root:

```bash
./bin/mathforge checkpoint 'Record bounded research milestone'
```

The helper stages only `research/`, rejects deletions, symlinks and detected secrets, commits the eligible changes and pushes the current branch to `origin`. Secret checks are a backstop; review the public content before checkpointing. Keep private material outside this directory from the start. Code changes require their own normal review workflow.

The launcher attempts a checkpoint after a successful `research`, `review` or `resume` CLI exit. Checkpoint explicitly at meaningful milestones and before replacing a worker or handing off a branch. Save the exact claim, evidence references, failed routes, unresolved objections and next test before transfer.

A failed push leaves the local work and commit available and returns a nonzero status. Inspect the error and retry the checkpoint after resolving it; do not report remote publication from a local commit alone. A retry must preserve existing history. Correct an inaccurate record with a dated amendment rather than deleting it through the checkpoint helper.

A checkpoint does not merge a pull request into `main`, accept a proof, launch a timer or create a cloud service. Git records what was submitted; mathematical status changes require the evidence and review specified above.
