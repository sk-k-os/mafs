"""Independent finite arithmetic for the run 003 scope review.

No author implementation is imported. Analytic ranks and full Sha are not computed.
"""
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path
import platform
import sys


def rank2(rows: list[list[int]]) -> int:
    a = [sum(value << j for j, value in enumerate(row)) for row in rows]
    pivots: dict[int, int] = {}
    for row in a:
        while row:
            leading = row.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = row
                break
            row ^= pivots[leading]
    return len(pivots)


def legendre(a: int, p: int) -> int:
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def pilot_trace(p: int) -> int:
    affine = sum(
        (y * y + y - x ** 3 + x * x + 10 * x + 20) % p == 0
        for x in range(p) for y in range(p)
    )
    return p - affine


def valuation(a: int, p: int) -> int:
    assert a != 0
    exponent = 0
    while a % p == 0:
        a //= p
        exponent += 1
    return exponent


def main() -> None:
    u, v = 2, 1
    q = 3 * u ** 4 + 3 * v ** 4 - 2 * u * u * v * v
    r = q + 4 * u * u * v * v
    assert (q, r) == (43, 59)
    for prime in (3, q, r):
        assert all(prime % d for d in range(2, prime) if d * d <= prime)
    n = 3 * q * r
    p1 = (F(-9 * q * (u * u - v * v) ** 2),
          F(36 * q * q * u * v * (u * u - v * v)))
    p2 = (F(3 * q * r * r, 4 * u * u * v * v),
          F(9 * q * q * r * r * (u * u + v * v), 8 * u ** 3 * v ** 3))
    assert all(y * y == x * (x * x - n * n) for x, y in (p1, p2))
    classes = [[1, 0, 0, 0], [0, 1, 1, 1], [1, 0, 0, 1], [0, 0, 1, 1]]
    assert rank2(classes) == 4
    cases: list[dict[str, object]] = []
    for bits in product((0, 1), repeat=3):
        a = [[0] * 3 for _ in range(3)]
        for (i, j), bit in zip(((0, 1), (0, 2), (1, 2)), bits):
            a[i][j] = bit
            a[j][i] = 1 - bit
        for i in range(3):
            a[i][i] = sum(a[i]) % 2
        ident = [[int(i == j) for j in range(3)] for i in range(3)]
        matrix = [[a[i][j] ^ ident[i][j] for j in range(3)] + ident[i] for i in range(3)]
        matrix += [ident[i] + a[i] for i in range(3)]
        rank = rank2(matrix)
        assert rank in (4, 6)
        cases.append({"upper_triangle_bits": bits, "rank": rank, "pure_selmer_rank": 6 - rank})
    primes = (3, q, r)
    sample_a = [[int(legendre(other, prime) == -1) if i != j else 0
                 for j, other in enumerate(primes)] for i, prime in enumerate(primes)]
    for i in range(3):
        sample_a[i][i] = sum(sample_a[i]) % 2
    sample_m = [[sample_a[i][j] ^ int(i == j) for j in range(3)]
                + [int(i == j) for j in range(3)] for i in range(3)]
    sample_m += [[int(i == j) for j in range(3)] + sample_a[i] for i in range(3)]
    assert rank2(sample_m) == 4

    traces = {str(p): pilot_trace(p) for p in (2, 3, 7)}
    assert traces == {"2": -2, "3": -1, "7": -2}
    assert legendre(traces["2"] ** 2 - 4 * 2, 3) == -1
    assert legendre(traces["3"] ** 2 - 4 * 3, 7) == -1
    assert traces["3"] % 3 and traces["7"] % 7
    b2, b4, b6, b8 = -4, -20, -79, -21
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    delta = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 ** 2 + 9 * b2 * b4 * b6
    assert (c4, c6, delta) == (496, 20008, -(11 ** 5))
    assert legendre(-c6, 11) == 1
    assert valuation(delta, 11) == 5
    assert all(5 % p for p in (3, 7))
    twist13_traces = {
        str(p): p - sum((y*y - x*x*x + 4*13*x*x + 160*13**2*x + 1264*13**3) % p == 0
                       for x in range(p) for y in range(p))
        for p in (3, 7)
    }
    assert twist13_traces == {"3": -1, "7": 2}

    twist_rows: list[dict[str, object]] = []
    for d in (1, 2, 5, 13):
        a, b = -27 * c4 * d * d, -54 * c6 * d ** 3
        short_delta = -16 * (4 * a ** 3 + 27 * b * b)
        assert short_delta == 6 ** 12 * delta * d ** 6
        chi = legendre(d, 5)
        twist_rows.append({"d": d, "delta_mod5": short_delta % 5,
                           "chi_at5": chi, "local_filter": short_delta % 5 != 0 and chi == -1})
        if d == 13:
            assert valuation(short_delta, 13) == 6
            assert valuation(-48 * a, 13) == 2
        if d == 5:
            assert valuation(short_delta, 5) == 6
            assert valuation(-48 * a, 5) == 2
    assert [row["d"] for row in twist_rows if row["local_filter"]] == [2, 13]
    record = {
        "python": platform.python_version(),
        "implementation": "separate_referee_standard_library_only",
        "arithmetic": "integer_and_Fraction",
        "random_seed": None,
        "family_sample": {"u": u, "v": v, "q": q, "r": r, "n": n,
                          "points": [[str(x), str(y)] for x, y in (p1, p2)]},
        "squareclass_matrix_rank": 4,
        "Monsky_cases": cases,
        "sample_Monsky_matrix": sample_m,
        "sample_Monsky_rank": rank2(sample_m),
        "pilot_traces": traces,
        "pilot_c4_c6_delta": [c4, c6, delta],
        "mod3_and_mod7_irreducibility_witnesses": True,
        "ordinary_at3_and7": True,
        "twist13_traces_scale2_model": twist13_traces,
        "twist13_v13_discriminant_c4": [6, 2],
        "local_filter_at5": twist_rows,
        "input_sha256": {name: hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in sys.argv[1:]},
        "finite_checks_passed": True,
        "analytic_rank_computed": False,
        "formal_verification": False,
    }
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
