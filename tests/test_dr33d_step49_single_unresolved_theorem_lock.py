from pathlib import Path

def test_dr33d_step49_single_unresolved_theorem_lock() -> None:
    s = Path("docs/math/DR33D_STEP_49_SINGLE_UNRESOLVED_THEOREM.md").read_text()
    assert "DR33D Step 49 — Single Unresolved Theorem" in s
    assert "Conditional." in s
    assert r"\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}" in s
    assert "single unresolved theorem status" in s
