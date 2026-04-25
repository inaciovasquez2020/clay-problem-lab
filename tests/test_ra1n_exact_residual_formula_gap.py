from pathlib import Path

def test_ra1n_exact_residual_formula_gap_lock():
    s = Path("docs/math/RA1N_EXACT_RESIDUAL_FORMULA_GAP.md").read_text()
    assert "Status: OPEN." in s
    assert "D_k := 2^k∇_ξ" in s
    assert "sup_{|ξ| ~ 2^k} |(2^k∇_ξ)^α r_k(ξ)| ≤ C_α" in s
    assert "r_k(ξ) = \\widehat G_k(ξ) − P_k \\widehat G_k(ξ)" in s
    assert "exact action of P_k on \\widehat G_k" in s
    assert "No RA1n closure claim is admissible until that exact formula is fixed." in s
