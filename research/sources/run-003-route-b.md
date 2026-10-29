# Route B: alternative primes for the pilot twist family

Date and source access: October 29, 2026. Revision 1. Status: candidate source audit and mathematical argument for separate review. This is a calibration observation, not a protected benchmark, novelty claim or formal verification. The author does not certify this record.

## Frozen family and result

Let B/Q have coefficients `[0,-1,1,-10,-20]`, so `y^2+y=x^3-x^2-10*x-20`. The family contains its usual quadratic twist E_d=B^(d) for every nonzero squarefree integer d, including d=1. Negative and even d are included. The squarefree radicand d is not always the associated fundamental discriminant; the latter is d when d is 1 modulo 4 and otherwise 4d.

The exact local test supplies irreducibility of B[3] and B[7], hence of E_d[3] and E_d[7] for every d. It also supplies a counterexample to inheritance of semistability: E_13 has additive reduction at 13. Consequently changing the prime in the inherited analytic rank one JSW theorem does not by itself cover the full twist family.

There is a useful positive alternative. For p in {3,7}, define the expressly restricted domain

\[
\mathcal D_p=\{d\in\mathbf Z\setminus\{0\}:d\text{ squarefree},\ \gcd(d,11p)=1\}.
\]

For every d in this domain, the local and residual hypotheses below hold. JSW Theorem 7.2.1(ii) then supplies the p part of BSD **conditional on** L(E_d,1) being nonzero. The newer Yan and Zhu theorem supplies a route for analytic rank zero or one under a primitive unipotent image condition; the Tate argument below checks that condition on the same domain. Neither the analytic premise nor a Selmer corank is certified for any new twist in this run. These are theorem application routes with a named missing input, not proofs that the family has low rank.

The run 001 obstruction at 5 remains valid for the irreducibility hypothesis of the selected JSW theorem. It excludes that theorem application at 5, not every theorem at 5. The coordinator separately audits newer results for reducible representations.

## Primary source audit

1. Jetchev, Skinner and Wan, *The Birch and Swinnerton Dyer formula for elliptic curves of analytic rank one*, Cambridge Journal of Mathematics 5 (2017), 369 to 434. [Published PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2017/0005/0003/CJM-2017-0005-0003-a002.pdf). Inspected Theorem 1.2.1 with its preceding hypotheses, printed page 370; Theorem 7.2.1(ii), page 422; and the limitations in section 7.4.4, page 429. PDF SHA256 `5a6978afcb2fad9ce4b13a88f9a93ffb77c700082f383f0b6e20980b5e3f7e76`.

2. Xiaojun Yan and Xiuwu Zhu, *Main conjectures for non CM elliptic curves at good ordinary primes*, [arXiv:2412.20078v4](https://arxiv.org/abs/2412.20078v4), January 23, 2026, final version; linked publication in Journal of Algebra, [DOI](https://doi.org/10.1016/j.jalgebra.2026.01.016). Inspected v4 PDF pages 2 and 3 for condition (Im) and Corollary 1.4, page 14 for section 5.1 assumptions, and page 17 for Remark 5.10 and Theorem 5.11 with proof. [Pinned PDF](https://arxiv.org/pdf/2412.20078v4). SHA256 `b0a5a76f0032c188ecbbaf7abd4a5aa9007d1597a9e1261549f0572747b1eb66`. An [author hosted copy](https://xwzhu.xyz/pub/BDP.pdf) provided readable matching theorem locators; the pinned arXiv copy defines this audit. The publication landing page was inspected for bibliographic confirmation; no complete comparison with the typeset article was performed.

3. Milne, *Elliptic Curves*, second edition (2021). [Author PDF](https://www.jmilne.org/math/Books/EC2.pdf). Printed pages 52 and 59 to 61 give invariant changes and reduction criteria; page 103 gives the Tate quotient, the discriminant product in equation (25) and the j expansion in (26); pages 220 and 221 give the Tate module and Frobenius bridges used in run 001. SHA256 `646c0c4f193cdaa35f32c7d60fbd46a75e2f5187db4301810e8613726e3ebbee`. The inference from the Tate quotient to the inertia matrix is spelled out below rather than assigned to an uninspected theorem number.

4. Cremona and Freitas, *Global methods for the symplectic type of congruences between elliptic curves*, Revista Matematica Iberoamericana 38 (2022), Lemma 2.2(2), equation (2.5), printed page 8. [Published paper](https://ems.press/content/serial-article-files/38965). The twist identity is already inspected and recorded in [run 001](../findings/run-001-representation-obstruction.md). This run reuses that fixed dependency and gives its elementary consequence below.

The entire proofs of the Iwasawa theory theorems and their dependencies were not rechecked in this bounded source audit. Search results, other agents' claims and article abstracts are not substituted for the inspected theorem statements.

## Theorem boundaries

The inherited JSW Theorem 1.2.1 requires E/Q semistable, good reduction at p, residual irreducibility and analytic order exactly one. It permits p at least 5, and p=3 with the extra zero trace condition in the supersingular case. B is ordinary at 3 and 7, but that does not remove global semistability. The counterexample below invalidates automatic passage of this theorem to all E_d.

JSW Theorem 7.2.1(ii) instead assumes p odd, good ordinary or multiplicative reduction at p, irreducible E[p], L(E,1) nonzero, and some multiplicative prime q at which E[p] is ramified. It has no global semistability hypothesis. Its conclusion is

\[
v_p\bigl(\#\Sha(E/\mathbf Q)[p^\infty]\bigr)
=v_p\left(\frac{L(E,1)}{\Omega_E\prod_{\ell\text{ finite}}c_\ell(E)}\right).
\]

Here the Néron period includes all real components, as in the run 001 audit. Irreducibility makes the rational torsion order prime to p. The separate analytic rank zero theorem gives rank zero and finite Sha once the nonvanishing premise is established. A prime valuation equality is not the full coefficient formula.

Yan and Zhu Theorem 5.11 uses p>2 and good ordinary reduction. Conservatively retain the residual irreducibility assumption explicitly present in section 5.1, even though the short statement in section 5.3 and Corollary 1.4 do not repeat it. For r in {0,1}, the theorem relates analytic rank r, p primary Selmer corank r, and algebraic rank r together with finite Sha. Under any of these conditions the p part formula also follows if

\[
\text{(Im)}\qquad
\exists\tau\in G_{\mathbf Q(\mu_{p^\infty})}:
T_pE/(\rho_E(\tau)-1)T_pE\text{ is free of rank one over }\mathbf Z_p.
\]

This route has no semistability assumption. Its valuation conclusion uses the full leading term `L^(r)(E,1)/(r! Omega_E Reg_E)` and the BSD product, including the torsion denominator. This audit uses the implication from a certified analytic rank in {0,1}, not an inference from an uncomputed Selmer corank or a database rank. The primitive quotient in (Im) is essential; irreducibility alone is not silently substituted for it.

## Local and residual applicability arguments

Exact counts give `a_2(B)=-2`, `a_3(B)=-1`, and `a_7(B)=-2`. The good Frobenius polynomial at 2 modulo 3 has discriminant `4-8=2 mod 3`, a nonsquare. The good Frobenius polynomial at 3 modulo 7 has discriminant `1-12=3 mod 7`, also a nonsquare. Therefore neither B[3] nor B[7] has a Galois invariant line over its coefficient field. This argument proves irreducibility, not surjectivity.

For either odd p, `E_d[p] = B[p] tensor chi_d`. Multiplying every matrix by a nonzero scalar preserves exactly the same invariant subspaces. Irreducibility therefore survives for **every** squarefree d, even if d contains p. The additional good reduction condition at p is separate. When p does not divide d, chi_d is unramified at p, the twist remains good, and `a_p(E_d)=chi_d(p)*a_p(B)` is a p unit. Thus E_d is ordinary at p. A ramified twist at p is not admitted by the good ordinary theorem merely because its representation is irreducible.

The base invariants are `c4=496`, `c6=20008`, `Delta=-11^5`. At 11, c4 is a unit and `-c6=1 mod 11`; the minimal curve has split multiplicative reduction. A Tate parameter q_T therefore has valuation 5 by Milne's discriminant product. For p=3 or 7 write `q_T=11^5*u`, with u a unit. Over the maximal unramified extension of Q_11, units have p power roots by Hensel's lemma. Torsion in the Tate quotient is represented by compatible roots of unity and roots of q_T. Tame inertia acts in this basis as

\[
\rho_{B,p}(\sigma)=
\begin{pmatrix}1&5t_p(\sigma)\\0&1\end{pmatrix},
\qquad t_p:I_{11}\longrightarrow\mathbf Z_p\text{ surjective}.
\]

This follows directly by adjoining compatible p power roots of the uniformizer. Since 5 is a p unit, inertia is nontrivial modulo p. For d in D_p the quadratic character is unramified at 11, so the twist has the identical inertia action and retains multiplicative reduction there. This proves the extra q=11 condition in JSW.

Choose sigma with `t_p(sigma)=1`. Inertia at 11 fixes every p power root of unity because p is different from 11. Hence sigma lies in `G_Q(mu_(p^infinity))`. The image of `rho(sigma)-1` is the first coordinate line since 5 is a unit. Its cokernel is free of rank one. This is the required (Im) witness for Yan and Zhu. The argument applies unchanged to an unramified nonsplit quadratic twist at 11; the unramified character is trivial on inertia. No claim about full p adic image is needed.

## Discriminating experiment and semistability failure

The [exact experiment](../experiments/run-003-route-b/README.md) enumerated points and computed invariants with integer arithmetic. It ran with Python 3.14.6, exited 0 and took 0.019833041995298117 measured seconds. The source, deterministic output and author receipt are retained there. There was no randomness or approximate arithmetic.

For d=13 an integral twist model is `[0,-52,0,-27040,-2777008]`. Its invariants satisfy

\[
v_{13}(c_4)=2,\qquad v_{13}(c_6)=3,\qquad v_{13}(\Delta)=6.
\]

The discriminant valuation is below 12, so this integral model is minimal at 13: a reduction to a smaller integral discriminant would decrease valuation by a positive multiple of 12. Its reduced equation is `Y^2=X^3`, a cusp in characteristic 13, hence the reduction is additive. This single member disproves the proposed inference that semistability of B passes to its entire twist family. At 3 and 7 this model remains good ordinary, with traces respectively negative one and two. Thus the local failure is specifically global semistability; it is not a failure of the replacement theorem's good ordinary or irreducibility inputs.

The experiment did not compute the conductor at 2 for arbitrary d, classify all semistable twists, compute any L value, or determine any Sha order. No universal assertion about twist ranks follows from it.

## Missing input, rejected routes and next test

The cheapest next application test is to select one d in D_3 or D_7, determine its exact functional equation sign, and certify the appropriate central value or derivative. If the sign is positive, use exact modular symbols or a rigorous nonzero enclosure for L(E_d,1); a positive sign alone is insufficient. If the sign is negative, L(E_d,1)=0 and the rank zero branch is unavailable; a derivative enclosure excluding zero can instead supply the analytic rank one premise of Yan and Zhu. No sign or analytic rank is assigned to d=13 by this record.

The tested local evidence cannot distinguish rank zero from rank two, or rank one from rank three. An exact Mordell Weil rank without a finiteness result is not the compound algebraic hypothesis in Theorem 5.11. The run 002 small conductor derivative inequality must not be transferred without recalculating conductor, coefficient data and error bounds.

The proposed domains omit twists ramified at 11 or at the selected p. This is a deliberate audited subset, not a claim that all omitted twists are inaccessible to every theorem. The complete pilot family also contains possible analytic ranks above one, to which the audited low rank formulas do not apply. The 2 part, 5 part, other prime parts and higher rank cases remain distinct obligations. Search located newer ordinary results and unrelated claims of general BSD progress; only the pinned primary statements above enter this record. Further searches or a full publication comparison can broaden the theorem audit in a later assignment.

Recommendation to the coordinator: retain Route B as a concrete low rank theorem coverage study, with one certified analytic premise as its next discriminating task. Compare its established theorem boundaries with the higher rank route before asking the director to choose. Separate referee review of this exact source application, the Tate inertia bridge and independent finite arithmetic is required before integrating the claim.
