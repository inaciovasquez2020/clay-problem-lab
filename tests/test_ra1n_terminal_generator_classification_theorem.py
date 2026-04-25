from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_GENERATOR_CLASSIFICATION_THEOREM.md")

def test_ra1n_terminal_generator_classification_status():
    s = DOC.read_text()
    assert "Status: OPEN TERMINAL STRUCTURAL THEOREM" in s

def test_ra1n_terminal_generator_classification_target():
    s = DOC.read_text()
    assert "\\mathcal G_{\\mathrm{terminal}}=\\{\\phi_1\\}" in s
    assert "F=a(F)\\phi_1" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s

def test_ra1n_terminal_generator_classification_failure_witness():
    s = DOC.read_text()
    assert "\\psi\\in V_{\\mathrm{RA1n}}^\\perp" in s
    assert "\\psi\\neq0" in s
    assert "(I-\\Pi_V)\\psi=\\psi\\neq0" in s
    assert "terminal packet exhaustion fails" in s

def test_ra1n_terminal_generator_classification_halt_condition():
    s = DOC.read_text()
    assert "\\neg\\exists\\psi\\in V_{\\mathrm{RA1n}}^\\perp" in s
    assert "No further RA1n theorem-level progress is possible" in s
    assert "excluding transverse terminal generators" in s
