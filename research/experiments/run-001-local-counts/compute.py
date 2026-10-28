#!/usr/bin/env python3
"""Deterministic finite arithmetic calibration; never a BSD verifier."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
from typing import Iterator

Coefficients = tuple[int, int, int, int, int]
Point = tuple[int, int, int]


def primes_at_most(bound: int) -> list[int]:
    return [n for n in range(2, bound + 1)
            if all(n % divisor for divisor in range(2, n))]


def invariants(a: Coefficients) -> dict[str, int]:
    a1, a2, a3, a4, a6 = a
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2**3 + 36 * b2 * b4 - 216 * b6
    delta = -b2 * b2 * b8 - 8 * b4**3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    return {"b2": b2, "b4": b4, "b6": b6, "b8": b8,
            "c4": c4, "c6": c6, "Delta": delta}


def direct_affine_count(a: Coefficients, q: int) -> int:
    a1, a2, a3, a4, a6 = a
    count = 0
    for x in range(q):
        for y in range(q):
            if (y*y + a1*x*y + a3*y - x*x*x - a2*x*x - a4*x - a6) % q == 0:
                count += 1
    return count


def quadratic_character(value: int, q: int) -> int:
    residue = value % q
    if residue == 0:
        return 0
    euler_value = pow(residue, (q - 1) // 2, q)
    if euler_value not in (1, q - 1):
        raise ValueError("Character evaluated outside an odd prime field")
    return 1 if euler_value == 1 else -1


def character_count(a: Coefficients, q: int) -> int:
    if q == 2:
        raise ValueError("Completing the square count requires odd characteristic")
    a1, a2, a3, a4, a6 = a
    character_sum = 0
    for x in range(q):
        discriminant_in_y = (a1*x + a3)**2 + 4*(x**3 + a2*x*x + a4*x + a6)
        character_sum += quadratic_character(discriminant_in_y, q)
    return 1 + q + character_sum


def projective_representatives(q: int) -> Iterator[Point]:
    # Normalize Z=1 on the affine chart; otherwise X=1 or [0:1:0].
    for x in range(q):
        for y in range(q):
            yield x, y, 1
    for y in range(q):
        yield 1, y, 0
    yield 0, 1, 0


def homogeneous_equation(a: Coefficients, point: Point) -> int:
    a1, a2, a3, a4, a6 = a
    x, y, z = point
    return y*y*z + a1*x*y*z + a3*y*z*z - x**3 - a2*x*x*z - a4*x*z*z - a6*z**3


def homogeneous_gradient(a: Coefficients, point: Point) -> Point:
    a1, a2, a3, a4, a6 = a
    x, y, z = point
    return (a1*y*z - 3*x*x - 2*a2*x*z - a4*z*z,
            2*y*z + a1*x*z + a3*z*z,
            y*y + a1*x*y + 2*a3*y*z - a2*x*x - 2*a4*x*z - 3*a6*z*z)


def projective_count_at_two(a: Coefficients) -> int:
    # F_2 has one nonzero scalar, so the seven nonzero triples are unique classes.
    return sum(homogeneous_equation(a, (x, y, z)) % 2 == 0
               for x in (0, 1) for y in (0, 1) for z in (0, 1)
               if (x, y, z) != (0, 0, 0))


def rational_singular_points(a: Coefficients, q: int) -> list[list[int]]:
    return [list(point) for point in projective_representatives(q)
            if homogeneous_equation(a, point) % q == 0
            and all(value % q == 0 for value in homogeneous_gradient(a, point))]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    start_utc = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()
    directory = Path(__file__).resolve().parent
    input_path = directory / "input.json"
    data = json.loads(input_path.read_text(encoding="utf-8"))
    require(data["coefficient_order"] == ["a1", "a2", "a3", "a4", "a6"], "Unexpected coefficient ordering")
    primes = primes_at_most(data["maximum_auxiliary_prime"])
    p = data["representation_prime"]
    require(p in primes_at_most(p) and p != 2, "Representation modulus must be an odd prime")
    curves: list[dict[str, object]] = []
    witness_candidates: list[dict[str, int]] = []
    rows = 0
    for curve in data["curves"]:
        raw = curve["coefficients"]
        require(len(raw) == 5 and all(type(value) is int for value in raw), "Invalid coefficient vector")
        a: Coefficients = (raw[0], raw[1], raw[2], raw[3], raw[4])
        inv = invariants(a)
        identity = inv["c4"]**3 - inv["c6"]**2 == 1728 * inv["Delta"]
        require(inv["Delta"] != 0, "Singular rational curve")
        require(identity, "Invariant identity failed")
        good_rows: list[dict[str, object]] = []
        bad_rows: list[dict[str, object]] = []
        for q in primes:
            singular_points = rational_singular_points(a, q)
            if inv["Delta"] % q == 0:
                bad_rows.append({"q": q, "Delta_mod_q": 0,
                                 "rational_singular_points": singular_points,
                                 "elliptic_count_computed": False})
                continue
            require(not singular_points, "Good reduction criterion conflicts with rational singular point")
            affine = direct_affine_count(a, q)
            count = affine + 1
            comparison = projective_count_at_two(a) if q == 2 else character_count(a, q)
            require(count == comparison, "Point count methods disagree")
            aq = q + 1 - count
            hasse = aq * aq <= 4 * q
            require(hasse, "Point count violates Hasse consistency check")
            good_rows.append({"q": q, "Delta_mod_q": inv["Delta"] % q,
                              "affine_points": affine, "points_at_infinity": 1,
                              "projective_points": count, "comparison_points": comparison,
                              "comparison_method": "seven nonzero triples over F2" if q == 2 else "quadratic character sum",
                              "a_q": aq, "methods_agree": True,
                              "hasse_consistency_check": hasse,
                              "rational_singular_points": singular_points})
            rows += 1
            if curve["input_alias"] == data["witness_curve_input_alias"] and q != p:
                characteristic_discriminant = aq * aq - 4 * q
                residue = characteristic_discriminant % p
                if quadratic_character(residue, p) == -1:
                    witness_candidates.append({"q": q, "a_q": aq,
                                               "a_q_squared_minus_4q": characteristic_discriminant,
                                               "residue_mod_representation_prime": residue})
        curves.append({"input_alias": curve["input_alias"], "coefficients": raw,
                       "invariants": inv, "nonzero_rational_discriminant": True,
                       "invariant_identity_verified": identity,
                       "good_prime_counts": good_rows, "singular_primes_in_range": bad_rows})
    result = {"experiment": data["experiment"], "status": "candidate exact computation; separate review required",
              "prime_range": primes, "curves": curves,
              "comparison_rows": rows, "method_discrepancies": 0,
              "residual_representation_witness_search": {
                  "curve_input_alias": data["witness_curve_input_alias"], "representation_prime": p,
                  "square_residues_mod_representation_prime": sorted({x*x % p for x in range(p)}),
                  "good_auxiliary_primes_only": True, "excluded_auxiliary_prime": p,
                  "candidates": witness_candidates,
                  "first_candidate": witness_candidates[0] if witness_candidates else None,
                  "status": "candidate only; mathematical bridge and hypotheses require separate sourced review"},
              "claims_not_established": ["catalog identity", "conductor", "rank", "torsion", "analytic rank", "BSD", "Galois representation irreducibility"]}
    output_path = directory / "output.json"
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    receipt = {"experiment": data["experiment"], "command": "python3 research/experiments/run-001-local-counts/compute.py",
               "started_utc": start_utc, "finished_utc": datetime.now(timezone.utc).isoformat(),
               "elapsed_seconds": time.perf_counter() - start, "python_version": platform.python_version(),
               "python_implementation": platform.python_implementation(), "standard_library_only": True,
               "exact_integer_arithmetic": True, "randomness_used": False,
               "hash_algorithm": "SHA256", "artifact_hashes": {name: sha256(directory / name) for name in ("input.json", "compute.py", "output.json")},
               "exit_status": 0, "comparison_rows": rows, "method_discrepancies": 0,
               "assurance": "self reported execution receipt; not an independent verifier"}
    (directory / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"experiment": data["experiment"], "comparison_rows": rows,
                      "method_discrepancies": 0, "first_witness_candidate": witness_candidates[0] if witness_candidates else None,
                      "output_sha256": sha256(output_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
