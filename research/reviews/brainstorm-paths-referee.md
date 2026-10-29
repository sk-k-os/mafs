# Skeptical review of exploratory BSD paths

Date: October 29, 2026. This is the director's authorized research discussion, not Run 005. Q004.2 remains open. The bounded discussion began at 18:07:55 UTC; author research stops at 18:16, with submissions by 18:17 and this review by 18:19. No next research branch starts here.

This is calibration, not a protected benchmark, a full proof audit or qualified human mathematical review. I received raw proposals and primary source locators before any other verdict. Model family, sources, tools and filesystem are shared; the exchange of objections is useful collaboration, not independent statistical authority. The frozen Run 004 result supplies rank equality two for E7611 and the earlier trivial 2 primary Sha statement, with its recorded trust boundary. No stronger starting result is assumed.

## Questions fixed before evaluating proposals

For every path, identify whether its conclusion concerns one curve, a restricted family or every elliptic curve over Q; one prime, a finite range or all primes; rational Selmer rank, primary finiteness, full finiteness or an exact leading coefficient. Require an independently established witness for the missing implication. A theorem equivalent to the desired conclusion is useful only when its alternative condition can be proved without assuming that conclusion.

The source statements I independently screened include Coates, Liang and Sujatha I Theorem 2.2 and II section 4; Castella's generalized Kato Theorems B and C; and the opening assumptions of Kim version 2. This is targeted scope screening. Their complete proofs, computational implementations and present applicability to every proposed auxiliary datum were not audited.

## Global finiteness and coefficient gates

The implication from finite primary components to finite full Sha is invalid. As an elementary falsifier, the torsion group direct sum over primes of (Z/pZ)^2 has finite primary components and admits a componentwise nondegenerate alternating pairing into Q/Z, but is infinite. Even square primary orders and pairing structure do not establish finite support.

One precise sufficient certificate would be a nonzero integer M, constructed independently of the BSD formula and the unknown Sha order, such that M annihilates Sha(E/Q). Then Sha equals Sha[M], which is finite as a quotient of the finite M Selmer group. Conversely a finite Sha has such an exponent. Thus naming M is an equivalent reformulation under standard Selmer finiteness, not a new mechanism. A claimed construction must say where M comes from and why it bounds every torsor, including arbitrarily large primes and primary exponents.

Full BSD requires more than this finiteness gate. Rational cohomology discards finite torsion. Integral control at selected primes does not supply finite support. To combine prime valuation identities into the complex leading coefficient identity, one also needs a common normalized leading term, its rationality and the correct integral lattice, periods, regulator, torsion and local factors. A numerical ratio cannot supply those missing premises.

## Initial path assessments

### CM special value valuation

Strongest form: use the original CLS theorem to certify one odd primary component by an exact special value valuation. For E7611, the displayed elementary choice p=5 is compatible with CM by Z[i], good split reduction, w=4, alpha=1, even rank parity and #E(F5)=8. The special value is a Hecke character power at s=5 normalized by the least real period; it is not the Run 004 complex second derivative divided by the full real period. The original theorem retains hypotheses suppressed in a later abbreviated summary. [CLS I, Theorem 2.2, printed page 5](https://arxiv.org/pdf/0901.3832v1).

The missing witness is the exact valuation. A value two would give triviality under the extra hypotheses; a value three still gives finiteness. A residue computation modulo 125 can identify valuation two but cannot distinguish three from larger values. A zero residue modulo 125 is therefore inconclusive, not a rejection of finiteness. Precision modulo 625 can distinguish valuation three if all denominator normalizations are units at 5.

The proposed division field degree over 25 million is a warning against naive construction, not an impossibility lower bound. The strongest practical version asks for selected traces or a compressed exact method. Its first falsifier is a missing normalization, nonunit denominator or precision certificate in the proposed trace algorithm. Verdict: **exploratory plausible for a one prime certificate; inconclusive as a full BSD path**.

### Generalized Kato class

Strongest form: under the precise CM, ordinary and auxiliary character hypotheses, independently certify a nonzero generalized Kato class. Castella's Theorem B then bounds the rational Selmer dimension by exactly two. With the known algebraic rank two and standard Selmer finite generation, this would force finiteness of the selected primary Sha. The converse has an extra localization condition. Theorem C already assumes primary Sha finiteness and cannot be used to prove that same premise. [Castella, Theorems B and C, printed pages 5 and 6](https://arxiv.org/pdf/2204.09608).

The weakest link is a usable exact nonvanishing witness for the class, independent of the desired Selmer or Sha conclusion. The cheapest falsifier is to trace every proposed computation of the class or localization and identify any invocation of primary finiteness or a conjectural rank two p adic BSD formula. Even success gives no primary order, integral index or finite prime support. Verdict: **exploratory plausible as a structural rank two route; the circular use of Theorem C is rejected**.

### Non CM derived point or modular symbol route

Strongest form: on a curve satisfying the actual theorem hypotheses, prove an arithmetic membership or nonvanishing criterion independently and use the theorem to control a primary Selmer or Sha component. This is a potentially useful comparison of mechanisms beyond CM, rather than a transfer justified by similar rank alone.

The present E7611 is CM. Kim version 2 assumes non CM and residual surjectivity throughout its introduction. That direct transfer fails. The author reports a further correction: global semistability is required in the supersingular branch, while the ordinary branch has separate conditions; one should not overstate a universal semistability obstruction. [Kim pinned version 2, opening section 1](https://arxiv.org/html/2609.15328v2).

The cheapest falsifier is a hypothesis table for the proposed comparison curve and the exact prime before computing any membership criterion. An equivalence alone does not establish its difficult side. Verdict: **direct application to E7611 rejected; a properly scoped non CM comparison remains exploratory plausible**.

### Integral higher rank construction and annihilator interface

The strongest long term program seeks arithmetic classes with norm relations and explicit reciprocity laws that control an integral Selmer lattice, then converts their indices into compatible leading term information. The rank two CM class provides a concrete laboratory for asking which rational statements lack integral refinements. This is a research proposal, not an available general theorem.

Its weakest links are the nonzero higher rank object, integral primitivity, local correction terms, compatibility across primes and a mechanism valid for arbitrary rank and non CM curves. The cheapest falsifier is to demand one precise lemma turning the currently available rational class into an integral index or a common annihilator without assuming BSD. If that lemma is merely the desired conclusion in new notation, the proposal has not advanced. Verdict: **inconclusive as an executable full BSD path; useful as an explicit obstruction framework**.

### Saturation and exact arithmetic preparation

The strongest form independently verifies a full Mordell Weil basis and local arithmetic, eliminating index and normalization ambiguity from a future coefficient comparison. This is concrete progress for one curve. It cannot bound every Sha component merely because a numerical BSD quotient is close to an integer. The cheapest falsifier of such an overclaim is to remove the conjectural coefficient identity from the argument and check whether any asserted Sha order remains justified. Verdict: **exploratory plausible for preparation; inference of full Sha from a numerical ratio rejected**.

## Submission reconciliation and recommendation

Final specialist artifact hashes and any corrected proposals will be appended before freezing. No new mathematical result is asserted by the preceding path assessments.

### Frozen submissions and corrections

Reviewed `research/sources/brainstorm-paths-cm.md`, SHA256 `9269c128fe79d5474653faec556ae68c9229e7c018b990c288ff83fa4f3e947d`, and `research/sources/brainstorm-paths-broad.md`, final SHA256 `97efb4ad86f2a3f40c347ed2dba18679ed859a376a0e87e94bccbe3eb683e00c`. The earlier broad draft hash `01fa8eb2facef503a9e9b4c2cb07985dbaf04496b8dde23231831218978dedaf` was superseded by an explicit feasibility correction: CLS offers a more concrete target, not an already feasible bounded computation. No proof or application verdict is inferred from either author note.

The CM note preserves the original theorem's extra hypotheses, the later correction to the trace factor, the distinction between its model family and tabulated examples, and the p=5 precision issue. I independently reconstructed the derivative polynomial: from W'=V, V'=2W³ and V²=W⁴−D, one gets V'''=24W⁵−12DW. Dividing the corrected trace by 4! gives the stated first and fifth trace combination. I also checked the integer field degree multiplication. These symbolic and elementary checks support the stated feasibility question; they do not supply either trace or a certified c5 value. Minimal differential normalization over K and the proposed compressed modular trace algorithm remain explicit gates.

The broad note adds an important sharper falsifier to the Kato path: the class lies in the kernel of restriction at p, so the ordinary local logarithm of that class cannot be the proposed nonzero detector. A nonzero local logarithm of a known point instead witnesses a different direction. This corrects a tempting but invalid shortcut. Its discussion also keeps the rank over Q equal to two separate from the rank over Q(i), which is four over Z and two over Z[i]. The rational representation in Castella's conclusion is over Q.

The original broad scope warning about Kim is refined, not erased: the current curve fails the non CM and residual surjectivity gates; the supersingular branch also has a semistability requirement, while the ordinary branch must be checked under its own conditions. I independently screened the opening non CM and image assumptions. The detailed membership algorithm and the adjacent modular symbol theorem were not fully reaudited here. Their status remains exploratory and conditional on the exact source hypotheses. Formulae stated after primary Sha finiteness cannot be used to infer that premise.

### Director recommendation

Ask for a **feasibility witness before a large computation**, with two distinct options and no implied selection:

1. For the CM valuation route: can the team derive and independently check the two required traces modulo 125, or modulo 625 when needed, without constructing the full degree 25724160 field and without an untracked denominator? The useful failure output is the exact missing compressed trace identity or algorithm. Selecting p=5 alone does not solve this problem.
2. For the generalized Kato route: can the team identify an explicitly computable functional that detects this global kernel class, prove that it does so, and evaluate it without assuming primary Sha finiteness? If the proposed detector vanishes by construction or uses Theorem C's premise, stop that attempt and preserve the reason.

The first is the more concrete immediate target; the second is the more structural higher rank lead. Neither is currently demonstrated to fit a short computation budget. A non CM comparison should wait until its own independent membership certificate is specified, rather than selecting a curve merely because it has rank two.

Maintain one separate global question for every local success: **what independently constructed object controls the untested primes and their exponents, and how does its integral index recover the normalized complex leading coefficient?** An answer limited to more local tests, a rational Selmer dimension or a BSD predicted order fails that question. This is the weakest common bridge toward full BSD. No inspected source in this discussion closes it for the pilot, much less uniformly for arbitrary rank and non CM curves.

Final exploratory verdict: the two CM mechanisms are plausible local research directions with different exact witnesses; direct transfer of the non CM theorem to this curve and the identified circular shortcuts are rejected; an executable route from these mechanisms to full BSD remains inconclusive. A complete claim would still need universal curve and rank coverage, finite support and primary bounds, and the full leading coefficient comparison. Q004.2 is not answered by this review. The coordinator must relay the director choices and checkpoint the records; no new branch starts automatically. Awaiting confirmed synced publication before ending.

### Synthesis coherence review

After freezing the evidence first assessments, I read `research/findings/brainstorm-paths-synthesis.md`, SHA256 `31e7ad1e9bb674a89ccdd4d57cccfedf549cac429e102a64427db72e66178292`. Its mathematical scope is coherent with the specialist records and this review. It preserves local versus global conclusions, finite support and coefficient obligations, the precise valuation target, the unresolved class detector, the non CM exclusion and the open director choice. No new research is authorized or mathematical acceptance implied.

One minor wording objection was sent to the coordinator: the phrase “fastest checkable next advance” claims a relative speed not established by these records. “Most concrete next feasibility test” is supported. This does not change the mathematical assessment; the concrete target is not yet a demonstrated efficient algorithm. Any revised synthesis hash should be recorded with the final checkpoint.

Resolution at final freeze: the coordinator made that wording amendment. The final synthesis SHA256 is `3cbfafa761dcd57435228c35e225833790116bb67d411bf5ac4b5c9deee176a3`, independently read and confirmed. The minor objection is resolved. Final synthesis verdict: exploratory scope coherent, with all missing bridges and director decisions retained. No further research or revision is planned; awaiting the coordinator checkpoint acknowledgement.
