#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTRY = ROOT / "docs/status/RA1N_ANGLE_GAP_TERMINAL_REGISTRY.json"
ANGLE = ROOT / "docs/math/RA1N_STRUCTURAL_COUNTEREXAMPLE_EXCLUSION.md"
PROJ = ROOT / "docs/math/RA1N_PROJECTION_ERROR_DOMINATION.md"
SYMBOLIC = ROOT / "docs/math/RA1N_SYMBOLIC_TRANSFER_LEMMA.md"

data = json.loads(REGISTRY.read_text())
angle = ANGLE.read_text()
proj = PROJ.read_text()
symbolic = SYMBOLIC.read_text()

assert data["status"] == "OPEN_CONDITIONAL"
assert data["full_ra1n_status"] == "CONDITIONAL"
assert data["projected_packet_ra1n_status"] == "CLOSED"
assert data["terminal_object"] == "Angle-Gap / Structural Counterexample Exclusion"
assert data["unrestricted_ra1n_unconditional_promotion"] is False
assert data["projection_error_domination_doc"] == "docs/math/RA1N_PROJECTION_ERROR_DOMINATION.md"
assert data["structural_counterexample_doc"] == "docs/math/RA1N_STRUCTURAL_COUNTEREXAMPLE_EXCLUSION.md"
assert data["symbolic_transfer_doc"] == "docs/math/RA1N_SYMBOLIC_TRANSFER_LEMMA.md"

assert "Status: OPEN" in angle
assert r"F=\frac{\overline g}{\|g\|_2}" in angle
assert r"F\notin g^\perp" in angle
assert r"|\langle F,g\rangle|" in angle
assert r"(1-\epsilon)\|F\|_2\|g\|_2" in angle
assert "Conditional." in angle
assert "Unrestricted RA1n remains OPEN" in angle

assert "Status: OPEN" in proj
assert r"\|P_k\widehat G_k\|_{\mathrm{err}}" in proj
assert "weakest sufficient missing inequality" in proj

assert "RA1N_STRUCTURAL_COUNTEREXAMPLE_EXCLUSION.md" in symbolic
assert "RA1N_PROJECTION_ERROR_DOMINATION.md" in symbolic

print("RA1n angle-gap terminal registry verified")
