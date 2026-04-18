from pathlib import Path

def test_dr33d_step45_admissibility_closure_template_lock() -> None:
    s = Path("docs/math/DR33D_STEP_45_ADMISSIBILITY_CLOSURE_TEMPLATE.md").read_text()
    assert "DR33D Step 45 — Admissibility Closure Template" in s
    assert "Conditional." in s
    assert r"E(u)\in\mathcal A_{\delta,m}" in s
    assert r"A(E(u))^2\le C(\theta,j_0,\delta,m)\,S(E(u))" in s
    assert "locked counterexamples" in s
