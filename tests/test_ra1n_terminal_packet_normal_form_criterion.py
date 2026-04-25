from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_PACKET_NORMAL_FORM_CRITERION.md")

def test_ra1n_terminal_packet_normal_form_status_open():
    s = DOC.read_text()
    assert "Status: OPEN." in s

def test_ra1n_terminal_packet_normal_form_target_locked():
    s = DOC.read_text()
    assert "\\forall F\\in \\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "F=a(F)\\phi_1" in s

def test_ra1n_terminal_packet_normal_form_consequence_locked():
    s = DOC.read_text()
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "\\subset" in s
    assert "V_{\\mathrm{RA1n}}" in s

def test_ra1n_terminal_packet_normal_form_halt_condition_locked():
    s = DOC.read_text()
    assert "r(F):=F-\\Pi_{V_{\\mathrm{RA1n}}}F" in s
    assert "then terminal packet exhaustion fails" in s
