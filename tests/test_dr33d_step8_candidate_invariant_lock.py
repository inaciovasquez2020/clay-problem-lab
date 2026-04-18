from pathlib import Path

def test_dr33d_step8_candidate_invariant_lock() -> None:
    s = Path("docs/math/DR33D_STEP_8_CANDIDATE_INVARIANT.md").read_text()
    assert "DR33D Step 8 — Candidate Invariant" in s
    assert r"\mathfrak I_{\beta,\theta}(E)" in s
    assert r"\sum_j 2^{-\beta j}E_j^{1+\theta}" in s
    assert r"\left(\sum_j 2^{-j}E_j^{1/2}\right)^2" in s
    assert "CANDIDATE — not yet verified." in s
