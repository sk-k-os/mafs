# run-001 source applicability audit

Date: 2026-10-28. Assignment: source audit worker. Status: submitted candidate; no independent review or formal verification. This is an applicability audit of existing mathematics, with elementary arithmetic witnesses. It is not a new BSD result.

The control curve passes the algebraic eligibility checks below at p = 5. Its analytic rank one hypothesis remains unproved in this dossier. The proposed pilot base fails the residual irreducibility requirement at p = 5.

The requested locator needs correction: both inspected versions number the result **Theorem 1.2.1**, inside Section 1.2. Neither labels it Theorem 1.2.

## Inspected sources and access

1. Jetchev, Skinner and Wan, *The Birch and Swinnerton-Dyer Formula for Elliptic Curves of Analytic Rank One*. [arXiv record](https://arxiv.org/abs/1512.06894v1), version 1, submitted 21 December 2015. [Original full PDF](https://arxiv.org/pdf/1512.06894v1). Inspected printed pages 1 and 2, Conjecture 1.1.1, Section 1.2, Theorem 1.2.1, equation (1.2.a), and the immediately following discussion. The landing page listed only v1. The 51 page PDF downloaded successfully; SHA256 `908562efdddaf46b2653317294cb65ae627802bc996400a779b1cd51b5a7d49d`.

2. The same paper, published in *Cambridge Journal of Mathematics* 5(3), 2017, pages 369 to 434. [Publisher full PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2017/0005/0003/CJM-2017-0005-0003-a002.pdf), [DOI](https://doi.org/10.4310/CJM.2017.v5.n3.a2). Inspected printed pages 369 to 371, especially **page 370, Section 1.2 and Theorem 1.2.1**. The eligibility statement and conclusion agree with v1. The 66 page PDF downloaded successfully; SHA256 `5a6978afcb2fad9ce4b13a88f9a93ffb77c700082f383f0b6e20980b5e3f7e76`. No assertion of a complete comparison of the two proofs is made.

3. J. S. Milne, *Elliptic Curves*, second edition, 2021, [author hosted full text](https://www.jmilne.org/math/Books/EC2.pdf). Inspected the author's mathematical exposition for the elementary bridges: Chapter II, Section 2, invariant formulas and Theorem 2.4, printed page 52; Chapter II, Section 3, reduction criteria, pages 59 to 61; Chapter II, Proposition 6.4; Chapter IV, Theorem 9.4 and proof, page 150; Chapter V, Propositions 8.1 and 8.3, pages 220 and 221. These give the model, reduction and Frobenius facts used below. SHA256 `646c0c4f193cdaa35f32c7d60fbd46a75e2f5187db4301810e8613726e3ebbee`. Page references are the printed numbering of this downloadable edition. An initial attempt at `https://www.jmilne.org/math/Books/ectext5.pdf` returned HTTP 404; the EC2 PDF was accessible.

This is two mathematical works, with two versions of JSW. No numerical database was consulted. Search results served only to locate the published JSW PDF; unrelated results were not adopted as evidence. Downloads and extracted text remain in ignored `work/bsd-run-001/`. No bulk source text is included here. The full JSW proof and its cited literature were not independently verified.

## Frozen statement and conventions

Read the hypotheses preceding the numbered theorem together with it. For an elliptic curve E over Q, require semistability, analytic order exactly one at s = 1, a prime p at least 5 with good reduction, and irreducible Galois action on E[p]. Then

\[
v_p\!\left(\frac{L'(E,1)}{\operatorname{Reg}(E/\mathbf Q)\,\Omega_E}\right)
=v_p\!\left(\#\Sha(E/\mathbf Q)\prod_{\ell\text{ finite}}c_\ell(E/\mathbf Q)\right).
\]

The p = 3 extension adds a_p(E) = 0 in the supersingular case. At p = 5, neither ordinarity, nonanomalous reduction, Tamagawa coprimality nor an additional residual ramification condition is imposed. [JSW, Theorem 1.2.1 and following discussion, pages 370 and 371](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2017/0005/0003/CJM-2017-0005-0003-a002.pdf).

JSW uses the Hasse Weil L function, regulator as the discriminant of the Néron Tate pairing, and \(\Omega_E=\int_{E(\mathbf R)}|\omega_E|\) for a Néron differential. The theorem's product is over finite primes; its abstract displays a different infinity convention. Use the numbered statement. The preceding paragraph attributes rank equality and Sha finiteness to Gross Zagier and Kolyvagin. The following paragraph attributes rationality of the normalized derivative to Gross Zagier. [JSW, page 370, Conjecture 1.1.1(b), Section 1.2 and equation (1.2.a)](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2017/0005/0003/CJM-2017-0005-0003-a002.pdf).

For this audit, v_p(p) = 1. The period therefore includes every real component; no extra real component factor should be inserted. The regulator must use a basis of the free Mordell Weil group, not an arbitrary point. The torsion denominator in the full BSD expression contributes zero valuation here: irreducibility implies E(Q)[p] = 0, since a rational point of order p would span an invariant line. Consequently p cannot divide the rational torsion order. This deduction explains the denominator's absence without assuming the torsion subgroup is trivial.

## Separate hypothesis witnesses

Write E_c for coefficients [0,0,1,−1,0] and E_b for [0,−1,1,−10,−20], in the order [a1,a2,a3,a4,a6]. Thus E_b has equation y² + y = x³ − x² − 10x − 20. These coefficient identities, rather than database labels, bind the calculation to the requested curves.

| Obligation | Control E_c | Pilot base E_b |
| :--- | :--- | :--- |
| Elliptic curve over Q | Integral coefficients; Δ = 37 ≠ 0. Witness A. | Integral coefficients; Δ = −11⁵ ≠ 0. Witness A. |
| Semistability at every finite prime | Good away from 37; multiplicative at 37. Witness A. | Good away from 11; multiplicative at 11. Witness A. |
| Eligible prime | 5 is prime and 5 ≥ 5. | Same. |
| Good reduction at 5 | 5 does not divide 37. | 5 does not divide −11⁵. |
| Irreducible E[5] over F5 | An irreducible Frobenius polynomial at 3 rules out an invariant line. Witness B. | Fails: the rational point (5,5) has order 5. Witness C. |
| ord at s = 1 of L(E,s) equals 1 | Missing certified analytic witness. Algebraic rank or a floating point derivative is insufficient. | No analytic witness obtained. Residual failure already excludes this application. |

**Witness A.** Exact invariant arithmetic gives:

| Curve | b2 | b4 | b6 | b8 | c4 | c6 | Δ |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| E_c | 0 | −2 | 1 | −1 | 48 | −216 | 37 |
| E_b | −4 | −20 | −79 | −21 | 496 | 20008 | −161051 |

The displayed integral models are minimal. At their only possible bad primes the discriminant valuations are respectively 1 and 5; an integral model with smaller discriminant valuation would decrease it by a positive multiple of 12, which is impossible. Elsewhere the valuation is zero. At 37, c4(E_c) is a unit; at 11, c4(E_b) is a unit. The nodal reduction criterion therefore proves multiplicative reduction at those primes and good reduction elsewhere. This proves semistability directly. The associated conductors are 37 and 11, using conductor exponent one for multiplicative reduction. The good reduction check at 5 does not depend on a database conductor. [Milne, Chapter II, Theorem 2.4 and Section 3, pages 52 and 59 to 61](https://www.jmilne.org/math/Books/EC2.pdf).

**Witness B.** Over F3, x³ − x = 0 for every x. The solutions of y² + y = 0 are y = 0 and 2, giving six affine points and the point at infinity. Hence #E_c(F3) = 7 and a3 = 3 + 1 − 7 = −3. For arithmetic Frobenius at 3 acting on E_c[5],

\[
\chi_3(T)=T^2-a_3T+3=T^2+3T+3\pmod5.
\]

Its discriminant is 9 − 12 ≡ 2 modulo 5, a nonsquare. Thus this element has no eigenline over F5. A Galois invariant line would be invariant under every element, contradicting this calculation. This proves the required irreducibility; it does not claim surjectivity of the whole image. The bridge from the point count to this polynomial uses good reduction at 3, the Tate module reduction identification and Frobenius determinant 3. [Milne, Chapter II, Proposition 6.4; Chapter IV, proof of Theorem 9.4, page 150; Chapter V, Proposition 8.3, page 221](https://www.jmilne.org/math/Books/EC2.pdf). This witness explicitly uses arithmetic Frobenius. Replacing it by its inverse, as with a geometric convention, preserves the invariant subspaces.

At 5, direct counting gives #E_c(F5) = 8, a5 = −2. For E_b it gives #E_b(F5) = 5, a5 = 1. Both are ordinary; the pilot is anomalous. Neither distinction replaces the irreducibility test, and anomaly itself is not an exclusion in the frozen theorem.

**Witness C.** On E_b, the group law gives

\[
P=(5,5),\quad 2P=(16,-61),\quad 3P=(16,60),\quad
4P=(5,-6)=-P,\quad 5P=O.
\]

All four affine points satisfy the exact equation, and P ≠ O. Since 5 is prime, P has order 5. The subgroup it spans is a rational invariant line in E_b[5]. The theorem therefore fails to apply at 5 independently of any proposed analytic rank certification. No analytic rank zero assertion for E_b is needed or proved here.

## Reproducible finite arithmetic

The invariant calculations, point counts at 2, 3, 5 and 7, and rational multiples above were executed using Python 3.14.6, integer arithmetic and `fractions.Fraction`; both executions exited 0. No approximation or database field enters these witnesses. The following self contained code reproduces the relevant checks. Software execution supports the arithmetic record; the mathematical bridges and calculations still require independent review.

```python
from fractions import Fraction as F

for name, a in [('control', (0,0,1,-1,0)),
                ('pilot', (0,-1,1,-10,-20))]:
    a1,a2,a3,a4,a6 = a
    b2 = a1*a1 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3*a3 + 4*a6
    b8 = b2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    delta = -b2*b2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    print(name, (b2,b4,b6,b8,c4,c6,delta))
    for q in (3,5):
        count = 1 + sum(
            (y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6) % q == 0
            for x in range(q) for y in range(q))
        print(q, count, q+1-count)

# Pilot only: a1=0, a2=-1, a3=1, a4=-10.
def add(P, Q):
    if P is None: return Q
    if Q is None: return P
    x,y = P
    u,v = Q
    if x == u and y+v+1 == 0: return None
    slope = ((3*x*x-2*x-10)/(2*y+1) if P == Q
             else (v-y)/(u-x))
    intercept = y-slope*x
    X = slope*slope+1-x-u
    return X, -slope*X-intercept-1

P = (F(5),F(5))
Q = None
for n in range(1,6):
    Q = add(Q,P)
    assert Q is None or Q[1]**2+Q[1] == Q[0]**3-Q[0]**2-10*Q[0]-20
    print(n, Q)
assert Q is None
```

Expected relevant count output: control at 3 gives (count,a3) = (7,−3), and at 5 gives (8,−2); pilot at 3 gives (5,−1), and at 5 gives (5,1). The invariant tuples and multiples must match the displayed witnesses.

The embedded code was subsequently extracted from this dossier and replayed. It exited 0 and reproduced these tuples, counts and multiples. This replay used the same interpreter and is not an independent implementation.

## Applicability boundary and next test

There are three distinct conclusions to track. A proved analytic order one would permit the existing rank equality theorem to give rank E_c(Q) = 1, and the existing finiteness theorem to give finite Sha(E_c/Q). JSW would additionally give the **5 part** of the leading coefficient formula. No claim about other prime parts, an exact order of Sha, or full BSD follows from this one application. The present dossier has not closed the analytic premise, and does not assert any of those conclusions unconditionally as a result of this run.

The next test is one certified analytic rank computation for the exact coefficients [0,0,1,−1,0]. Require two receipts: an exact proof that L(E_c,1) = 0, and an interval enclosing L′(E_c,1) that excludes zero, with a proved truncation error and rounding enclosure. A functional equation sign calculation can supply the first receipt; a certified modular L function calculation can supply the second. Record the exact curve and modular form identification, local signs, precision, truncation bound, software version and commands. A decimal output from an `analytic_rank` routine without its certification contract does not discharge this obligation. If the required certified tool is unavailable, leave the application conditional.

An equivalent exact theorem proving analytic rank one for this precise curve, with its hypotheses checked and full source inspected, could replace those receipts. Neither route was executed here. Independently replay and review Witnesses A, B and C before promotion. The source assignment ends with this dossier; the parent owns reconciliation, STATE.md and Git publication. No child agents, credentials, service installation, Git mutations or checkpoints were used. API cost, token usage and exact elapsed duration were not measured.
