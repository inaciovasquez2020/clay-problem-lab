from pathlib import Path

DOC = Path("docs/math/RA1N_UNARY_ROUTE_CONDITIONAL_CLOSURE.md").read_text()

def test_ra1n_unary_route_conditional_status():
    assert "Status: CONDITIONAL." in DOC
    assert "strongest admissible consequence" in DOC

def test_ra1n_unary_route_canonical_surface():
    assert "\\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}." in DOC
    assert "P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k)." in DOC
    assert "r_k(ξ)=\\widehat G_k(ξ)−P_k\\widehat G_k(ξ)." in DOC

def test_ra1n_unary_route_derivative_closure():
    assert "D_k := 2^k∇_ξ" in DOC
    assert "sup_{|ξ|~2^k}|(2^k∇_ξ)^α r_k(ξ)| ≤ C_α 2^{-4k} ≤ C_α" in DOC
    assert "normalized symbol-derivative obstruction is closed" in DOC

def test_ra1n_unary_route_boundary():
    assert "does not close full RA1n unless" in DOC
    assert "sole canonical RA1n first-moment surface" in DOC
    assert "No full RA1n closure claim is admissible until the canonical-surface selection gate is resolved." in DOC
