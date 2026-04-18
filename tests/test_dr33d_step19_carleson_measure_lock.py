from pathlib import Path

def test_dr33d_step19_carleson_measure_lock() -> None:
    s = Path("docs/math/DR33D_STEP_19_CARLESON_TYPE_MEASURE_BOUND.md").read_text()
    assert "DR33D Step 19 — Carleson-Type Measure Bound on Shell Energies" in s
    assert r"\mu(I):=\sum_{j\in I} E_j" in s
    assert r"I_{m,N}:=\{j\in\mathbb Z: m\le j\le m+N\}" in s
    assert r"\sum_{j=m}^{m+N} E_j" in s
    assert r"A\,2^{(1-\theta)m}" in s
    assert r"\sum_j 2^{-j}E_j^{1/2}" in s
    assert "OPEN ROUTE — requires derivation of the subquartic shell-sum consequence from the stated Carleson-type hypothesis." in s
