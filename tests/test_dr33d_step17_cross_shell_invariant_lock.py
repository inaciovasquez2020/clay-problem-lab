from pathlib import Path

def test_dr33d_step17_cross_shell_invariant_lock() -> None:
    s = Path("docs/math/DR33D_STEP_17_CROSS_SHELL_INTERACTION_INVARIANT.md").read_text()
    assert "DR33D Step 17 — Candidate Cross-Shell Interaction Invariant" in s
    assert r"\mathfrak I_{\mathrm{cross}}(E)" in s
    assert r"\sum_{j\le k} 2^{-(j+k)}E_j^{1/2}E_k^{1/2}" in s
    assert r"\left(\sum_j 2^{-j}E_j^{1/2}\right)^2" in s
    assert r"\sum_j E_j^{1+\theta}" in s
    assert "CANDIDATE INVARIANT — domination by subquartic shell sum remains open." in s
