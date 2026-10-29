# Run 004 exact interval computation

The input is E_7611/Q, `y^2=x^3-7611^2*x`, with conductor 1853674272 as a separately audited mathematical dependency. The [candidate argument](../../findings/run-004-analytic-certificate.md) describes the formulas, assumptions and every truncation bound.

From the repository root:

```bash
python3 research/experiments/run-004-analytic/compute.py
```

This reproduces [output.json](output.json) deterministically. The [receipt](receipt.json) records the actual source hash, output hash, Python version, measured elapsed time and exit status. It is an author execution record, not a trusted verifier signature. Elapsed time is measured with a machine clock and has no role in the proof arithmetic.

The program uses only Python integers and `fractions.Fraction`; it has no random input, external package or network dependency. Its fixed scale is 10^45. It constructs outward intervals using integer floor and ceiling, with exact Machin bounds for pi, a positive logarithm series, an elementary harmonic bound for Euler's constant, and Cremona's convergent series for G2. It sums coefficients through 220000 and bounds every omitted Fourier coefficient.

The coefficient array is generated from the sourced CM prime formula, the quadratic character and Euler recurrences. Its output hash covers JSON serialization of the complete array including a zero at index zero. The output also gives selected coefficients for inspection. This array hash is not a replacement for the mathematical coefficient identification or independent reproduction.

The asserted coarse enclosure is `1561/100 < L''(E_7611,1) < 1563/100`. All exact endpoint numerators and their common denominator are retained in the output. Passing this script only verifies the implemented finite arithmetic relative to the analytic and CM dependencies. It does not formally verify those theorems, prove Sha finite, or verify BSD's full leading coefficient formula.
