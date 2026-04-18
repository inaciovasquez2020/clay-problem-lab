from pathlib import Path

def test_dr33d_step35_pde_to_shell_frontier_lock() -> None:
    s = Path("docs/math/DR33D_STEP_35_PDE_TO_SHELL_ADMISSIBILITY_FRONTIER.md").read_text()
    assert "DR33D Step 35 — PDE-to-Shell Admissibility Frontier" in s
    assert "Conditional." in s
    assert r"\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}" in s
    assert r"\mathfrak C(E(u))\le 1-\delta" in s
    assert r"S(E(u))\ge m>0" in s
    assert r"A(E(u))^2\le C(\theta,j_0,\delta,m)\,S(E(u))" in s
    assert "exact PDE-to-shell frontier" in s
