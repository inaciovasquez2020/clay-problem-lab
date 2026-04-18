from pathlib import Path

def test_dr33d_step20_discrete_hardy_gain_lock() -> None:
    s = Path("docs/math/DR33D_STEP_20_DISCRETE_HARDY_GAIN.md").read_text()
    assert "DR33D Step 20 — Discrete Hardy-Type Inequality with Exponent Gain" in s
    assert r"a_j:=E_j^{1/2}" in s
    assert r"H_j:=\sum_{m\le j}2^{-m}a_m" in s
    assert r"\sum_j H_j^{\,2+\varepsilon}" in s
    assert r"\sum_{m\le j}2^{-m}E_m^{1/2}" in s
    assert r"\sum_j E_j^{1+\theta}" in s
    assert "OPEN ROUTE — exponent gain beyond quadratic remains unproved." in s
