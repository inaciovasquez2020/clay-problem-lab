from pathlib import Path

def test_ra1n_transversality_witness_lemma_doc():
    s = Path("docs/math/RA1N_TRANSVERSALITY_WITNESS_LEMMA.md").read_text()
    assert "Status: PROVED ABSTRACTLY" in s
    assert "h:=\\frac{\\overline g}{\\|g\\|_2}" in s
    assert "\\Lambda:L^2\\to\\mathbb C" in s
    assert "\\Lambda(F)=0" in s
    assert "\\Lambda(h)\\neq0" in s
    assert "h\\notin V_{\\mathrm{RA1n}}" in s
    assert "RA1N_ANGLE_GAP_LEMMA.md" in s
    assert "\\Lambda|_{V_{\\mathrm{RA1n}}}=0" in s

def test_ra1n_angle_gap_links_transversality_witness():
    s = Path("docs/math/RA1N_ANGLE_GAP_LEMMA.md").read_text()
    assert "RA1N_TRANSVERSALITY_WITNESS_LEMMA.md" in s
    assert "bounded linear functional annihilating" in s
    assert "not annihilating \\(h=\\overline g/\\|g\\|_2\\)" in s
