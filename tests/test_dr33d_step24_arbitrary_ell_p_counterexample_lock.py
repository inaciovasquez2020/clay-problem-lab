from pathlib import Path

def test_dr33d_step24_arbitrary_ell_p_counterexample_lock() -> None:
    s = Path("docs/math/DR33D_STEP_24_ARBITRARY_ELL_P_COUNTEREXAMPLE.md").read_text()
    assert "DR33D Step 24 — Failure on Arbitrary \\(\\ell^{1+\\theta}\\) without Lower-Shell Cutoff" in s
    assert r"\left(\sum_{j\in\mathbb Z} 2^{-j}E_j^{1/2}\right)^2" in s
    assert r"\sum_{j\in\mathbb Z} E_j^{1+\theta}" in s
    assert r"E^{(N)}_j :=" in s
    assert r"j=-N" in s
    assert r"2^{2N}" in s
    assert r"E_j=0\qquad\text{for all }j<j_0" in s
    assert "LOCKED IMPOSSIBILITY — Step 23 fails on arbitrary \\(\\ell^{1+\\theta}\\) without added structure." in s
