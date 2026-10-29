#!/usr/bin/env python3
"""Independent exact arithmetic checks for the run 002 analytic certificate.

Uses no author code and no external mathematics packages. This checks finite
arithmetic witnesses; it does not formalize the surrounding analytic proof.
"""

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys


def arctan_bounds(q: Fraction, pairs: int) -> tuple[Fraction, Fraction]:
    """Alternating sum with an even term count; omitted term bounds remainder."""
    low = sum(
        ((-1) ** j * q ** (2 * j + 1) / (2 * j + 1) for j in range(2 * pairs)),
        Fraction(0),
    )
    return low, low + q ** (4 * pairs + 1) / (4 * pairs + 1)


def curve_points(p: int) -> list[tuple[int, int]]:
    return [
        (x, y)
        for x in range(p)
        for y in range(p)
        if (y * y + y - x * x * x + x) % p == 0
    ]


def main() -> None:
    b2, b4, b6, b8 = 0, -2, 1, -1
    c4 = b2 ** 2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    discriminant = -b2 ** 2 * b8 - 8 * b4 ** 3 - 27 * b6 ** 2 + 9 * b2 * b4 * b6
    assert (c4, c6, discriminant) == (48, -216, 37)
    assert c4 ** 3 - c6 ** 2 == 1728 * discriminant

    points2 = curve_points(2)
    assert len(points2) == 4
    a2 = 2 - len(points2)
    assert a2 == -2

    points37 = curve_points(37)
    singular = [
        (x, y) for x, y in points37
        if (3 * x * x - 1) % 37 == 0 and (2 * y + 1) % 37 == 0
    ]
    assert singular == [(5, 18)]
    # At the multiplicative prime, a_p = p - #E_ns(F_p).
    nonsingular_projective = len(points37) + 1 - len(singular)
    a37 = 37 - nonsingular_projective
    assert a37 == -1
    squares37 = {t * t % 37 for t in range(1, 37)}
    assert 15 not in squares37 and 216 % 37 not in squares37

    # atan(1/2) + atan(1/3) = pi/4 by the addition law and angle ranges.
    half_lo, half_hi = arctan_bounds(Fraction(1, 2), 5)
    third_lo, third_hi = arctan_bounds(Fraction(1, 3), 5)
    pi_lo = 4 * (half_lo + third_lo)
    pi_hi = 4 * (half_hi + third_hi)
    assert pi_lo > Fraction(31, 10)
    assert pi_hi < Fraction(22, 7)
    assert 4 * Fraction(31, 10) ** 2 > 37
    assert 4 * Fraction(22, 7) ** 2 < 37 * Fraction(11, 10) ** 2

    # Also check the distinct finite comparisons stated in the frozen author text.
    author_pi_lower = 4 * sum(
        (Fraction((-1) ** k, 2 * k + 1) for k in range(26)), Fraction(0)
    )
    author_pi_upper = 4 * sum(
        (Fraction((-1) ** k, 2 * k + 1) for k in range(7)), Fraction(0)
    )
    assert author_pi_lower > Fraction(31, 10)
    assert author_pi_upper < Fraction(33, 10)
    z = Fraction(11, 10)
    author_exp_upper = 1 + z + z ** 2 / (2 * (1 - z / 3))
    assert author_exp_upper == Fraction(1161, 380) < Fraction(10, 3)

    points3 = curve_points(3)
    assert len(points3) + 1 == 7
    assert all((t * t + 3 * t + 3) % 5 != 0 for t in range(5))

    # e > sum(k=0..3,1/k!) = 8/3, hence e^(-1) < 3/8.
    factorial = 1
    e_partial = Fraction(0)
    for k in range(4):
        if k:
            factorial *= k
        e_partial += Fraction(1, factorial)
    assert e_partial == Fraction(8, 3)
    q = 1 / e_partial
    assert q == Fraction(3, 8)

    # Analytic factorial comparison gives e < 3 and e^(1/10) < 10/9.
    exp_upper = 3 / (1 - Fraction(1, 10))
    e1_lower = 1 / exp_upper / (1 + Fraction(11, 10))
    assert e1_lower == Fraction(1, 7)
    e1_second_upper = q ** 2 / 2
    coefficient_tail_upper = 2 * q ** 3 / (3 * (1 - q))
    assert e1_second_upper == Fraction(9, 128)
    assert coefficient_tail_upper == Fraction(9, 160)
    derivative_lower = 2 * (e1_lower - e1_second_upper - coefficient_tail_upper)
    derivative_upper = 2 * (q + coefficient_tail_upper)
    assert derivative_lower == Fraction(73, 2240) > 0
    assert derivative_upper == Fraction(69, 80)

    files = [Path(name) for name in sys.argv[1:]]
    inputs = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    record = {
        "role": "separate_model_referee",
        "implementation": "independently_written_standard_library_python",
        "python": platform.python_version(),
        "arithmetic": "exact_integer_and_Fraction",
        "random_seed": None,
        "formal_proof": False,
        "input_hashes": inputs,
        "a2": a2,
        "a37": a37,
        "c4_c6_discriminant": [c4, c6, discriminant],
        "singular_mod37": singular,
        "pi_interval": [str(pi_lo), str(pi_hi)],
        "author_pi_interval": [str(author_pi_lower), str(author_pi_upper)],
        "author_exp_upper": str(author_exp_upper),
        "x_interval": ["1", "11/10"],
        "e1_lower": str(e1_lower),
        "e1_second_upper": str(e1_second_upper),
        "coefficient_tail_upper": str(coefficient_tail_upper),
        "derivative_interval": [str(derivative_lower), str(derivative_upper)],
        "C_mod3_point_count": len(points3) + 1,
        "C_mod5_Frobenius_at3_has_no_root": True,
        "finite_checks_passed": True,
        "analytic_bridges_checked_in_prose": True,
    }
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
