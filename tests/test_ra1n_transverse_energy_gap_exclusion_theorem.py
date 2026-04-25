from pathlib import Path

DOC = Path("docs/math/RA1N_TRANSVERSE_ENERGY_GAP_EXCLUSION_THEOREM.md")

def test_ra1n_transverse_energy_gap_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_transverse_energy_gap_target():
    s = DOC.read_text()
    assert "\\neg\\exists\\psi\\in V_{\\mathrm{RA1n}}^\\perp" in s
    assert "\\psi\\neq0" in s
    assert "\\psi\\in\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s

def test_ra1n_transverse_energy_gap_hypothesis():
    s = DOC.read_text()
    assert "E_{\\mathrm{term}}:L^2\\to[0,\\infty]" in s
    assert "E_{\\mathrm{term}}(F)\\le E_*" in s
    assert "E_{\\mathrm{term}}(\\psi)\\ge E_*+\\eta" in s
    assert "\\eta>0" in s

def test_ra1n_transverse_energy_gap_consequence():
    s = DOC.read_text()
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}\n\\cap\nV_{\\mathrm{RA1n}}^\\perp\n=\n\\{0\\}" in s
    assert "RA1N_TERMINAL_GENERATOR_CLASSIFICATION_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
