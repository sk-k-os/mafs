# Exact local sign for the control

Date: October 28, 2026. Coordinator source and arithmetic note. Candidate mathematical argument, awaiting separate review. Curve C is fixed by `[0,0,1,-1,0]` over Q.

## Source

David E. Rohrlich, *Galois theory, elliptic curves, and root numbers*, Compositio Mathematica 100(3), 1996, pages 311 to 349. [Primary paper](https://www.numdam.org/item/CM_1996__100_3_311_0.pdf). Accessed October 28, 2026. PDF SHA256 `0a1c0de28382b7474c3c59c549b4092f5c76f8d800758f96377abd7e05a1fe31`.

Theorem 2(i),(ii), printed page 329, gives the archimedean sign and the potentially multiplicative formula, including the character attached to the square root of negative c6. Proposition 8(i), page 332, supplies the good reduction case. Section 4, page 336, defines the global product. The relevant pages were inspected; page 329 was also rendered to check the formula absent from text extraction. With the trivial twisting representation, these give sign negative one over R, positive one at good primes, negative one for split multiplicative reduction and positive one for nonsplit multiplicative reduction. This is a specialization of the cited formulas, not a new root number theorem.

## Arithmetic specialization

Run 001 established the minimal integral invariants `c4=48`, `c6=-216`, `Delta=37` and conductor 37. Their source and arithmetic witnesses remain in the [earlier audit](run-001-jsw-audit.md).

At 37, the valuation of `j=c4^3/Delta` is negative one. Also `-c6=216` reduces to 31. The nonzero squares modulo 37 are

```
1, 3, 4, 7, 9, 10, 11, 12, 16, 21, 25, 26, 27, 28, 30, 33, 34, 36.
```

Thus 31 is not a square. A unit with nonsquare residue defines the unramified quadratic extension of Q37; the corresponding character chi is nontrivial, has chi(-1)=1 and has no trivial constituent. Substitution in Rohrlich's formula gives local sign positive one at 37. Equivalently the multiplicative reduction is nonsplit.

All other finite places have good reduction. The global product is therefore negative one. This calculation does not infer an exact analytic order from parity. Its use in the analytic functional equation also requires the modularity and sign identification recorded in the [analytic source dossier](run-002-analytic-sources.md).

## Boundary and handoff

An odd analytic functional equation proves central vanishing, but permits orders 1, 3, 5 and higher. A separate derivative nonvanishing argument remains mandatory. The primary paper's root number computations are used as established mathematics; their complete proofs were not reverified or formalized here. The referee must check this arithmetic and the analytic sign bridge before closing the run's missing premise.
