from pathlib import Path

def test_ra1n_terminal_packet_exhaustion_theorem_doc():
    s = Path("docs/math/RA1N_TERMINAL_PACKET_EXHAUSTION_THEOREM.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "V_{\\mathrm{RA1n}}=\\operatorname{span}\\{\\phi_1\\}" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "\\exists a(F)\\in\\mathbb C" in s
    assert "F=a(F)\\phi_1" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}\n\\subset\nV_{\\mathrm{RA1n}}" in s
    assert "\\operatorname{dist}_{L^2}" in s
    assert "RA1N_PACKET_EXHAUSTION_CERTIFIED_CLOSURE.md" in s
    assert "RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md" in s
    assert "rank-one terminal packet hypothesis" in s
