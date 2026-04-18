from pathlib import Path

def test_dr33d_step34_weakest_sufficient_lemma_lock() -> None:
    s = Path("docs/math/DR33D_STEP_34_WEAKEST_SUFFICIENT_LEMMA.md").read_text()
    assert "DR33D Step 34 — Weakest Sufficient Lemma for the Surviving Frontier" in s
    assert "Conditional." in s
    assert r"\mathfrak C(E):=\frac{\sup_j E_j^{1+\theta}}{S(E)}" in s
    assert r"\widetilde E_j:=\frac{E_j}{S(E)^{1/(1+\theta)}}" in s
    assert r"\mathfrak C(E)\le 1-\delta" in s
    assert r"A(E)^2\le \Lambda^2\, S(E)^{1/(1+\theta)}" in s
    assert r"S(E)\ge m>0" in s
    assert r"\mathcal A_{\delta,m}" in s
    assert "weakest sufficient frontier object" in s
