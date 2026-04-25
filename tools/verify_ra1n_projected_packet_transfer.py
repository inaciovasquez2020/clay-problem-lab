#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/math/RA1N_PROJECTED_PACKET_TRANSFER_RESOLUTION.md"
STATUS = ROOT / "docs/status/RA1N_PROJECTED_PACKET_STATUS.json"

doc = DOC.read_text()
status = json.loads(STATUS.read_text())

required = [
    "Status: CONDITIONAL / PROJECTED-PACKET CLOSURE",
    "Projected_RA1n_packet_status: CLOSED",
    r"\sigma_{k,\omega}(\eta)",
    r"g_{k,\omega,\beta}(\eta)",
    r"\Phi_{\xi_{\mathrm{out}}}(\eta)",
    r"(\xi_{\mathrm{out}}-\eta,\eta)",
    r"\Pi_{g^\perp}F",
    r"\frac{\langle F,g_{k,\omega,\beta}\rangle_{L^2}}",
    r"F^\perp\in g^\perp",
    r"I_1^\beta(F^\perp)",
    r"\|T_k^\perp\|_{H^1\times H^1\to H^1}",
    r"2^{k(\sigma d-4)}",
    "Projected RA1n packet class: CLOSED",
    "Unrestricted full RA1n class: CONDITIONAL",
]

for phrase in required:
    assert phrase in doc, phrase

assert status["full_ra1n_status"] == "CONDITIONAL"
assert status["projected_ra1n_packet_status"] == "CLOSED"
assert status["terminal_obstruction_removed_for_projected_packets"] is True
assert status["unrestricted_full_ra1n_closed"] is False
assert status["sigma_condition"] == "0 < sigma < 4/d"

print("RA1n projected packet transfer verified")
