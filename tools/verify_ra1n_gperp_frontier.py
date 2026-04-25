#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/math/RA1N_GPERP_TERMINAL_ASSUMPTION.md"
REGISTRY = ROOT / "docs/status/RA1N_GPERP_FRONTIER_REGISTRY.json"

doc = DOC.read_text()
data = json.loads(REGISTRY.read_text())

required_doc = [
    "Status: TERMINAL FRONTIER / CONDITIONAL",
    "Full_RA1n_status: CONDITIONAL",
    r"F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}",
    r"F\in g^\perp",
    "Weighted Affine-Transfer Cancellation",
    "Without this exact antisymmetry,",
]

for phrase in required_doc:
    assert phrase in doc, phrase

assert data["full_ra1n_status"] == "CONDITIONAL"
assert data["terminal_missing_assumption"] == "F in g^perp"
assert data["f_in_g_perp_proved_from_packets"] is False
assert data["g_identically_zero_proved"] is False
assert data["unconditional_full_ra1n_closure"] is False
assert data["counterexample_guard"] == r"F=\frac{\overline g}{\|g\|_2}"

print("RA1n g-perp terminal frontier verified")
