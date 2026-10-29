# Runtime implementation manual

Status: proposed next implementation slice. The skill package and HUD design exist. The service described below does not.

Revision 3 preserves the six subscription design as a portable repository baseline. Read [six account architecture](six-account-architecture.md) and [transport evidence](account-transport-evidence.md) before implementing account connections. No implementation slice is activated by this manual.

## Fixed starting paths

Package root relative to the repository: `.agents/skills/mathforge`.

Proposed runtime root relative to the repository: `runtime`. Resolve both against the absolute checkout path before implementation.

Use `contracts.ts`, `workflow.json`, `account-plan.json`, and `campaign-policy.json` in the package root as the reviewed design inputs. Before implementation, record the exact accepted revisions and a single runtime source of truth for each schema. The more detailed lifecycle records in the reference are proposed extensions, not a competing live schema. Account records in contracts.ts are normalized design interfaces; generated provider protocol types remain a separate pinned dependency.

## Slice 1: operator screen

Build a React 19 and TypeScript app with Vite and the user's Tailwind conventions. Use Montserrat from the current preview assets. The standalone hud.html is a visual design reference, not a production application. Keep fixture data explicitly labeled and isolated from live mode.

Create these files under the proposed runtime root:

```text
src/contracts/records.ts
src/features/hud/ResearchHud.tsx
src/features/hud/ClaimGraph.tsx
src/features/hud/RunTimeline.tsx
src/features/hud/CallInspector.tsx
src/features/hud/AgentLineage.tsx
src/features/hud/EvaluationView.tsx
src/features/hud/HumanReview.tsx
src/features/hud/AccountCapacity.tsx
src/features/hud/AccountReadiness.tsx
src/features/hud/hudAdapter.ts
src/features/hud/types.ts
src/fixtures/researchPreview.ts
```

Every claim view displays scope, assumptions, disposition, formal status, expert review and source references separately. Every worker view displays role, model binding, task difficulty, calibration evidence, resource use, and lineage. Unknown values remain null. Include missing payload, stale data, pending human input, invalidated dependencies and no active research states.

Define HudAdapter methods for snapshot, events after cursor, payload lookup, evaluations, and checkpoints. Keep mutation methods separate from read methods. A failed live request must not return fixtures. Store selected activation and attempt identity across updates.

Account cards show reported price separately from authenticated plan. Keep connection identity receipt, model, permission, usage timestamp, individual windows, pool relationship and hold reason distinct. Never add percentages across windows or accounts. Do not display private credential paths, emails or provider account identifiers in model accessible payloads. The six disconnected design records must never appear as live measurements.

Verify the screen at desktop and narrow widths, keyboard only navigation, graph and timeline selection, input and output tabs, exact source display, and stale telemetry. Do not claim a working pause button before its backend receipt is bound.

## Slice 2: durable coordinator

After the reviewed frontend slice, create these service owners:

```text
src/server/main.ts
src/server/store/eventStore.ts
src/server/store/artifactStore.ts
src/server/store/claimRegistry.ts
src/server/scheduler/queue.ts
src/server/scheduler/budgetController.ts
src/server/scheduler/leaseController.ts
src/server/scheduler/lifecycleController.ts
src/server/agents/definitionRegistry.ts
src/server/agents/contextAssembler.ts
src/server/adapters/modelAdapter.ts
src/server/adapters/codexAppServerAdapter.ts
src/server/accounts/accountRegistry.ts
src/server/accounts/accountEnrollment.ts
src/server/accounts/usageEligibility.ts
src/server/accounts/fundingBoundary.ts
src/server/accounts/poolRegistry.ts
src/server/broker/envelopeRouter.ts
src/server/broker/reviewVisibility.ts
src/server/adapters/sourceAdapter.ts
src/server/adapters/sandboxAdapter.ts
src/server/adapters/formalVerifier.ts
src/server/reviews/checkpointService.ts
src/server/hud/hudService.ts
migrations/001_initial.sql
migrations/001_verify.sql
migrations/002_accounts.sql
migrations/002_verify.sql
```

Use SQLite for the initial single operator service. Write actual schema migrations as explicit SQL files. Required entities are campaigns, assignments, attempts, agent definitions and instances, immutable artifact references, claim revisions, typed dependency edges, review receipts, verification receipts, resource reservations, checkpoints, benchmark runs, and ordered events. Fields use the canonical contracts and explicit constraints. Do not mark a mathematical claim accepted solely because a JSON document contains that value.

Transactions must atomically reserve budget and create a lease; consume checkpoint decisions once; commit accepted claim revisions with required receipt references; and invalidate affected dependents. One trusted writer owns accepted state. Candidate workers have no database credentials. Preserve append only event history and immutable artifacts; repair projections from the event log when required.

Bind the model adapter to six separately owned native Codex app server processes using stdio. Regenerate and pin protocol types from the selected CLI build, then implement initialization, managed login, account and usage reads, model discovery, thread and turn operations, cancellation and notifications against those exact types. Keep each child environment and private Codex home separate from the user's default home. Account identity and usage evidence must match the current connection generation. Do not infer support solely from examples in newer web documentation.

Require one current lease per slot, at most one active model turn per authenticated account and at most six globally. All model based judges, summaries and descendants pass through this same broker. Disable unaccounted delegation or reject its qualification. Encode protected identity uniqueness, active lease ownership, immutable attempt identity and event idempotency as database constraints where possible. Do not use a shared pool ID to identify an account or treat a metering bucket name as a pool key.

Local CLI help and generated schemas establish interface availability only. Live authentication, process isolation, usage behavior and billing boundaries still need actual qualification. Begin with mocked protocol transport and disposable canaries; then qualify one bounded included assignment with one account before six. Do not invoke a CLI with approval or sandbox bypass flags to make a test pass. Do not buy credits or alter billing to run a failure test.

Future account migrations must include protected account references, connection generations, slots, observations, pool relationships, leases, dispatch permits, review input manifests and usage attribution. Verification SQL must identify duplicate active account bindings, more than six active model turns, multiple current leases for a slot, permits without matching identity and funding receipts, and accepted claims with stale evidence. Test real transaction conflicts and crash recovery; design SQL has no enforcement effect until implemented.

A local service must bind to loopback, validate origin and session tokens, and separate operator access from worker access. A raw unauthenticated HTTP endpoint is not a private control plane merely because it is convenient.

## Slice 3: mathematics and trusted verification

Select the qualified computation environment before executing generated mathematics code. Build pinned images for Sage and the selected Lean toolchain. Verify artifact export, resource caps, cancellation and network restrictions. Keep proof generation and trusted checking in separate environments.

Create controls from the opening curve dossiers. Independently check small local invariants, record analytic estimates as numerical, and preserve unresolved global obligations. Add the exact Lean challenge, a valid proof, an imported omitted proof, an extra axiom, and a changed definition case. A verifier must distinguish all of them before its receipts can authorize promotion.

Add a gap audit for the selected mathlib revision. Missing theory becomes an explicit formalization task. Do not introduce axioms to make missing foundations disappear.

## Slice 4: evaluations and lifecycle

Convert evals/acceptanceCases.json into independently adjudicated fixtures. Freeze expected outcomes and suite versions before tuning. Keep protected tests outside worker access and run graders outside candidate code. Pin baseline and candidate revisions, model settings, sources, budgets, and repetitions.

Implement all 38 additional account and broker case specifications from [six account evaluation](six-account-evaluation.md). Preserve their candidate status until each has a concrete fixture, adjudicated outcome and actual run evidence. Scope later live tests to authorized included usage. Null usage permission, conflicting identity and unknown paid fallback are explicit unavailable states, not positive qualification results.

Implement role admission, reviewer calibration, probation, retirement, and successor admission. Initially require human review for changing the scientific branch or lifecycle thresholds. Routine replacement for a verified tool or context failure may follow an accepted standing policy. A child never receives a fresh budget independent of its parent.

If this becomes a Git repository with pull requests, create the trusted `mathforge-regression` CI check and require it through actual branch protection. A workflow YAML file alone does not establish enforcement. The repository includes package integrity and launcher CI. Mathematical regression CI and enforced merge protection are not configured by this baseline.

## Intended verification commands

The following are implementation acceptance interfaces to create, not commands available in the current package:

```bash
cd runtime
npm ci
npm run typecheck
npm run test:contracts
npm run test:recovery
npm run test:accounts
npm run test:broker
npm run test:funding
npm run test:review-visibility
npm run test:verification
npm run test:hud
npm run eval:calibration
```

Tests must establish behavior rather than match instruction wording. Directly attempt overspending through parallel dispatch, duplicate job submission, stale checkpoint replay, unauthorized promotion, mutation of accepted artifacts, benchmark answer access, forged checker output, canceled worker output, and indirect external instructions. Confirm expected denial at the actual trusted boundary.

Recovery tests terminate the coordinator during a running job, restart it, and establish that no accepted result is lost, no unknown job is blindly duplicated, and reservations are reconciled. HUD tests replay out of order and duplicate events, recover a disconnect, and preserve every lifecycle transition.

The final calibration evidence must include actual source revisions, image digests, toolchain versions, model bindings, run IDs, failed and passed cases, limitations, and real resource measurements. A synthetic HUD or passed type check cannot substitute for this evidence.

## Release boundary

The first live release conducts one bounded calibration assignment with trace inspection and a human review packet. Only after that evidence is accepted should the program expand to a research pilot. A 1,000 hour allocation needs explicit units, monetary ceiling, stop conditions, named operator, actual model access and recovery evidence. Never represent a design milestone as an active long duration campaign.
