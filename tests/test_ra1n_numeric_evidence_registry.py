import json
import subprocess
import sys
from pathlib import Path

REGISTRY = Path("docs/status/RA1N_NUMERIC_EVIDENCE_REGISTRY.json")


def test_ra1n_numeric_evidence_registry_values_locked():
    data = json.loads(REGISTRY.read_text())
    assert data["status"] == "NUMERICAL_NON_PROOF_FRONTIER_AID"
    assert data["full_ra1n_status"] == "CONDITIONAL"
    assert data["terminal_frontier"] == "Weighted Affine-Transfer Cancellation Lemma"
    assert data["active_terminal_dependency"] == "F in g^perp or g == 0"
    assert data["proof_status"] == "not a proof"
    assert data["unrestricted_full_ra1n_closed"] is False
    assert data["projected_packet_route_closed"] is True


def test_ra1n_numeric_evidence_registry_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_numeric_evidence_registry.py"],
        check=True,
    )
