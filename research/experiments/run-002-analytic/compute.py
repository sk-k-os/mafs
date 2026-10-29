"""Exact rational arithmetic supporting the run 002 analytic argument.

This is a finite arithmetic verifier, not a formal verification of modularity,
the functional equation, Hasse's bound, or the analytic inequalities in the
accompanying mathematical argument. No floating point arithmetic is used.
"""

from __future__ import annotations

from fractions import Fraction
import json
from math import factorial


def arctangent_one_partial(terms: int) -> Fraction:
    """Integral on [0,1] of the first terms of the geometric polynomial."""
    assert terms > 0
    return sum(
        (Fraction((-1) ** index, 2 * index + 1) for index in range(terms)),
        Fraction(0),
    )


def points_mod_two() -> list[list[int]]:
    return [
        [x, y]
        for x in range(2)
        for y in range(2)
        if (y * y + y - x * x * x + x) % 2 == 0
    ]


def rational_string(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def compute() -> dict[str, object]:
    pi_lower: Fraction = 4 * arctangent_one_partial(26)
    pi_upper: Fraction = 4 * arctangent_one_partial(7)
    assert pi_lower > Fraction(31, 10)
    assert pi_upper < Fraction(33, 10)
    assert Fraction(31, 5) ** 2 > 37
    assert 6**2 < 37
    assert Fraction(2) * Fraction(33, 10) / 6 == Fraction(11, 10)

    exp_one_lower: Fraction = sum(
        (Fraction(1, factorial(index)) for index in range(5)), Fraction(0)
    )
    assert exp_one_lower == Fraction(65, 24)
    assert exp_one_lower > Fraction(8, 3)

    exponent: Fraction = Fraction(11, 10)
    tail_ratio: Fraction = exponent / 3
    assert 0 < tail_ratio < 1
    exp_upper: Fraction = 1 + exponent + exponent**2 / (2 * (1 - tail_ratio))
    assert exp_upper == Fraction(1161, 380)
    assert exp_upper < Fraction(10, 3)
    main_lower: Fraction = 1 / (Fraction(10, 3) * (1 + exponent))
    assert main_lower == Fraction(1, 7)

    affine_points: list[list[int]] = points_mod_two()
    point_count: int = len(affine_points) + 1
    a_two: int = 2 + 1 - point_count
    assert point_count == 5
    assert a_two == -2

    q_upper: Fraction = Fraction(3, 8)
    second_upper: Fraction = q_upper**2 / 2
    remainder_upper: Fraction = 2 * q_upper**3 / (3 * (1 - q_upper))
    derivative_lower: Fraction = 2 * (main_lower - second_upper - remainder_upper)
    derivative_upper: Fraction = 2 * (q_upper + remainder_upper)
    assert second_upper == Fraction(9, 128)
    assert remainder_upper == Fraction(9, 160)
    assert derivative_lower == Fraction(73, 2240)
    assert derivative_upper == Fraction(69, 80)
    assert 0 < derivative_lower < derivative_upper

    return {
        "status": "finite rational checks passed",
        "curve_coefficients": [0, 0, 1, -1, 0],
        "arithmetic": "Python integers and fractions.Fraction only",
        "randomness": "none",
        "pi_lower_partial_terms": 26,
        "pi_lower_partial": rational_string(pi_lower),
        "pi_lower_comparison": "pi > 31/10",
        "pi_upper_partial_terms": 7,
        "pi_upper_partial": rational_string(pi_upper),
        "pi_upper_comparison": "pi < 33/10",
        "x_bounds": {"strict_lower": "1/1", "strict_upper": "11/10"},
        "exp_one_lower_partial": rational_string(exp_one_lower),
        "exp_eleven_tenths_upper": rational_string(exp_upper),
        "affine_points_mod_two": affine_points,
        "point_count_mod_two": point_count,
        "a_two": a_two,
        "main_term_strict_lower": rational_string(main_lower),
        "second_term_strict_upper": rational_string(second_upper),
        "remainder_absolute_strict_upper": rational_string(remainder_upper),
        "L_prime_enclosure_conditional_on_recorded_analytic_bridges": {
            "strict_lower": rational_string(derivative_lower),
            "strict_upper": rational_string(derivative_upper),
        },
        "excluded_scope": [
            "modularity theorem verification",
            "conductor and root number derivation",
            "Hasse theorem verification",
            "formal checking of analytic inequalities",
            "BSD beyond this analytic rank premise",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(compute(), indent=2, sort_keys=True))
