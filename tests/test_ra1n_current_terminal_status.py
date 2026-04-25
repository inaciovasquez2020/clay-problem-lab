from pathlib import Path

DOC = Path("docs/status/RA1N_CURRENT_TERMINAL_STATUS.md").read_text()

def test_ra1n_current_terminal_status_conditional():
    assert "Status: CONDITIONAL." in DOC
    assert "closed unary closure lane, not a full RA1n closure" in DOC

def test_ra1n_current_terminal_status_unary_lane():
    assert "RA1n-unary-closure-lane" in DOC
    assert "\\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}." in DOC
    assert "P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k)." in DOC
    assert "r_k(ξ)=\\widehat G_k(ξ)−P_k\\widehat G_k(ξ)." in DOC

def test_ra1n_current_terminal_status_theorem():
    assert "sup_{|ξ|~2^k}|(2^k∇_ξ)^α r_k(ξ)| ≤ C_α 2^{-4k} ≤ C_α" in DOC
    assert "normalized symbol-derivative obstruction is closed" in DOC

def test_ra1n_current_terminal_status_full_boundary():
    assert "Full RA1n remains conditional" in DOC
    assert "binary, ternary, transverse high-high, sampled surrogate" in DOC
    assert "No full RA1n closure claim is made." in DOC
