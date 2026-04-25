from pathlib import Path

def test_ra1n_obstruction_projector_certificate_doc():
    s = Path("docs/math/RA1N_OBSTRUCTION_PROJECTOR_CERTIFICATE.md").read_text()
    assert "Status: PROVED ABSTRACTLY" in s
    assert "h=\\frac{\\overline g}{\\|g\\|_2}" in s
    assert "h\\notin V_{\\mathrm{RA1n}}" in s
    assert "\\alpha:=\\|\\Pi_V h\\|_2<1" in s
    assert "Q_h u=\\langle u,h\\rangle_{L^2}h" in s
    assert "\\Phi_{Q_h}(h)" in s
    assert "\\epsilon=1-\\alpha" in s
    assert "RA1N_QUADRATIC_INVARIANT_CERTIFICATE.md" in s

def test_ra1n_quadratic_certificate_links_projector_certificate():
    s = Path("docs/math/RA1N_QUADRATIC_INVARIANT_CERTIFICATE.md").read_text()
    assert "RA1N_OBSTRUCTION_PROJECTOR_CERTIFICATE.md" in s
    assert "Q_hu=\\langle u,h\\rangle h" in s
    assert "separates the normalized terminal packet set" in s
