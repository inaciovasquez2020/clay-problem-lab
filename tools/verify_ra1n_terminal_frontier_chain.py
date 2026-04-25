#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAIN = ROOT / "docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md"
GPERP = ROOT / "docs/math/RA1N_GPERP_TERMINAL_ASSUMPTION.md"
TRANSFER = ROOT / "docs/math/RA1N_CONSERVATION_TRANSFER_FRONTIER.md"

chain = CHAIN.read_text()
gperp = GPERP.read_text()
transfer = TRANSFER.read_text()

required_chain = [
    "Status: CONDITIONAL FRONTIER CHAIN",
    "Full_RA1n_status: CONDITIONAL",
    "Weighted Affine-Transfer Cancellation Lemma",
    r"F\in g^\perp",
    r"g\equiv 0",
    r"\Phi_{\xi_{\mathrm{out}}}(\eta)",
    r"(\xi_{\mathrm{out}}-\eta,\eta)",
    r"F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}",
    "full RA1n promotion remains CONDITIONAL",
]

for phrase in required_chain:
    assert phrase in chain, phrase

assert r"F\in g^\perp" in gperp
assert "Weighted Affine-Transfer Cancellation Lemma" in transfer
assert r"\Phi_{\xi_{\mathrm{out}}}(\eta)" in transfer
assert r"F=\frac{\overline g}{\|g\|_2}" in transfer

print("RA1n terminal frontier chain verified")
