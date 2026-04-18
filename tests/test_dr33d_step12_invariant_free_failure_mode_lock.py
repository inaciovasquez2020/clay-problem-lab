from pathlib import Path

def test_dr33d_step12_invariant_free_failure_mode_lock() -> None:
    s = Path("docs/math/DR33D_STEP_12_INVARIANT_FREE_FAILURE_MODE.md").read_text()
    assert "DR33D Step 12 — Exact Failure Mode for Invariant-Free Routes" in s
    assert r"\left(\sum_j 2^{-j}E_j(t)^{1/2}\right)^2" in s
    assert r"\sum_j a_j E_j(t) < \infty" in s
    assert r"\sum_j b_j E_j(t)^2 < \infty" in s
    assert r"2\sum_{j<k}2^{-(j+k)}E_j(t)^{1/2}E_k(t)^{1/2}" in s
    assert "LOCKED FAILURE MODE — invariant required." in s
