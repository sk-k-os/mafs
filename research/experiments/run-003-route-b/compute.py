"""Exact local tests for the pilot twist comparison; no analytic rank output."""

from __future__ import annotations

import json

Model = tuple[int, int, int, int, int]


def invariants(model: Model) -> dict[str, int]:
    a1, a2, a3, a4, a6 = model
    b2: int = a1 * a1 + 4 * a2
    b4: int = a1 * a3 + 2 * a4
    b6: int = a3 * a3 + 4 * a6
    b8: int = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    return {
        "c4": b2 * b2 - 24 * b4,
        "c6": -b2**3 + 36 * b2 * b4 - 216 * b6,
        "delta": -b2 * b2 * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6,
    }


def point_count(model: Model, prime: int) -> int:
    a1, a2, a3, a4, a6 = model
    return 1 + sum(
        (y * y + a1 * x * y + a3 * y - x**3 - a2 * x * x - a4 * x - a6) % prime == 0
        for x in range(prime)
        for y in range(prime)
    )


def valuation(integer: int, prime: int) -> int:
    assert integer != 0
    result: int = 0
    while integer % prime == 0:
        integer //= prime
        result += 1
    return result


def main() -> dict[str, object]:
    base: Model = (0, -1, 1, -10, -20)
    base_inv: dict[str, int] = invariants(base)
    assert base_inv == {"c4": 496, "c6": 20008, "delta": -(11**5)}
    counts: dict[str, dict[str, int]] = {
        str(prime): {"points": point_count(base, prime), "a_q": prime + 1 - point_count(base, prime)}
        for prime in (2, 3, 7)
    }
    assert [counts[str(prime)]["a_q"] for prime in (2, 3, 7)] == [-2, -1, -2]
    witnesses: list[dict[str, object]] = []
    for p, q in ((3, 2), (7, 3)):
        trace: int = counts[str(q)]["a_q"]
        roots: list[int] = [t for t in range(p) if (t * t - trace * t + q) % p == 0]
        discriminant: int = (trace * trace - 4 * q) % p
        assert roots == []
        assert counts[str(p)]["a_q"] % p != 0
        witnesses.append({"residual_prime": p, "frobenius_prime": q, "trace": trace,
                          "discriminant_mod_p": discriminant, "roots_mod_p": roots,
                          "base_ordinary": True, "five_is_p_unit": 5 % p != 0})
    d: int = 13
    twist: Model = (0, -4 * d, 0, -160 * d * d, -1264 * d**3)
    twist_inv: dict[str, int] = invariants(twist)
    assert twist_inv["c4"] == 2**4 * d**2 * base_inv["c4"]
    assert twist_inv["c6"] == 2**6 * d**3 * base_inv["c6"]
    assert twist_inv["delta"] == 2**12 * d**6 * base_inv["delta"]
    valuations: dict[str, int] = {name: valuation(value, 13) for name, value in twist_inv.items()}
    assert valuations == {"c4": 2, "c6": 3, "delta": 6}
    assert [entry % 13 for entry in twist] == [0, 0, 0, 0, 0]
    twist_counts: dict[str, dict[str, int]] = {
        str(p): {"points": point_count(twist, p), "a_p": p + 1 - point_count(twist, p)}
        for p in (3, 7)
    }
    assert twist_counts["3"]["a_p"] == -1
    assert twist_counts["7"]["a_p"] == 2
    assert (-base_inv["c6"]) % 11 == 1
    assert valuation(base_inv["delta"], 11) == 5
    return {
        "status": "all finite exact checks passed",
        "arithmetic": "integers only",
        "base_model": base,
        "base_invariants": base_inv,
        "base_counts": counts,
        "irreducibility_witnesses": witnesses,
        "split_multiplicative_11_test": {"minus_c6_mod_11": 1, "v11_delta": 5},
        "twist_d": d,
        "twist_integral_model": twist,
        "twist_invariants": twist_inv,
        "twist_13_valuations": valuations,
        "twist_counts": twist_counts,
        "analytic_rank": "not computed or certified",
        "trust_limit": "finite arithmetic; mathematical bridges require separate review",
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
