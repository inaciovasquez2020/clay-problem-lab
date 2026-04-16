from pathlib import Path

def test_ra1n_ghat_formula_no_placeholder_doc():
    s = Path("docs/math/RA1N_GHAT_FORMULA.md").read_text()
    assert "Paste the exact normalized formula" not in s
    assert "\\widehat G(\\xi)=" in s
