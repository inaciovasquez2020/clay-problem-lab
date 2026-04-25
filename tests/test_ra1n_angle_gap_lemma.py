from pathlib import Path

def test_ra1n_angle_gap_lemma_doc():
    s = Path("docs/math/RA1N_ANGLE_GAP_LEMMA.md").read_text()
    assert "Status: CONDITIONAL" in s
    assert "h:=\\frac{\\overline g}{\\|g\\|_2}" in s
    assert "h\\notin V_{\\mathrm{RA1n}}" in s
    assert "\\alpha:=\\|\\Pi_Vh\\|_2" in s
    assert "\\epsilon:=1-\\alpha>0" in s
    assert "\\left|\\int F(\\eta)g(\\eta)\\,d\\eta\\right|" in s
    assert "(1-\\epsilon)\\|F\\|_2\\|g\\|_2" in s
    assert "Conditional Closure" in s
