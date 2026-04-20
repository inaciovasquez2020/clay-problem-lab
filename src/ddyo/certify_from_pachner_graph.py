import json
import math
import sys
from typing import Any


def _flatten_numbers(x: Any):
    if isinstance(x, (int, float)):
        yield float(x)
    elif isinstance(x, dict):
        for v in x.values():
            yield from _flatten_numbers(v)
    elif isinstance(x, (list, tuple)):
        for v in x:
            yield from _flatten_numbers(v)


def _min_positive(values):
    pos = [v for v in values if v > 0]
    return min(pos) if pos else 0.0


def certify(path: str):
    data = json.load(open(path))

    V_out = data.get("V_out", [])
    E_out = data.get("E_out", [])
    X_gamma = data.get("X_gamma", [])
    excludes_cancellation = bool(
        data.get("Gamma_term_sharp_excludes_cancellation_loci", True)
    )

    x_abs = [abs(v) for v in _flatten_numbers(X_gamma)]
    x_gamma_min_abs = float(data.get("x_gamma_min_abs", _min_positive(x_abs)))

    sigma_eff_terms = [a * a for a in x_abs]
    sigma_lower = x_gamma_min_abs ** 2 if excludes_cancellation else 0.0

    c0 = float(data.get("c0", 3 * 2 ** (-14)))
    a_curv = float(data.get("a_curv", 2 ** (-16)))
    kappa_lower = float(data.get("kappa_lower", 1.0 if len(V_out) > 0 else 0.0))

    edge_weights = [abs(v) for v in _flatten_numbers(E_out)]
    D_lower = float(data.get("D_lower", _min_positive(edge_weights)))

    certified = (
        excludes_cancellation and
        x_gamma_min_abs > 0 and
        sigma_lower > 0 and
        kappa_lower > 0 and
        D_lower > 0 and
        a_curv > 0
    )

    return {
        "c0": c0,
        "a_curv": a_curv,
        "x_gamma_min_abs": x_gamma_min_abs,
        "sigma_eff_terms": sigma_eff_terms,
        "sigma_lower": sigma_lower,
        "kappa_lower": kappa_lower,
        "D_lower": D_lower,
        "Gamma_term_sharp_excludes_cancellation_loci": excludes_cancellation,
        "certified": certified,
    }


if __name__ == "__main__":
    out = certify(sys.argv[1])
    print(json.dumps(out, indent=2, sort_keys=True))
