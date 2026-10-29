# Run 002 separate referee report

Date: October 28, 2026. Verdict: accepted under the recorded standard theorem dependencies at the scope of separate model review. No unresolved material mathematical objection was found in the exact artifacts below. This verdict is an assessment of the submitted argument, not a trusted claim promotion, formal proof receipt, human expert endorsement or BSD solution claim.

## Exact reviewed claim

For C over Q with coefficients `[0,0,1,-1,0]`, and its Hasse Weil L function normalized with center one,

\[
L(C,1)=0,\qquad
\frac{73}{2240}<L'(C,1)<\frac{69}{80}.
\]

Consequently the analytic order at one is exactly one. The inequalities use strict rational endpoints and a proved bound for every omitted coefficient, rather than a numerical zero or database rank.

## Frozen revisions

| Artifact | SHA256 |
| :--- | :--- |
| [Argument revision 1](../findings/run-002-analytic-certificate.md) | `a30416e889e9f267e3dc673914720953ea12600e265f132e05eb690dc6ae7ea8` |
| [Analytic source dossier](../sources/run-002-analytic-sources.md) | `a4081f61449bbfac550e453cb66ae52b2d865905414bf2541888a5bf0138d36b` |
| [Local sign note](../sources/run-002-root-number.md) | `0d485e06df9f50c8e9f946ee985b52ac4fc1059d515e60cc47e0e9ecf59f0ee6` |
| [Inherited JSW audit](../sources/run-001-jsw-audit.md) | `4561bf87427c86859a925043460a0866e389ec8afa8ad8fa3da7ef06e4f46366` |
| [Inherited irreducibility argument](../findings/run-001-representation-obstruction.md) | `cfef65411425b63a59c51a782090241fa8e7a8f1c3b6688fcd75cbfcbfd86f3b` |
| [Author computation](../experiments/run-002-analytic/compute.py) | `37175eb7d136208fcdbdbb896e0943186753c23a814180cc3d1aa7dfe0ed6e02` |

The [referee execution receipt](../experiments/run-002-referee/receipt.json) binds these and the author output, author receipt and referee implementation to their exact hashes. Inputs were unchanged throughout replay. Any changed mathematical input needs renewed review.

## Mathematical checks

The invariant identities give c4 = 48, c6 = negative 216 and discriminant 37. Minimality follows from the discriminant valuations zero or one. The only bad prime is 37 and has multiplicative reduction, so the conductor is 37. Independent enumeration identifies the singular point `(5,18)` modulo 37; its tangent slopes require a square root of 15, which does not exist there. Counting nonsingular projective points independently gives a37 = negative one. This verifies nonsplit multiplicative reduction without a database. Rohrlich's Theorem 2(ii), including its displayed formula on printed page 329, agrees with the local sign note; Proposition 8(i) supplies good signs.

Wiles's Theorem 0.4 applies because C is semistable over Q. The referee inspected its statement in the retained source text, and inspected Milne's normalized newform definition and equivalence on page 208. These establish the exact curve and newform L function identification at conductor 37. Cremona's equation 2.6.1 on page 25 then gives Fricke eigenvalue positive one from a37 = negative one. Equation 2.8.6 on page 29 gives the opposite analytic sign. Its completion is holomorphic at one with a nonzero archimedean factor, so central vanishing is exact. This direct coefficient and Fricke route independently checks the sign convention used in the local root number route.

For the derivative, Proposition 2.13.1 on page 43 requires order at least one, already established. It does not assume exact order one. The referee also reconstructed the split Mellin calculation before reading the frozen proof. The factor two and the cancellation of `x=2π/√37` are correct. The bound `|a_n|≤d(n)√n≤2n` follows from Hasse and local reciprocal Euler factors, including multiples of 37. It supplies exponential domination uniformly near s = 1, justifying differentiation and integration term by term. The integration by parts boundary terms vanish. No analytic continuation, rank or BSD conjecture is being assumed.

The lower bound for E1 follows from the exact tangent line identity displayed in the argument; integration uses the zeroth and first exponential moments. The upper bound follows directly from the defining integral. The alternating integral bounds for π, the exponential series comparison and both strict bounds on x are valid. With a2 = negative two, the tail beginning at index three is bounded before the outer factor two by 9/160. The upper derivative bound correctly drops the negative second term. The final fractions are exactly 73/2240 and 69/80. Positivity and holomorphy prove simplicity of the zero.

## Independent finite replay

The [referee implementation](../experiments/run-002-referee/check.py) was written independently before inspection of the author program. It uses integer enumeration and exact rational arithmetic. Its initial π enclosure uses the different identity `π/4=atan(1/2)+atan(1/3)`. It separately checks the author's stated finite π and exponential comparisons, all final fractions, the local singularity, a2 and a37. It also recounts C over F3 and checks that `T²+3T+3` has no F5 root, supporting the inherited residual irreducibility witness.

The final run exited zero under Python 3.14.6. The [output](../experiments/run-002-referee/output.json) and [receipt](../experiments/run-002-referee/receipt.json) retain the actual execution duration, source hashes and environment. A replay of the author's recipe separately reproduced its saved output byte for byte. These executions check finite arithmetic; the analytic inequalities and published theorem applications received prose review rather than machine formalization.

## JSW consequence and exact boundary

The referee inspected the published JSW Theorem 1.2.1 and its preceding hypotheses on page 370. Semistability, good reduction at 5 and irreducibility of C[5] are established by the inherited witnesses. The reviewed analytic certificate supplies its previously missing premise. Therefore its stated prime part conclusion applies at p = 5:

\[
v_5\!\left(\frac{L'(C,1)}{\operatorname{Reg}(C/\mathbf Q)\,\Omega_C}\right)
=v_5\!\left(\#\Sha(C/\mathbf Q)\prod_{\ell\text{ finite}}c_\ell\right).
\]

Here Ω includes all real components, the regulator uses a basis of the free rational Mordell Weil group, and v5(5)=1. Irreducibility excludes rational 5 torsion, so no omitted torsion factor changes this valuation. The background analytic rank one theorem, stated immediately before JSW's theorem and attributed there to Gross, Zagier and Kolyvagin, also gives algebraic rank one and finite Sha. Its original proof closure was not reaudited in this run; it remains an established theorem dependency.

This is one curve and one prime valuation identity. The present enclosure computes neither the regulator nor the normalized derivative exactly, and supplies no numerical order of Sha, full rational leading coefficient identity or conclusion for all primes or curves. Those stronger claims would exceed the reviewed evidence.

## Objections, independence and handoff

The review actively checked potential circularity in the derivative formula, confusion between Fricke and analytic signs, omission of bad prime powers from the tail, and incorrect treatment of the negative second term in the upper bound. Each was resolved by the exact statements and calculations above. No correction to the frozen candidate is requested.

The referee saw no other run 002 verdict before completing this assessment. It shares the model family, mathematical literature, source downloads, tools, Python library and filesystem with the authors. The coordinator communicated proposed inequalities before freezing the proof; this is separate checking with an independent finite implementation, not fully isolated discovery or independent model lineage. Preparatory notes preserve that sequence and a corrected transcription error. No formal prover, trusted acceptance service or external human mathematician participated. Full proofs of the established source theorems were not reverified. Aggregate tokens and monetary cost are unknown; only the finite replay duration is measured in its receipt.

The coordinator may record that the missing analytic premise is supported at this assurance level, reconcile the JSW application and publish a checkpoint. The next assignment should distinguish further control arithmetic from a substantive frontier branch. Preserve these exact artifacts and this review when handing off. This agent ran no Git mutation commands and leaves checkpoint ownership with the coordinator.

## Appended integration scope assessment

October 28, 2026. The original report body above is preserved. It was checkpointed at commit `dd9320c25892e19612f3bbad08ef470da9fd30f9`, with coordinator confirmation of exit zero and `synced: true`. Publication does not certify mathematics.

The referee then checked the [coordinator integration record](../findings/run-002-control-consequences.md), SHA256 `ff160ea9e518157b560458fccf8589d8a9e4fcd992b6c2c9a653a7924a8c9e12`. Its analytic rank statement, application of JSW at 5, period and regulator conventions, absence of rational 5 torsion, and distinction between established theorem dependencies and newly checked arithmetic all agree with this review. Its statements about algebraic rank one and finite Sha explicitly retain the known analytic rank one theorem dependency. It does not claim an exact Sha order or a full leading coefficient identity.

The appended Mellin clarification is correct: the Fricke eigenvalue gives `g(1/t)=-t²g(t)`, and change of variables in the lower half of the Mellin integral yields the split representation. The original certificate already supplied that Fricke hypothesis and a direct source for the derivative identity. This is explanatory precision, not a material proof correction. The certificate hash and the original mathematical verdict remain unchanged.

One minor provenance phrase initially described both certificate and review as unchanged. Before final integration review, the coordinator clarified that the original assessment is unchanged while an appended report has a new file revision. No mathematical claim changed. There is no unresolved material objection to the integration at this assurance level.

This final scope check required no new research or computation. All assigned referee work is complete. The coordinator should retain the revised report hash in the final manifest and checkpoint the integration and handoff before retirement. No further mathematical work is pending in this agent's assignment.
