from pathlib import Path

def test_ra1n_corrected_scale_normalized_coercivity_lock():
    s = Path("docs/math/RA1N_CORRECTED_SCALE_NORMALIZED_COERCIVITY.md").read_text()
    assert "Status: CONDITIONAL." in s
    assert "r_k(ξ) = \\widehat G_k(ξ) − P_k \\widehat G_k(ξ)." in s
    assert "unscaled uniform shell coercivity" in s
    assert "is false on dyadic annuli of radius 2^k" in s
    assert "∫_{A_k} |2^k ∇_ξ r_k(ξ)|² w_k(ξ) dξ ≥ c ∫_{A_k} |r_k(ξ)|² w_k(ξ) dξ" in s
    assert "D_k := 2^k∇_ξ" in s
