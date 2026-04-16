from pathlib import Path

def test_ddyo_ra1n_post_symbol_frontiers_gate_is_false():
    s = Path("docs/math/DDYO_RA1N_POST_SYMBOL_FRONTIERS.md").read_text()
    assert "POST_SYMBOL_FRONTIERS_ENABLED" in s
    assert "false" in s
    assert "LPS/ESS" in s
