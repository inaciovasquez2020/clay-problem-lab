from pathlib import Path

def test_ra1n_goodbounds_frontier_doc():
    s = Path("docs/math/RA1N_GOODBOUNDS_FRONTIER.md").read_text()
    assert "# Conditional: RA1n GoodBounds frontier" in s
    assert "alpha < 3" in s
    assert "eps > 0" in s
    assert "GoodBounds -> L1_integrable -> C = 1" in s
    assert "Do not claim GoodBounds, L1_integrable, or C = 1" in s
