import subprocess
import sys
from pathlib import Path

SNAPSHOT = Path("docs/status/RA1N_CANONICAL_STATUS_SNAPSHOT_2026_04_25.md")


def test_ra1n_canonical_snapshot_locked():
    text = SNAPSHOT.read_text()
    assert "Status: CANONICAL SNAPSHOT" in text
    assert "Full_RA1n_status: CONDITIONAL" in text
    assert "Weighted Affine-Transfer Cancellation Lemma" in text
    assert r"F\in g^\perp" in text
    assert r"g\equiv0" in text
    assert r"\Phi_{\xi_{\mathrm{out}}}(\eta)" in text
    assert r"F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}" in text
    assert "RA1n is conditionally frontier-locked" in text


def test_ra1n_canonical_snapshot_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_canonical_snapshot.py"],
        check=True,
    )
