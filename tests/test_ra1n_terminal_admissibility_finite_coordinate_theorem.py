from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_ADMISSIBILITY_FINITE_COORDINATE_THEOREM.md")

def test_ra1n_terminal_admissibility_finite_coordinate_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_terminal_admissibility_finite_coordinate_target():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "a(\\chi)\\phi_1" in s
    assert "\\sum_{j=1}^m c_j(\\chi)\\psi_j" in s

def test_ra1n_terminal_admissibility_finite_coordinate_projection():
    s = DOC.read_text()
    assert "\\Phi_{\\mathrm{term}}" in s
    assert "W_{\\mathrm{term}}" in s
    assert "\\Pi_W:L^2\\to W_{\\mathrm{term}}" in s
    assert "\\chi=\\Pi_W\\chi" in s
    assert "(I-\\Pi_W)\\chi=0" in s

def test_ra1n_terminal_admissibility_finite_coordinate_consequence():
    s = DOC.read_text()
    assert "RA1N_TERMINAL_GENERATOR_FINITE_GRAMMAR_EXCLUSION_THEOREM.md" in s
    assert "\\mathcal G_{\\mathrm{terminal}}" in s
    assert "\\operatorname{span}\\{\\phi_1,\\psi_1,\\dots,\\psi_m\\}" in s
    assert "Remaining Non-Conditional Obligation" in s
