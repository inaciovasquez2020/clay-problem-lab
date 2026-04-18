from pathlib import Path

def test_dr33d_step41_no_new_terminal_obstruction_lock() -> None:
    s = Path("docs/math/DR33D_STEP_41_NO_NEW_TERMINAL_OBSTRUCTION.md").read_text()
    assert "DR33D Step 41 — No New Terminal Obstruction" in s
    assert "Conditional." in s
    assert r"\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}" in s
    assert "weighted Hölder reduction" in s
    assert "normalization" in s
    assert "unrestricted counterexamples" in s
    assert "monotone-cutoff counterexamples" in s
