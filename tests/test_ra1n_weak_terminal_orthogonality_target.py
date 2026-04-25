from pathlib import Path

def test_ra1n_weak_terminal_orthogonality_target_is_open_and_exact():
    p = Path("docs/status/RA1N_WEAK_TERMINAL_ORTHOGONALITY_TARGET.md")
    s = p.read_text()
    assert "Status: OPEN." in s
    assert r"\mathcal A_{\mathrm{term}}(\chi)" in s
    assert r"\mathcal W_{\mathrm{term}}(\chi)=0" in s
    assert r"(I-\Pi_W)\chi=0" in s
    assert "It is not proved here." in s
