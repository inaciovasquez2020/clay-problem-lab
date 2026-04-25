#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SNAPSHOT = ROOT / "docs/status/RA1N_CANONICAL_STATUS_SNAPSHOT_2026_04_25.md"
CHAIN = ROOT / "docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md"
GPERP = ROOT / "docs/math/RA1N_GPERP_TERMINAL_ASSUMPTION.md"
TRANSFER = ROOT / "docs/math/RA1N_CONSERVATION_TRANSFER_FRONTIER.md"
REGISTRY = ROOT / "docs/status/RA1N_TERMINAL_FRONTIER_REGISTRY.json"

snapshot = SNAPSHOT.read_text()
chain = CHAIN.read_text()
gperp = GPERP.read_text()
transfer = TRANSFER.read_text()
registry = REGISTRY.read_text()

required_snapshot = [
    "Status: CANONICAL SNAPSHOT",
    "Full_RA1n_status: CONDITIONAL",
    "Conservation-transfer frontier: LOCKED.",
    "Terminal frontier registry: LOCKED.",
    "Unconditional-promotion audit: ACTIVE.",
    r"F\in g^\perp",
    r"g\equiv0",
    r"\Phi_{\xi_{\mathrm{out}}}(\eta)",
    r"(\xi_{\mathrm{out}}-\eta,\eta)",
    r"F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}",
    "Weighted Affine-Transfer Cancellation Lemma",
    "RA1n is conditionally frontier-locked",
]

for phrase in required_snapshot:
    assert phrase in snapshot, phrase

assert "Full_RA1n_status: CONDITIONAL" in chain
assert r"F\in g^\perp" in gperp
assert "Weighted Affine-Transfer Cancellation Lemma" in transfer
assert '"full_ra1n_status": "CONDITIONAL"' in registry
assert '"unconditional_closure": false' in registry

print("RA1n canonical status snapshot verified")
