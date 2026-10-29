# Run 003 separate referee report

Reviewer: specialist referee agent. Date: October 29, 2026. This report reviews theorem scope, exact applicability arguments and finite arithmetic. It is a calibration observation, not a benchmark, a formal proof certificate or an external human review. No other Run 003 verdict was read before this report. Authors and referee share the model family, source access, tools and filesystem; this is separation of responsibilities and implementations, not statistical independence.

## Review contract and source coverage

The predeclared failure tests are in [the calibration record](run-003-calibration.md). I inspected primary theorem statements and nearby assumptions myself, including RSY Theorem 1 and its full short proof, Dujella, Janfada and Salami's descent normalization, JSW Theorem 7.2.1, Yan and Zhu version 4 section 5.1 and Theorem 5.11, Castella, Grossi and Skinner version 2 Theorems A and D, and Keller and Yin version 2 Theorem 4.2.1. The source publications and arXiv version histories were checked on October 29, 2026. Entire proofs of the cited Iwasawa theory results and all their dependencies were not reverified. A current source check does not establish an exhaustive literature frontier.

The referee implementation in [check.py](../experiments/run-003-referee/check.py) was written independently without importing author code. It uses Python integers and exact rational arithmetic. It computes no analytic rank or L value and gives no formal verification. Frozen output and execution receipt are linked below when all submitted artifacts have been received.

## Route B verdict

Reviewed artifact: `research/sources/run-003-route-b.md`, SHA256 `abfd0d36f6b3a60195d658ead3a80aaeb741163516c65c0a2c2a16f222da0ba4`.

Verdict: **pass as a conditional theorem application route and local obstruction analysis**. This is not a certification of an analytic premise or a full BSD formula for a new twist.

The Frobenius discriminants at 2 modulo 3 and at 3 modulo 7 independently certify residual irreducibility. Scalar quadratic twisting preserves the invariant subspaces, so this part is uniform in the twist. For the explicitly restricted squarefree domains with `gcd(d,11p)=1`, good ordinary reduction at p follows from unramified twisting and the nonzero traces modulo p. These are separate arguments; irreducibility alone does not imply good reduction.

The Tate argument closes the residual ramification condition rather than merely citing multiplicative reduction. At 11 the base curve has split multiplicative reduction and Tate parameter valuation 5. Inertia has a primitive upper triangular entry `5*t_p` at p equal to 3 or 7. Unramified twisting leaves this inertia action unchanged. The tame character onto Z_p permits an element whose matrix minus identity has primitive image of rank one. Inertia at 11 fixes all p power roots of unity, placing this element in the cyclotomic kernel required by condition (Im). Thus the same argument supplies both JSW's residual ramification and Yan and Zhu's integral quotient condition. It does not prove a full image assertion, and none is needed.

JSW Theorem 7.2.1(ii), printed page 422, indeed has no global semistability hypothesis. It does require nonzero L(E,1), which remains unproved here. Yan and Zhu version 4 Theorem 5.11 relates analytic order r, Selmer corank r, and the compound condition of Mordell Weil rank r plus finite Sha for r in {0,1}; the record conservatively retains section 5.1 residual irreducibility. An exact Mordell Weil rank alone is not the stated compound premise. Its p part formula additionally requires (Im), supplied above. [JSW primary paper](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2017/0005/0003/CJM-2017-0005-0003-a002.pdf); [Yan and Zhu pinned version](https://arxiv.org/pdf/2412.20078v4).

The d=13 discriminant valuation 6 and c4 valuation 2 at 13 prove minimal additive reduction there. The cusp can also be read directly in characteristic 13. This falsifies inherited global semistability without excluding the replacement ordinary theorem. The author's scale 2 integral model is valid for point counts at 3; using the unrelated scale 6 short model there would have been invalid. No such invalid count occurs in the frozen candidate.

No material amendment is required for this artifact. Remaining input: certify an analytic order of zero or one, or another exact premise actually named by the theorem, for a selected twist. No particular order is inferred for d=13. The 2 part, 5 part and other prime parts remain separate.

## Reducible prime exploration verdict

Reviewed artifact: `research/sources/run-003-exploration.md`, SHA256 `f12fbf4a8b648ff2edb756eeb33aacc48da1b4da820f61e2cfb62d5328ca4225`.

Verdict: **pass as a source comparison and conditional local applicability test**, retaining the explicit preprint status of the broader Keller and Yin result. This revision includes the d=5 minimality explanation; the earlier draft hash `818cb760c179a6d4de18f29b23eb37872c0f4551f2c8490025c0b0f2f13427af` is not the object of this final verdict.

The rational 5 torsion line on B becomes a stable line with character chi_d after twisting. If d is prime to 5 and chi_d(5)=-1, the local character is unramified nontrivial and differs both from 1 and from the ramified mod 5 cyclotomic character. This verifies the local restriction in Castella, Grossi and Skinner Theorem A; Theorem D still needs analytic order zero or one. Their Remark 1.2.1 explicitly treats this exact pilot. Thus reducibility invalidates one chosen theorem's hypothesis but is an input to this different published result. [Pinned primary source](https://arxiv.org/pdf/2303.04373v2).

The d=13 local filter passes; d=1 fails this particular character filter. The d=5 displayed integral model has discriminant valuation 6, below 12, so is minimal and has additive reduction; this establishes failure of the good reduction hypothesis rather than just a singular nonminimal reduction. The short model has scale 6, which is a unit at 5, so the good reduction checks at 5 are legitimate.

Keller and Yin version 2 Theorem 4.2.1, pinned printed page 42, removes the local character restriction and retains the rational torsion denominator. It remains recorded as a preprint theorem statement; the separate review has not promoted it to a proved campaign lemma or audited its complete proof. Its rank restriction remains analytic order zero or one. [Pinned primary source](https://arxiv.org/pdf/2402.12781v2).

No particular twist's analytic premise is established by the finite local filter. The resulting formula, if applied, concerns the 5 part, not every prime or any analytic rank two case.

## Route A and final handoff

The Route A frozen statement and final experiment receipt are pending. No verdict for that artifact is implied by the preceding reviews. This section will be appended before the coordinator checkpoint; prior objections and resolutions will remain visible.

### Final Route A assessment, appended after receipt

Reviewed artifact: `research/sources/run-003-route-a.md`, SHA256 `868a60d0288f33a1992931a1a10eb9b3b53a3781d0132e81ee1501b1d50f5628`. The preceding pending status is superseded by this assessment.

Verdict: **pass for Mordell Weil rank exactly two and trivial 2 primary Sha on the stated restricted domain**, using the named descent and Monsky theorems. No analytic rank two or full BSD result is certified.

The exact domain uses coprime positive u greater than v of opposite parity, with q and r prime. The primes are distinct, greater than 3 and congruent to 3 modulo 8. This is a restriction of the published RSY domain. I independently inspected all six pages of that paper. Its omitted uniform specialization descent and inconsistent proof crossreferences were raised before the frozen submission. These objections are resolved for the present claim by the supplementary argument, rather than by pretending to have inspected the omitted proof. Infinitude remains unproved. [RSY primary paper](https://math.colgate.edu/~integers/l20/l20.pdf).

I reconstructed the two point identities and the four square classes directly. In the ordered coordinates given by sign and valuations at r, 3 and q, the classes of T0, Tn, P1 and P2 are independent. The x coordinate descent is a homomorphism on E(Q)/2E(Q), including the exceptional value minus n squared at T0. Consequently its image has dimension at least four. The full rational 2 torsion contributes two dimensions, giving rank at least two. The two torsion classes already have independent images, so the two point classes remain independent modulo the torsion image. This proves their independence modulo torsion; it does not prove that their index in a full basis is one.

The normalization in Dujella, Janfada and Salami is explicitly `#Sel^(2)=2^(s(n)+2)`, and their odd squarefree Monsky matrix has the stated diagonal blocks. At three primes congruent to 3 modulo 8, quadratic reciprocity leaves eight upper triangle patterns, with D2=I and Dminus2=0. My independent binary elimination gives matrix rank four in two cases and six in six cases, hence pure Selmer rank at most two. Combining the lower and upper bounds gives rank two and Selmer dimension four. The exact descent sequence therefore gives Sha[2]=0. Any nonzero element of 2 power order yields a nonzero element of order two, so Sha[2 infinity]=0 as stated. This argument says nothing about odd primary components or global finiteness. [Descent normalization and matrix source](https://cs.uwaterloo.ca/journals/JIS/VOL12/Janfada/janfada3.pdf); [Milne's descent reference](https://www.jmilne.org/math/Books/EC2.pdf).

I also inspected Tian, Yuan and Zhang printed pages 721 to 724 and Burungale and Tian version 2 printed pages 1 and 2. The former defines its analytic invariant to be zero above analytic rank one, and its full rank zero consequence requires a finite Mordell Weil group. The latter's converse requires Selmer corank zero; its density one result is not a statement about a selected exceptional subfamily. Neither audited theorem supplies the missing pointwise rank two conclusion. The positive functional equation sign and the classical low analytic rank implication, combined with rank two, leave analytic order two or a higher even order. They do not certify a nonzero second derivative. [Genus periods primary source](https://web.math.princeton.edu/~shouwu/publications/cn.pdf); [CM converse pinned source](https://arxiv.org/pdf/2506.03465v2).

### Exact execution evidence

The referee's independent program completed with exit status zero, using exact integer and rational arithmetic. Its [captured output](../experiments/run-003-referee/output.json) has SHA256 `411e4361a8b7baf3c1d61218ff60c01e81218605833e7dbe4868c6877b5614f9`; the [program](../experiments/run-003-referee/check.py) has SHA256 `98c027770a20c1bc3c3ac248ec23ef6a80b7d9ac157d13da39b0ec45ae12a797`; the [execution receipt](../experiments/run-003-referee/receipt.json) has SHA256 `d01cb61c5104348a3e396e525c89431554455fa9a5a4fb2644d4a805ed2d87c8`. Inputs were hashed before and after execution and were unchanged. All three author programs were then executed separately; their parsed JSON outputs matched their retained records. The receipt binds those author program and output hashes as well.

The independent checks include n=7611 primality and point identities, four square class independence, the actual sample Monsky matrix and all eight reciprocity patterns, pilot traces and invariants, irreducibility discriminants at 3 and 7, the d=13 scale 2 model traces, and the local character filter at 5 including d=5 additive reduction invariants. Replays do not constitute independent proofs of the general descent theorem, modularity, the Iwasawa results or any analytic rank.

### Preserved objections, limits and handoff

1. The original RSY lower bound omission was a real reconstruction gap. The final restricted family proof closes it through four square classes and an explicit normalization source. The source's omission and crossreference defects remain in the author record.
2. Point membership alone would not prove independence. The descent image calculation supplies the needed additional evidence.
3. A scale 6 short model cannot be reduced naively at 3. The frozen Route B computation instead uses scale 2. The scale 6 model in the exploration is used only at 5, where it is valid.
4. Global semistability does not survive arbitrary twists. The d=13 counterexample blocks the inherited rank one JSW theorem, while the audited replacement ordinary theorem has different hypotheses.
5. Residual irreducibility at 5 is unavailable for the pilot, but this excludes only the earlier irreducible theorem. The alternative Eisenstein theorem uses reducibility and a separately verified local character condition.
6. The bounded literature inspection is not a proof that no stronger result exists. Published status, pinned version and preprint status remain distinct from a complete proof audit.

All three route conclusions are suitable for a director comparison with these limits intact. Route A offers an exact algebraic rank two family and a sharply stated analytic second derivative task for n=7611; the full Sha and leading coefficient obligations remain afterward. Route B and the 5 part exploration offer different low rank theorem applications, each still requiring a certified analytic premise. No route is automatically selected or launched. No external human checker or formal proof service participated. The coordinator may integrate this report into the decision packet, but should preserve the exact hypotheses and avoid interpreting separate agent agreement or Git publication as mathematical certification. Awaiting the coordinator's confirmed synced checkpoint before ending this assignment.

### Integration coherence review

After completing the mathematical conclusions above, I read the coordinator's comparison and director packet. The reviewed integration artifacts are `research/findings/run-003-comparison.md`, SHA256 `e8321b9c6ce64fb6a080c49d694a20254fb15c3b5bb20447daf624ea507f9a89`, and `research/sessions/run-003-director-packet.md`, SHA256 `1b471de062bf04488a2e6d8ff582f710bf5e2754cd0477e90679e3278405b3a2`.

Verdict: **coherent with the scoped mathematical reviews**. The comparison preserves exact domains, the pending analytic premises, published versus preprint scope, the limitation to prime valuations, and the unproved full Sha obligations. The packet proposes future work without launching it. Its alternative d=5 belongs to both D3 and D7 since it is coprime to 33 and 77, while the recorded additive reduction at 5 excludes the good reduction Eisenstein routes. No analytic sign or rank is assigned to that twist. Its recommended E7611 second derivative task would establish analytic rank two only if the analytic formula, lower order vanishing and enclosure are justified; it does not establish the later Sha or coefficient claims. This is an integration check, not a second independent proof audit or an endorsement of any model performance metric. No correction is required.
