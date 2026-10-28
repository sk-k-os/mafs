# Run 001 exact local counts

Status: candidate computation, awaiting a separate review. This is a finite calibration experiment, not a BSD proof or a novelty claim.

## Approach fixed before computation

On October 28, 2026, the arithmetic worker registered this procedure before examining the generated outputs:

1. Use the exact general Weierstrass equation `y^2 + a1*x*y + a3*y = x^3 + a2*x^2 + a4*x + a6` for the three supplied coefficient vectors. The supplied labels are input aliases; the computation does not establish their catalog identity, conductor or rank.
2. Compute the integral invariants from the formulas recorded in the script. Require a nonzero integer discriminant and check `c4^3 - c6^2 = 1728*Delta` exactly.
3. For each prime at most 43, use the nonvanishing discriminant modulo the prime as the good reduction criterion. Skip singular reduction in the elliptic point count table and preserve it separately.
4. Count all affine solutions directly and add the one projective point at infinity. For odd primes, compare with a second algorithm using the quadratic character of the discriminant in `y`. At 2, enumerate the seven nonzero triples in the projective plane directly. Compare the counts exactly and check the integer inequality `a_q^2 <= 4*q` as a consistency test.
5. Check for rational singular points by evaluating the homogeneous equation and all three first derivatives on a complete set of projective representatives. This finite check supplements the discriminant criterion; absence of rational singular points alone is not a proof of geometric smoothness.
6. For the second supplied curve, search good primes `q <= 43` with `q != 5` for which `a_q^2 - 4*q` is a nonsquare modulo 5. Record the first such `q` and all candidates in this finite range. Treat these only as possible witnesses for a later representation argument. No irreducibility conclusion is accepted here.

The computations use Python standard library integers only, no floating point, no random sampling and no L function values. The two algorithms share the input, interpreter and some orchestration. Their agreement is a useful cross check, not fully independent mathematical verification. A referee must check the formulas, input interpretation, program and receipts independently.

## Artifacts and replay

`input.json` freezes the input. `compute.py` writes `output.json` and `receipt.json` next to itself. Run from the repository root:

```bash
python3 research/experiments/run-001-local-counts/compute.py
```

The output is deterministic. The receipt records UTC time, elapsed computation time, Python version and SHA256 hashes of input, script and output. Replaying regenerates the receipt. The receipt records execution by this script, not an external verification authority. It deliberately contains no absolute machine paths, account details or raw chat.

For the formulas, `b2 = a1^2 + 4*a2`, `b4 = 2*a4 + a1*a3`, `b6 = a3^2 + 4*a6`, `b8 = a1^2*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3^2 - a4^2`, `c4 = b2^2 - 24*b4`, `c6 = -b2^3 + 36*b2*b4 - 216*b6`, and `Delta = -b2^2*b8 - 8*b4^3 - 27*b6^2 + 9*b2*b4*b6`.

For an odd prime and each `x`, completing the square gives `(2*y + a1*x + a3)^2 = (a1*x + a3)^2 + 4*(x^3 + a2*x^2 + a4*x + a6)`. Since 2 is invertible, the number of `y` is `1 + chi(D_x)` with `chi(0)=0`. Summing and adding infinity yields the comparison count. This elementary calculation does not supply the separate bridge from these counts to a residual Galois representation.

## Scope limits

No statement about the rank, conductor, torsion, analytic rank, Tate Shafarevich group, regulator, periods or BSD leading coefficient follows from this experiment alone. No point of order 5 is searched for in this bounded assignment. No theorem citation or proof of the Galois representation bridge is supplied by this worker. That bridge and its hypotheses require a separate sourced argument and review. The artifacts cannot promote themselves to accepted research findings.

## Observed result

The recorded run completed 40 comparisons with no count discrepancies. The invariant identity held for all three inputs.

| Input alias | Delta | c4 | c6 | Good prime rows | Singular primes in range |
| :--- | ---: | ---: | ---: | ---: | :--- |
| 11a1 | -161051 | 496 | 20008 | 13 | 11 |
| 37a1 | 37 | 48 | -216 | 13 | 37 |
| 389a1 | 389 | 112 | -856 | 14 | None |

For the second input at `q=3`, there are six affine points and the point at infinity. Indeed, for each `x` in `{0,1,2}`, the right side `x^3-x` is zero modulo 3, and `y^2+y=0` has exactly the two roots `0` and `2`. Thus `a_3=3+1-7=-3`, and `a_3^2-4*3=-3` has residue 2 modulo 5. The squares modulo 5 are `{0,1,4}`. This supplies the finite arithmetic for a possible witness; applying it to irreducibility still needs the separately audited theoretical bridge. Other candidate auxiliary primes in the fixed range are 7, 13, 17, 23, 31, 41 and 43.

At `q=5`, the second input has 8 projective points and `a_5=-2`. This is local finite field data. It is not a computation of its global rank or L function.

The optional torsion search was not performed, keeping this assignment within its prescribed local count scope. No failed count comparison was observed; all theorem applicability obligations remain with the source and review assignments.
