from pathlib import Path

def test_dr33d_step32_normalization_lock() -> None:
    s = Path("docs/math/DR33D_STEP_32_NORMALIZATION_AND_SIZE_FLOOR.md").read_text()
    assert "DR33D Step 32 — Normalization and the Exact Size-Floor Obstruction" in s
    assert r"\widetilde E_j:=\frac{E_j}{S^{1/(1+\theta)}}" in s
    assert r"\sum_j \widetilde E_j^{\,1+\theta}" in s
    assert "1." in s
    assert r"\widetilde A:=\sum_j 2^{-j}\widetilde E_j^{1/2}" in s
    assert r"A^2" in s
    assert r"S^{1/(1+\theta)}" in s
    assert r"S\ge m>0" in s
    assert r"E_j=a\,\mathbf 1_{\{j=j_\ast\}}" in s
    assert "LOCKED NORMALIZATION — obstruction is exactly the vanishing-size regime \\(S\\to0\\); linear upgrade requires a positive size-floor invariant." in s
