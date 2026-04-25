from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_GENERATOR_NORMAL_FORM_THEOREM.md")

def test_ra1n_terminal_generator_normal_form_status():
    s = DOC.read_text()
    assert "Status: OPEN STRUCTURAL MECHANISM" in s

def test_ra1n_terminal_generator_normal_form_target():
    s = DOC.read_text()
    assert "\\forall F\\in\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "F=a(F)\\phi_1" in s
    assert "(I-\\Pi_V)F=0" in s
    assert "V_{\\mathrm{RA1n}}=\\operatorname{span}\\{\\phi_1\\}" in s

def test_ra1n_terminal_generator_normal_form_mechanism():
    s = DOC.read_text()
    assert "terminal packet grammar" in s
    assert "scalar multiplication only" in s
    assert "\\neg\\exists \\psi\\in V_{\\mathrm{RA1n}}^\\perp" in s
    assert "\\mathcal G_{\\mathrm{terminal}}" in s

def test_ra1n_terminal_generator_normal_form_non_wrapper_obligation():
    s = DOC.read_text()
    assert "Remaining Non-Wrapper Obligation" in s
    assert "no production rule other than scalar multiplication of \\(\\phi_1\\)" in s
