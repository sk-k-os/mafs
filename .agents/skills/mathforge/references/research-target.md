# Research target and scientific boundaries

Research checked October 28, 2026. The director selected the Birch and Swinnerton Dyer conjecture for elliptic curves over the rational numbers as the research direction. Start with a finite arithmetic research program whose claims can be checked individually. The recommendation concerned feedback quality, accessible computational objects and research infrastructure. It does not imply that BSD is close to a solution, or that more agents make a solution probable.

Clay currently lists all three proposed problems as unsolved. The operational objective should be verified mathematical progress, including useful failed approaches, with the Millennium problem retained as the motivating question. [Clay unresolved problems](https://www.claymath.org/problem/unsolved/)

## Comparison

| Candidate | Mathematical target | Useful opening work | Main obstacle for this system |
| :--- | :--- | :--- | :--- |
| Hodge | For every smooth projective complex variety, every rational Hodge class is a rational linear combination of algebraic cycle classes. | Explicit families, cycle constructions, period calculations and rigorous special cases. | Much of the decisive work concerns constructing algebraic cycles, comparison maps and geometric structures. Numerical periods or examples do not establish algebraicity. The integral version is a different statement and is false in general. |
| Yang Mills existence and mass gap | Construct a nontrivial quantum theory on four dimensional Euclidean space for every compact simple gauge group, with the required axioms and positive mass gap. | Controlled lattice models, bounds, constructive field theory and simplified dimensions. | A finite lattice spectral gap or convincing simulation does not control the continuum and infinite volume limits. Existence, axioms, nontriviality and the gap are separate obligations. |
| BSD over the rationals | Relate the rank of rational points to the order of vanishing of the associated L function; the stronger form also predicts its leading coefficient. | Exact curve arithmetic, descent, Selmer information, certified special values, twists, theorem applicability audits and formalized auxiliary lemmas. | Higher rank arithmetic, finiteness of the Tate Shafarevich group and leading coefficient identities remain deep obstacles. Finite computations can suggest a pattern but cannot prove the universal claim. |

Mathematical statements come from the official problem descriptions by [Deligne](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf), [Jaffe and Witten](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) and [Wiles](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf). The comparison of research suitability is our inference from these targets and the available tools.

## Exact BSD scope

For an elliptic curve \(E/\mathbb Q\), let \(r_{\mathrm{alg}}=\operatorname{rank}E(\mathbb Q)\) and \(r_{\mathrm{an}}=\operatorname{ord}_{s=1}L(E,s)\).

1. **Weak BSD:** \(r_{\mathrm{alg}}=r_{\mathrm{an}}\).
2. **Finiteness:** \(\Sha(E/\mathbb Q)\) is finite.
3. **Full leading coefficient formula:** with consistent standard normalizations,

\[
\frac{L^{(r)}(E,1)}{r!}
=\frac{\Omega_E\,\operatorname{Reg}(E/\mathbb Q)\,\#\Sha(E/\mathbb Q)\,\prod_p c_p}
{\#E(\mathbb Q)_{\mathrm{tors}}^2}.
\]

Here \(r=r_{\mathrm{alg}}=r_{\mathrm{an}}\), the product runs over finite primes, and \(\Omega_E\) includes all real components. Period, height and regulator conventions must be recorded together. Wiles separates the rank assertion from the refined formula. [Official BSD statement](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf)

For elliptic curves over \(\mathbb Q\), analytic rank zero or one implies rank equality and finiteness of \(\Sha\), through modularity and the results of Gross, Zagier and Kolyvagin. This does not by itself establish the entire leading coefficient formula. Do not silently replace an analytic rank hypothesis by an algebraic rank hypothesis; converse statements require their own cited theorem and hypotheses. [Skinner, published introduction and precise theorem context](https://annals.math.princeton.edu/wp-content/uploads/annals-v191-n2-p01-s.pdf)

A useful example of the required precision is Jetchev, Skinner and Wan: for semistable curves of analytic rank one, their stated result proves the relevant prime part of the formula for primes at least five of good reduction with irreducible residual representation, with an additional statement for three. This is a theorem to apply after checking every hypothesis, not a universal shortcut. [Original paper](https://arxiv.org/abs/1512.06894)

Do not summarize the frontier as “nothing is known at rank two.” Particular curves, conditional statements and substantial special results exist. The unsolved goal is the general theorem. The opening program must maintain a current theorem applicability ledger rather than infer the research frontier from a software routine returning unresolved cases.

## First bounded project

**Project:** build and audit a reproducible evidence atlas for a fixed family of quadratic twists, then bring the director a focused discussion of the most useful unresolved mechanisms. Seek specialized mathematical assessment where a technical claim needs it; the director remains the research director.

**Family:** start from \(E:y^2+y=x^3-x^2-10x-20\), coefficient vector \([0,-1,1,-10,-20]\). Study its quadratic twists \(E^{(d)}\) for squarefree integers with \(1\leq |d|\leq 200\). Define the twist convention explicitly and store the resulting minimal model and transformation. This is a deliberately small proposed pilot, not a claim that these cases are new or strategically optimal.

The base curve is Cremona **11a1** but LMFDB **11.a2**. These naming systems do not preserve the same terminal index. The canonical identity is the coefficient vector plus field and model transformations. [Verified base curve](https://www.lmfdb.org/EllipticCurve/Q/11/a/2)

Each curve receives a dossier containing:

1. Exact coefficients, discriminant, conductor, torsion information, root number, local factors and the applicable definitions.
2. A proved rank interval, explicit points and a separate saturation status. Independent points give a lower bound; a point search that finds no point gives no rank zero proof.
3. Numeric analytic estimates with precision and truncation assumptions. A separate certified analytic claim requires valid error bounds or exact identities. A small floating point number is not an exact zero.
4. Leading coefficient evidence with normalization ledger and a separate record of what is known about actual \(\Sha\). Computing an “analytic order of Sha” from the conjectural formula cannot then verify the same formula.
5. Theorems used, exact theorem number, source version, hypotheses, witnesses for hypotheses and dependency graph.
6. Disagreements, known failure modes and the smallest unresolved statement. Every claim is labeled conjectural, numerical, conditional, proved by a documented mathematical argument, or checked by a proof assistant.

Controls include rank zero curve 11a1, rank one curve 37a1 with coefficients \([0,0,1,-1,0]\), and rank two curve 389a1 with coefficients \([0,1,1,-2,0]\). Their published database records are calibration references, not evidence of novelty. [37a1](https://www.lmfdb.org/EllipticCurve/Q/37/a/1), [389a1](https://www.lmfdb.org/EllipticCurve/Q/389/a/1)

**First acceptance gate:** reproduce selected known cases with independent arithmetic checks, correctly reject seeded invalid arguments, preserve unresolved obligations and produce a mathematician readable dependency graph. Success is trustworthy infrastructure and a precise research question. It is not progress measured as a percentage of BSD solved.

**Research branches after calibration:** compare descent obstructions across the fixed twists; audit theorem hypotheses for a selected prime part of BSD; investigate a rigorously specified local condition that predicts a Selmer phenomenon; or formalize an auxiliary descent lemma. Before searching for a new theorem, locate the nearest existing theorem and assess whether the proposed contribution is already known. The director selects direction using the team's evidence and discussion; specialized review supports important novelty claims.

## Available mathematical tools and their boundaries

| Tool | Useful role | Required boundary |
| :--- | :--- | :--- |
| SageMath | Curve construction, exact arithmetic, modular symbols, descent interfaces, point searches and theorem driven BSD computations. | Record version, algorithm, database use, precision and proof settings. Its current documentation explicitly treats some database results as `proof=True`. For 389a its documented `prove_BSD()` leaves all primes unresolved, while `proof=False` can return an empty unresolved set. A successful return is not enough to classify a claim. |
| PARI/GP | Fast exact and analytic number theory; curve reduction, local information and rank intervals. | `ellrank` returns lower and upper bounds. `ellanalyticrank` decides zero by a numerical tolerance. It supplies evidence unless an independent certification argument validates the relevant analytic facts. |
| eclib and mwrank | Concrete descent and Mordell Weil computations over the rationals. | Preserve rank bounds and saturation details. A second wrapper over the same engine is not an independent implementation. |
| LMFDB | Curated examples, labels, comparison data and provenance. | Preserve query, record date, label scheme and field level status. Database completeness and reliability have stated algorithmic assumptions. Do not train a discovery benchmark on its evaluation answers. |
| Lean and mathlib | Kernel checked auxiliary mathematics and explicit dependencies. | Audit the actual statement and transitive axiom footprint. Kernel acceptance does not show that the formal proposition captures the intended mathematical claim. An imported assumption can trivially make a hard goal provable. |
| Original papers and maintained mathematical references | Theorem retrieval, notation, hypotheses, literature context and novelty checks. | Search snippets and abstracts identify candidate sources. Applicable theorems require full statement and proof context. Preprints remain preprints until independently assessed. |

Tool sources: [Sage elliptic curve reference](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html), [PARI elliptic curve reference](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html), [eclib package documentation](https://doc.sagemath.org/html/en/reference/spkg/eclib.html), [LMFDB reliability](https://www.lmfdb.org/EllipticCurve/Q/Reliability), [mathlib Weierstrass curve definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/EllipticCurve/Weierstrass.html), [Lean proof validation](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).

Sage incorporates PARI and mwrank functionality. Comparing “Sage versus PARI” may compare two routes to the same code. Track dependency lineage before counting independent checks. For small finite fields, an independently written exhaustive point count offers a useful separate check of local data. [Sage advanced tutorial](https://doc.sagemath.org/html/en/tutorial/tour_advanced.html)

The verified mathlib page exposes Weierstrass curves, discriminants, invariants and associated algebraic facts. It does not establish that the full research stack needed for BSD is available. Before committing to formalization, inspect a pinned mathlib revision and enumerate missing definitions and theorems. Treat this gap audit as a deliverable. [mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/AlgebraicGeometry/EllipticCurve/Weierstrass.html)

Lean checks must fail on command errors and unexpected axioms. The authoritative Mathforge formal acceptance policy is in verification-and-lifecycle.md: approved foundational axiom closure, trusted replay and statement comparison, plus semantic review. Exploratory native computation does not bypass that policy. [Lean validation guidance](https://lean-lang.org/doc/reference/latest/ValidatingProofs/), [Lean axioms](https://lean-lang.org/doc/reference/latest/Axioms)

These resources were researched, not installed or integrated by this report. No claim is made that Sage, PARI, Lean or a theorem proving service is currently configured on the user's machines.

Use the [Stacks project](https://stacks.math.columbia.edu/) for tagged algebraic geometry definitions and lemmas. Store the tag and source revision, then verify that its hypotheses match the use. For LMFDB dataset studies, save the [published completeness boundary](https://www.lmfdb.org/EllipticCurve/Q/Completeness) with the extraction; a sampled collection cannot silently become an exhaustive population.

## Lessons from Perelman's work

Use methods visible in the mathematics, without claiming to reproduce Perelman's personality or cognition. His first paper introduces monotone quantities and geometric controls that address obstacles in Hamilton's program. The transferable research questions are: what obstruction prevents an existing strategy from closing; what invariant exposes it; what rescaling or limiting model makes it tractable; and which lemma would convert that structure into a proof? Applying these questions to BSD is an analogy, not a proposed Ricci flow proof of BSD. [Entropy paper](https://arxiv.org/abs/math/0211159)

His surgery paper also explicitly identifies an earlier unjustified assertion and explains its irrelevance to the remaining conclusions. This supports a process norm: retract the exact defective claim, invalidate dependent work, and retain only conclusions whose dependency paths survive. “A genius would see it” must never substitute for an argument. [Surgery paper](https://arxiv.org/abs/math/0303109)

## Consequences for agent design

The screenshot motivates a distinction between all statements one could prove and the much smaller set that matters. Implement this as a relevance review: every proposed lemma states the bottleneck it addresses and the dependency path by which it helps the target. A thousand disconnected lemmas are not a thousand steps toward BSD.

Discovery agents may propose unconventional analogies, definitions and speculative mechanisms. Every proposal must yield a falsifiable prediction, a tractable example, a precise lemma or an explicitly stated impossibility test. Speculation remains quarantined from the accepted theorem ledger.

Measure agents on independent correctness, useful falsification, reproducibility, hypothesis accuracy and marginal research value. Do not reward the volume of confident text. Repeated contradiction, fabricated sources, circular assumptions or failed calibration should trigger review and replacement. A difficult branch with no result is not automatically low productivity; preserving a well specified obstruction can be valuable.

Replacement agents receive exact claim identifiers, checked results, unresolved gaps, failed paths and source provenance. They should not inherit an unreviewed narrative as established truth. A second agent agreeing with a first is peer discussion, not proof. Formal checks, mathematically independent arguments and a qualified human researcher address different failure modes.

The director is the human research director. Bring him the pilot's strongest findings, precise obstructions and alternative branches so the conversation can generate new directions. Independent arithmetic geometers familiar with elliptic curves, descent, Selmer groups and BSD provide a separate source of specialized assessment for major claims. No claim of solving a Millennium problem should be published on agent consensus alone.
