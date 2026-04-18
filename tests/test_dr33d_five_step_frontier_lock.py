from pathlib import Path

def test_dr33d_five_step_frontier_lock() -> None:
    p1 = Path("docs/math/DR33D_STEP_1_SHELL_WEIGHTED_CARLESON_MEASURE.md").read_text()
    p3 = Path("docs/math/DR33D_STEP_3_NONLINEAR_INTERPOLATION.md").read_text()
    p4 = Path("docs/math/DR33D_STEP_4_FLUX_RENORMALIZATION_VARIABLE.md").read_text()
    p2 = Path("docs/math/DR33D_STEP_2_CONVEXITY_DEFECT_INEQUALITY.md").read_text()
    p5 = Path("docs/math/DR33D_STEP_5_INVARIANT_LINKING_ENERGY_TO_DECAY.md").read_text()

    assert "DR33D Step 1 — Shell-Weighted Carleson Measure" in p1
    assert r"\mathfrak C_T(E)" in p1
    assert r"\sum_j 2^{-j}E_j(t)\,dt" in p1

    assert "DR33D Step 3 — Nonlinear Interpolation Between L2 and L4 Shell Regimes" in p3
    assert r"\left(\sum_j 2^{-j}E_j(t)^{1/2}\right)^2" in p3
    assert r"\sum_j E_j(t)^{1+\theta}" in p3

    assert "DR33D Step 4 — Flux Renormalization Variable" in p4
    assert r"F_j(t):=2^{-j\alpha}E_j(t)" in p4
    assert r"2^{-j+\alpha j/2}" in p4

    assert "DR33D Step 2 — Convexity Defect Inequality on Shell Square-Roots" in p2
    assert r"\mathfrak D(E)" in p2
    assert r"2\sum_{j<k}2^{-(j+k)}E_j^{1/2}E_k^{1/2}" in p2

    assert "DR33D Step 5 — Invariant Linking Shell Energy to Dyadic Decay" in p5
    assert r"\mathfrak I_\beta(E)" in p5
    assert r"\sum_j 2^{-j}E_j^{1/2}" in p5
