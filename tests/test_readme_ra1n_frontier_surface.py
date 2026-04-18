from pathlib import Path

def test_readme_ra1n_frontier_surface():
    s = Path("README.md").read_text()
    assert "## Current DDYO / RA1n frontier" in s
    assert "RA1n remains Open." in s
    assert "r_k = \\widehat G_k - P_k\\widehat G_k" in s
    assert "terminal_high_high_resonance_curvature_gain" in s
    assert "TERMINAL_HIGH_HIGH_RESONANCE_GAIN_ROUTE.md" in s
