from pathlib import Path

def test_dr33d_step16_minimal_invariant_axiom_lock() -> None:
    s = Path("docs/math/DR33D_STEP_16_MINIMAL_INVARIANT_AXIOM.md").read_text()
    assert "DR33D Step 16 — Minimal Invariant Axiom Schema" in s
    assert r"\mathfrak I(E)" in s
    assert r"\left(\sum_j 2^{-j}E_j^{1/2}\right)^2" in s
    assert r"\sum_j E_j^{1+\theta}" in s
    assert "OPEN AXIOM SCHEMA — realization of \\(\\mathfrak I\\) still missing." in s
