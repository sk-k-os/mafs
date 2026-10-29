# Run 003 Route A: a precisely qualified rank two family

Date: 2026-10-29 UTC. Author role: source specialist. Status at freezing: candidate source audit and mathematical deductions for separate review. This is a calibration observation, not a model benchmark. The coordinator alone publishes checkpoints. Git publication does not certify mathematics.

## Decision object and exact domain

Consider only the following subfamily over Q. Choose integers u > v > 0 with gcd(u,v) = 1 and opposite parity. Require both

q = 3u^4 + 3v^4 − 2u²v²,

r = 3u^4 + 3v^4 + 2u²v²

to be prime. Set n = 3qr and E_n: y² = x³ − n²x. The primes q and r are distinct, greater than 3, and both congruent to 3 modulo 8. Thus n is positive, squarefree, and congruent to 3 modulo 8. These restrictions define the family; no assertion is made about all congruent number curves. The member u = 2, v = 1 has q = 43, r = 59, and n = 7611. Infinitude of the prime qualified family is not established here and is expressly conjectural in the principal source.

The strongest direct theorem found and inspected for this exact family during this bounded search is Reinholz, Spearman, and Yang, Theorem 1: the Mordell Weil rank is exactly two. Their theorem permits nonzero integer u,v whenever q,r are prime, so the present domain is a restriction of its domain. Its generic specialization argument alone allows exceptions. Remark 5 asserts an additional descent excluding those exceptions but omits its details. The published theorem remains a cited dependency; the omitted argument is recorded rather than silently treated as reconstructed. Their proof paragraph also has inconsistent lemma numbers. Use statement locators below.

## Source register and inspection scope

All accesses below were on 2026-10-29. Only inspected primary mathematical texts are used for positive claims. Hashes identify downloaded inspection copies, which remain in ignored scratch. No database rank is used.

1. Lindsey Reinholz, Blair K. Spearman, and Qiduan Yang, *On Congruent Numbers with Three Prime Factors*, Integers 11 (2011), A20, six pages. [Publisher PDF](https://math.colgate.edu/~integers/l20/l20.pdf). Inspected all six pages. Printed page 2: Theorem 1 and the preceding infinitude qualification. Page 3: Lemma 4, generic family and equations (5), (6). Page 4: Remark 5, equations (7), (8), and Lemma 6. Page 5: eight case table. Page 6: proof and Example 8. Scratch `work/run003-a/reinholz-spearman-yang.pdf`; SHA256 `27691d72c8b58c17e1267158c46cf718f7cb3615286e183a3c6efc9de57cc987`.

2. Andrej Dujella, Ali S. Janfada, and Sajad Salami, *A Search for High Rank Congruent Number Elliptic Curves*, Journal of Integer Sequences 12 (2009), Article 09.5.8. [Publisher PDF](https://cs.uwaterloo.ca/journals/JIS/VOL12/Janfada/janfada3.pdf). Inspected printed pages 3 and 4. Section 2 fixes the convention #Sel^(2)(E_n/Q) = 2^(s(n)+2). Theorem 1 gives the injective descent map using (x,x−n), with exceptional values at rational 2 torsion. Section 3 gives the odd squarefree Monsky matrix and s(n) = 2t − rank_F2(M). These locators support the normalization and finite matrix interpretation; computational search tables are not used as rank evidence.

3. J. S. Milne, *Elliptic Curves*, second edition, 2021. [Author PDF](https://www.jmilne.org/math/Books/EC2.pdf). Inspected Chapter IV, section 2, printed page 113 for the descent exact sequence; Remark 3.7, page 116 for the square class homomorphism; Proposition 5.5 and proof, page 131 for the rank plus rational 2 torsion dimension. Existing inspection copy `work/bsd-run-001/milne-ec2.pdf`; SHA256 `646c0c4f193cdaa35f32c7d60fbd46a75e2f5187db4301810e8613726e3ebbee`.

4. Ye Tian, Xinyi Yuan, and Shou Wu Zhang, *Genus Periods, Genus Points and Congruent Number Problem*, Asian Journal of Mathematics 21 (2017), 721–774. [Author PDF](https://web.math.princeton.edu/~shouwu/publications/cn.pdf). Inspected printed pages 721–724, especially the definition of L(n), Theorem 1.1, Corollary 1.3, and Theorem 1.4. Their curve ny² = x³−x is isomorphic to ours by (X,Y) = (nx,n²y). Their invariant L(n) is defined to be zero when analytic rank exceeds one. Corollary 1.3 requires a finite Mordell Weil group for the rank zero full BSD consequence; trivial 2 primary Sha alone is insufficient. Theorem 1.4 has residue classes 5,6,7 modulo 8. Neither supplies rank two BSD for the present domain. Scratch `work/run003-a/tian-yuan-zhang.pdf`; SHA256 `417f6bbe7f7b775f77a2593cc2f32cbab2f2782cf07d0ba0a15f2708b2475595`.

5. Ashay Burungale and Ye Tian, *A rank zero p converse to a theorem of Gross–Zagier, Kolyvagin and Rubin*, [arXiv:2506.03465v2](https://arxiv.org/abs/2506.03465v2), 11 October 2025. Inspected its seven page text, especially Theorem 1.1 on printed page 1 and Theorem 1.2 on page 2. The [Annals publication metadata](https://annals.math.princeton.edu/2026/203-1/p01) gives volume 203 (2026), pages 1–13; the publication PDF was not compared line by line. Theorem 1.1 requires p primary Selmer corank zero for a CM elliptic curve over its imaginary quadratic CM field, with the stated consequence for curves descending to Q. Theorem 1.2 is a density one rank zero result in the squarefree congruent number domain n ≡ 1,2,3 modulo 8. Neither is a pointwise rank two theorem. Scratch `work/run003-a/burungale-tian-v2.pdf`; SHA256 `cbb8284a13ed40bd15df9713001485724bc4d2a3b5c38d8fd83f9b6f3f3e4664`.

## Supplementary reconstruction for review

This paragraph is an author reconstruction, not a quotation or a claim that the omitted published proof has been inspected. It gives a short check of the lower bound that a referee can accept or leave pending independently of the cited theorem.

Put D = u²−v². Define

P1 = (−9qD², 36q²uvD),

P2 = (3qr²/(4u²v²), 9q²r²(u²+v²)/(8u³v³)).

The denominators are nonzero and D is nonzero on the chosen domain. For P1 one has x−n = −6q² and x+n = 24qu²v². For P2 one has x−n = 3q²r/(4u²v²) and x+n = 9qr(u²+v²)²/(4u²v²). Multiplication proves y² = x(x−n)(x+n) in both cases.

Let φ0:E_n(Q)/2E_n(Q) → Q*/Q*² be the x coordinate descent homomorphism, with the conventional exceptional value at (0,0). Its values on T0=(0,0), Tn=(n,0), P1, P2 are respectively −1, 3qr, −q, 3q. These four square classes are independent: in a relation with exponents a,b,c,d in F2, the r valuation first gives b=0, the 3 valuation then gives d=0, the q valuation gives c=0, and the sign gives a=0. Thus E_n(Q)/2E_n(Q) has dimension at least four. Its dimension is rank E_n(Q)+2 because all three nonidentity 2 torsion points are rational. Hence rank E_n(Q) ≥ 2. This also establishes independence modulo torsion of the two displayed points: their classes are independent after quotienting by the two dimensional torsion image. It does not establish that they are a saturated basis.

For the upper bound, use the cited normalization s(n) = dim_F2 Sel^(2)(E_n/Q)−2. If the three prime factors are all 3 modulo 8, then D2=I and D_(−2)=0 in the odd Monsky matrix. With A's off diagonal entries given by Legendre symbol bits, quadratic reciprocity makes each opposite pair sum to one; diagonal entries are row sums. The matrix is

M = [[A+I,I],[I,A]].

There are eight possible upper triangular bit triples. Exact elimination gives rank four in two cases and rank six in the other six; therefore s(n) ≤ 2. Mordell Weil rank is at most s(n), yielding rank exactly two when combined with either the reconstructed lower bound or the published theorem. These arithmetic checks do not independently prove Monsky's theorem.

Finally, the exact sequence

0 → E_n(Q)/2E_n(Q) → Sel^(2)(E_n/Q) → Sha(E_n/Q)[2] → 0

has dimensions four, four, zero. Therefore Sha[2] = 0 and Sha[2^∞] = 0: any nonzero element of finite 2 power order would yield an element of order two. This is a deduction from the cited descent interpretation and rank result. It does not prove finiteness of the entire Sha.

## Cheap discriminating test performed

The exact Python experiment is [check.py](../experiments/run-003-route-a/check.py); its captured result is [output.json](../experiments/run-003-route-a/output.json). Standard library integers, rational fractions, trial division through integer square root, and binary elimination suffice. No floating point rank or analytic approximation is used.

For u=2,v=1, the script verifies the primes 43 and 59, the two on curve points

P1 = (−3483,399384),

P2 = (449049/16,289636605/64),

the rank four square class matrix including T0,Tn, and rank four of the six by six Monsky matrix. Thus its mathematical interpretation is rank two and trivial 2 primary Sha, conditional on the explicitly cited descent and matrix theorems. The script also replays all eight reciprocity patterns. This finite experiment is neither an analytic rank calculation nor a full Sha computation. On curve membership alone would not prove independence; the square class calculation is essential.

## Remaining BSD obligations and decisive next test

The family provides a rigorously qualified higher rank starting point, but it does not close BSD. Separate obligations remain:

1. Analytic rank equality: prove ord_(s=1)L(E_n,s)=2. The classical analytic rank zero or one implication, recalled in Tian, Yuan, Zhang page 722 and Burungale, Tian page 1, combined with algebraic rank two rules out analytic orders zero and one. It does not exclude order four or higher. The functional equation sign is positive for n ≡ 3 modulo 8, consistent with even order. These deductions do not certify a nonzero second derivative.

2. Finiteness of Sha: trivial 2 primary Sha leaves every odd primary component and global finiteness unresolved. No inference from finite 2 primary Sha to finite full Sha is allowed.

3. The full leading coefficient formula: even after analytic rank equality, the required value is L''(E_n,1)/2 with the correct Néron period, regulator of a full Mordell Weil basis, local Tamagawa numbers, torsion denominator, and full Sha order. Two independent points do not determine the full regulator until their index is controlled. Nothing here verifies the odd prime BSD valuations or full equality.

The cheapest next assignment, if the director selects this branch, is one member only: n=7611. Freeze a primary second derivative formula and conductor/functional equation normalization, establish the exact lower order vanishing using the above rank implication, and obtain a rigorous nonzero enclosure for L''(E_7611,1). A numerical nonzero decimal is insufficient. Success would settle analytic rank two for that member; it would not by itself establish Sha finiteness or the leading coefficient formula. Failure to get a usable enclosure within a separate bound should be recorded without expanding to more members. This assignment is specified, not started.

The rank zero CM converse cannot supply the missing higher rank step: Mordell Weil rank two injects a corank two divisible subgroup into every p primary Selmer group over Q, and rank cannot decrease after extension to the CM field. The density one rank zero theorem also cannot settle a selected exceptional subfamily. These are quantifier and hypothesis failures, not contradictions.

## Comparison scope, failures, and handoff

This bounded search compared the direct rank theorem with the inspected congruent number genus results and the recent CM rank zero converse. It did not exhaust all rank two BSD literature or claim a globally strongest theorem. Queries included congruent number rank two prime families, rank two 2 primary BSD, and recent CM converse results. General search results making broad BSD claims were not adopted without inspected primary statements. An unrelated arXiv identifier fetch was discarded. No database sample, heuristic rank score, or density statement was promoted to a pointwise proof.

The main source's omitted descent and incorrect crossreference numbers remain visible objections. The supplementary proof and exact experiment are offered for independent reconstruction, not as author certification. The chosen family may be finite; neither this comparison nor its experiment addresses infinitude. The branch stops at comparison and handoff. The coordinator should compare this route's higher rank bottleneck against Route B's distinct analytic rank premise, preserve the referee's conclusions separately, and publish the frozen record only through the configured checkpoint command.
