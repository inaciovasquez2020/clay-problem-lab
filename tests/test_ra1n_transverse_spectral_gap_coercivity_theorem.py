from pathlib import Path

DOC = Path("docs/math/RA1N_TRANSVERSE_SPECTRAL_GAP_COERCIVITY_THEOREM.md")

def test_ra1n_transverse_spectral_gap_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_transverse_spectral_gap_operator():
    s = DOC.read_text()
    assert "A_{\\perp}:V_{\\mathrm{RA1n}}^\\perp\\to V_{\\mathrm{RA1n}}^\\perp" in s
    assert "self-adjoint" in s
    assert "\\eta>0" in s

def test_ra1n_transverse_spectral_gap_bound():
    s = DOC.read_text()
    assert "\\langle r,A_{\\perp}r\\rangle_{L^2}" in s
    assert "\\ge\n\\eta\\|r\\|_2^2" in s
    assert "E_{\\perp}(r):=\\langle r,A_{\\perp}r\\rangle_{L^2}" in s

def test_ra1n_transverse_spectral_gap_consequence():
    s = DOC.read_text()
    assert "RA1N_NORMALIZED_TRANSVERSE_COERCIVITY_THEOREM.md" in s
    assert "E_{\\mathrm{term}}(\\psi)\\ge E_*+\\eta" in s
    assert "A_{\\perp}\\ge \\eta I" in s
