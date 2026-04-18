from pathlib import Path

def test_dr33d_step23_minimal_unifying_invariant_lock() -> None:
    s = Path("docs/math/DR33D_STEP_23_MINIMAL_UNIFYING_INVARIANT.md").read_text()
    assert "DR33D Step 23 — Minimal Unifying Invariant (Sharp Frontier Object)" in s
    assert r"\mathfrak I(E)" in s
    assert r"\left(\sum_j 2^{-j}E_j^{1/2}\right)^2" in s
    assert r"\sum_{j\le k}2^{-(j+k)}E_j^{1/2}E_k^{1/2}" in s
    assert r"\sum_j E_j^{1+\theta}" in s
    assert r"\|E\|_{\ell^{1+\theta}}" in s
    assert r"F_K" in s
    assert "FINAL WALL — no known inequality achieves this domination without additional structural assumptions." in s
