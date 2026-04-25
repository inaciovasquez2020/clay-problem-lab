from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_PACKET_EXHAUSTION_THEOREM.md")

def test_ra1n_terminal_packet_exhaustion_status_open():
    s = DOC.read_text()
    assert "Status: OPEN." in s

def test_ra1n_terminal_packet_exhaustion_target_locked():
    s = DOC.read_text()
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "\\subset" in s
    assert "\\operatorname{span}\\{\\phi_1\\}" in s

def test_ra1n_terminal_packet_exhaustion_equivalent_residual_locked():
    s = DOC.read_text()
    assert "\\operatorname{dist}_{L^2}" in s
    assert "\\|(I-\\Pi_{V_{\\mathrm{RA1n}}})F\\|_2=0" in s

def test_ra1n_terminal_packet_exhaustion_dependency_locked():
    s = DOC.read_text()
    assert "The theorem is not proved by the finite-basis Gram certificate alone." in s
    assert "The missing object is the packet-exhaustion proof" in s
