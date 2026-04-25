from pathlib import Path

DOC = Path("docs/math/RA1N_TRANSVERSE_RAYLEIGH_GAP_CERTIFICATE_THEOREM.md")

def test_ra1n_transverse_rayleigh_gap_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_transverse_rayleigh_gap_target():
    s = DOC.read_text()
    assert "A_{\\perp}\\ge \\eta I" in s
    assert "V_{\\mathrm{RA1n}}^\\perp" in s

def test_ra1n_transverse_rayleigh_gap_basis_and_matrix():
    s = DOC.read_text()
    assert "W_{\\perp}" in s
    assert "\\operatorname{span}\\{\\psi_1,\\dots,\\psi_m\\}" in s
    assert "M_{ij}:=\\langle \\psi_i,A_{\\perp}\\psi_j\\rangle_{L^2}" in s
    assert "c^*Mc\\ge \\eta\\,c^*c" in s

def test_ra1n_transverse_rayleigh_gap_consequence_and_remaining():
    s = DOC.read_text()
    assert "RA1N_TRANSVERSE_SPECTRAL_GAP_COERCIVITY_THEOREM.md" in s
    assert "RA1N_NORMALIZED_TRANSVERSE_COERCIVITY_THEOREM.md" in s
    assert "RA1N_TRANSVERSE_ENERGY_GAP_EXCLUSION_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
    assert "r\\in W_{\\perp}" in s
