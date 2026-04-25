from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_GRAMMAR_FINITE_RESIDUAL_THEOREM.md")

def test_ra1n_terminal_grammar_finite_residual_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_terminal_grammar_finite_residual_target():
    s = DOC.read_text()
    assert "(I-\\Pi_V)F" in s
    assert "\\sum_{j=1}^m c_j(F)\\psi_j" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s

def test_ra1n_terminal_grammar_finite_residual_hypothesis():
    s = DOC.read_text()
    assert "\\mathcal G_{\\mathrm{terminal}}" in s
    assert "\\{\\phi_1,\\psi_1,\\dots,\\psi_m\\}" in s
    assert "finite complex linear combination" in s
    assert "F\n=\na(F)\\phi_1" in s

def test_ra1n_terminal_grammar_finite_residual_projection():
    s = DOC.read_text()
    assert "\\Pi_V\\psi_j=0" in s
    assert "\\Pi_V\\phi_1=\\phi_1" in s
    assert "(I-\\Pi_V)\\phi_1=0" in s
    assert "(I-\\Pi_V)\\psi_j=\\psi_j" in s

def test_ra1n_terminal_grammar_finite_residual_remaining_obligation():
    s = DOC.read_text()
    assert "RA1N_TRANSVERSE_RESIDUAL_FINITE_SPAN_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
    assert "\\neg\\exists \\chi" in s
    assert "\\chi\\notin" in s
