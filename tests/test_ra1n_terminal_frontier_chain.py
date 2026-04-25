import subprocess
import sys
from pathlib import Path

CHAIN = Path("docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md")


def test_ra1n_terminal_frontier_chain_doc_locked():
    text = CHAIN.read_text()
    assert "Status: CONDITIONAL FRONTIER CHAIN" in text
    assert "Full_RA1n_status: CONDITIONAL" in text
    assert "Weighted Affine-Transfer Cancellation Lemma" in text
    assert r"F\in g^\perp" in text
    assert r"g\equiv 0" in text
    assert r"\Phi_{\xi_{\mathrm{out}}}(\eta)" in text
    assert r"F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}" in text


def test_ra1n_terminal_frontier_chain_verifier_runs():
    subprocess.run(
        [sys.executable, "tools/verify_ra1n_terminal_frontier_chain.py"],
        check=True,
    )
