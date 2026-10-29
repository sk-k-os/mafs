"""Exact finite checks for the qualified rank two congruent number family.

This checks arithmetic, not the cited descent or Selmer theorems.
"""
from fractions import Fraction
from itertools import product
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform
import sys


def rank_f2(rows: list[list[int]]) -> int:
    matrix = [row[:] for row in rows]
    rank = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for i in range(len(matrix)):
            if i != rank and matrix[i][col]:
                matrix[i] = [a ^ b for a, b in zip(matrix[i], matrix[rank])]
        rank += 1
    return rank


def is_prime(n: int) -> bool:
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def monsky_matrix(a: list[list[int]]) -> list[list[int]]:
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    top = [[a[i][j] ^ identity[i][j] for j in range(3)] + identity[i] for i in range(3)]
    bottom = [identity[i] + a[i] for i in range(3)]
    return top + bottom


def squareclass(value: Fraction) -> tuple[int, ...]:
    basis = (-1, 2, 3, 43, 59)
    result = [int(value < 0)]
    num, den = abs(value.numerator), value.denominator
    for p in basis[1:]:
        parity = 0
        while num % p == 0:
            num //= p
            parity ^= 1
        while den % p == 0:
            den //= p
            parity ^= 1
        result.append(parity)
    assert num == den == 1
    return tuple(result)


u, v = 2, 1
q = 3 * u**4 + 3 * v**4 - 2 * u**2 * v**2
r = 3 * u**4 + 3 * v**4 + 2 * u**2 * v**2
n = 3 * q * r
assert (q, r, n) == (43, 59, 7611)
assert is_prime(q) and is_prime(r)
assert q % 8 == r % 8 == n % 8 == 3
points = [
    (Fraction(-9 * q * (u*u-v*v)**2), Fraction(36 * q*q * u*v*(u*u-v*v))),
    (Fraction(3*q*r*r, 4*u*u*v*v), Fraction(9*q*q*r*r*(u*u+v*v), 8*u**3*v**3)),
]
assert all(y*y == x*(x*x-n*n) for x, y in points)
classes = [squareclass(Fraction(-n*n)), squareclass(Fraction(n))]
classes.extend(squareclass(point[0]) for point in points)
assert rank_f2([list(row) for row in classes]) == 4

cases = []
for upper in product((0, 1), repeat=3):
    a = [[0] * 3 for _ in range(3)]
    for (i, j), bit in zip(((0, 1), (0, 2), (1, 2)), upper):
        a[i][j], a[j][i] = bit, bit ^ 1
    for i in range(3):
        a[i][i] = sum(a[i]) % 2
    rank = rank_f2(monsky_matrix(a))
    assert rank in (4, 6)
    cases.append({"upper_A_bits": upper, "matrix_rank": rank, "pure_selmer_rank": 6-rank})

primes = (3, q, r)
a = [[0] * 3 for _ in range(3)]
for i, p in enumerate(primes):
    for j, other in enumerate(primes):
        if i != j:
            a[i][j] = int(pow(other, (p-1)//2, p) == p-1)
    a[i][i] = sum(a[i]) % 2
matrix = monsky_matrix(a)
assert rank_f2(matrix) == 4

output = {
    "python": platform.python_version(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "input": {"u": u, "v": v, "q": q, "r": r, "n": n},
    "points": [[str(x), str(y)] for x, y in points],
    "point_equations_verified": True,
    "squareclass_basis": [-1, 2, 3, 43, 59],
    "squareclass_rows_T0_Tn_P1_P2": classes,
    "squareclass_rank": 4,
    "sample_monsky_matrix": matrix,
    "sample_matrix_rank": 4,
    "sample_pure_selmer_rank": 2,
    "all_eight_reciprocity_cases": cases,
    "scope": "Exact finite arithmetic conditional on cited descent and Monsky interpretations. No analytic L function or full Sha computation.",
}
rendered = json.dumps(output, indent=2) + "\n"
if len(sys.argv) == 2:
    Path(sys.argv[1]).write_text(rendered)
else:
    print(rendered, end="")
