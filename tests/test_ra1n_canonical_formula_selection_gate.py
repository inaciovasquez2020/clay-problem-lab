from pathlib import Path

DOC = Path("docs/math/RA1N_CANONICAL_FORMULA_SELECTION_GATE.md").read_text()

def test_ra1n_canonical_formula_selection_gate_status():
    assert "Status: OPEN." in DOC
    assert "not total absence of r_k" in DOC
    assert "non-unique competing residual surfaces" in DOC

def test_ra1n_canonical_formula_selection_gate_unary_choice():
    assert "\\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}." in DOC
    assert "P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k)." in DOC
    assert "r_k(ξ)=\\widehat G_k(ξ)−P_k\\widehat G_k(ξ)." in DOC

def test_ra1n_canonical_formula_selection_gate_competing_surfaces():
    assert "Unary residuals r_k(ξ)." in DOC
    assert "Binary residuals r_k(ξ,η), r_k(η,ζ)." in DOC
    assert "Ternary residuals r_k(ξ,η,ζ)." in DOC
    assert "transverse high-high route" in DOC

def test_ra1n_canonical_formula_selection_gate_next_theorem():
    assert "sup_{|ξ|~2^k} |(2^k∇_ξ)^α r_k(ξ)| ≤ C_α" in DOC
    assert "No RA1n closure claim is admissible before canonical formula selection." in DOC
