import json
import subprocess
import sys
from pathlib import Path

DOC = Path("docs/status/RA1N_NUMERIC_TRANSFER_SWEEP.md")
ARTIFACT = Path("artifacts/ra1n_numeric/test_transfer_sweep.json")


def test_numeric_transfer_sweep_doc_locked():
    text = DOC.read_text()
    assert "Status: NUMERICAL / NON-PROOF / FRONTIER AID" in text
    assert "Full_RA1n_status: CONDITIONAL" in text
    assert "This sweep is not an admissible proof of RA1n closure." in text
    assert r"F\in g^\perp" in text
    assert r"g\equiv0" in text


def test_numeric_transfer_sweep_runs_and_preserves_frontier():
    subprocess.run(
        [
            sys.executable,
            "tools/ra1n_numeric_transfer_sweep.py",
            "--ks",
            "4",
            "6",
            "8",
            "10",
            "--n",
            "257",
            "--out",
            str(ARTIFACT),
        ],
        check=True,
    )
    data = json.loads(ARTIFACT.read_text())
    assert data["status"] == "NUMERICAL_NON_PROOF"
    assert data["full_ra1n_status"] == "CONDITIONAL"
    assert data["generic_guard_active_all"] is True
    assert data["generic_projection_success_all"] is True
    assert data["even_antisymmetry_success_all"] is True
    assert data["max_projected_inner_abs"] < 1.0e-10
    assert data["max_even_relative_antisym_defect"] < 1.0e-12
