from pathlib import Path

def test_ra1n_ghat_tail_bound_frontier_doc():
    s = Path("docs/math/RA1N_GHAT_TAIL_BOUND_FRONTIER.md").read_text()
    assert "# Conditional: RA1n Ghat tail bound frontier" in s
    assert "eps > 0" in s
    assert "Cinf > 0" in s
    assert "tail half of GoodBounds" in s
    assert "Do not claim GoodBounds or L1_integrable" in s
