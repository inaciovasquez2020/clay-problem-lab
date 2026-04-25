from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_RESIDUAL_ZERO_THEOREM.md")

def test_ra1n_terminal_residual_zero_status_open():
    s = DOC.read_text()
    assert "Status: OPEN." in s

def test_ra1n_terminal_residual_zero_target_locked():
    s = DOC.read_text()
    assert "R(F):=(I-\\Pi_V)F" in s
    assert "R(F)=0" in s
    assert "\\forall F\\in\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s

def test_ra1n_terminal_residual_zero_consequence_locked():
    s = DOC.read_text()
    assert "F=\\Pi_VF" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "\\subset" in s
    assert "V_{\\mathrm{RA1n}}" in s

def test_ra1n_terminal_residual_zero_failure_witness_locked():
    s = DOC.read_text()
    assert "\\psi\\in V_{\\mathrm{RA1n}}^\\perp" in s
    assert "\\langle F,\\psi\\rangle_{L^2}\\neq 0" in s
