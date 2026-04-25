import json
import subprocess
import sys
from pathlib import Path

REGISTRY = Path("docs/status/RA1N_ANGLE_GAP_TERMINAL_REGISTRY.json")


def test_ra1n_angle_gap_terminal_registry_values_locked():
    data = json.loads(REGISTRY.read_text())
    assert data["status"] == "OPEN_CONDITIONAL"
    assert data["full_ra1n_status"] == "CONDITIONAL"
    assert data["projected_packet_ra1n_status"] == "CLOSED"
    assert data["terminal_object"] == "Angle-Gap / Structural Counterexample Exclusion"
    assert data["angle_gap_condition"] == "|<F,g>| <= (1-epsilon)||F||_2||g||_2"
    assert data["excluded_counterexample"] == r"F=\frac{\overline g}{\|g\|_2}"
    assert data["unrestricted_ra1n_unconditional_promotion"] is False


def test_ra1n_angle_gap_terminal_registry_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_angle_gap_terminal_registry.py"],
        check=True,
    )
