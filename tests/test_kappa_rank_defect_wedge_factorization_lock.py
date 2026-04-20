from pathlib import Path
import json

ART = json.loads(Path("artifacts/ra1n_ddyo_exact_symbol/kappa_rank_defect_formula.json").read_text())
WEDGE = json.loads(Path("artifacts/ra1n_ddyo_exact_symbol/kappa_rank_defect_wedge_factorization.json").read_text())
DOC = Path("docs/math/RA1N_DDYO_COERCIVITY_FRONTIER.md").read_text()
STATUS = Path("docs/status/RA1N_DDYO_STATUS_SNAPSHOT.md").read_text()

def test_exact_formula_lock_present() -> None:
    assert ART["source_path"] == "navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py"
    assert ART["canonical_formula"] == 'kappa_rank_defect(xi: tuple[float, float, float], eta: tuple[float, float, float], ) -> float: l1, l2 = eigenvalue_pair_vieta(interaction_matrix(xi, eta)) if abs(l1) <= 1.0e-12: return 0.0 return l2 / l1 def D_j( xi: tuple[float, float, float], eta: tuple[float, float, float], j: int, ) -> float: zeta = add3(xi, eta) zeta_n2 = dot3(zeta, zeta) if zeta_n2 <= 1.0e-12: return 0.0 wedge = xi[0] * eta[1] - xi[1] * eta[0] return ((wedge * wedge) / (norm3(xi) * norm3(eta) * zeta_n2)) * chi_k(zeta, j) def F_k( xi: tuple[float, float, float], eta: tuple[float, float, float], k: int, ) -> float: zeta = add3(xi, eta) nxi = norm3(xi) neta = norm3(eta) if nxi <= 1.0e-12 or neta <= 1.0e-12: return 0.0 align = dot3(xi, eta) / (nxi * neta) sig = sigma_eff(k) prefactor = chi_k(zeta, k) * align * (kappa_rank_defect(xi, eta) / (3.0 + sig)) gaussian = math.exp(-dot3(zeta, zeta) / ((2.0 ** (2 * k)) * (sig ** 2))) tail = (1.0 / 7.0) * D_j(xi, eta, k + 1) return prefactor * gaussian * tail def run_generation(g: int, seed: int) -> tuple[float, float, float, float, int, dict]: rng = random.Random(seed + g) lambda_search = None best = -1.0 best_xi = 0.0 best_eta = 0.0 best_k = 0 best_log: dict = {} min_xi = 0.0 min_eta = 0.0 min_k = 0 min_log: dict = {} for _ in range(20000) = lambda_search, best, best_xi, best_eta, best_k, {'

def test_wedge_factorization_literal_lock() -> None:
    assert WEDGE["factorization_status"] == "CONDITIONAL"
    assert WEDGE["factorized_formula"] == "kappa_rank_defect(xi,eta) = wedge(xi,eta) * G(xi,eta)"
    assert WEDGE["canonical_G"] == "G(xi,eta) := kappa_rank_defect(xi,eta) / wedge(xi,eta)"

def test_doc_contains_wedge_lock() -> None:
    assert "## Wedge factorization lock" in DOC
    assert "kappa_rank_defect(xi,eta) = wedge(xi,eta) * G(xi,eta)" in DOC
    assert "inf_{Gamma_term_sharp} |G| > 0" in DOC
    assert "sigma_lower = epsilon_gamma**2" in DOC

def test_status_contains_conditional_wedge_targets() -> None:
    assert "Wedge factorization lock: CONDITIONAL" in STATUS
    assert "Positivity target: inf_{Gamma_term_sharp} |G| > 0." in STATUS
    assert "Replacement target after proof: sigma_lower = epsilon_gamma**2." in STATUS
