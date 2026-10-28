# Run 002 referee preparation

Date: October 28, 2026. Author role: separate skeptical model referee. This file records preparatory checks before receipt of a frozen candidate. It supplies no verdict on an author artifact.

## Scope and independence

The target is the exact analytic order at one for the Hasse Weil L function of C over Q with coefficients `[0,0,1,-1,0]`. A rational point or a numerical database rank is insufficient. It suffices to prove the completed function has sign negative one and to enclose the first derivative in a strictly positive interval.

The referee read the assignment, research state, run 001 source audit and Mathforge review policy. It did not read another run 002 review verdict. Model family, tools, workspace and standard literature are shared with the authors. The coordinator subsequently communicated the author's proposed elementary positivity bound. These dependencies limit independence. No formal checker or external human mathematician is involved.

## Independent local calculation

The standard invariant formulas yield c4 = 48, c6 = negative 216 and discriminant 37. Valuation one at 37 forces minimality there; the discriminant is a unit elsewhere. The finite bad reduction is multiplicative, hence the conductor is 37. Direct exhaustive arithmetic found the unique affine singular point modulo 37 to be `(5,18)`. Translation gives tangent cone `v² = 15u²`. Both 15 and negative c6 modulo 37 are nonsquares: negative c6 is 31, and `31^18 mod 37 = 36`. Thus the bad reduction is nonsplit. Standard local signs then give global sign negative one.

These calculations use no database identification. The standard local sign and modularity theorems still require precise source coverage in the submitted argument.

## Analytic bridge

Independently splitting the Mellin integral at its symmetry point gives, with x = 2π/√37 and sign negative one,

\[
L'(C,1)=2\sum_{n\ge1}\frac{a_n}{n}E_1(nx),
\qquad E_1(z)=\int_1^\infty e^{-zt}\frac{dt}{t}.
\]

Cremona's corrected online second edition, Chapter II, printed pages 42 and 43, Proposition 2.13.1 and equation 2.13.2, verifies this identity under order at least one and Fricke eigenvalue positive one. The Fricke eigenvalue is the negative of the functional equation sign. The proposition does not assume exact order one, so it is usable without circularity. [Author hosted chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf).

Review must check exact coefficient normalization, termwise differentiation, root sign, error bounds and the rational enclosures of constants. A finite positive decimal without these bridges is insufficient.

## Author proposal communicated after initial derivation

The coordinator communicated a proposed bound using only a1 = 1 and a2 = negative 2, with 1 < x < 11/10. For z > 0,

\[
\frac{e^{-z}}{z+1}\le E_1(z)\le\frac{e^{-z}}{z}.
\]

The lower inequality follows by writing the integral as `e^(negative z)` times the exponential average of `1/(z+t)`, and integrating its tangent line at t = 1. The upper bound follows from `1/t ≤ 1` in the defining integral. The Hasse bound and Euler recurrences give `|a_n| ≤ d(n)√n ≤ 2n`. These facts imply that the entire contribution of indices at least three has absolute value, before the factor two, at most

\[
\frac{2e^{-3}}{3(1-e^{-1})}.
\]

Assuming the proposed elementary exponential bounds are established, the suggested comparison reduces exactly to

\[
\frac{L'(C,1)}2>
\frac{100}{651}-\frac9{128}-\frac9{160}
=\frac{11269}{416640}.
\]

The right side is positive and twice it exceeds 1/20. This is a check of a communicated proposal, not a verdict on an as yet unfrozen candidate.

Preparation correction: the first draft typed the numerator as 11273. Exact Fraction arithmetic returned 11269; the displayed value above was corrected before submission for review.

## Handoff

Await the exact frozen artifact and evidence hashes. Review each cited theorem and execute an independently written arithmetic reconstruction. Preserve any objection and its resolution. Do not modify author files or write Git state. The coordinator owns checkpoint publication.

## Completion amendment

The frozen candidate was subsequently supplied and reviewed. Its intentionally weaker lower endpoint is 73/2240, not the earlier exploratory bound discussed above. The [final report](run-002-referee.md) assesses the exact submitted revisions and the [independent receipt](../experiments/run-002-referee/receipt.json) records a successful exact replay. The candidate needed no mathematical correction. The coordinator has received the report and owns publication before retirement.
