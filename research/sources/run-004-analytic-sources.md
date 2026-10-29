# Run 004 analytic source audit for E_7611

Date: 2026-10-29 UTC. Author role: source specialist. Status: candidate source audit for separate review. The assignment is one rigorous second derivative test for E = E_7611 over Q, given by Y² = X³ − 7611²X. This record fixes dependencies and conventions; it does not assert that the companion numerical enclosure has passed review. This is a calibration observation, not a benchmark.

## Frozen input and scope

The inherited input is the restricted family argument in [Run 003 Route A](run-003-route-a.md), SHA256 `868a60d0288f33a1992931a1a10eb9b3b53a3781d0132e81ee1501b1d50f5628`, and its [separate review](../reviews/run-003-referee.md), SHA256 `d6a9dce3f93a4d216403ee3d77e11a5febcb8e49cacfa72401eb5f86a463c5fb`. The member u=2,v=1 has n=3·43·59=7611 and algebraic rank two under the recorded descent and Monsky dependencies. This run does not replace those dependencies or infer analytic rank from their numerical sample.

The required conclusion is L(E,1)=L'(E,1)=0 and L''(E,1) nonzero. Such a conclusion establishes analytic rank two for this one curve. It does not establish full Sha finiteness, its odd primary components, or the full BSD leading coefficient formula.

## Inspected sources

All accesses or local reinspections occurred on 2026-10-29. Downloaded PDFs remain under ignored work directories. A source statement is distinct from an independently reconstructed proof of that statement.

1. J. E. Cremona, *Algorithms for Modular Elliptic Curves*, corrected online second edition, [Chapter II](https://johncremona.github.io/book/fulltext/chapter2.pdf). Reinspected printed page 29, equations (2.8.5), (2.8.6); pages 42 and 43, the split Mellin derivation and Proposition 2.13.1; and page 44, the series and Q2 polynomial. The proposition assumes a normalized newform, vanishing order at least r, and Fricke eigenvalue (−1)^(r−1). It does not assume the order is exactly r. The formula uses 2r!, with the kernel divided by (r−1)!. Inspection copy `work/bsd-run-002/sources/cremona-chapter2.pdf`, SHA256 `432fa5290b2b2ac0d623169e9198d928e5dd75acb490db2d58775630d0f6ea94`.

2. Christophe Breuil, Brian Conrad, Fred Diamond, and Richard Taylor, *On the Modularity of Elliptic Curves over Q: Wild 3 Adic Exercises*, Journal of the American Mathematical Society 14 (2001), 843–939. [Publisher DOI](https://doi.org/10.1090/S0894-0347-01-00370-8), [inspected author prepublication PDF](https://www.math.u-psud.fr/~breuil/PUBLICATIONS/STW.pdf). The author copy's date line contains placeholders for 2000 and January 2001. Inspected Theorem A on its printed page 1 and equivalent conditions (1), (2) on page 3: every elliptic curve over Q is modular, with equality of its L function to that of a weight two eigenform at its conductor. The normalized newform formulation is also explained in Milne, Chapter V, pages 208–210. The full proof was not reverified. Inspection copy `work/run004-a/bcdt.pdf`, SHA256 `cbbdc24c26cdfcbd77f0e084194643e8804a724f004eb02e431ead9d932c498d`.

3. Mark Watkins, Stephen Donnelly, Noam D. Elkies, Tom Fisher, Andrew Granville, and Nicholas F. Rogers, *Ranks of quadratic twists of elliptic curves*, Publications mathématiques de Besançon, 2014/2, 63–98. [Publisher record](https://pmb.centre-mersenne.org/articles/10.5802/pmb.9/), [published PDF](https://www.numdam.org/item/10.5802/pmb.9.pdf). Inspected the curve definition on printed page 63 and the conductor statement on printed page 86, section 10: for squarefree d the conductor is 32d² if d is odd and 16d² if d is even. The same statement occurs on page 26 of the [author copy](https://www.dpmms.cam.ac.uk/~taf1000/papers/rankcongr.pdf), whose SHA256 is `0fb963c40c7eea037d3ee68717763d0be5c3fcdc884c8e838839bb9ba37f1534`. The published inspection copy `work/run004-a/rankcongr-published.pdf` has SHA256 `8774d21baf5d9a7e6979d887844c409d739481f281e36d8d4a948a734d9ddbea`. The conductor statement is used as an exact standard fact; nearby speculative rank heuristics and GRH dependent bounds are not used. This audit does not claim to have replayed Tate's full local algorithm.

4. Ye Tian, Xinyi Yuan, and Shou Wu Zhang, *Genus Periods, Genus Points and Congruent Number Problem*, Asian Journal of Mathematics 21 (2017), 721–774. [Author hosted published PDF](https://web.math.princeton.edu/~shouwu/publications/cn.pdf). Reinspected printed pages 721 and 722. The domain is positive squarefree n and the model is ny²=x³−x, isomorphic to ours by (X,Y)=(nx,n²y). Page 722 records root sign +1 for n≡1,2,3 modulo 8 and −1 for n≡5,6,7. It also recalls that analytic order at most one implies rank equality and finite Sha, citing Coates, Wiles, Rubin, Gross, Zagier, and Kolyvagin. Its real period convention is given on the same page. The original proofs of those recalled theorems are not newly reverified. Inspection copy `work/run003-a/tian-yuan-zhang.pdf`, SHA256 `417f6bbe7f7b775f77a2593cc2f32cbab2f2782cf07d0ba0a15f2708b2475595`.

5. Kenneth A. Ribet, *Modular Forms and Diophantine Questions*, [author PDF](https://math.berkeley.edu/~ribet/Articles/icfs.pdf), version marked submitted to World Scientific on 13 February 2001. Inspected section 6, printed pages 9–11, especially Theorem 1 on page 11. This is an author exposition of Gauss's point count theorem, not the original Gauss publication. For p≡1 modulo 4, write p=a²+b², with a odd, b even, and a+b≡1 modulo 4. The affine count on y²=x³−x is p−2a. For p≡3 modulo 4 the affine count is p, as explained on page 10. Adding the point at infinity gives the required Frobenius traces. Inspection copy `work/run004-a/ribet-icfs.pdf`, SHA256 `b70e5baf54f03e7b3fcbe109c22eb2ed37909af1aee9f95cd67bcda735781b40`.

6. J. S. Milne, *Elliptic Curves*, second edition, 2021, [author PDF](https://www.jmilne.org/math/Books/EC2.pdf). Reinspected Chapter II section 7, printed page 76, for discriminant scaling and minimal models; page 82 for differential scaling; Chapter IV Theorem 9.4, page 150, for Hasse's bound; and page 164 for Euler factors. The modularity formulation is in Chapter V, pages 208–210. This is an author exposition, not the original publication of each result. Inspection copy `work/bsd-run-001/milne-ec2.pdf`, SHA256 `646c0c4f193cdaa35f32c7d60fbd46a75e2f5187db4301810e8613726e3ebbee`.

## Conductor, minimal model, and sign

The exact conductor is

N = 32·7611² = 1853674272,

so √N = 4√2·7611 and x0 = 2π/√N = π/(2√2·7611). The hypotheses of the cited conductor formula hold because 7611=3·43·59 is odd and squarefree. Its factor at 2 is 2^5, and the three odd factors each have exponent two.

For this integral equation, c4=48n², c6=0, and Δ=64n^6. Each nonzero prime valuation of Δ is six. A change between Weierstrass equations changes the discriminant valuation by a multiple of twelve. Since an integral discriminant has nonnegative valuation, this equation is minimal at every prime. This is a reconstruction using the cited scaling law, not a second execution of Tate's algorithm. The bad primes are exactly 2,3,43,59. At the odd bad primes the reduced equation is Y²=X³, a cusp. At 2 its singular point is (1,0); after shifting X by 1 the tangent cone is a repeated line. Thus the bad reductions are additive, and every bad Euler factor is one. In particular this curve is not within the semistable only version of Wiles's theorem; the full modularity theorem above is used.

Since n≡3 modulo 8, the cited root number formula gives analytic sign w=+1. In Cremona's convention the Fricke eigenvalue is ε_N=−w=−1. These two signs must not be identified with one another.

## Exact lower order vanishing

Let r_an=ord_(s=1)L(E,s). Modularity supplies an entire L function that is not identically zero, so the order is defined. If r_an were zero or one, the cited low analytic rank theorem would give rank E(Q)=r_an. The inherited rank two result excludes both possibilities. Therefore

L(E,1)=0 and L'(E,1)=0.

This is a contraposition of an established implication, not an assumption of BSD rank equality in rank two. An alternative sufficient route uses only the rank zero implication to obtain L(E,1)=0 and then the positive functional equation sign to force L'(E,1)=0. Positive sign alone does not force L(E,1)=0, and positive sign alone forces the first derivative of the completed L function, rather than the uncompleted function, to vanish.

## Completion and second derivative formula

Take the normalized weight two newform f(z)=Σ_(m≥1)a_m exp(2πimz) corresponding to E, with a_1=1 and L(E,s)=Σ a_m m^(−s) in its convergence half plane. Fix the completion

Λ(s)=N^(s/2)(2π)^(−s)Γ(s)L(E,s).

Here Γ is the ordinary Euler gamma function. No extra factor two from an alternative complex gamma convention is inserted. Cremona's Mellin formula and w=+1 give

Λ(s)=∫_0^∞ f(iy/√N)y^(s−1)dy

=∫_1^∞ f(iy/√N)[y^(s−1)+y^(1−s)]dy,

and Λ(2−s)=Λ(s). Differentiating twice at one yields

Λ''(1)=2∫_1^∞ f(iy/√N)(log y)²dy.

Put A(s)=N^(s/2)(2π)^(−s)Γ(s). The product rule gives Λ''=A L''+2A'L'+A''L. Both lower order terms vanish exactly at one, and A(1)=√N/(2π). Consequently

L''(E,1)=(2π/√N)Λ''(1)

=(4π/√N)Σ_(m≥1)a_m∫_1^∞ exp(−x0 m y)(log y)²dy.

Integrating each summand by parts gives the computation interface

L''(E,1)=4Σ_(m≥1)(a_m/m)G2(x0m),

G2(z)=∫_1^∞ exp(−zy)log(y)dy/y = ∫_z^∞ exp(−t)log(t/z)dt/t.

This is precisely the r=2 instance of Cremona's Proposition 2.13.1. Its order at least two assumption has already been supplied. A nonzero result then establishes order exactly two; no nonzero premise is needed to invoke the formula. The leading Taylor coefficient would be L''(E,1)/2, not L''(E,1).

The same source, printed page 44, gives the exact computational series

G2(z) = (log z+γ)²/2 + π²/12 + Σ_(k≥1)(−z)^k/(k²k!), for z>0,

where γ is Euler's constant. Its exact identity does not authorize approximate constants or uncontrolled truncation. The computation worker must enclose π, √2, γ, logarithms, finite arithmetic, the series remainder, and the outer tail separately. Alternating remainders require checking that the retained tail terms decrease; cancellation at larger z requires adequate interval precision.

## Coefficient interface and exact twist character

For E1:y²=x³−x at an odd prime p, the inspected Gauss formula gives a_p(E1)=0 when p≡3 modulo 4. For p≡1 modulo 4, write p=a²+b² with a odd, b even, a+b≡1 modulo 4; then a_p(E1)=2a. The sign condition on a is necessary. The sign of the even b is irrelevant modulo four.

The twist relation can be reconstructed without a new CM theorem. For p not dividing 2n, the exact character sum is

a_p(E_n)=−Σ_(X∈F_p) Legendre(X³−n²X,p).

Substitute X=nz. Multiplicativity of the Legendre symbol gives a_p(E_n)=Legendre(n,p)a_p(E1). Set a_p(E_n)=0 at p=2,3,43,59, as established by additive reduction above.

For every good prime, a_(p^0)=1 and a_(p^k)=a_p a_(p^(k−1))−p a_(p^(k−2)) for k≥2. At a bad prime a_(p^k)=0 for every k≥1. Coefficients multiply at coprime indices. These recurrences are the Euler factor expansions, and determine every a_m exactly.

If the implementation twists a full coefficient table rather than prime traces, use D=4n=30444, the fundamental discriminant of Q(√7611), and χ_D(m)=Kronecker(D/m). Then

a_m(E_n)=χ_D(m)a_m(E1)

for all positive m. At odd m the character equals Jacobi(7611,m); it vanishes at even m and at multiples of 3,43,59. A shorthand χ_7611 must retain this convention. The base coefficients already vanish at even indices, but that fact does not make 7611 itself the fundamental discriminant.

## Absolute convergence and an outer tail bound

The Hasse bound and good Euler factors give |a_(p^k)|≤(k+1)p^(k/2); the bad coefficients satisfy this as well. Multiplicativity therefore gives |a_m|≤d(m)√m≤2m. This is the same elementary coefficient bridge recorded in Run 002, now with the present additive factors.

For z>0, log y≤y−1 and 1/y≤1 on y≥1 imply

0<G2(z)≤∫_1^∞ exp(−zy)(y−1)dy=exp(−z)/z².

Thus for any positive integer M, the omitted part R_M of the second derivative series obeys

|R_M|≤8 exp(−x0(M+1)) / [x0²(M+1)²(1−exp(−x0))].

This proves absolute convergence and supplies one valid explicit tail; a computation may use a sharper justified bound. Differentiation and termwise integration in the split Mellin formula are justified by exponential decay on y≥1 and this coefficient growth. The finite coefficient computation still requires exact implementation verification.

## Period convention and boundaries

The minimal invariant differential is ω=dX/(2Y). The full real period convention relevant to BSD is Ω_E=∫_(E(R))|ω|. Since this cubic has three real roots, E(R) has two components. Direct substitution X=nt and the equality of the two component periods give

Ω_E = (2/√n)∫_1^∞ dt/√(t³−t),

matching Tian, Yuan, Zhang page 722. The least positive real lattice period is half this full real period. No Ω_E, regulator, Manin constant, or period of a modular parametrization enters the nonvanishing formula above. Equality of L functions suffices; no identification of their period lattices is asserted.

Even a successful L'' enclosure leaves the odd primary Sha and full coefficient formula unresolved. The two inherited independent points are not automatically a saturated Mordell Weil basis. No low analytic rank theorem is applied after obtaining analytic rank two to infer Sha finiteness.

## Source failures, corrections, and handoff

The publisher BCDT PDF returned HTTP 403 through web retrieval; the Harvard repository fetch returned HTTP 429; an author PDF web fetch timed out. Direct retrieval of the author PDF then succeeded and the relevant pages were inspected locally. A William Stein lecture PDF timed out and was superseded by the inspected published conductor statement. An AMS book preview was searchable but its direct fetch returned HTTP 403, so it is not used as the operative Gauss source; Ribet's author text was inspected instead. Two guessed Stanford paths were inaccessible and supplied no evidence. A local search command containing an unintended null byte was rejected before execution and was rerun with a corrected query; no file was changed by that failure.

The conductor statement is an inspected literature input, not a claimed local algorithm receipt. The root number and low rank implications are recorded as recalled theorems in the inspected primary research paper, with the original proof dependencies retained. Ribet is explicitly an exposition of Gauss, not the original source. No database label or floating rank output supplies a premise.

The computation worker received the factor four formula, kernel series, conductor, coefficient sign rule, twist character correction, and tail bound. The referee received exact claims and source locators before any outcome conclusion. Freeze this record, bind the separate interval artifact and review by hashes, and checkpoint through the coordinator. No Git mutation, external correspondence, installation, model or permission change was performed by this worker. No hook error event or exact hook error text was visible in this worker's tool context; that limited observation does not certify desktop capture health or the absence of errors elsewhere.
