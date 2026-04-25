from pathlib import Path

FRONTIER = Path("docs/math/RA1N_CONSERVATION_TRANSFER_FRONTIER.md")
STATUS = Path("docs/status/RA1N_FULL_PROMOTION_STATUS.md")


def test_weighted_affine_transfer_phrase_locked():
    text = FRONTIER.read_text()
    assert "Weighted Affine-Transfer Cancellation Lemma" in text


def test_exact_sigma_parametrization_locked():
    text = FRONTIER.read_text()
    assert r"\Phi_{\xi_{\mathrm{out}}}(\eta)" in text
    assert r"(\xi_{\mathrm{out}}-\eta,\eta)" in text


def test_counterexample_guard_locked():
    text = FRONTIER.read_text()
    assert r"F=\frac{\overline g}{\|g\|_2}" in text


def test_full_ra1n_status_conditional_not_closed():
    text = STATUS.read_text()
    assert "Full_RA1n_status: CONDITIONAL" in text
    assert "Full_RA1n_status: CLOSED" not in text
