import subprocess
import sys
from pathlib import Path

AUDIT = Path("docs/status/RA1N_UNCONDITIONAL_CLOSURE_AUDIT.md")


def test_ra1n_unconditional_closure_audit_doc_locked():
    text = AUDIT.read_text()
    assert "Full_RA1n_status: CONDITIONAL" in text
    assert "Weighted Affine-Transfer Cancellation Lemma" in text
    assert "Forbidden repository claims:" in text


def test_ra1n_unconditional_closure_audit_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_no_unconditional_closure.py"],
        check=True,
    )
