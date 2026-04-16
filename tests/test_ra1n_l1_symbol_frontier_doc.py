from pathlib import Path

def test_ra1n_l1_symbol_frontier_doc():
    s = Path("docs/math/RA1N_L1_SYMBOL_FRONTIER.md").read_text()
    assert "# Conditional: RA1n L1 symbol frontier" in s
    assert "Weakest sufficient lemma" in s
    assert "alpha < 3" in s
    assert "eps > 0" in s
    assert "Extract the concrete formula for Ghat" in s
    assert "Lift L^1_integrable to the registry flag C = 1" in s
