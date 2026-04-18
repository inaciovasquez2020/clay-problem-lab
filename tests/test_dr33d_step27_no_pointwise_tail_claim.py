from pathlib import Path

def test_dr33d_step27_no_pointwise_tail_claim() -> None:
    s = Path("docs/math/DR33D_STEP_27_TAIL_SUM_REDUCTION.md").read_text()
    assert "CORRECTED REDUCTION" in s
    assert r"\sum_{m\le j}2^{-m}E_m^{1/2}\le C\,2^{-j}E_j^{1/2}" in s
    assert "does not follow from monotonicity" in s
    assert "pointwise growth bound" not in s
