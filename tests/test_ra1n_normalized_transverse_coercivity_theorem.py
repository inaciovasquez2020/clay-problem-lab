from pathlib import Path

DOC = Path("docs/math/RA1N_NORMALIZED_TRANSVERSE_COERCIVITY_THEOREM.md")

def test_ra1n_normalized_transverse_coercivity_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_normalized_transverse_coercivity_normalization():
    s = DOC.read_text()
    assert "\\psi\\in V_{\\mathrm{RA1n}}^\\perp" in s
    assert "\\|\\psi\\|_2=1" in s
    assert "uniform transverse gap is admissible only on the normalized terminal transverse class" in s

def test_ra1n_normalized_transverse_coercivity_decomposition():
    s = DOC.read_text()
    assert "E_{\\mathrm{term}}(F)" in s
    assert "E_{\\parallel}(\\Pi_VF)" in s
    assert "E_{\\perp}((I-\\Pi_V)F)" in s
    assert "E_{\\perp}(r)\\ge \\eta\\|r\\|_2^2" in s

def test_ra1n_normalized_transverse_coercivity_consequence():
    s = DOC.read_text()
    assert "E_{\\mathrm{term}}(\\psi)\\ge E_*+\\eta" in s
    assert "RA1N_TRANSVERSE_ENERGY_GAP_EXCLUSION_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
