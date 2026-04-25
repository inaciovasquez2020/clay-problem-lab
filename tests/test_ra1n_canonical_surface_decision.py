from pathlib import Path

DOC = Path("docs/math/RA1N_CANONICAL_SURFACE_DECISION.md").read_text()

def test_ra1n_canonical_surface_decision_status():
    assert "Status: CONDITIONAL." in DOC
    assert "Full RA1n closure is admissible only under" in DOC

def test_ra1n_canonical_surface_decision_identity():
    assert "RA1n first-moment shell-product surface" in DOC
    assert "selected unary Taylor-remainder surface" in DOC
    assert "\\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}." in DOC
    assert "P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k)." in DOC
    assert "r_k(ξ)=\\widehat G_k(ξ)−P_k\\widehat G_k(ξ)." in DOC

def test_ra1n_canonical_surface_decision_closure_boundary():
    assert "then the RA1n normalized derivative obstruction is closed" in DOC
    assert "then full RA1n remains open" in DOC
    assert "Audit every RA1n downstream theorem" in DOC
