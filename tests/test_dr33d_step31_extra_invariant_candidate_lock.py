from pathlib import Path

def test_dr33d_step31_extra_invariant_candidate_lock() -> None:
    s = Path("docs/math/DR33D_STEP_31_EXTRA_INVARIANT_CANDIDATE.md").read_text()
    assert "DR33D Step 31 — Extra Invariant Candidate for Linear Upgrade" in s
    assert r"\mathfrak J(E):=\mathbf 1_{\{S\ge m\}}" in s
    assert r"S\ge m" in s
    assert r"S^{1/(1+\theta)}" in s
    assert r"m^{-\theta/(1+\theta)}S" in s
    assert "CANDIDATE EXTRA INVARIANT — power-gap removal works once a positive lower size floor is imposed." in s
