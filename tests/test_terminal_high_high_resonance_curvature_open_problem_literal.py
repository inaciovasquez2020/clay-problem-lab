from pathlib import Path

def test_terminal_high_high_resonance_curvature_open_problem_literal():
    text = Path(
        "docs/status/TERMINAL_HIGH_HIGH_RESONANCE_CURVATURE_GAIN_OPEN_PROBLEM.md"
    ).read_text(encoding="utf-8")
    assert "Status: OPEN" in text
    assert "terminal_high_high_resonance_curvature_gain" in text
    assert r"r_k=\widehat G_k-P_k\widehat G_k" in text
    assert r"|r_k(\xi,\eta)| \ge c\,2^{-\alpha k}|\xi\wedge\eta|^2" in text
    assert r"\mathcal R_K(t) \lesssim \mathcal E_K(t)^{1+\theta}\mathcal D_K(t)^{\frac{1-\theta}{2}}" in text
