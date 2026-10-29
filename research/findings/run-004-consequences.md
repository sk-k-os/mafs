# Run 004 integration and remaining obligations

October 29, 2026. Exact curve over Q: E_7611:y²=x³−7611²x, with coefficient vector [0,0,0,−57927321,0]. This synthesis preserves the frozen source audit, exact computation and separate referee conclusions. It is not a formal certificate, an external human review or a full BSD claim.

## Supported result

The [source audit](../sources/run-004-analytic-sources.md) fixes conductor N=1853674272, analytic sign +1, Fricke eigenvalue −1 and the Hasse Weil L function normalization. The inherited algebraic rank two result, combined with the established implication from analytic rank zero or one to algebraic rank equality, rules out both lower analytic orders. Thus L(E,1)=L'(E,1)=0 exactly; this does not assume BSD in rank two.

The [integer interval certificate](run-004-analytic-certificate.md) gives the strict rational enclosure

1561/100 < L''(E,1) < 1563/100.

The exact second derivative formula assumes vanishing order at least two, which the preceding argument supplies. It does not assume the desired exact order. A nonzero second derivative therefore establishes ord_(s=1)L(E,s)=2. Together with Run 003 this gives algebraic and analytic rank equality, both equal to two, for this one curve under the recorded theorem dependencies and computational trust boundary.

The derivative formula uses the raw L function and no real period division. The minimal differential is dx/(2y); the full real Néron period includes both real components. The leading Taylor coefficient is L''(E,1)/2. Neither this normalization nor the interval proves the BSD coefficient identity.

## Evidence and review scope

The [separate referee](../reviews/run-004-referee.md) directly checked the cited statements and reconstructed the normalization and implication chain. A separate implementation agreed on all 220000 Fourier coefficients and direct point counts at 164 good primes at most 1000. Seven independent rational kernel checks and tighter constant intervals were contained in the author intervals. The tail was recomputed exactly, and the complete author output was reproduced byte for byte.

This is separate coefficient and kernel checking plus a full replay of the author summation, not two independent implementations of the entire second derivative certificate. Python integer arithmetic, the interpreter, the inherited algebraic rank argument and the inspected established theorems remain dependencies. No ordinary floating point calculation supplies a proof premise. No formal prover, trusted acceptance service or qualified human mathematical referee participated. Shared model lineage and sources remain explicit; agent agreement is not proof.

No material unresolved mathematical objection was found in the frozen candidate. The referee retained and corrected its preliminary wording about exponential decay: Fourier terms decay after the Mellin split; the coefficients instead obey the bound |a_m|≤2m. Source access failures and the fundamental discriminant correction to 30444 remain visible in the source dossier. No novelty is claimed.

## What remains

The inherited trivial 2 primary Sha statement remains available. This run does not establish finiteness of the full Tate Shafarevich group, any missing odd primary information, or its exact full order. Analytic rank two does not permit applying a rank zero or one finiteness theorem.

The two inherited independent points are not shown to form a saturated Mordell Weil basis. The full regulator, all required local factors and the exact BSD leading coefficient identity remain separate obligations. A numerical ratio suggested by BSD would be exploratory unless its mathematical bridge were proved.

The family wide analytic rank statement remains unproved. A calculation at n=7611 does not prove the corresponding result for every prime qualified family member, and the family infinitude question remains unchanged.

## Director handoff

The chosen analytic task is complete at the stated assurance level. The [director packet](../sessions/run-004-director-packet.md) asks whether the next bounded assignment should audit a route to full Sha finiteness for this exact curve or first verify saturation and arithmetic inputs for a later coefficient comparison. The source and obstruction audit of full Sha finiteness is recommended because it addresses a remaining substantive BSD obligation. Neither branch starts automatically.
