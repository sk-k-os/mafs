# Exploration: use the reducible representation as an input

Access date October 29, 2026. Coordinator candidate source comparison for separate review. This small allocation explores a different mechanism, not a novelty claim. The pilot is B over Q with coefficients `[0,-1,1,-10,-20]`; twists are indexed by nonzero squarefree integers d.

## Inspected primary sources

Castella, Grossi and Skinner, *Mazur's main conjecture at Eisenstein primes*, final arXiv version 2, October 15, 2025, [record](https://arxiv.org/abs/2303.04373v2), [PDF](https://arxiv.org/pdf/2303.04373v2). Theorem A, printed page 2, assumes an elliptic curve over Q, odd prime p of good reduction, a rational p isogeny and a kernel character whose restriction at p is neither the trivial nor the mod p cyclotomic character. Theorem D, pages 4 and 5, adds analytic rank zero or one and gives the p valuation of the BSD formula. Remark 1.2.1, page 5, explicitly treats the exact pilot equation and quadratic characters with value negative one at 5. The paper is published in Mathematische Annalen; the pinned source inspected here is the final arXiv text. PDF SHA256 `5046d7571ed3a1b13baa56b2c94186d9c9488d76181062f4ba82b8ab5158af90`.

Keller and Yin, *On the anticyclotomic Iwasawa theory of newforms at Eisenstein primes of semistable reduction*, [arXiv version 2](https://arxiv.org/abs/2402.12781v2), October 30, 2024, [PDF](https://arxiv.org/pdf/2402.12781v2). Theorem 4.2.1, printed page 42 in this version, states the p part of BSD for elliptic curves over Q with good reduction at an odd p, reducible E[p], and analytic rank zero or one. It removes the above local character restriction and explicitly retains the rational torsion denominator. This is recorded as a preprint theorem statement, not a newly reconstructed proof or independently validated result. PDF SHA256 `bb64820b49aa1eb2574c912c0d03067f904e52b9bf71f441fda78bb6dba9c90a`. An author mirror has different pagination; do not transfer its page 41 locator to the pinned arXiv version.

The full relevant statements and nearby hypotheses were inspected. Their complete proofs were not audited. Source downloads stay in ignored scratch. Broad searches also returned unvetted claims of full BSD; their search summaries were not adopted as established mathematics. The university thesis page was blocked by a JavaScript challenge; the accessible primary papers supplied the actual statements.

## Mathematical bridge and falsifier

Run 001 proves that B has a rational point of order 5. On B twisted by d, its stable line carries the quadratic character chi_d. Thus reducibility is an exclusion for the earlier JSW theorem at 5 but is the required Eisenstein input in these papers. If 5 does not divide d and chi_d(5) is negative one, this character at 5 is unramified and nontrivial; it is neither the trivial character nor the ramified mod 5 cyclotomic character. Good reduction at 5 persists under the unramified twist. This verifies the additional local hypothesis of the published theorem, without changing prime.

The discriminating test is this exact local character filter. For d=13, the residue is 3 modulo 5, a nonsquare, and the twist retains good reduction at 5. The filter passes. For d=1 the character is trivial and this particular theorem's local restriction fails. For d=5 the twist has discriminant valuation 6 and c4 valuation 2 at 5: the first is below 12, so the displayed local integral model is minimal and has additive reduction. Thus good reduction fails. These are falsifiers of applicability, not counterexamples to BSD. The broader preprint statement changes the local restriction and must be labeled separately.

The [finite check](../experiments/run-003-exploration/check.py), [output](../experiments/run-003-exploration/output.json) and [receipt](../experiments/run-003-exploration/receipt.json) use exact integer arithmetic. The integral short model is `Y²=X³-27*c4*d²*X-54*c6*d³`, with `c4=496,c6=20008`. It is related to B by a rational change of variables with scale 6, a unit at 5. Its nonzero discriminant modulo 5 certifies good reduction for the tested twists. No analytic rank is computed.

## Remaining obligation and decision impact

For any chosen twist, exact analytic order zero or one is still needed for either stated BSD corollary. The resulting conclusion concerns the 5 part; it does not establish every prime part or any rank two formula. A future application must preserve the period, regulator and torsion conventions, especially in the preprint statement. The cheap local test changes which theorem is promising but does not remove the analytic bottleneck.

This mechanism is established literature, not an unusual analogy presented as a theorem. It prevents an overbroad conclusion that the pilot is unusable at 5. It is a useful alternative within the comparison; no new branch is launched automatically.
