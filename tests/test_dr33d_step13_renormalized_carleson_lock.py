from pathlib import Path

def test_dr33d_step13_renormalized_carleson_lock() -> None:
    s = Path("docs/math/DR33D_STEP_13_RENORMALIZED_CARLESON_IMPLICATION.md").read_text()
    assert "DR33D Step 13 — Renormalized Carleson Implication" in s
    assert r"F_j(t):=2^{-\alpha j}E_j(t)" in s
    assert r"\mathfrak C_T^{(\alpha)}(F)" in s
    assert r"\sum_j 2^{-j+\alpha j}F_j(t)" in s
    assert r"\sum_j F_j(t)^{1+\theta}" in s
    assert "OPEN — renormalized Carleson bridge not yet established." in s
