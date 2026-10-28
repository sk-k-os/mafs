# What counts as a solution

Revision 1. Target selected by the director on October 28, 2026. The acceptance policy below is a proposed specification. It has not been implemented or satisfied.

## Exact mathematical target

Use the full Birch and Swinnerton Dyer conjecture for every elliptic curve over Q as the program's conservative completion target. The official rank assertion and the stronger leading coefficient assertion must remain separate named obligations. Choosing full BSD prevents the system from silently reporting success after a restricted or weaker result. [Official problem description](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf)

For every nonsingular elliptic curve E over Q, with the standard rational point group, standard Hasse Weil L function and standard arithmetic invariants:

1. The order of vanishing of L(E,s) at s = 1 equals rank E(Q).
2. The Tate Shafarevich group Sha(E/Q) is finite.
3. Writing their common rank as r, the leading coefficient satisfies

\[
\frac{L^{(r)}(E,1)}{r!}
=\frac{\Omega_E\operatorname{Reg}(E/\mathbb Q)\#\Sha(E/\mathbb Q)\prod_p c_p}
{\#E(\mathbb Q)_{\mathrm{tors}}^2}.
\]

The statement ledger freezes the real period convention, height and regulator conventions, local Tamagawa factors, torsion denominator, analytic continuation, and curve model transformations. All curves and all relevant primes are covered; CM, reduction types, torsion, rank, and other special cases cannot be quietly excluded.

An accepted proof of rank equality alone would be a major resolution of that named obligation. It would be reported exactly as such, while the stronger Mathforge target remains incomplete. A finite list of curves, a family of twists, a prime part of the formula, a density result, or a theorem conditional on another open conjecture is a scoped mathematical result. None closes the full target.

## Evidence required

The solution bundle contains the frozen target and definitions; a complete mathematical manuscript; every newly needed lemma and its proof; a dependency manifest for established results; exact theorem citations and hypothesis witnesses; all computational certificates and their mathematical bridges; all formal source and pinned dependencies where formal verification is claimed; independent referee reports; every objection and its disposition; and a reproducibility manifest of hashes and tool versions.

Known mathematics can be used. The requirement is an auditable proof dependency closure with no hidden conjectural premise, no circular appeal to BSD, no assumed finiteness where it must be proved, and no unproved generalization. Standard logical foundations remain explicit. A proof conditional on a custom axiom expressing BSD is not a proof of BSD.

Formal checking concerns the exact formal statement. Independent statement review must establish that its definitions and quantifiers express the intended BSD target. There must be no redefinition making analytic rank equal to algebraic rank by construction, no impossible hypothesis, and no empty class of curves.

## Observable states

| State | Required evidence | What the system may say |
| :--- | :--- | :--- |
| Research active | Valid assignment and actual runtime receipt | Research is active on this named obligation |
| Candidate complete | A submitted manuscript claims every positive target obligation, or presents an exact counterexample and complete argument refuting a named obligation; structural completeness audit passes for that resolution type | A complete candidate resolution has been submitted; correctness is unestablished |
| Internally verified | All required automated checks have actual current receipts; independent internal reviews have no unresolved material objection; assumption and scope audit passes | The candidate passed the recorded internal verification profile |
| Independently validated | At least two qualified human mathematicians external to the proposing agent team reconstruct the full argument, confirm the stated positive proof or counterexample scope, and close material objections against the exact bundle; one has relevant BSD expertise | External human mathematical review supports the recorded resolution and its precise scope |
| Solution accepted | Independently validated bundle; current reproducibility checks; no hidden conditional premise; all checks for the declared positive proof or disproof pass; the director records acceptance of the evidence and verification profile | Solution accepted under this explicit evidence standard; proved or disproved is displayed with exact scope |
| Externally recognized | A named journal, community body, or Clay makes its actual recorded decision | Recognized by that named body; state the precise recognition |

These are research program states, not a metaphysical guarantee that no error can exist. A rigorous mathematical proof is the substantive requirement. Formal tools, expert scrutiny and reproducibility address different ways an apparent proof can fail.

The director's acceptance acknowledges the evidence and closes the program's goal. It cannot turn a failed mathematical check into a pass. The program must not label a work item solved merely because the director, a referee, or a model clicks accept.

## Two assurance profiles

**Formal complete profile:** the complete intended positive theorem or exact refutation statement and all new proof dependencies are checked under the approved foundations, with a trusted immutable challenge, current replay receipts, and external human review of mathematical meaning. Existing imported formal mathematics is pinned and included in the dependency audit. No required theorem, definition, bridge or computation remains only an unchecked assumption. The external human review requirement for independent validation applies to this profile as well.

**Expert proof profile:** a complete conventional mathematical proof or counterexample argument is reconstructed by at least two qualified human mathematicians external to the proposing agent team, including one with appropriate BSD expertise, with authenticated written reports, every material objection resolved, and any computational ingredient certified for its exact role. Formal coverage may be partial and must be displayed as such. Reviewer identity, independence, conflicts, and shared proof sources are recorded. Agent referee outputs cannot satisfy these human review slots. This is conventional mathematical validation, not a claim of full machine verification.

The profile must be selected before final acceptance. If the formal profile is selected and its requirements cannot be met, remain incomplete. Switching to the expert profile requires an explicit recorded decision and displays the change in assurance; it cannot be used silently to clear a failed formal check. A mathematical defect blocks both profiles. Missing formal library support alone is an implementation limitation and must not be confused with a mathematical disproof.

The proposed default is the formal complete profile as an engineering objective, with independent mathematical review still required. A serious conventional proof should be assessed immediately rather than discarded while formalization remains unfinished. The director can select the expert proof profile explicitly after seeing its complete evidence and limitations.

## Disproof and partial resolution

Discovery must not assume the conjecture is true. A proposed counterexample requires an exact object satisfying the original hypotheses and a rigorous failure of a named target assertion. A simulation anomaly, timeout, or failed proof search is not a counterexample.

Record proved and disproved as distinct resolution types. Disproving a stronger formula does not by itself disprove rank equality; retain each obligation's status. A validated counterexample can resolve the full conjunction negatively while leaving the other component questions open. It must receive the same level of scrutiny as a positive proof.

The acceptance engine must branch on resolution type. A positive proof requires all three universal obligations. A disproof requires an exact witness, proof that it satisfies the original hypotheses, and rigorous refutation of a specifically identified obligation. It must preserve the unresolved or independently known status of every unaffected component. The positive requirement to prove all three assertions cannot be imposed on a valid disproof, and a disproof cannot be labeled a positive proof.

## State transition rules

All receipts bind to exact artifact hashes, target revision, verification profile, and dependency closure. A changed definition, proof, critical dependency, checker or material review invalidates affected receipts. The trusted controller returns the result to under review and preserves earlier history. Missing checks, unavailable checkers, timeouts, stale evidence, or unresolved objections never count as passed.

Models can submit candidates and recommendations. The trusted verifier issues check receipts. The evidence steward commits accepted ledger transitions only when the policy service validates those receipts and any required human decision. The author cannot promote its own work or edit the target, checks or reviewer assignments.

External recognition is recorded separately from proof validation. Do not predict a prize, invent peer review, or automatically submit a manuscript. Any application to Clay follows its current actual rules, checked at the time, with explicit publication and communication authorization.

## How the teams talk with the director

The operator serves as human research director. Ask him when his judgment can change the research: competing mechanisms deserve prioritization; a pattern changes the current picture; a branch cannot produce a new discriminating test; an unexpected connection suggests new definitions; a meaningful resource allocation changes; or a final solution packet is ready.

As a proposed conversation trigger, after two completed exploration rounds produce no new test or meaningful change in the obstruction map, prepare a direction discussion. This is a coordination heuristic, not a productivity verdict. Ask sooner when a specific idea needs human judgment. Do not interrupt merely to narrate activity or request approval for routine steps already within scope.

The discussion packet presents the exact question, the current obstruction in plain language, what was tried, the strongest evidence, two or three possible next moves, and the team's recommendation. Leave room for the director to introduce an entirely different perspective. Capture his original response, the interpretation, new hypotheses, and the first tests separately.

A conversation can generate several experimental branches without treating an inspired suggestion as a theorem. Continue independent authorized work while a direction question is pending. Hold only assignments that require the unanswered decision. Never infer acceptance from silence.
