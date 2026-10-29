from __future__ import annotations
import json

def rows() -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for d in (1, 2, 5, 13):
        A, B = -27*496*d*d, -54*20008*d*d*d
        delta = -16*(4*A**3+27*B**2)
        residue = pow(d % 5, 2, 5)
        chi = 0 if residue == 0 else (1 if residue == 1 else -1)
        result.append({"d":d,"short_model_delta_mod5":delta%5,
                       "legendre_d_at5":chi,
                       "CGS_local_filter_passes":delta%5!=0 and chi==-1})
    assert [r["d"] for r in result if r["CGS_local_filter_passes"]] == [2,13]
    return result

print(json.dumps({"rows":rows(),"analytic_rank_computed":False,
                  "meaning":"Finite local filter only; not a BSD certificate"},indent=2))
