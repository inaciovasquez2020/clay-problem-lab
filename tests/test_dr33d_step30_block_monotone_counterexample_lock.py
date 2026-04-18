from pathlib import Path

def test_dr33d_step30_block_monotone_counterexample_lock() -> None:
    s = Path("docs/math/DR33D_STEP_30_BLOCK_MONOTONE_TEST_FAMILY.md").read_text()
    assert "DR33D Step 30 — Block-Monotone Test Family Beyond the Geometric Case" in s
    assert r"E^{(a,L)}_j" in s
    assert r"E^{(a,L)}_{j+1}\le E^{(a,L)}_j" in s
    assert r"A(a,L)^2" in s
    assert r"S(a,L)" in s
    assert r"a^{-\theta}" in s
    assert "LOCKED COUNTEREXAMPLE — monotone cutoff alone does not imply Step 25." in s
