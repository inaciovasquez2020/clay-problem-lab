from pathlib import Path

def test_dr33d_step44_bridge_closure_form_lock() -> None:
    s = Path("docs/math/DR33D_STEP_44_BRIDGE_CLOSURE_FORM.md").read_text()
    assert "DR33D Step 44 — Bridge Closure Form" in s
    assert "Conditional." in s
    assert r"\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}" in s
    assert r"A(E(u))^2\le C(\theta,j_0,\delta,m)\,S(E(u))" in s
    assert "final bridge from PDE admissibility to the linear shell estimate" in s
