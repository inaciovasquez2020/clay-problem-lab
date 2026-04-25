import json
import subprocess
import sys
from pathlib import Path

REGISTRY = Path("docs/status/RA1N_TERMINAL_FRONTIER_REGISTRY.json")


def test_ra1n_terminal_frontier_registry_values():
    data = json.loads(REGISTRY.read_text())
    assert data["full_ra1n_status"] == "CONDITIONAL"
    assert data["unconditional_closure"] is False
    assert data["terminal_frontier"] == "Weighted Affine-Transfer Cancellation Lemma"
    assert data["closed_status_forbidden"] is True


def test_ra1n_terminal_frontier_registry_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_terminal_frontier_registry.py"],
        check=True,
    )
