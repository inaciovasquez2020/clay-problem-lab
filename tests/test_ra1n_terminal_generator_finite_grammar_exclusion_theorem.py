from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_GENERATOR_FINITE_GRAMMAR_EXCLUSION_THEOREM.md")

def test_ra1n_terminal_generator_finite_grammar_exclusion_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_terminal_generator_finite_grammar_exclusion_target():
    s = DOC.read_text()
    assert "\\neg\\exists \\chi" in s
    assert "\\chi\\in\\mathcal G_{\\mathrm{terminal}}" in s
    assert "\\chi\\notin" in s
    assert "\\operatorname{span}\\{\\phi_1,\\psi_1,\\dots,\\psi_m\\}" in s

def test_ra1n_terminal_generator_finite_grammar_exclusion_admissibility():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\chi\\in\\mathcal G_{\\mathrm{terminal}}" in s
    assert "\\Longleftrightarrow" in s

def test_ra1n_terminal_generator_finite_grammar_exclusion_hypothesis():
    s = DOC.read_text()
    assert "finite terminal coordinates" in s
    assert "a(\\chi)\\phi_1" in s
    assert "\\sum_{j=1}^m c_j(\\chi)\\psi_j" in s
    assert "a(\\chi),c_1(\\chi),\\dots,c_m(\\chi)\\in\\mathbb C" in s

def test_ra1n_terminal_generator_finite_grammar_exclusion_consequence():
    s = DOC.read_text()
    assert "RA1N_TERMINAL_GRAMMAR_FINITE_RESIDUAL_THEOREM.md" in s
    assert "(I-\\Pi_V)F" in s
    assert "\\sum_{j=1}^m c_j(F)\\psi_j" in s
    assert "Remaining Non-Conditional Obligation" in s
