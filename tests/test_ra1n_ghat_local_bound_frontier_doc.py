from pathlib import Path

def test_ra1n_ghat_local_bound_frontier_doc():
    s = Path("docs/math/RA1N_GHAT_LOCAL_BOUND_FRONTIER.md").read_text()
    assert "# Conditional: RA1n Ghat local bound frontier" in s
    assert "alpha < 3" in s
    assert "C0 > 0" in s
    assert "local half of GoodBounds" in s
    assert "Do not claim GoodBounds or L1_integrable" in s
