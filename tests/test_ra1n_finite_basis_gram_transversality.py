from pathlib import Path

def test_ra1n_finite_basis_gram_transversality_doc():
    s = Path("docs/math/RA1N_FINITE_BASIS_GRAM_TRANSVERSALITY.md").read_text()
    assert "Status: PROVED ABSTRACTLY" in s
    assert r"h:=\frac{\overline g}{\|g\|_2}" in s
    assert r"V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1,\dots,\phi_m\}" in s
    assert r"G_{ij}:=\langle \phi_j,\phi_i\rangle_{L^2}" in s
    assert r"b_i:=\langle h,\phi_i\rangle_{L^2}" in s
    assert r"\|\Pi_Vh\|_2^2" in s
    assert r"b^*G^{-1}b<1" in s
    assert "RA1N_ANGLE_GAP_LEMMA.md" in s
    assert "Angle-Gap" in s

def test_ra1n_riesz_witness_links_finite_basis_gram_source():
    s = Path("docs/math/RA1N_RIESZ_WITNESS_REDUCTION.md").read_text()
    assert "RA1N_FINITE_BASIS_GRAM_TRANSVERSALITY.md" in s
    assert r"b^*G^{-1}b<1" in s
