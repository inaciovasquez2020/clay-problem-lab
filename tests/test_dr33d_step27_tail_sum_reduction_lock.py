from pathlib import Path

def test_dr33d_step27_tail_sum_reduction_lock() -> None:
    s = Path("docs/math/DR33D_STEP_27_TAIL_SUM_REDUCTION.md").read_text()
    assert "DR33D Step 27 — Tail-Sum Reduction Under Monotonicity (Corrected)" in s
    assert r"E_{j+1}\le E_j" in s
    assert r"E_j=0 \quad\text{for all }j<j_0" in s
    assert r"\sum_{m\le j}2^{-m}E_m^{1/2}" in s
    assert r"2^{-j}\sum_{n=0}^{j-j_0}2^{n}E_{j-n}^{1/2}" in s
    assert r"\ge" in s
    assert r"\asymp" in s
    assert r"\sum_{m\le j}2^{-m}E_m^{1/2}\le C\,2^{-j}E_j^{1/2}" in s
    assert r"q=2(1+\theta)" in s
    assert r"p=\frac{q}{q-1}" in s
    assert r"\left(\sum_{j\ge j_0}2^{-pj}\right)^{1/p}" in s
    assert r"\left(\sum_{j\ge j_0}E_j^{q/2}\right)^{1/q}" in s
    assert "CORRECTED REDUCTION — prior pointwise reduction invalid; replaced by Hölder-based bound." in s
