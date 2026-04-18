from pathlib import Path

def test_dr33d_step11_weighted_holder_lock() -> None:
    s = Path("docs/math/DR33D_STEP_11_WEIGHTED_HOLDER_ROUTE.md").read_text()
    assert "DR33D Step 11 — Weighted Hölder Route" in s
    assert r"\sum_j A_j B_j" in s
    assert r"A_j := 2^{-j+\alpha j/2}" in s
    assert r"B_j := F_j(t)^{1/2}" in s
    assert r"\sum_j F_j(t)^{1+\theta}" in s
    assert "FAILURE ROUTE — insufficient without additional invariant." in s
