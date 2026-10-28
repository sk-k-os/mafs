#!/usr/bin/env python3
"""Separate exact arithmetic replay. This is not a formal proof checker."""
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform
import time


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "research/experiments/run-001-local-counts"
REVIEWED = [
    "research/findings/run-001-representation-obstruction.md",
    "research/sources/run-001-jsw-audit.md",
    "research/sources/run-001-representation-bridges.md",
    *["research/experiments/run-001-local-counts/" + name
      for name in ("input.json", "compute.py", "output.json", "receipt.json", "README.md")],
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(point, q):
    first = next(value for value in point if value % q)
    scale = pow(first, -1, q)
    return tuple(value * scale % q for value in point)


def representatives(q):
    # First nonzero coordinate is 1, unlike the submitted affine chart scheme.
    for y in range(q):
        for z in range(q):
            yield (1, y, z)
    for z in range(q):
        yield (0, 1, z)
    yield (0, 0, 1)


def equation(a, point):
    a1, a2, a3, a4, a6 = a
    x, y, z = point
    return (y*y*z + a1*x*y*z + a3*y*z*z
            - x*x*x - a2*x*x*z - a4*x*z*z - a6*z*z*z)


def partials(a, point):
    a1, a2, a3, a4, a6 = a
    x, y, z = point
    return (a1*y*z - 3*x*x - 2*a2*x*z - a4*z*z,
            2*y*z + a1*x*z + a3*z*z,
            y*y + a1*x*y + 2*a3*y*z - a2*x*x - 2*a4*x*z - 3*a6*z*z)


def short_invariants(a):
    a1, a2, a3, a4, a6 = map(F, a)
    # Complete the square, then remove the quadratic term over Q.
    h = a2 + a1*a1/4
    j = a4 + a1*a3/2
    k = a6 + a3*a3/4
    A = j - h*h/3
    B = k - h*j/3 + 2*h*h*h/27
    result = {"c4": -48*A, "c6": -864*B,
              "Delta": -16*(4*A*A*A + 27*B*B)}
    assert all(value.denominator == 1 for value in result.values())
    return {name: int(value) for name, value in result.items()}


def pilot_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u and y + v == -1:
        return None
    m = (3*x*x-2*x-10)/(2*y+1) if P == Q else (v-y)/(u-x)
    b = y-m*x
    X = m*m + 1 - x - u
    return (X, -m*X-b-1)


def main():
    started = datetime.now(timezone.utc).isoformat()
    timer = time.perf_counter()
    hashes = {name: digest(ROOT / name) for name in REVIEWED}
    inputs = json.loads((EXPERIMENT / "input.json").read_text())
    submitted = json.loads((EXPERIMENT / "output.json").read_text())
    author_receipt = json.loads((EXPERIMENT / "receipt.json").read_text())
    assert inputs["coefficient_order"] == ["a1", "a2", "a3", "a4", "a6"]
    assert inputs["maximum_auxiliary_prime"] == 43
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    assert submitted["prime_range"] == primes
    for name, expected in author_receipt["artifact_hashes"].items():
        assert digest(EXPERIMENT / name) == expected
    rows, bad_rows, invariants = [], [], []
    witness_primes = []
    for frozen, result in zip(inputs["curves"], submitted["curves"]):
        assert frozen["coefficients"] == result["coefficients"]
        assert frozen["input_alias"] == result["input_alias"]
        a = frozen["coefficients"]
        inv = short_invariants(a)
        assert all(result["invariants"][key] == value for key, value in inv.items())
        assert inv["c4"]**3 - inv["c6"]**2 == 1728*inv["Delta"]
        invariants.append({"coefficients": a, **inv})
        good = {row["q"]: row for row in result["good_prime_counts"]}
        bad = {row["q"]: row for row in result["singular_primes_in_range"]}
        assert set(good).isdisjoint(bad) and set(good) | set(bad) == set(primes)
        for q in primes:
            points = [pt for pt in representatives(q) if equation(a, pt) % q == 0]
            singular = {pt for pt in points if all(g % q == 0 for g in partials(a, pt))}
            if inv["Delta"] % q == 0:
                assert q in bad
                expected_singular = {canonical(pt, q) for pt in bad[q]["rational_singular_points"]}
                assert singular == expected_singular
                bad_rows.append({"coefficients": a, "q": q,
                                 "singular_points_first_coordinate_normalization": sorted(singular)})
                continue
            assert q in good and not singular
            row = good[q]
            n = len(points)
            aq = q+1-n
            assert n == row["projective_points"] == row["comparison_points"]
            assert n-1 == row["affine_points"] and row["points_at_infinity"] == 1
            assert row["Delta_mod_q"] == inv["Delta"] % q
            assert aq == row["a_q"] and aq*aq <= 4*q
            assert row["methods_agree"] and row["hasse_consistency_check"]
            assert row["rational_singular_points"] == []
            rows.append({"coefficients": a, "q": q, "projective_points": n, "a_q": aq})
            if frozen["input_alias"] == "37a1" and q != 5:
                if all((t*t-aq*t+q) % 5 for t in range(5)):
                    witness_primes.append(q)
    assert len(inputs["curves"]) == len(submitted["curves"]) == 3
    assert len(rows) == submitted["comparison_rows"] == 40
    assert witness_primes == [item["q"] for item in submitted["residual_representation_witness_search"]["candidates"]]
    P, Q, multiples = (F(5), F(5)), None, []
    for n in range(1, 6):
        Q = pilot_add(Q, P)
        if Q is not None:
            x, y = Q
            assert y*y+y == x*x*x-x*x-10*x-20
        multiples.append({"n": n, "point": None if Q is None else [str(v) for v in Q]})
    assert multiples == [{"n": 1, "point": ["5", "5"]},
                         {"n": 2, "point": ["16", "-61"]},
                         {"n": 3, "point": ["16", "60"]},
                         {"n": 4, "point": ["5", "-6"]},
                         {"n": 5, "point": None}]
    # B transformed by t=2y+1 has t^2=4x^3-4x^2-40x-79.
    # Its negative twist is -t^2=4x^3-4x^2-40x-79, with three F3 points.
    negative_twist_affine = [(x, t) for x in range(3) for t in range(3)
                             if (-t*t - (4*x**3-4*x*x-40*x-79)) % 3 == 0]
    assert negative_twist_affine == [(0, 1), (0, 2)]
    assert all(digest(ROOT / name) == value for name, value in hashes.items())
    record = {
        "status": "exact finite replay passed; separate model review, not formal verification",
        "started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": time.perf_counter()-timer,
        "python_version": platform.python_version(), "python_implementation": platform.python_implementation(),
        "command": "python3 research/reviews/run-001-replay.py",
        "reviewed_artifact_sha256": hashes, "replay_script_sha256": digest(Path(__file__)),
        "author_receipt_hashes_match": True, "reviewed_artifacts_unchanged_during_replay": True,
        "method": "independently written first nonzero coordinate projective enumeration; rational short model invariants; exact rational group law",
        "shared_dependencies": ["same supplied coefficients", "same mathematical identities", "Python interpreter family", "shared filesystem and source evidence"],
        "randomness_used": False, "floating_point_arithmetic_for_math": False,
        "count_rows_checked": len(rows), "count_discrepancies": 0, "rows": rows,
        "singular_rows": bad_rows, "invariants": invariants,
        "irreducible_frobenius_polynomial_primes": witness_primes,
        "pilot_multiples": multiples,
        "negative_twist_probe": {"d": -1, "q": 3, "affine_points": negative_twist_affine,
                                 "projective_count": len(negative_twist_affine)+1},
        "exit_status": 0,
        "not_established": ["analytic rank", "BSD", "formal proof", "qualified external human review", "trusted service attestation"],
    }
    destination = ROOT / "research/reviews/run-001-replay.json"
    destination.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "passed", "count_rows_checked": len(rows),
                      "count_discrepancies": 0, "receipt_sha256": digest(destination)}))


if __name__ == "__main__":
    main()
