import json
import subprocess
from pathlib import Path

def test_ra1n_packet_exhaustion_certified_closure_doc():
    s = Path("docs/math/RA1N_PACKET_EXHAUSTION_CERTIFIED_CLOSURE.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "\\subset" in s
    assert "V_{\\mathrm{RA1n}}" in s
    assert "RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md" in s
    assert "\\epsilon=1" in s
    assert "\\int Fg=0" in s
    assert "Packet exhaustion is certified closed" in s

def test_ra1n_packet_exhaustion_certificate_json():
    data = json.loads(Path("artifacts/ra1n/packet_exhaustion_certificate.json").read_text())
    assert data["object"] == "RA1N packet exhaustion certificate"
    assert data["status"] == "conditional-packet-exhaustion-certificate"
    assert data["certifies"] == "P_RA1n_terminal subset V_RA1n"
    assert all(x["basis_space"] == "V_RA1n" for x in data["terminal_generators"])

def test_ra1n_packet_exhaustion_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_packet_exhaustion_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "P_RA1n_terminal subset V_RA1n" in r.stdout
