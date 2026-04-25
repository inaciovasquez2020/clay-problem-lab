#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTRY = ROOT / "docs/status/RA1N_NUMERIC_EVIDENCE_REGISTRY.json"
SWEEP = ROOT / "artifacts/ra1n_numeric/transfer_sweep.json"
PROBE_DOC = ROOT / "docs/status/RA1N_NUMERIC_TRANSFER_PROBE.md"
SWEEP_DOC = ROOT / "docs/status/RA1N_NUMERIC_TRANSFER_SWEEP.md"

registry = json.loads(REGISTRY.read_text())
sweep = json.loads(SWEEP.read_text())
probe_doc = PROBE_DOC.read_text()
sweep_doc = SWEEP_DOC.read_text()

assert registry["status"] == "NUMERICAL_NON_PROOF_FRONTIER_AID"
assert registry["full_ra1n_status"] == "CONDITIONAL"
assert registry["terminal_frontier"] == "Weighted Affine-Transfer Cancellation Lemma"
assert registry["active_terminal_dependency"] == "F in g^perp or g == 0"
assert registry["proof_status"] == "not a proof"
assert registry["unrestricted_full_ra1n_closed"] is False
assert registry["projected_packet_route_closed"] is True

assert sweep["status"] == "NUMERICAL_NON_PROOF"
assert sweep["full_ra1n_status"] == "CONDITIONAL"
assert sweep["generic_guard_active_all"] is True
assert sweep["generic_projection_success_all"] is True
assert sweep["even_antisymmetry_success_all"] is True
assert sweep["max_projected_inner_abs"] < 1.0e-10
assert sweep["max_even_relative_antisym_defect"] < 1.0e-12

assert "Status: NUMERICAL / NON-PROOF / FRONTIER AID" in probe_doc
assert "Status: NUMERICAL / NON-PROOF / FRONTIER AID" in sweep_doc
assert "This sweep is not an admissible proof of RA1n closure." in sweep_doc
assert "It is not an admissible proof of RA1n closure." in probe_doc

print("RA1n numerical evidence registry verified")
