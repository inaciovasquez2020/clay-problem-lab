from pathlib import Path

def test_dr33d_step25_monotone_cutoff_frontier_lock() -> None:
    s = Path("docs/math/DR33D_STEP_25_MONOTONE_CUTOFF_FRONTIER.md").read_text()
    assert "DR33D Step 25 — Exact Monotone-Cutoff Frontier Lemma" in s
    assert r"E_{j+1}\le E_j" in s
    assert r"E_j=0\qquad\text{for all }j<j_0" in s
    assert r"\left(\sum_{j\in\mathbb Z}2^{-j}E_j^{1/2}\right)^2" in s
    assert r"\sum_{j\in\mathbb Z}E_j^{1+\theta}" in s
    assert r"\mathfrak I(E):=" in s
    assert r"\|E\|_{\ell^{1+\theta}}" in s
    assert "OPEN FRONTIER LEMMA — unrestricted form is false; monotone-cutoff form remains unresolved." in s
