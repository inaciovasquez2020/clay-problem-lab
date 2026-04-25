import json
import subprocess
import sys
from pathlib import Path

DOC = Path("docs/math/RA1N_PROJECTED_PACKET_TRANSFER_RESOLUTION.md")
STATUS = Path("docs/status/RA1N_PROJECTED_PACKET_STATUS.json")


def test_projected_packet_resolution_doc_locked():
    text = DOC.read_text()
    assert "Projected_RA1n_packet_status: CLOSED" in text
    assert r"\sigma_{k,\omega}(\eta)" in text
    assert r"g_{k,\omega,\beta}(\eta)" in text
    assert r"\Pi_{g^\perp}F" in text
    assert r"F^\perp\in g^\perp" in text
    assert r"I_1^\beta(F^\perp)" in text
    assert r"2^{k(\sigma d-4)}" in text
    assert "Unrestricted full RA1n class: CONDITIONAL" in text


def test_projected_packet_status_locked():
    data = json.loads(STATUS.read_text())
    assert data["full_ra1n_status"] == "CONDITIONAL"
    assert data["projected_ra1n_packet_status"] == "CLOSED"
    assert data["terminal_obstruction_removed_for_projected_packets"] is True
    assert data["unrestricted_full_ra1n_closed"] is False
    assert data["sigma_condition"] == "0 < sigma < 4/d"


def test_projected_packet_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_projected_packet_transfer.py"],
        check=True,
    )
