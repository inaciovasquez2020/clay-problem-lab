from pathlib import Path

DOC = Path("docs/math/RA1N_UNARY_TAYLOR_REMAINDER_DERIVATIVE_BOUND.md").read_text()

def test_ra1n_unary_taylor_bound_status_and_formula():
    assert "Status: CONDITIONAL." in DOC
    assert "\\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}." in DOC
    assert "P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k)." in DOC
    assert "r_k(ξ)=\\widehat G_k(ξ)−P_k\\widehat G_k(ξ)." in DOC

def test_ra1n_unary_taylor_bound_rescaling_identity():
    assert "\\widehat G_k(2^kη)=2^{-4k} φ(η)|η|^{-4}." in DOC
    assert "g(η):=φ(η)|η|^{-4}." in DOC
    assert "r_k(2^kη)" in DOC
    assert "2^{-4k}" in DOC

def test_ra1n_unary_taylor_bound_normalized_derivative():
    assert "(2^k∇_ξ)^α r_k(2^kη)" in DOC
    assert "sup_{|ξ|~2^k}|(2^k∇_ξ)^α r_k(ξ)|" in DOC
    assert "≤ C_α 2^{-4k}" in DOC
    assert "≤ C_α." in DOC

def test_ra1n_unary_taylor_bound_conditional_boundary():
    assert "selected unary Taylor-remainder RA1n surface" in DOC
    assert "It does not close binary, ternary, transverse high-high, sampled surrogate, or noncanonical residual surfaces." in DOC
