from pathlib import Path
import subprocess

def test_ra1n_terminal_residual_zero_certified_closure_doc():
    s = Path("docs/math/RA1N_TERMINAL_RESIDUAL_ZERO_CERTIFIED_CLOSURE.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "V_{\\mathrm{RA1n}}=\\operatorname{span}\\{\\phi_1\\}" in s
    assert "R(F):=(I-\\Pi_V)F" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}\n\\subset\nV_{\\mathrm{RA1n}}" in s
    assert "(I-\\Pi_V)F=0" in s
    assert "\\operatorname{dist}_{L^2}(F,V_{\\mathrm{RA1n}})" in s
    assert "certified closed on the packet-exhausted finite-basis RA1n surface" in s

def test_ra1n_terminal_residual_zero_uses_packet_exhaustion_verifier():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_packet_exhaustion_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "P_RA1n_terminal subset V_RA1n" in r.stdout
