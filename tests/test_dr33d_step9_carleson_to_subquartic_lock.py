from pathlib import Path

def test_dr33d_step9_carleson_to_subquartic_lock() -> None:
    s = Path("docs/math/DR33D_STEP_9_CARLESON_TO_SUBQUARTIC.md").read_text()
    assert "DR33D Step 9 — Carleson-to-Subquartic Implication" in s
    assert r"\mathfrak C_T(E)" in s
    assert r"\int_0^T\left(\sum_j 2^{-j}E_j(t)^{1/2}\right)^2dt" in s
    assert r"\int_0^T\sum_j E_j(t)^{1+\theta}\,dt" in s
    assert "OPEN — implication not yet derived." in s
