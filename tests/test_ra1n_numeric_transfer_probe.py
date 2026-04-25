import json
import subprocess
import sys
from pathlib import Path

TOOL = "tools/ra1n_numeric_transfer_probe.py"
ARTIFACT = Path("artifacts/ra1n_numeric/test_transfer_probe.json")
DOC = Path("docs/status/RA1N_NUMERIC_TRANSFER_PROBE.md")


def run_probe(sigma: str) -> dict:
    subprocess.run(
        [
            sys.executable,
            TOOL,
            "--n",
            "257",
            "--k",
            "8",
            "--sigma",
            sigma,
            "--out",
            str(ARTIFACT),
        ],
        check=True,
    )
    return json.loads(ARTIFACT.read_text())


def test_numeric_probe_doc_nonproof_status_locked():
    text = DOC.read_text()
    assert "Status: NUMERICAL / NON-PROOF / FRONTIER AID" in text
    assert "Full_RA1n_status: CONDITIONAL" in text
    assert "It is not an admissible proof of RA1n closure." in text


def test_generic_sigma_counterexample_guard_active():
    data = run_probe("generic")
    assert data["status"] == "NUMERICAL_NON_PROOF"
    assert data["guard_active"] is True
    assert data["counterexample_guard_inner"] > 0


def test_projected_packet_kills_weighted_fm1_numerically():
    data = run_probe("generic")
    assert data["projection_success"] is True
    assert data["projected_inner_abs"] < 1.0e-10


def test_even_sigma_signed_pair_antisymmetry_detected():
    data = run_probe("even")
    assert data["relative_antisym_defect"] < 1.0e-12
