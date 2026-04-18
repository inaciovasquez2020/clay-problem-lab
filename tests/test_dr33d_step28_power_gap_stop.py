from pathlib import Path

def test_dr33d_step28_power_gap_stop() -> None:
    s = Path("docs/math/DR33D_STEP_28_WEIGHTED_HOLDER_MONOTONE_CUTOFF.md").read_text()
    assert r"S^{1/(1+\theta)}" in s
    assert "sublinear-power bound" in s
    assert "not yet the desired linear domination" in s
    assert "LOCKED REDUCTION — Step 25 reduces exactly to removal of the power gap \\(1/(1+\\theta)<1\\)." in s
