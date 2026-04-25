from pathlib import Path

def test_ra1n_downstream_scale_compatibility_doc_lock():
    s = Path("docs/math/RA1N_DOWNSTREAM_SCALE_COMPATIBILITY.md").read_text()
    assert "Status: CONDITIONAL." in s
    assert "D_k := 2^k∇_ξ" in s
    assert "sup_{|ξ| ~ 2^k} |(2^k∇_ξ)^α r_k(ξ)| ≤ C_α" in s
    assert "2^{k|α|}(∂^α r_k)(2^kη)" in s
    assert "Unscaled uniform coercivity" in s
    assert "is not an admissible RA1n target on dyadic annuli" in s
    assert "r_k(ξ) = \\widehat G_k(ξ) − P_k \\widehat G_k(ξ)." in s

def test_existing_kernel_route_uses_normalized_derivative_form():
    s = Path("docs/math/DDYO_RA1N_SHELL_PRODUCT_KERNEL_ESTIMATE_CONDITIONAL.md").read_text()
    assert "r_k(2^k\\eta)" in s
    assert "2^{k|\\delta|}" in s
    assert "symbol-derivative hypothesis on \\(r_k\\)" in s
