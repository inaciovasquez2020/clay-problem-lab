from pathlib import Path

def test_dr33d_step26_monotone_geometric_test_lock() -> None:
    s = Path("docs/math/DR33D_STEP_26_MONOTONE_GEOMETRIC_TEST.md").read_text()
    assert "DR33D Step 26 — Monotone Geometric Test Family" in s
    assert r"E_j^{(\alpha,j_0)}" in s
    assert r"2^{-\alpha (j-j_0)}" in s
    assert r"E_{j+1}^{(\alpha,j_0)}\le E_j^{(\alpha,j_0)}" in s
    assert r"E_j^{(\alpha,j_0)}=0" in s
    assert r"\mathfrak I\!\left(E^{(\alpha,j_0)}\right)" in s
    assert r"\frac{2^{-2j_0}}{\left(1-2^{-(1+\alpha/2)}\right)^2}" in s
    assert r"\frac{1}{1-2^{-\alpha(1+\theta)}}" in s
    assert r"R(\alpha,j_0,\theta)" in s
    assert "NEGATIVE TEST — standard geometric monotone cutoff family does not refute the Step 25 frontier." in s
