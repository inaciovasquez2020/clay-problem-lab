from pathlib import Path

def test_dr33d_step21_monotone_rearrangement_lock() -> None:
    s = Path("docs/math/DR33D_STEP_21_MONOTONE_REARRANGEMENT_ROUTE.md").read_text()
    assert "DR33D Step 21 — Monotone Rearrangement Structure on Shell Energies" in s
    assert r"E_{j+1}\le E_j" in s
    assert r"A:=\sum_j 2^{-j}E_j^{1/2}" in s
    assert r"\left(\sum_j 2^{-j}E_j^{1/2}\right)^2" in s
    assert r"\sum_j E_j^{1+\theta}" in s
    assert r"\sum_{m\le j}2^{-m}E_m^{1/2}" in s
    assert r"E_j^{\theta/2}" in s
    assert "OPEN ROUTE — the stated tail estimate under monotonicity remains unproved." in s
