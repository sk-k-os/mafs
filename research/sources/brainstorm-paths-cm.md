# CM strategy brainstorm: one ordinary prime before any global claim

Status: exploratory source audit and feasibility screening, 2026-10-29. This is not selection of Run 005 or Q004.2, a complete applicability audit, a new theorem, or a computational certificate. Author: analytic_sources. Independent review is assigned separately. Only the coordinator publishes.

## Proposed mechanism and director explanation

For E: y²=x³−7611²x, use the CM main conjecture through an exact higher weight Hecke value to try to eliminate the 5 primary part of Sha. This curve has separately reviewed algebraic and analytic rank two and trivial 2 primary Sha. Those results neither determine its odd primary parts nor prove full BSD.

Plain English: the extra symmetry of this curve supplies an arithmetic test for one prime at a time. Passing the test at 5 could remove the possible obstruction built from powers of 5. It would not remove obstructions at other primes, determine the full leading coefficient, or provide a general solution for curves without that symmetry. The immediate practical question is whether the exact test can be computed without building a number field with over 25 million dimensions.

## Inspected primary inputs

Access date for both sources: 2026-10-29. The versioned arXiv PDFs, not abstract summaries, were inspected. PDF internal generated dates differ from version metadata; version identifiers fix the references here.

S1: Coates, Liang, Sujatha, *The Tate-Shafarevich group for elliptic curves with complex multiplication II*, [arXiv:1005.4206v2](https://arxiv.org/pdf/1005.4206v2), submitted 2010-05-27. Printed pp12–15, Section 4, Lemma 4.4 and equations 69–74 give the trace construction for fourth power free nonzero D in y²=x³−Dx, with D divisible by an odd prime. The field H has degree φ(f)/8. Printed pp18–19, equations 76–78 use the least positive real period Ω⁺ and c_p⁺=(Ω⁺)^(−p)L(ψ̄_E^p,p), and the corrected trace formula. Printed p19 corrects an extraneous factor w in paper I. Theorems 1.2–1.3 concern six specified curves, none ours. Theorem 1.1 only bounds the ordinary prime corank by (1/2+ε)p−rank eventually; that bound does not force zero.

S2: Coates, Liang, Sujatha, *The Tate-Shafarevich group for elliptic curves with complex multiplication*, [arXiv:0901.3832v1](https://arxiv.org/pdf/0901.3832v1), submitted 2009-01-24. Printed pp3–5 fix K, End_K(E)=O_K, a global minimal equation and its Néron period lattice Ω∞O_K; Ω⁺=α(E)Ω∞. Theorem 2.2, printed p5, assumes E/Q, good split p, p∤wα(E), and analytic/algebraic rank parity. It gives finite Sha(E/K)(p) when v_p(c_p⁺)<g+2; equality v_p(c_p⁺)=g gives triviality provided p∤6#E(F_p). Printed p13, Lemma 3.2 gives f=(1+i)^3 rad(D) for D≡1 mod4. Printed p16 gives α=1 for D>0. This theorem statement was also inspected as a page image. Its Iwasawa dependency is Theorem 2.5, printed p8. Proofs of all dependencies were not reaudited.

## Exact candidate bridge and first missing premise

Here K=Q(i), D=7611²=57,927,321=3²43²59². D is fourth power free, although not squarefree. The endomorphism i acts by (x,y)↦(−x,iy). For the paper's positive D normalization α=1 and w=4. The rank parity premise is supplied by the separate Run 003 and Run 004 records, not by BSD.

Candidate prime p=5 is split, good, and coprime to 6wα. Direct enumeration over F5 gives the seven affine points (0,0),(1,0),(2,1),(2,4),(3,2),(3,3),(4,0), hence #E(F5)=8 including infinity. This exact five element check was performed with Python integer arithmetic during the brainstorm; no numerical Hecke value was computed.

Conditional on the exact normalization and theorem applicability being independently audited, an exact value v5(c5⁺)=2 would imply Sha(E/K)(5)=0. A value v5(c5⁺)=3 would imply finiteness, not triviality. Restriction followed by corestriction multiplies by [K:Q]=2, so these conclusions pass to the 5 primary subgroup over Q. The first missing mathematical premise is the exact valuation of c5⁺. Neither the positive L'' interval nor a real BSD quotient supplies it: c5⁺ is a different Hecke value, not L''(E,1)/Ω.

Before certifying this bridge, audit the Néron differential and any change from a global minimal model over K. A change supported above 2 would preserve a 5 valuation, but that observation is not a substitute for documenting the change. Ω⁺ is the least positive real period; do not substitute an integral over both real components without tracking its factor.

## Cheap feasibility screen and narrowly specified test

The source formulas yield conductor ideal f=(1+i)^3·7611. Since 3,43,59 are inert in Q(i),

φ(f)=4(3²−1)(43²−1)(59²−1)=205,793,280,

and [H:K]=φ(f)/8=25,724,160. This integer calculation was performed. A proposal requiring an explicit full defining polynomial is therefore rejected as a cheap next step. This degree is a warning about that representation, not a complexity lower bound or impossibility theorem. No field was constructed and no cost estimate in money is asserted.

There is a smaller target, but no efficient method for obtaining it has yet been established. Choose f=2(1+i)7611, so β=fα/(1+i)=2·7611. From the paper's W'=V, V'=2W³ and V²=W⁴−D, direct differentiation gives

A1(W)=V'''=24W⁵−12DW.

The corrected equation 77 then specializes to

c5⁺=±[Tr_H/K(ρ⁵)−(D/2)Tr_H/K(ρ)]/(2·7611)^5.

The sign does not affect the valuation. All displayed denominators are units at 5. The trace lives over K; a certificate must track the selected prime above 5 and the rationality of c5⁺. A proved compressed trace identity giving these two traces modulo 125 would determine whether c5⁺/25 is nonzero modulo 5, after auditing normalization and integrality. If it is zero, this proposed triviality certificate is inconclusive; modulus 625 could then distinguish valuation three from larger valuation. That failure would not refute BSD or imply nontrivial Sha. If a computed valuation is below two, it instead flags a normalization or computation error against the theorem and established rank. Any additional normalization denominator involving 5 would require extra modular precision; none appears in the displayed formula, but the preceding audit remains mandatory.

The cheapest next gate is documentary and symbolic: find and independently verify a method for these two traces modulo 125 that avoids constructing H. Stop this bounded route if it requires the full 25,724,160 degree field. This is a precisely specified discriminating test, not an assertion that it will be fast or succeed. The low trace formula is a supplementary derivation, separately exposed to the referee.

## Limits, alternative connection and handoff

Even success at 5 leaves every other odd primary group unresolved. Good split primes form only one class; inert supersingular primes and bad primes need separate treatment. Finiteness for each tested primary group is not finite support, and finite support itself must be justified before concluding total finiteness. The asymptotic corank bound in S1 grows with p and supplies neither vanishing nor finite support. A universal result would need a uniform arithmetic mechanism controlling all relevant primes, followed by the leading coefficient identity with proved arithmetic factors.

The computation specialist is examining Castella's generalized Kato classes as the one adjacent mechanism. No conclusion from that route is imported here. The transferable idea beyond CM is a certified arithmetic class or p adic value whose nonvanishing bounds the Selmer group. The explicit Hecke character and Gaussian ray class trace construction are CM specific. Removing CM requires a different theorem and independently checked hypotheses, not reusing this calculation.

Retained objections and corrections: paper II's short recap omits conditions explicitly present in paper I, so this note retains the original parity, nonanomalous and p∤6 requirements. Paper I's trace factor is corrected in II; use equation 77 of II. The tabulated examples do not include D=7611². Original paper I statements about earlier computations are subject to paper II's explicit corrections; no historical table is used as evidence for this curve. No absence of search results is treated as novelty.

Handoff: preserve the rank and Sha assumptions above; first audit minimal differential normalization and the compressed trace feasibility gate. Do not start computation or select a new run from this brainstorm. No full applicability verdict or full BSD claim is made. Await separate review and coordinator checkpoint acknowledgement.
