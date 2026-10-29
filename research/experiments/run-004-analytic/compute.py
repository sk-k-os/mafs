"""Integer interval certificate for the analytic derivative of E_7611.

Analytic and CM identities are explicit external mathematical dependencies.
Every numerical bound in this program uses Python integers or Fraction.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from math import isqrt

Interval = tuple[int, int]
SCALE: int = 10**45
LIMIT: int = 220_000
KERNEL_TERMS: int = 200
LOG_TERMS: int = 55
HARMONIC_TERMS: int = 1_000_000
RADICAND: int = 7611


def ceildiv(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def ratio(a: int, b: int) -> Interval:
    return a * SCALE // b, ceildiv(a * SCALE, b)


def add(a: Interval, b: Interval) -> Interval:
    return a[0] + b[0], a[1] + b[1]


def sub(a: Interval, b: Interval) -> Interval:
    return a[0] - b[1], a[1] - b[0]


def times(a: Interval, n: int) -> Interval:
    return (a[0] * n, a[1] * n) if n >= 0 else (a[1] * n, a[0] * n)


def divide(a: Interval, n: int) -> Interval:
    return a[0] // n, ceildiv(a[1], n)


def multiply(a: Interval, b: Interval) -> Interval:
    products: tuple[int, int, int, int] = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(products) // SCALE, ceildiv(max(products), SCALE)


def square(a: Interval) -> Interval:
    low: int = 0 if a[0] <= 0 <= a[1] else min(a[0]*a[0], a[1]*a[1])
    return low // SCALE, ceildiv(max(a[0]*a[0], a[1]*a[1]), SCALE)


def atanh_twice(z: Interval) -> Interval:
    assert 0 <= z[0] <= z[1] <= ceildiv(SCALE, 3)
    z2: Interval = square(z)
    power: Interval = z
    result: Interval = (0, 0)
    for k in range(LOG_TERMS):
        result = add(result, divide(power, 2*k+1))
        power = multiply(power, z2)
    # Remaining positive terms <= z^(2K+1)/((2K+1)(1-z²)).
    remainder: int = ceildiv(power[1]*SCALE, (2*LOG_TERMS+1)*(SCALE-z2[1]))
    return 2*result[0], 2*(result[1]+remainder)


LOG_TWO: Interval = atanh_twice(ratio(1, 3))


def logarithm(a: Interval) -> Interval:
    assert 0 < a[0] <= a[1]
    low: int = a[0]
    high: int = a[1]
    denominator: int = SCALE
    exponent: int = 0
    while low < denominator:
        low *= 2
        high *= 2
        exponent -= 1
    while low >= 2*denominator:
        denominator *= 2
        exponent += 1
    assert high < 2*denominator
    z: Interval = ((low-denominator)*SCALE//(low+denominator),
                   ceildiv((high-denominator)*SCALE, high+denominator))
    return add(times(LOG_TWO, exponent), atanh_twice(z))


def atan_reciprocal(denominator: int, terms: int) -> tuple[Fraction, Fraction]:
    total: Fraction = sum((Fraction((-1)**k, (2*k+1)*denominator**(2*k+1))
                           for k in range(terms)), Fraction(0))
    next_term: Fraction = Fraction((-1)**terms, (2*terms+1)*denominator**(2*terms+1))
    return min(total, total+next_term), max(total, total+next_term)


def pi_interval() -> Interval:
    a: tuple[Fraction, Fraction] = atan_reciprocal(5, 40)
    b: tuple[Fraction, Fraction] = atan_reciprocal(239, 12)
    low: Fraction = 16*a[0]-4*b[1]
    high: Fraction = 16*a[1]-4*b[0]
    return low.numerator*SCALE//low.denominator, ceildiv(high.numerator*SCALE, high.denominator)


def gamma_interval() -> Interval:
    low: int = sum(SCALE//k for k in range(1, HARMONIC_TERMS+1))
    high: int = sum(ceildiv(SCALE, k) for k in range(1, HARMONIC_TERMS+1))
    harmonic_minus_log: Interval = sub((low, high), logarithm((HARMONIC_TERMS*SCALE,)*2))
    return harmonic_minus_log[0]-ceildiv(SCALE, HARMONIC_TERMS), harmonic_minus_log[1]


def coefficients() -> list[int]:
    smallest: list[int] = list(range(LIMIT+1))
    for p in range(2, isqrt(LIMIT)+1):
        if smallest[p] == p:
            for multiple in range(p*p, LIMIT+1, p):
                if smallest[multiple] == multiple:
                    smallest[multiple] = p
    prime_trace: list[int] = [0]*(LIMIT+1)
    for a in range(1, isqrt(LIMIT)+1, 2):
        for b in range(2, isqrt(LIMIT-a*a)+1, 2):
            p: int = a*a+b*b
            if smallest[p] == p:
                signed_a: int = a if (a+b) % 4 == 1 else -a
                character: int = pow(RADICAND % p, (p-1)//2, p)
                if character == p-1:
                    character = -1
                assert character in (-1, 0, 1)
                prime_trace[p] = 2*signed_a*character
    values: list[int] = [0]*(LIMIT+1)
    values[1] = 1
    for m in range(2, LIMIT+1):
        p = smallest[m]
        if (2*RADICAND) % p == 0:
            values[m] = 0
        else:
            rest: int = m//p
            values[m] = prime_trace[p]*values[rest]
            if rest % p == 0:
                values[m] -= p*values[rest//p]
        assert abs(values[m]) <= 2*m
    return values


def kernel(x: Interval, gamma: Interval, pi: Interval) -> Interval:
    result: Interval = add(divide(square(add(logarithm(x), gamma)), 2), divide(square(pi), 12))
    term: Interval = x
    for k in range(1, KERNEL_TERMS+1):
        result = sub(result, term) if k % 2 else add(result, term)
        term = divide(times(multiply(term, x), k*k), (k+1)**3)
    # Terms now decrease: absolute remaining tail <= next/(1-x/(K+2)).
    assert x[1] < (KERNEL_TERMS+2)*SCALE
    remainder: int = ceildiv(term[1]*(KERNEL_TERMS+2)*SCALE,
                             (KERNEL_TERMS+2)*SCALE-x[1])
    return result[0]-remainder, result[1]+remainder


def render(a: Interval) -> dict[str, str]:
    return {"lower_numerator": str(a[0]), "upper_numerator": str(a[1]), "denominator": str(SCALE)}


def main() -> dict[str, object]:
    pi: Interval = pi_interval()
    gamma: Interval = gamma_interval()
    conductor: int = 32*RADICAND**2
    root_floor: int = isqrt(conductor*SCALE*SCALE)
    x: Interval = (2*pi[0]*SCALE//(root_floor+1), ceildiv(2*pi[1]*SCALE, root_floor))
    values: list[int] = coefficients()
    total: Interval = (0, 0)
    used: int = 0
    for m in range(1, LIMIT+1):
        if values[m] != 0:
            total = add(total, divide(times(kernel(times(x, m), gamma, pi), 4*values[m]), m))
            used += 1
    t_lower: int = x[0]*(LIMIT+1)
    exponent: int = t_lower//SCALE
    # exp(-t) < 2^(-floor(t)); 1/(1-exp(-x)) <= (1+x)/x.
    tail: int = ceildiv(8*SCALE**3*(SCALE+x[0]), (2**exponent)*t_lower*t_lower*x[0])
    enclosure: Interval = (total[0]-tail, total[1]+tail)
    coefficient_json: str = json.dumps(values, separators=(",", ":"))
    assert 100*enclosure[0] > 1561*SCALE
    assert 100*enclosure[1] < 1563*SCALE
    return {
        "curve_coefficients": [0, 0, 0, -RADICAND**2, 0],
        "conductor_dependency": conductor,
        "interval_scale": str(SCALE),
        "coefficient_cutoff": LIMIT,
        "nonzero_coefficient_terms_used": used,
        "coefficient_sha256": hashlib.sha256(coefficient_json.encode()).hexdigest(),
        "kernel_terms": KERNEL_TERMS,
        "log_terms": LOG_TERMS,
        "harmonic_terms": HARMONIC_TERMS,
        "pi_interval": render(pi),
        "gamma_interval": render(gamma),
        "x_interval": render(x),
        "partial_second_derivative": render(total),
        "absolute_tail_upper_numerator": str(tail),
        "second_derivative_enclosure": render(enclosure),
        "lower_bound_positive": enclosure[0] > 0,
        "coarse_strict_lower": "1561/100",
        "coarse_strict_upper": "1563/100",
        "sample_coefficients": {str(m): values[m] for m in (1,2,3,5,7,9,13,17,25,43,49,59,121,169)},
        "status": "integer interval computation; analytic and CM bridges require separate review",
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
