from pathlib import Path

def test_terminal_high_high_resonance_gain_route_surface():
    s = Path("docs/math/TERMINAL_HIGH_HIGH_RESONANCE_GAIN_ROUTE.md").read_text()
    assert "resonance" in s
    assert r"|r_k(\xi,\eta)| \ge c\,2^{-\alpha k}|\xi\wedge\eta|^2" in s
    assert r"\mathcal R_K(t) \lesssim \mathcal E_K(t)^{1+\theta}\mathcal D_K(t)^{\frac{1-\theta}{2}}" in s
    assert "Open." in s
