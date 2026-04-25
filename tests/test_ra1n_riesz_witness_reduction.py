from pathlib import Path

def test_ra1n_riesz_witness_reduction_doc():
    s = Path("docs/math/RA1N_RIESZ_WITNESS_REDUCTION.md").read_text()
    assert "Status: PROVED ABSTRACTLY" in s
    assert "h:=\\frac{\\overline g}{\\|g\\|_2}" in s
    assert "w\\in V_{\\mathrm{RA1n}}^\\perp" in s
    assert "\\langle h,w\\rangle_{L^2}\\neq0" in s
    assert "w:=(I-\\Pi_V)h" in s
    assert "\\Lambda_w(F):=\\langle F,w\\rangle_{L^2}" in s
    assert "RA1N_TRANSVERSALITY_WITNESS_LEMMA.md" in s
    assert "Angle-Gap" in s

def test_ra1n_transversality_links_riesz_witness():
    s = Path("docs/math/RA1N_TRANSVERSALITY_WITNESS_LEMMA.md").read_text()
    assert "RA1N_RIESZ_WITNESS_REDUCTION.md" in s
    assert "Riesz witness \\(w\\in V_{\\mathrm{RA1n}}^\\perp\\)" in s
    assert "\\left\\langle" in s
    assert "\\neq0" in s
