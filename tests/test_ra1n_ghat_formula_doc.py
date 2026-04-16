from pathlib import Path

def test_ra1n_ghat_formula_doc():
    s = Path("docs/math/RA1N_GHAT_FORMULA.md").read_text()
    assert "# Conditional: RA1n concrete Ghat formula" in s
    assert "Exact definition of Ghat(xi)" in s
    assert "Do not claim GoodBounds, L1_integrable, or C = 1" in s
