# Run 001 separate mathematical review

Date: October 28, 2026. Reviewer: a separate model process assigned to reconstruct the submitted arguments. No other review conclusion was supplied. Shared inputs, sources, mathematical conventions, model lineage and the filesystem remain common dependencies. The researcher and source worker shared useful evidence during the review.

**Verdict:** Claims A and B are supported under the stated standard elliptic curve facts. The 40 finite count rows pass the separate exact replay. The source audit correctly identifies a conditional application of JSW Theorem 1.2.1 to the control at 5. Its analytic rank premise remains open in this dossier. No material defect in the final submitted representation argument was found.

This verdict is a model reconstruction and an acceptance recommendation at that assurance level. It is not formal verification, qualified external human review, a trusted service attestation, a novelty judgment or an accepted BSD solution. No current domain benchmark qualification or automated acceptance service was supplied. Authors cannot use this record to certify their own claims.

## Evidence revision

The [replay receipt](run-001-replay.json) binds every reviewed local artifact by its actual SHA256, including the original author receipt. The decisive revisions are:

| Artifact | SHA256 |
| :--- | :--- |
| [Submitted finding](../findings/run-001-representation-obstruction.md) | `cfef65411425b63a59c51a782090241fa8e7a8f1c3b6688fcd75cbfcbfd86f3b` |
| [JSW source audit](../sources/run-001-jsw-audit.md) | `4561bf87427c86859a925043460a0866e389ec8afa8ad8fa3da7ef06e4f46366` |
| [Representation sources](../sources/run-001-representation-bridges.md) | `3407e24dfac88fe0173643d3eb41c5b3b1e57f762a128e44b44d394db4a4ca3d` |
| [Submitted finite output](../experiments/run-001-local-counts/output.json) | `dc6176361b30139372d6cd25fc5b8f5c49ed9908e56973d58cea3ad528beff2f` |
| [Separate replay script](run-001-replay.py) | `ef7b3d93dc45f61a341271fad19bdd327c9204633e2078dfc6bffde5f1ea22ef` |
| [Separate replay receipt](run-001-replay.json) | `ce2cdcdfec56e4777035a92c4f0a5d976184ba95f908ee7c9a8ae3d9e6adce37` |

A minor source locator error was identified in the initial submission: the Sutherland definition of irreducibility occurs on printed page 5, Section 25.4; pages 3 and 4 contain the Frobenius conventions and identities. The coordinator corrected that locator before the final finding was frozen and hashed. The original and reviewed descriptions must not be presented as identical revisions. No mathematical inference depended on the locator error.

## Reconstruction of Claim A

The curve C is identified by coefficients `[0,0,1,-1,0]` over Q. The independently recomputed discriminant is 37, so reduction at 3 is good and 3 differs from the torsion prime 5. Directly in F3, every x has x³ − x = 0, and precisely y = 0, 2 solve y² + y = 0. Thus there are seven projective points and a3 = −3.

The arithmetic Frobenius convention and its trace and determinant were checked in the actual [Sutherland lecture PDF](https://math.mit.edu/classes/18.783/2025/LectureNotes25.pdf), Section 25.3, printed pages 3 and 4. Its polynomial on C[5] is T² + 3T + 3 modulo 5. Its discriminant is 2, outside the square set {0,1,4}. Equivalently, direct evaluation at all five field elements gives no zero.

If a one dimensional F5 subspace were invariant under the entire Galois group, Frobenius would act on that line by an F5 scalar. That scalar would be a root of the characteristic polynomial, a contradiction. This establishes precisely irreducibility over F5. Surjectivity of the Galois image is not established or required. The inverse Frobenius convention gives the same invariant subspaces and would not change the conclusion.

## Reconstruction of Claim B

The curve B is identified by coefficients `[0,-1,1,-10,-20]`. Substitution verifies P = (5,5). The tangent y = 5x − 20 intersects B with x polynomial

\[
(x-5)^2(x-16).
\]

Reflecting the third intersection by (x,y) ↦ (x,−y−1) gives 2P = (16,−61). The secant y = −6x + 35 has intersection polynomial

\[
(x-5)(x-16)^2.
\]

Reflection gives 3P = (16,60) = −2P. Hence 5P = O, and P is nonzero of exact order 5. The separate rational arithmetic checker additionally returns 4P = (5,−6), then O.

The short model twist map in the submission is correctly directed from the twist to the base curve. For every nonzero rational d it is an isomorphism over Q(√d); conjugating √d changes it by negation. Transporting Galois action therefore multiplies the matrices by the quadratic character χd. Multiplying matrices by nonzero scalars preserves invariant subspaces. The rational line spanned by P thus supplies an invariant line on every quadratic twist. The square class case has trivial character and is included.

The publisher's full relevant passage confirms this representation identity in [Cremona and Freitas, Lemma 2.2(2), equation (2.5), printed page 8](https://ems.press/content/serial-article-files/38965). The scalar identity has no irreducibility requirement. The invariant line is not asserted to have a rational generator after twisting.

Claim B is a universal statement proved by this descent argument. The finite computation is used for the base torsion point; no finite enumeration of d is being promoted to the universal conclusion.

## Exact replay and local hypotheses

The [review script](run-001-replay.py) was written separately and did not import or execute the author's script. It enumerates projective points by normalizing the first nonzero coordinate. It derives c4, c6 and Δ through a rational short model obtained by completing the square and removing the quadratic term. It checks all submitted count and singular rows, the invariant identity, the Frobenius witness list and exact rational multiples of P. It preserves the author's files and checks their hashes before and after execution.

All 40 good prime count rows, for the three frozen coefficient vectors and primes at most 43, agree. The excluded singular primes are 11 for B and 37 for C. Their rational singular point sets agree after changing projective normalization. Absence of rational singular points is not used as a substitute for geometric smoothness. The discriminant criterion supplies that bridge. The first witness is 3; all eight recorded witness primes agree. These are exact finite results with the Python runtime and elementary formulas in the trust boundary.

For C, Δ = 37 and c4 = 48. For B, Δ = −11⁵ and c4 = 496. At the only possible bad primes the discriminant valuations are 1 and 5. A smaller integral discriminant would differ by a positive multiple of 12 in valuation, which is impossible. Thus the models are minimal. The c4 values are units at 37 and 11 respectively, giving multiplicative reduction there; elsewhere reduction is good. Both bases are semistable and have good reduction at 5. The local criteria and discriminant transformation were checked in [Milne, Chapter II, Theorem 2.4 and Section 3, printed pages 52 and 59 to 61](https://www.jmilne.org/math/Books/EC2.pdf).

This does not assert that every quadratic twist is semistable. For example, the twist of B by 13 has discriminant valuation 6 and c4 valuation 2 at 13; its local integral model is minimal and has additive reduction. The universal irreducibility obstruction does not need semistability of the twists. A future application at another prime must still check semistability and the other hypotheses for its exact twist.

## Theorem applicability and conventions

The published [JSW PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2017/0005/0003/CJM-2017-0005-0003-a002.pdf), printed pages 370 and 371, was inspected directly. Theorem 1.2.1 must be read with its preceding hypotheses: a semistable curve over Q, analytic order exactly one, good reduction at the prime, and irreducible residual representation. At 5 it does not add ordinarity, nonanomalous reduction, Tamagawa coprimality or the residual ramification restriction discussed for earlier results.

The source audit correctly fixes the period as the integral over all real components, uses the Néron differential and the regulator of a basis of the free Mordell Weil group, and takes the theorem's product over finite primes. Irreducibility excludes rational 5 torsion, so the torsion denominator has zero 5 valuation. The conclusion is an equality of 5 valuations. Rank equality and Sha finiteness are separate analytic rank one consequences cited in the paper. No full proof of the cited deep theorems was reconstructed in this review.

Consequently the control meets the algebraic eligibility conditions. Applying the theorem remains conditional on a proof that its analytic order is exactly one. Claim B excludes this theorem at 5 for the entire pilot twist family, regardless of their analytic ranks. It excludes neither BSD for those curves nor every alternative theorem or prime.

## Transparent calibration probes

These three inferences were supplied openly during review. They are checks of specific reasoning errors, not a hidden benchmark or a general performance estimate.

1. **A finite point search finds no nontorsion rational point, therefore algebraic rank is zero. Rejected.** A bounded search excludes only the searched region. A nontorsion generator may have greater height or denominator. Without an exhaustive height theorem, a certified descent bound or another rank upper bound, rank zero does not follow.

2. **A finite precision L value rounds to zero, therefore analytic rank is at least one. Rejected.** Rounding permits a nonzero value smaller than the rounding threshold. Even a certified interval containing zero does not prove exact vanishing. One needs an exact vanishing argument, such as a correctly identified odd functional equation, or an equivalent exact certificate.

3. **B has rational 5 torsion, therefore every quadratic twist has a rational point of order 5. Rejected.** A stable line may carry a nontrivial character rather than trivial action. There is also an explicit counterexample: set t = 2y + 1 on B and form its twist by d = −1,

   \[
   -t^2=4x^3-4x^2-40x-79.
   \]

   It has good reduction at 3. Over F3 its only affine points are (x,t) = (0,1), (0,2); with infinity its group has order 3. The replay confirms this enumeration. Reduction is injective on rational torsion of order prime to 3, so this twist cannot have a rational point of order 5. The reduction fact is also covered by [Milne, Chapter II, Corollary 5.7](https://www.jmilne.org/math/Books/EC2.pdf). This does not contradict the invariant line proved in Claim B.

## Open obligations and handoff

The locator correction is resolved in the hashed finding. No remaining repair is required to the exact statements of Claims A and B. The source audit is available now; the finding's request that it freeze the theorem is fulfilled by the linked audit.

Before an unconditional application to C, supply either a rigorously sourced exact analytic rank theorem for these coefficients or both an exact central vanishing certificate and a certified nonzero enclosure for L′(C,1). The latter route must retain the modular identification, truncation error and rounding control. A database rank label or an approximate derivative is insufficient. Calculation of an exact Sha order or the full coefficient formula would require additional evidence beyond the present valuation theorem.

The replay ran on CPython 3.9.6 at 21:01:00 UTC and measured 0.010810208 seconds of its own execution. Total review time, token use and monetary cost were not instrumented and are unknown. No formal mathematics tool or qualified external human reviewer was used. No Git mutation or checkpoint was performed by this reviewer; the coordinator owns reconciliation and publication. Changing a hashed dependency requires renewed review of the affected inference.
