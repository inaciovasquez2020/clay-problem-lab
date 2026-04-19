from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json
import math
import random
import time

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "artifacts" / "terminal_high_high_resonance_curvature_gain"
ART.mkdir(parents=True, exist_ok=True)

@dataclass
class State:
    generation: int
    status: str
    obstruction: str
    missing_input: str
    local_gain_found: bool
    best_score: float
    witness_xi: float
    witness_eta: float
    witness_shell: int
    lambda_search: float | None
    timestamp: float
    exact_symbol_curvature_lemma_instantiated: bool = False
    exact_symbol_available: bool = False

def F_k(xi: float, eta: float, k: int) -> float:
    raise NotImplementedError("Provide the explicit closed-form DDYO symbol formula m_k(xi,eta)=F_k(xi,eta).")

def exact_m_k(xi: float, eta: float, k: int) -> float:
    xi_vec, eta_vec = shell_vectors(xi, eta, k)
    return F_k(xi_vec, eta_vec, k)

def transverse_renormalized_r_k(xi: float, eta: float, k: int) -> float:
    parallel_value = exact_m_k(xi, xi, k)
    return exact_m_k(xi, eta, k) - parallel_value

def exact_curvature_lower_bound(xi: float, eta: float, k: int) -> float:
    return abs(transverse_renormalized_r_k(xi, eta, k))

def admissible_patch(xi: float, eta: float) -> bool:
    return abs(math.sin(eta - xi)) > 1.0e-6

def shell_vectors(theta_xi: float, theta_eta: float, k: int) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
    r = 2.0 ** (k + 1)
    xi = (r * math.cos(theta_xi), r * math.sin(theta_xi), 0.0)
    eta = (r * math.cos(theta_eta), r * math.sin(theta_eta), 0.0)
    return xi, eta

def h_transition(x: float) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    a = math.exp(-1.0 / x)
    b = math.exp(-1.0 / (1.0 - x))
    return a / (a + b)

def phi_bump(r: float) -> float:
    return 1.0 - h_transition(r - 1.0)

def norm3(v: tuple[float, float, float]) -> float:
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

def chi_k(vec: tuple[float, float, float], k: int) -> float:
    r = norm3(vec)
    return phi_bump((2.0 ** (-k)) * r) - phi_bump((2.0 ** (-(k - 1))) * r)

def dot3(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def add3(a: tuple[float, float, float], b: tuple[float, float, float]) -> tuple[float, float, float]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def green_hat(vec: tuple[float, float, float]) -> float:
    n2 = dot3(vec, vec)
    if n2 <= 0.0:
        raise ValueError("green_hat undefined at zero vector")
    return 1.0 / n2

def sup_green_hat_k(k: int) -> float:
    return 2.0 ** (2 - 2 * k)

def sigma_eff(k: int, nu: float = 1.0) -> float:
    return math.sqrt(nu * (2.0 ** (2 * k)) / sup_green_hat_k(k))

def sym_advection_tensor(
    xi: tuple[float, float, float],
    eta: tuple[float, float, float],
) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    return (
        (0.5 * (xi[0] * eta[0] + eta[0] * xi[0]), 0.5 * (xi[0] * eta[1] + eta[0] * xi[1]), 0.5 * (xi[0] * eta[2] + eta[0] * xi[2])),
        (0.5 * (xi[1] * eta[0] + eta[1] * xi[0]), 0.5 * (xi[1] * eta[1] + eta[1] * xi[1]), 0.5 * (xi[1] * eta[2] + eta[1] * xi[2])),
        (0.5 * (xi[2] * eta[0] + eta[2] * xi[0]), 0.5 * (xi[2] * eta[1] + eta[2] * xi[1]), 0.5 * (xi[2] * eta[2] + eta[2] * xi[2])),
    )

def leray_projector(vec: tuple[float, float, float]) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    n2 = dot3(vec, vec)
    if n2 <= 0.0:
        raise ValueError("leray_projector undefined at zero vector")
    return (
        (1.0 - vec[0] * vec[0] / n2,      - vec[0] * vec[1] / n2,      - vec[0] * vec[2] / n2),
        (     - vec[1] * vec[0] / n2, 1.0 - vec[1] * vec[1] / n2,      - vec[1] * vec[2] / n2),
        (     - vec[2] * vec[0] / n2,      - vec[2] * vec[1] / n2, 1.0 - vec[2] * vec[2] / n2),
    )

def matmul3(
    a: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]],
    b: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]],
) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    return tuple(
        tuple(sum(a[i][m] * b[m][j] for m in range(3)) for j in range(3))
        for i in range(3)
    )

def transpose3(
    a: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]
) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))

def interaction_matrix(
    xi: tuple[float, float, float],
    eta: tuple[float, float, float],
) -> tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]:
    zeta = add3(xi, eta)
    P = leray_projector(zeta)
    S = sym_advection_tensor(xi, eta)
    return matmul3(matmul3(P, S), transpose3(P))

def run_generation(g: int, seed: int) -> tuple[float, float, float, int]:
    rng = random.Random(seed + g)
    lambda_search = None
    best = -1.0
    best_xi = 0.0
    best_eta = 0.0
    best_k = 0
    for _ in range(20000):
        k = rng.randint(1, 40)
        xi = rng.uniform(0.0, math.pi)
        eta = rng.uniform(0.0, math.pi)
        if not admissible_patch(xi, eta):
            continue
        try:
            score = exact_curvature_lower_bound(xi, eta, k)
            exact_symbol_available = True
        except NotImplementedError:
            score = 0.0
            exact_symbol_available = False
        lambda_search = score if lambda_search is None else min(lambda_search, score)
        if score > best:
            best = score
            best_xi = xi
            best_eta = eta
            best_k = k
    if lambda_search is None:
        lambda_search = -1.0
    return lambda_search, best_xi, best_eta, best_k

def write_json(name: str, payload: dict) -> None:
    (ART / name).write_text(json.dumps(payload, indent=2, sort_keys=True))

def main() -> int:
    obstruction = "terminal_high_high_resonance_curvature_gain"
    missing_input = "Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain"
    state = State(
        generation=0,
        status="OPEN",
        obstruction=obstruction,
        missing_input=missing_input,
        local_gain_found=False,
        best_score=0.0,
        witness_xi=0.0,
        witness_eta=0.0,
        witness_shell=0,
        lambda_search=None,
        exact_symbol_curvature_lemma_instantiated=False,
        timestamp=time.time(),
    )
    max_generations = 12
    lambda_search = None
    for g in range(1, max_generations + 1):
        lambda_search, xi, eta, k = run_generation(g, seed=1729)
        exact_symbol_available = False
        state.generation = g
        state.best_score = lambda_search
        state.witness_xi = xi
        state.witness_eta = eta
        state.witness_shell = k
        state.lambda_search = lambda_search
        state.exact_symbol_available = exact_symbol_available
        state.exact_symbol_curvature_lemma_instantiated = exact_symbol_available
        state.exact_symbol_curvature_lemma_instantiated = exact_symbol_available
        state.status = "CLOSED" if lambda_search > 0.0 else "OPEN"
        state.missing_input = "resolved" if lambda_search > 0.0 else "Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain"
        state.timestamp = time.time()
        write_json(f"generation_{g:03d}.json", asdict(state))
        if state.status != "CLOSED":
            issue = {
                "generation": g,
                "issue": "simulation_cannot_upgrade_placeholder_to_theorem_without_exact_symbol_curvature_lemma",
                "needed_information": {
                    "name": "Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain",
                    "target": "DDYO high-high interaction symbol for canonical residual r_k = Ghat_k - P_k Ghat_k",
                    "required_output": "verified positivity of exact curvature lower bound on P_adm via |r_k(xi,eta)| > 0",
                    "reduction_doc": "docs/math/RA1N_TERMINAL_REDUCTION_TO_EXACT_SYMBOL_CURVATURE_LEMMA.md"
                }
            }
            write_json(f"issue_{g:03d}.json", issue)
            continue
        state.local_gain_found = True
        state.status = "CLOSED"
        write_json("closure.json", asdict(state))
        return 0
    state.lambda_search = lambda_search
    write_json("frontier_summary.json", asdict(state))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
