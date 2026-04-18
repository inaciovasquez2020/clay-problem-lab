from pathlib import Path

def test_dr33d_step14_parameter_region_lock() -> None:
    s = Path("docs/math/DR33D_STEP_14_PARAMETER_REGION.md").read_text()
    assert "DR33D Step 14 — Admissible Parameter Region" in s
    assert r"\alpha>0,\qquad \beta>0,\qquad \theta\in(0,1)" in s
    assert r"\beta=\alpha(1+\theta)" in s
    assert r"\alpha<2" in s
    assert r"\alpha\in(0,2)" in s
    assert "LOCKED REGION — candidate parameter geometry only, not a proof." in s
