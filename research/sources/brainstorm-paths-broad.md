# Two mechanisms to investigate beyond the rank two certificate

Date: 2026-10-29. Author: analytic computation specialist. Status: bounded exploratory strategy note for separate review; not a theorem application, selected Run 005, or protected benchmark. Q004.2 remains open. Primary sources inspected on this date. Source proofs have not been audited in full.

## Starting point and target

For E = E_7611: y² = x³ − 7611²x, the campaign records establish algebraic rank two, analytic rank two, and Sha(E/Q)[2∞] = 0, with the qualifications and separate model review in Runs 003 and 004. The exact enclosure for the uncompleted derivative is 15.61 < L''(E,1) < 15.63. It does not compute an odd primary Selmer group, a saturated regulator, or the complete leading coefficient formula.

The full target has three distinct layers: identify the Mordell–Weil rank from the analytic order; prove the entire Sha finite; prove its exact order in the leading coefficient formula. A method that settles only one prime of one curve is a useful local advance, not a route already completing all three layers.

## Mechanism one: construct a nonzero rank two cohomology class

Plain English: construct a special arithmetic object which forces the space of possible global obstructions to have only the two directions already occupied by rational points. Then the remaining obstruction at that prime has finite size. This uses geometry and cohomology to rule out hidden directions instead of extrapolating numerical L values.

Primary anchor: Francesc Castella, [Generalised Kato classes on CM elliptic curves of rank 2](https://web.math.ucsb.edu/~castella/Kato-Schoen.pdf), author PDF dated 2026-02-13. Inspected §1.1–1.3, printed pp.3–6, especially Theorems A, B, C; also located Theorem 6.3.1. Theorem B says κ_p ≠ 0 implies dim_Qp Sel(Q,V_pE) = 2 for CM E, good ordinary p ≥ 5 and positive even analytic order, with its specified auxiliary Hecke characters. Exact character requirements are Eq.(1.5) and Theorem A(i),(ii), alongside §1.1's conductor, central character, infinity type and class number hypotheses. No auxiliary characters have been constructed here. The converse assumes Selmer dimension two and nonzero restriction at p. Section 1.3 places nonzero κ_p in the kernel of that restriction. Theorem C assumes primary Sha finiteness; using it to prove that finiteness would be circular. Theorem A's characteristic ideal identity is stated after tensoring with Q_p, so it is not an integral BSD formula.

The present curve passes the evident CM, rank and sign gates. At p = 5 it has good ordinary reduction; K = Q(i) has class number one. These checks do not discharge the character construction or class nonvanishing obligations. In particular, our complex L'' certificate does not imply κ_5 ≠ 0 by the inspected theorem.

The precise missing first bridge is an independent certificate that the constructed κ_5 is nonzero. If obtained, the theorem and the known rank two force the p primary Sha corank to be zero. Its finite generation properties then imply Sha(E/Q)[5∞] is finite. No exact order follows merely from this dimension argument.

Cheapest discriminating test: before computing any diagonal cycles, identify an explicit computable detector for the required class, with a theorem proving that the proposed nonzero output detects κ_5. A usual local logarithm at p cannot do this, since the class lies in the restriction kernel. A calculation which merely reconstructs a nonzero logarithm of a known rational point fails this test. A rigorously established κ_5 = 0 would defeat this particular nonvanishing strategy at 5; it would not refute BSD. No such detector or calculation was supplied in this discussion.

Compared with this geometric construction, the CM specialist's exact Coates–Liang–Sujatha valuation criterion specifies a more concrete first calculation. Its input is a higher weight Hecke value, not our complex second derivative. The companion CM note must govern that criterion and its rank conventions. A concrete target is not yet a feasible computation: that note reports a trace field of degree 25,724,160 and requires a compressed trace method before attempting c_5. No scalable method was established. Neither calculation by itself addresses infinitely many primes.

The next bridges would be an integral class index or Euler system bound with every local correction accounted for, a comparison with the real leading coefficient and saturated regulator, and a uniform source of a finite set of possible prime divisors. To become general BSD, the construction would additionally need a replacement in arbitrary rank and outside CM. These are missing research statements, not consequences asserted here.

Rank convention check: rank_Z E(Q) = 2. Over K = Q(i), rank_Z E(K) = 4, because the quadratic twist by −1 has the identical short equation and the two eigenspaces each have rank two. Hence rank_Z[i] E(K) = 2. Castella's conclusion concerns Sel(Q,V_pE), not the full representation's Selmer group over K. A CM character component over K must be distinguished from that full group.

## Mechanism two: force derived Heegner classes to come from points

Plain English: special points over larger number fields generate enough cohomology classes to describe the obstruction. Prove that the relevant classes actually descend from rational points with the required divisibility. This could turn a structural description of the obstruction into a proof that its infinite part is absent.

Primary anchor: Chan-Ho Kim, [On the arithmetic of Tate–Shafarevich groups via Kolyvagin's conjecture](https://arxiv.org/html/2609.15328v2), preprint v2 dated 2026-10-24. Inspected Theorem 1.1, §1.1.2–1.1.3 and §1.5. It assumes non-CM E, good p ≥ 5, surjective residual representation and Selmer corank at least two. Global semistability is required for the supersingular case. Theorem 1.1 equates primary Sha finiteness with specified derived Heegner points belonging to p^∂(E(Q) + p^k E(K[n])). Its k must annihilate the finite Selmer quotient to the stated precision; the chosen points must be the prescribed generators. Supersingular auxiliary K has odd discriminant below −4, 2 and p split, an even number of inert conductor factors, a ramified conductor prime if the inert part is empty, and twist analytic rank at most one. Ordinary hypotheses are separate in Remark 1.9. The advertised finite field verification remains conditional on effective reductions of Mordell–Weil groups over ring class fields.

Adjacent computational framework: Kim, [The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf), author version dated 2025-05-12, Theorem 1.1, printed p.2. For p ≥ 5, semistable reduction at p and surjective residual representation, an Iwasawa main conjecture after inverting p, or analytic rank at most one, gives nontriviality of Kato's Kolyvagin system and a description of the primary Selmer structure through Kurihara numbers. The stated formulas for Mordell–Weil rank and primary Sha order additionally assume primary Sha finiteness. This is an adjacent tool to determine Selmer data, not permission to identify Selmer corank with Mordell–Weil rank.

The exact missing bridge is a geometric or arithmetic proof of the derived point membership condition independent of assuming primary Sha finiteness. Repeating the equivalence is not that proof. A second missing bridge would make the resulting bounds uniform in p, with controlled integral indices, so they furnish a finite support bound and eventually the BSD order rather than merely primary finiteness.

Cheapest discriminating test: audit whether the chosen proposed construction can produce the theorem's required generators, precision k and ∂, and certify their membership using independently known point lattices. If the proposed algorithm requires a complete unknown Mordell–Weil group over a large ring class field or assumes the desired primary finiteness to certify its generators, the bounded test fails. Only after a feasible certificate is specified would selecting a small non-CM contrast curve be justified. No contrast curve or family is selected here.

The current curve is excluded by non-CM and surjectivity hypotheses. Its additive bad reduction also excludes the supersingular semistable route. The global semistability condition must not be incorrectly imposed on every ordinary case. Neither this preprint nor the adjacent modular symbol theorem has been promoted to a campaign dependency.

## What would make either mechanism a path to full BSD?

Finite calculations at p = 5, 13, or any prescribed finite list leave untested primes. Even proving every individual Sha[p∞] finite leaves the possibility of infinitely many nonzero primary parts. The elementary torsion group direct_sum_p Z/pZ demonstrates that logical gap; it is not asserted to occur as an elliptic curve's Sha.

A sufficient global interface would be an independently constructed nonzero integer M annihilating Sha, together with finiteness of the relevant M Selmer group. The standard Selmer exact sequence would then force Sha finite and confine its support to divisors of M. Merely naming M, or setting it equal to a BSD predicted order, restates the missing problem. The promising source would have to be an integral geometric or Euler system construction yielding actual annihilator information. No such M is constructed here.

After finiteness, the exact BSD formula still requires the complete lattice index, local factors and normalized leading coefficient identity. Agreement of approximate numerical ratios is insufficient. A uniform annihilator would establish finiteness but still not prove that identity.

The CM pilot is useful because its split character theory exposes computable primary tests and a concrete class construction. It also conceals generic difficulties: non-CM representations do not split into Hecke characters, the current rank two construction supplies no arbitrary rank determinant, and ordinary split primes omit supersingular and bad primes. Completing this curve would therefore be substantial evidence about methods, not a proof mechanism automatically covering all elliptic curves over Q.

## Handoff and failed shortcuts

No new mathematical claim or computation is promoted. The substantive near term choice is between an exact CM valuation certificate and auditing whether a computable detector for the generalized Kato class exists. The broader derived point mechanism remains a source and feasibility audit. Q004.2 remains for the director.

Rejected shortcuts preserved: complex L'' nonzero does not establish generalized Kato nonvanishing; the local logarithm of that kernel class is not a detector; Theorem C cannot supply its own finiteness premise; Kim's equivalence is not a proof of its membership condition; every primary part finite does not prove finite support; naming an annihilator without an independent construction is circular; repeating the CM pilot does not resolve generic non-CM or arbitrary rank obstructions.
