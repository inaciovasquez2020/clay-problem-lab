from pathlib import Path

def test_ra1n_ghat_formula_exact_doc():
    s = Path("docs/math/RA1N_GHAT_FORMULA.md").read_text()
    assert "# Conditional: RA1n exact Ghat formula" in s
    assert "## Exact definition of \\(\\widehat G(\\xi)\\)" in s
    assert "\\widehat G(\\xi)=" in s
    assert "Do not claim GoodBounds" in s
