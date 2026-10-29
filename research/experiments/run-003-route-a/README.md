# Exact Route A arithmetic

Run from the repository root:

```sh
python3 research/experiments/run-003-route-a/check.py research/experiments/run-003-route-a/output.json
```

The standard library script checks one prime qualified member n=7611, its two rational points, four independent descent square classes including rational 2 torsion, and the Monsky matrix. It also enumerates the eight reciprocity patterns for three primes congruent to 3 modulo 8. The interpretation depends on the exact descent and Monsky theorem statements recorded in [the source audit](../../sources/run-003-route-a.md).

Execution observed on 2026-10-29, completed before the 14:28:33 UTC clock observation. Exit status: 0. Python version captured by the script: 3.14.6. Script SHA256: `e336dc7d3d948ac535c10ab3f0ccbc7848ed9a475ef97f89f1dac9022257e63e`.

The execution checks arithmetic and matrix ranks. It does not establish an analytic rank, prove the cited theorems, determine full Sha, or prove a BSD leading coefficient formula. It is not a formal proof assistant certificate.
