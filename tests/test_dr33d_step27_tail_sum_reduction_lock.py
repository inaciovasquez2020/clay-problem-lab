from pathlib import Path

def test_dr33d_step27_tail_sum_reduction_lock() -> None:
    s = Path("docs/math/DR33D_STEP_27_TAIL_SUM_REDUCTION.md").read_text()
    assert "DR33D Step 27 — Tail-Sum Reduction Under Monotonicity" in s
    assert r"E_{j+1}\le E_j" in s
    assert r"E_j=0 \quad\text{for all }j<j_0" in s
    assert r"\sum_{m\le j}2^{-m}E_m^{1/2}" in s
    assert r"\sup_{j\ge j_0}\left(2^{-j}E_j^{1/2}\right)" in s
    assert r"\sum_j E_j^{1+\theta}" in s
    assert r"E_j \le C\,2^{2j}" in s
    assert "REDUCTION LOCK — Step 25 is equivalent to a uniform pointwise growth bound under monotone cutoff." in s
