from pathlib import Path

def test_dr33d_step28_weighted_holder_reduction_lock() -> None:
    s = Path("docs/math/DR33D_STEP_28_WEIGHTED_HOLDER_MONOTONE_CUTOFF.md").read_text()
    assert "DR33D Step 28 — Exact Weighted Hölder Reduction Under Monotone Cutoff" in s
    assert r"E_{j+1}\le E_j" in s
    assert r"E_j=0\qquad\text{for all }j<j_0" in s
    assert r"A:=\sum_{j\in\mathbb Z}2^{-j}E_j^{1/2}" in s
    assert r"S:=\sum_{j\in\mathbb Z}E_j^{1+\theta}" in s
    assert r"q:=2(1+\theta)" in s
    assert r"p:=\frac{q}{q-1}=\frac{2(1+\theta)}{1+2\theta}" in s
    assert r"\left(\sum_{j\ge j_0}2^{-pj}\right)^{1/p}" in s
    assert r"S^{1/(1+\theta)}" in s
    assert "LOCKED REDUCTION — Step 25 reduces exactly to removal of the power gap \\(1/(1+\\theta)<1\\)." in s
