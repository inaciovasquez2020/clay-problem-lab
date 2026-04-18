from pathlib import Path

def test_simslv_frontier_closure_surface():
    s = Path("docs/math/SIMSLV_FRONTIER_CLOSURE.md").read_text()
    assert "SiMSLV frontier closure" in s
    assert "terminal_high_high_resonance_curvature_gain" in s
    assert "r_k = \\widehat G_k - P_k \\widehat G_k" in s
    assert r"|r_k(\xi,\eta)| \ge c\,2^{-\alpha k}|\xi\wedge\eta|^2" in s
    assert r"\mathcal R_K(t) \lesssim \mathcal E_K(t)^{1+\theta}\mathcal D_K(t)^{\frac{1-\theta}{2}}" in s
    assert "Conditional." in s
