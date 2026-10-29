# Run 002 analytic source dossier

Date: October 28, 2026. Status: candidate source audit for separate review. Frozen curve: C over Q with coefficients `[0,0,1,-1,0]`, hence equation \(y^2+y=x^3-x\). This record supplies dependencies for an exact analytic rank argument; it does not itself verify the companion enclosure or certify a theorem application.

## Inspected sources

**Wiles.** Andrew Wiles, *Modular elliptic curves and Fermat’s Last Theorem*, Annals of Mathematics 141 (1995), pages 443 to 551. [Publisher record](https://annals.math.princeton.edu/1995/141-3/p01), [inspected scan](https://sites.math.rutgers.edu/~zeilberg/EM22/AW1995.pdf). Theorem 0.4, printed page 448, PDF page index 6, says that every semistable elliptic curve over Q is modular. The definition on page 443 uses a modular parametrization. No BSD hypothesis occurs. The theorem and introductory definition were inspected; the full proof was not reverified. SHA256: `69b968590df204c59702ee9ffcc857d8ee3cf683146c04133ff098c27bc2b831`.

**Cremona.** J. E. Cremona, *Algorithms for Modular Elliptic Curves*, corrected online second edition, [edition information](https://johncremona.github.io/book/fulltext/index.html), [Chapter II](https://johncremona.github.io/book/fulltext/chapter2.pdf). Inspected page 25, equations (2.6.1) and (2.6.2); page 29, equations (2.8.4) through (2.8.6); pages 42 and 43, Mellin derivation and Proposition 2.13.1. At a prime q with q exactly dividing N, the newform coefficient satisfies \(a_q=-\epsilon_q\), where \(\epsilon_q\) is its Atkin Lehner eigenvalue. For the Fricke eigenvalue \(\epsilon_N\),

\[
\Lambda(f,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(f,s),
\qquad \Lambda(f,2-s)=-\epsilon_N\Lambda(f,s).
\]

Proposition 2.13.1 assumes a normalized newform, \(\operatorname{ord}_{s=1}L(f,s)\ge r\), and \(\epsilon_N=(-1)^{r-1}\). For r = 1 it yields

\[
L'(f,1)=2\sum_{n\ge1}\frac{a_n}{n}E_1(2\pi n/\sqrt N),
\qquad E_1(u)=\int_u^\infty e^{-t}\frac{dt}{t}.
\]

The premise is order at least one, not order exactly one. This distinction prevents circular use of the formula. SHA256: `432fa5290b2b2ac0d623169e9198d928e5dd75acb490db2d58775630d0f6ea94`.

**Dogra and Le Fourn.** Netan Dogra and Samuel Le Fourn, *Quadratic Chabauty for modular curves and modular forms of rank one*, Mathematische Annalen 380 (2021), pages 393 to 448; published online November 19, 2020. [Publisher article](https://link.springer.com/article/10.1007/s00208-020-02112-3), [PDF](https://link.springer.com/content/pdf/10.1007/s00208-020-02112-3.pdf). Lemma 15, printed page 422, gives the same derivative formula for every \(f\in S_2(\Gamma_0(M))^+\), with M any positive integer; plus denotes the Fricke eigenspace. Its proof, pages 422 and 423, gives the completion and functional equation in (27) and (28). This independently locates the formula in a primary research article. The lemma and proof were inspected in publisher HTML and extracted PDF text. No full paper verification is claimed.

**Milne.** J. S. Milne, *Elliptic Curves*, second edition (2021), [author hosted text](https://www.jmilne.org/math/Books/EC2.pdf). This is an author exposition with proofs, not the original publication of Hasse’s theorem. Inspected Chapter IV, Theorem 9.4 and proof, page 150, giving the Hasse bound. Page 164 gives the good and bad Euler factors. Chapter V, Theorem 5.2 and Definition 5.3, page 208; the footnote there; and pages 209 and 210 identify modularity with equality to the L function of a normalized weight two newform at the curve’s conductor. This supplies the precise analytic meaning used with Wiles. SHA256, identical to run 001: `646c0c4f193cdaa35f32c7d60fbd46a75e2f5187db4301810e8613726e3ebbee`.

## Applicability and elementary deductions

The [run 001 audit](run-001-jsw-audit.md) establishes minimal discriminant 37, multiplicative reduction at 37, good reduction elsewhere, semistability and conductor 37. Wiles therefore applies. In the modern equivalent formulation explained above, there is a normalized newform \(f_C\in S_2(\Gamma_0(37))\) with the exact Euler product equality \(L(C,s)=L(f_C,s)\). No database label or approximate period lattice identification is needed.

Once the local calculation proves nonsplit multiplicative reduction at 37, the bad Euler factor is \((1+37^{-s})^{-1}\), so \(a_{37}=-1\). Since the conductor is the prime 37, Cremona’s relation gives \(\epsilon_{37}=+1\). The analytic functional equation has sign minus one, forcing \(L(C,1)=0\). This route directly connects local reduction, newform coefficient, Fricke sign and analytic sign. The separate coordinator record contains the local calculation. This source worker has not supplied independent review of that calculation.

Here is the coefficient bound reconstructed from the Euler factors. For a good prime p, write

\[
1-a_pT+pT^2=(1-\alpha_pT)(1-\beta_pT).
\]

Hasse implies \(|\alpha_p|=|\beta_p|=\sqrt p\). Expanding the reciprocal factors as geometric series gives

\[
a_{p^k}=\sum_{j=0}^k\alpha_p^j\beta_p^{k-j},
\qquad |a_{p^k}|\le(k+1)p^{k/2}.
\]

At a multiplicative bad prime, the prime power coefficients have modulus one; an additive factor contributes zero at positive powers. Multiplication of the local expansions yields multiplicativity. Consequently, for every positive integer n,

\[
|a_n|\le d(n)\sqrt n\le2n.
\]

The last inequality pairs each divisor with its complementary divisor, leaving at most \(\lfloor\sqrt n\rfloor\) pairs. This is an elementary deduction from stated standard inputs, not an extra conjecture. It includes indices divisible by 37. With \(E_1(u)\le e^{-u}/u\), it also proves absolute convergence of the derivative series and provides a geometric truncation estimate. The companion computation worker supplies its chosen exact enclosure.

## Routes retained and limitations

Cremona’s [worked examples](https://johncremona.github.io/book/fulltext/examples.pdf), Example 3, pages 58 to 60, give a level 37 newform with Hecke eigenvalue minus two at 2 and Fricke eigenvalue plus one. They identify the curve equation through numerically computed invariants and state a nonzero approximate derivative. This is useful corroboration, but this run does not adopt those decimal computations as its certificate. The example PDF SHA256 is `20a4118e6cd82e9d9adc59070fa039594f09888f26a1259e1ebe18426484878c`.

No standalone exact rank theorem for this particular model was promoted. The bounded search instead found adequate inputs for a short exact inequality proof. Broad search results, an OEIS coefficient list, software rank examples and a recent unvetted rank computation were not used as evidence. Initial web fetches of Wiles’s scan timed out; a direct download succeeded. The first William Stein mirror timed out and was superseded by the Rutgers scan. The derivative article was inspected through accessible publisher content; its screenshot retrieval failed, so no screenshot inspection is claimed. Source downloads and extracted text remain under ignored `work/`; no bulk copyrighted material is committed.

## Handoff

The coordinator should bind these locators to the frozen argument, obtain separate review of the exact local reduction and rational inequalities, and retain the distinction between published theorems, newly reconstructed elementary deductions and actual executed checks. A fully positive derivative enclosure plus the exact central vanishing proves analytic order exactly one. That conclusion must then be reconciled with the separate JSW applicability dossier; it does not prove full BSD.

This worker made no Git mutations, external correspondence, installations or purchases. The coordinator owns the checkpoint before ending the team. Actual token usage and monetary cost are unknown; wall time was not independently measured. No trusted formal checker or qualified human mathematical referee participated in this source audit.
