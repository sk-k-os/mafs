# Run 004 separate referee

Date: October 29, 2026. Target: E over Q with equation y²=x³−7611²x. This is calibration of a separate review process, not a model benchmark, formal proof certificate or external human acceptance. Sources, tools, filesystem and model family are shared. No other Run 004 review verdict has been read. The research cutoff is 16:13:37 UTC; the target report time is 16:14 UTC; the complete run deadline is 16:21:37 UTC. The coordinator alone writes Git.

## Predeclared scope and failure tests

The proposed conclusion is analytic order exactly two, using a rigorous nonzero enclosure for the second derivative. The accepted input from Run 003 is algebraic rank exactly two, not analytic rank two. Existing low analytic rank theorems can exclude analytic orders zero and one; this logical bridge must not assume BSD or import a numerical rank as an exact premise.

1. Freeze the exact conductor, including its exponent at 2, and establish the functional equation sign for this squarefree parameter.
2. Check completed versus uncompleted L function normalization, the factor from the second derivative, and every use of lower order vanishing to remove derivatives of gamma and exponential factors.
3. Independently derive the kernel and compare its definition to the cited source. Check that the derivative formula assumes order at least two, rather than exactly two.
4. Verify coefficient generation against exact point counts, including p=2 and primes dividing 7611. Multiplicativity and prime power recurrences must match good or additive reduction as appropriate.
5. Distinguish an approximate decimal from a certified enclosure. Every transcendental or quadrature evaluation needs a proved enclosure or an explicitly trusted interval implementation with recorded settings.
6. Verify direction of rounding for signed terms and cancellation. A bound valid for one term cannot be silently reused after summing many terms.
7. Prove a uniform omitted coefficient bound and a complete tail bound at the actual cutoff. Include any numerical integration tail and any truncation of special function expansions separately.
8. Keep period and regulator conventions explicit, while recognizing that proving a raw nonzero L second derivative does not compute the BSD coefficient or full Sha.
9. Hash the exact reviewed artifacts and replay from those inputs. A changed artifact invalidates its prior hash bound review until reassessed.
10. Stop with the exact missing ingredient if a rigorous enclosure cannot be obtained inside the bound. A failed certification attempt does not imply vanishing.

## Preliminary independent normalization check

For a weight two normalized newform with positive analytic sign, put a=1/sqrt(N) and let f(iy) have Fourier coefficients a_m. Splitting the Mellin integral at a gives

Lambda(s)=integral from a to infinity of f(iy) times ((sqrt(N)y)^s+(sqrt(N)y)^(2−s)) dy/y,

where Lambda(s)=N^(s/2)(2pi)^(−s)Gamma(s)L(s). If L(1)=L'(1)=0, differentiating twice gives Lambda''(1)=sqrt(N)L''(1)/(2pi). The split integral gives Lambda''(1)=2sqrt(N) integral f(iy)log(sqrt(N)y)^2dy. Therefore

L''(1)=4pi integral from a to infinity f(iy)log(sqrt(N)y)^2dy.

Termwise integration and integration by parts give

L''(1)=4 sum over m>=1 of (a_m/m) G2(2pi m/sqrt(N)),

where G2(x)=integral from 1 to infinity exp(−xy)log(y)dy/y. This independently matches the source specialist's stated formula. Absolute convergence on y>=a and exponential coefficient decay after the Mellin split justify the exchange; the final report will bind the actual conductor and coefficient bound. A nonzero second derivative is not yet established.

## Submission and final verdict

Pending frozen candidate and independent execution. No positive numerical verdict is implied by the normalization check.

## Final assessment after frozen submission

Completed October 29, 2026, before 16:09 UTC. The preceding pending status is superseded by this assessment. No other Run 004 review verdict was consulted.

Verdict: **accepted under the stated established mathematical dependencies and the recorded computational trust boundary**. For E:y²=x³−7611²x over Q, the submitted exact interval implies

1561/100 < L''(E,1) < 1563/100.

Together with the exact lower order vanishing, this proves analytic order exactly two for this one curve at the campaign's separately reviewed model assurance level. It is not a full BSD proof, a formal certificate, an external human mathematical review or a new theorem for every member of the family.

### Exact reviewed revisions

| Artifact | SHA256 |
| :--- | :--- |
| `research/sources/run-004-analytic-sources.md` | `a55e63e919ab0c75345050666ca85f79bcda307594189dde4230b6bf73920602` |
| `research/findings/run-004-analytic-certificate.md` | `109db2dd0b3a88fbc4b133e9e9237b1bb8fdcdabaff5bdccb0eae5ba94184e43` |
| `research/experiments/run-004-analytic/compute.py` | `4372d439f42c9e16718f971bdb83e84d8110e1a25507c30999745e2d5047747a` |
| `research/experiments/run-004-analytic/output.json` | `b21b3d403a18e982e870e02439ba1155ba1fec72a99576e9156df703398acfae` |

The inherited rank proof and its earlier review retain the exact hashes recorded in the source dossier. The current review does not replace or erase their descent and Monsky dependencies.

### Source and normalization assessment

I inspected the relevant source contents directly: Cremona Chapter II printed pages 29 and 42 to 44; BCDT Theorem A and its modularity equivalences on printed pages 1 and 3; Watkins and collaborators' odd squarefree conductor statement in section 10 of the author copy; Ribet section 6 and its Gauss theorem on printed pages 9 to 11; the previously inspected Tian, Yuan and Zhang printed pages 721 and 722; and the retained Milne facts for local factors and coefficient bounds. The source dossier additionally identifies the published conductor location. These are cited theorem applications, not a complete new audit of the proofs of modularity, the classical low rank implication or Gauss's theorem.

The conductor is 32 times 7611 squared, namely 1853674272. Its exponent at 2 is five. The equation is integral with discriminant 64 times 7611 to the sixth power. Each bad valuation is six, so no integral model can lower it by a positive multiple of twelve. The model is minimal. All four bad primes 2, 3, 43 and 59 are additive; the repeated tangent at the singular point in characteristic two is consistent with this classification. Their Euler factors are one. The full modularity theorem is used, not a semistable only statement. [Conductor source](https://www.dpmms.cam.ac.uk/~taf1000/papers/rankcongr.pdf); [BCDT source](https://www.math.u-psud.fr/~breuil/PUBLICATIONS/STW.pdf).

The exact root sign is positive, whereas the Fricke eigenvalue is negative in Cremona's convention. Algebraic rank two contradicts either analytic order zero or analytic order one under the classical low analytic rank theorem. Thus both L(1) and L'(1) vanish without assuming BSD at rank two. In particular, the product rule for the completion removes both A'L' and A''L terms. The split Mellin calculation above independently recovers the factor four and the same G2 integral as the cited proposition, whose hypothesis is order at least two. There is no circular use of an exact order two hypothesis. [Cremona primary text](https://johncremona.github.io/book/fulltext/chapter2.pdf); [root sign and low rank source](https://web.math.princeton.edu/~shouwu/publications/cn.pdf).

A wording correction to the preliminary paragraph: it is the Fourier terms after the Mellin split that decay exponentially, not the coefficients themselves. The actual uniform coefficient estimate is |a_m|<=2m. This estimate justifies the termwise operations and is explicitly used in the final tail bound.

The minimal differential is dX/(2Y). The source's full real period integrates its absolute value over both real components, and is twice the least positive real lattice period in this case. This period does not divide the raw L second derivative formula. The future leading Taylor coefficient is L''(1)/2. Neither the period convention nor the completed gamma factor introduces an unaccounted factor two in the present nonvanishing result.

### Coefficients and exact arithmetic assessment

The Gauss sign rule is necessary and correctly implemented: choose the odd coordinate a in p=a²+b² so that a+b is one modulo four; the affine count is p−2a, giving trace 2a after adding the point at infinity. The quadratic twist character follows directly by substituting X=7611z in the finite field character sum. The source correctly distinguishes the fundamental discriminant 30444 from the radicand 7611. Its good prime recurrences and additive bad factors determine all coefficients. [Inspected Gauss exposition](https://math.berkeley.edu/~ribet/Articles/icfs.pdf).

I wrote a separate coefficient implementation before reading the author implementation. It uses full prime power factorization instead of the author's iterative recurrence. All 220000 coefficients agree. Independent direct point counting agrees at every one of the 164 good primes at most 1000. Bad prime multiples are zero in both implementations. These finite comparisons supplement the cited general coefficient theorem; they do not replace it.

Every fixed scale numerical operation was inspected. Floor and ceiling divisions enclose signed inputs, negative scalar multiplication reverses endpoints, multiplication checks all four products, and a square crossing zero has lower bound zero. Logarithmic range reduction is exact and its positive atanh tail is bounded. Machin's identity and alternating rational tails enclose pi. The author's elementary harmonic comparison encloses gamma with width about one millionth; its proof is valid and does not assume a decimal approximation. Integer square root bounds enclose the conductor square root and hence x. Assertions check the implementation's actual argument ranges.

The 200 term kernel recurrence correctly produces z^k/(k² k!). After term 200, the consecutive ratio is bounded by z/202. The resulting geometric absolute remainder is conservative even though alternation could give a sharper estimate. Interval dependency and large cancellation can widen the interval but cannot exclude the exact value under these outward operations.

My separate Fraction implementation computes much tighter rational intervals for pi, gamma and seven kernels at z=1/10000, 1/10, 1, 3, 10, 30 and 33. Gamma uses an independent harmonic expansion with a bounded Bernoulli remainder, rather than the author's million term inequality. Every complete referee interval lies inside its author counterpart. The independent remainder dependencies and exact calculation conventions are documented in the [referee experiment notes](../experiments/run-004-referee/README.md). The selected kernels test the implementation across and beyond its actual range; they are not a second full summation of every Fourier term.

### Tail and replay assessment

The coefficient bound follows from Hasse, the prime power recurrences, multiplicativity and d(m)<=2sqrt(m), including additive primes. The inequality G2(z)<=exp(−z)/z² follows from log(t)/t<=t−1 for t>=1. Bounding the decreasing denominator at M+1 and summing the geometric exponential gives exactly the stated Fourier tail. Replacing exp(−t) by 2 to the negative floor of t and replacing 1/(1−exp(−x)) by (1+x)/x are conservative. Both replacements are applied to a rational lower bound for x in a direction that increases the tail. I independently recomputed the final tail as a Fraction and checked its outward integer bound.

The complete frozen author program was executed again with exit status zero. Its output reproduced byte for byte. Exact cross multiplication verifies that the final endpoints, after both kernel and Fourier tails, lie strictly inside (1561/100,1563/100). The positive lower bound is therefore not based on a displayed floating point decimal.

The [referee execution receipt](../experiments/run-004-referee/receipt.json), SHA256 `92e43f8ca5ab732dd6a022d49c7d21ecf690c6370baf5d68d89f3078aa6124ab`, records input hashes before and after execution, separate coefficient equality, direct counts, seven kernel comparisons, constant containment, exact tail recomputation and the byte identical full replay. The [independent output](../experiments/run-004-referee/output.json) has SHA256 `a24ef0856592711e3d180b49151840aeb26539571885c05c20618c1a5f306ceb`. The independent check program has SHA256 `9077c4e975fa327d6f3c01b814c6c5622f618c1890046fbcc5c60de80b3b9e97`; the replay program has SHA256 `e57a52d8d5ae4a4d24fcacda3d253d1a8b1d33f0b88a901a6e538e8fc1293b70`. Inputs were unchanged across the replay.

### Objections, limits and handoff

No material unresolved objection was found in the frozen submitted argument. The predeclared risks were addressed by source identification, direct reconstruction, outward interval analysis and actual replay. The only correction in this report is the preliminary coefficient decay wording above. No author artifact required a mathematical amendment after freezing.

The entire second derivative sum was replayed from author code, while coefficient generation and selected kernel calculations used separate implementations. This is more specific than claiming two independent full certificates. Python's integer arithmetic, interpreter, the displayed source theorem statements and the inherited algebraic rank argument remain in the trust boundary. No proof assistant, qualified human mathematical referee or external computation service verified this result. Agreement among agents and a later Git checkpoint do not certify it beyond the recorded evidence.

The precise supported advance is rank equality for E7611: both algebraic and analytic ranks are two. The inherited trivial 2 primary Sha result remains available. Full Sha finiteness, odd primary information, saturation and the full regulator, and the BSD leading coefficient identity remain unresolved. No low analytic rank theorem can now be reused to infer those rank two consequences. The next assignment is a human director choice, not automatically launched. The mathematical work is complete; the coordinator owns integration and checkpoint publication. Awaiting confirmed synced status before ending this reviewer assignment.
