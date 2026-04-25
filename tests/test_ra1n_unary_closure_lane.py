from pathlib import Path

DOC = Path("docs/status/RA1N_UNARY_CLOSURE_LANE.md").read_text()

def test_ra1n_unary_closure_lane_status():
    assert "Status: CONDITIONAL." in DOC
    assert "RA1n-unary-closure-lane" in DOC
    assert "selected unary Taylor-remainder surface only" in DOC

def test_ra1n_unary_closure_lane_formula():
    assert "\\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}." in DOC
    assert "P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k)." in DOC
    assert "r_k(ξ)=\\widehat G_k(ξ)−P_k\\widehat G_k(ξ)." in DOC

def test_ra1n_unary_closure_lane_theorem_and_boundary():
    assert "sup_{|ξ|~2^k}|(2^k∇_ξ)^α r_k(ξ)| ≤ C_α 2^{-4k} ≤ C_α" in DOC
    assert "normalized symbol-derivative obstruction is closed for the RA1n unary closure lane" in DOC
    assert "No full RA1n closure claim is made here." in DOC

def test_ra1n_unary_closure_lane_exclusions():
    assert "binary residuals" in DOC
    assert "ternary residuals" in DOC
    assert "transverse high-high residuals" in DOC
    assert "sampled surrogate residuals" in DOC
    assert "mixed conditional symbolic residuals" in DOC
