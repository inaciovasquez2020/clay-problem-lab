#!/usr/bin/env python3
"""
Numerical RA1n transfer probe.

Status:
    NUMERICAL / NON-PROOF / FRONTIER AID

This script checks three finite-grid facts:

1. generic sigma: counterexample guard is active;
2. antisymmetric sigma: signed-pair cancellation is numerically detected;
3. projected packets: <Pi_{g^perp}F,g> is numerically zero.

No theorem-level closure is claimed.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Callable


Vector = tuple[float, float]


def dot(a: Vector, b: Vector) -> float:
    return a[0] * b[0] + a[1] * b[1]


def norm2(values: list[float], weight: float) -> float:
    return math.sqrt(sum(v * v * weight for v in values))


def inner(a: list[float], b: list[float], weight: float) -> float:
    return sum(x * y * weight for x, y in zip(a, b))


def grid(radius: float, cap_width: float, n: int) -> list[Vector]:
    pts: list[Vector] = []
    for i in range(n):
        t = -cap_width + 2.0 * cap_width * i / max(n - 1, 1)
        eta = (radius, radius * t)
        pts.append(eta)
    return pts


def sigma_generic(eta: Vector, radius: float) -> float:
    t = eta[1] / radius
    return 1.0 + 0.25 * t + 0.10 * t * t


def sigma_odd(eta: Vector, radius: float) -> float:
    t = eta[1] / radius
    return t


def sigma_even(eta: Vector, radius: float) -> float:
    t = eta[1] / radius
    return 1.0 + t * t


def build_g(
    pts: list[Vector],
    sigma: Callable[[Vector, float], float],
    radius: float,
    xi_out: Vector,
    xi_center: Vector,
    beta: Vector,
) -> list[float]:
    vals: list[float] = []
    for eta in pts:
        xi1_minus_center = (
            xi_out[0] - eta[0] - xi_center[0],
            xi_out[1] - eta[1] - xi_center[1],
        )
        affine = dot(xi1_minus_center, beta)
        jacobian = 1.0
        vals.append(affine * sigma(eta, radius) * jacobian)
    return vals


def project_g_perp(F: list[float], g: list[float], weight: float) -> list[float]:
    gg = inner(g, g, weight)
    if gg == 0.0:
        return F[:]
    coeff = inner(F, g, weight) / gg
    return [f - coeff * gi for f, gi in zip(F, g)]


def run_probe(n: int, k: int, sigma_name: str) -> dict[str, float | str | int | bool]:
    radius = 2.0**k
    cap_width = 2.0 ** (-0.25 * k)
    pts = grid(radius, cap_width, n)
    weight = (2.0 * cap_width * radius) / max(n - 1, 1)

    xi_center = (radius, 0.0)
    xi_out = (2.0 * radius, 0.0)
    beta = (0.0, 1.0)

    sigmas: dict[str, Callable[[Vector, float], float]] = {
        "generic": sigma_generic,
        "odd": sigma_odd,
        "even": sigma_even,
    }

    sigma = sigmas[sigma_name]
    g = build_g(pts, sigma, radius, xi_out, xi_center, beta)
    g_norm = norm2(g, weight)

    if g_norm == 0.0:
        F_guard = [0.0 for _ in g]
    else:
        F_guard = [gi / g_norm for gi in g]

    guard_inner = inner(F_guard, g, weight)

    F_test = [math.cos(i + 1.0) + 0.25 * math.sin(3.0 * i) for i in range(len(g))]
    F_proj = project_g_perp(F_test, g, weight)
    projected_inner = inner(F_proj, g, weight)

    half = len(g) // 2
    antisym_defect = 0.0
    antisym_norm = 0.0
    for i in range(half):
        a = g[i]
        b = g[-1 - i]
        antisym_defect += abs(a + b) * weight
        antisym_norm += (abs(a) + abs(b)) * weight

    relative_antisym_defect = antisym_defect / antisym_norm if antisym_norm else 0.0

    return {
        "status": "NUMERICAL_NON_PROOF",
        "k": k,
        "n": n,
        "sigma": sigma_name,
        "g_norm": g_norm,
        "counterexample_guard_inner": guard_inner,
        "projected_inner_abs": abs(projected_inner),
        "relative_antisym_defect": relative_antisym_defect,
        "guard_active": abs(guard_inner) > 1.0e-8,
        "projection_success": abs(projected_inner) < 1.0e-10,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=257)
    parser.add_argument("--k", type=int, default=8)
    parser.add_argument("--sigma", choices=["generic", "odd", "even"], default="generic")
    parser.add_argument("--out", default="artifacts/ra1n_numeric/transfer_probe.json")
    args = parser.parse_args()

    result = run_probe(args.n, args.k, args.sigma)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
