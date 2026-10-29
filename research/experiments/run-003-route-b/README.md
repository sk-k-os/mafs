# Exact alternative prime and ramified twist test

Run `python3 research/experiments/run-003-route-b/compute.py` from the repository root. It needs only the Python standard library and uses integers throughout. The input is the exact pilot model and the squarefree twist parameter d=13. No randomness, approximate L value or mathematical database enters the computation.

The output tests the Frobenius witnesses for residual primes 3 and 7, ordinarity there, the multiplicative witness at 11, and the minimal additive reduction witness at 13 for the twist. The transformation `X=4*x`, `Y=8*y+4` sends the base equation to `Y^2=X^3-4*X^2-160*X-1264`; multiplying the three coefficients by d, d² and d³ gives its quadratic twist. The coordinate scaling is a unit at every odd local prime used here.

The [source and argument record](../../sources/run-003-route-b.md) supplies the mathematical bridges. [output.json](output.json) and [receipt.json](receipt.json) retain the actual execution, hashes and scope. The receipt is an author execution record, not a trusted verifier signature. No analytic premise is certified by this experiment.
