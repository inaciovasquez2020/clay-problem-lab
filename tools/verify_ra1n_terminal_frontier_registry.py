#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTRY = ROOT / "docs/status/RA1N_TERMINAL_FRONTIER_REGISTRY.json"
FRONTIER = ROOT / "docs/math/RA1N_CONSERVATION_TRANSFER_FRONTIER.md"
STATUS = ROOT / "docs/status/RA1N_FULL_PROMOTION_STATUS.md"

data = json.loads(REGISTRY.read_text())
frontier = FRONTIER.read_text()
status = STATUS.read_text()

assert data["full_ra1n_status"] == "CONDITIONAL"
assert data["closed_status_forbidden"] is True
assert data["unconditional_closure"] is False
assert data["terminal_frontier"] == "Weighted Affine-Transfer Cancellation Lemma"

assert "Weighted Affine-Transfer Cancellation Lemma" in frontier
assert "Full_RA1n_status: CONDITIONAL" in status
assert "Full_RA1n_status: CLOSED" not in status

assert r"\Phi_{\xi_{\mathrm{out}}}(\eta)" in frontier
assert r"(\xi_{\mathrm{out}}-\eta,\eta)" in frontier
assert r"F=\frac{\overline g}{\|g\|_2}" in frontier

print("RA1n terminal frontier registry verified")
