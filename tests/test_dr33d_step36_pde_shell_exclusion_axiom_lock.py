from pathlib import Path

def test_dr33d_step36_pde_shell_exclusion_axiom_lock() -> None:
    s = Path("docs/math/DR33D_STEP_36_PDE_SHELL_EXCLUSION_AXIOM.md").read_text()
    assert "DR33D Step 36 — PDE Shell-Exclusion Axiom" in s
    assert "Conditional." in s
    assert r"S(E(u)):=\sum_{j\in\mathbb Z}E_j(u)^{1+\theta}" in s
    assert r"\mathfrak C(E(u)):=\frac{\sup_j E_j(u)^{1+\theta}}{S(E(u))}" in s
    assert r"E_{j+1}(u)\le E_j(u)" in s
    assert r"\mathfrak C(E(u))\le 1-\delta" in s
    assert r"S(E(u))\ge m" in s
    assert r"\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}" in s
    assert "exact PDE shell-exclusion axiom" in s
