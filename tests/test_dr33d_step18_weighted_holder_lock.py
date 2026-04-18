from pathlib import Path

def test_dr33d_step18_weighted_holder_lock() -> None:
    s = Path("docs/math/DR33D_STEP_18_WEIGHTED_HOLDER_DYADIC_ASYMMETRY.md").read_text()
    assert "DR33D Step 18 — Weighted Hölder Inequality with Dyadic Decay Asymmetry" in s
    assert r"\sum_j 2^{-j} E_j^{1/2}" in s
    assert r"S:=\sum_{j\in\mathbb Z} E_j^{1+\theta}\le M<\infty" in s
    assert r"E_j=0 \quad \text{for } j<j_0" in s
    assert r"q:=2(1+\theta)" in s
    assert r"p:=\frac{q}{q-1}=\frac{2(1+\theta)}{1+2\theta}" in s
    assert r"C(j_0,\theta,M)" in s
    assert "CONDITIONAL ROUTE — closes Step 16 only under the added boundedness and support assumptions." in s
