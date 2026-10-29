# Run 002 exact analytic arithmetic

The [argument](../../findings/run-002-analytic-certificate.md) reduces positivity of the derivative to rational comparisons. `compute.py` checks those comparisons and enumerates C(F2) directly. It uses only the Python standard library, integers and `fractions.Fraction`. There is no random input, approximate quadrature, floating point evaluation, package installation or network dependency.

From the repository root, reproduce the deterministic output with:

```bash
python3 research/experiments/run-002-analytic/compute.py
```

Compare it with [output.json](output.json). The [receipt](receipt.json) records the actual source and output hashes, command, Python version, exit status and measured elapsed execution time. This receipt was produced by the submitting agent; it is not a trusted verifier signature. Separate replay and mathematical review are required.

The output proves finite arithmetic facts only. The implications involving the integral E1, the infinite coefficient bound, modularity, conductor, root number and differentiation remain in the accompanying mathematical argument and its sourced dependencies. No claim of formal verification is made.
