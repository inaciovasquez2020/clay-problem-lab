import json
import subprocess
import sys
from pathlib import Path

DOC = Path("docs/math/RA1N_GPERP_TERMINAL_ASSUMPTION.md")
REGISTRY = Path("docs/status/RA1N_GPERP_FRONTIER_REGISTRY.json")


def test_gperp_terminal_assumption_doc_locked():
    text = DOC.read_text()
    assert "Status: TERMINAL FRONTIER / CONDITIONAL" in text
    assert r"F\in g^\perp" in text
    assert r"F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}" in text
    assert "Without this exact antisymmetry," in text


def test_gperp_registry_values_locked():
    data = json.loads(REGISTRY.read_text())
    assert data["full_ra1n_status"] == "CONDITIONAL"
    assert data["terminal_missing_assumption"] == "F in g^perp"
    assert data["f_in_g_perp_proved_from_packets"] is False
    assert data["g_identically_zero_proved"] is False
    assert data["unconditional_full_ra1n_closure"] is False


def test_gperp_frontier_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_gperp_frontier.py"],
        check=True,
    )
