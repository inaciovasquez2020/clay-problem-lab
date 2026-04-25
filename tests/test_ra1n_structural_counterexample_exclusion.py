from pathlib import Path

def test_ra1n_structural_counterexample_exclusion_doc():
    s = Path("docs/math/RA1N_STRUCTURAL_COUNTEREXAMPLE_EXCLUSION.md").read_text()
    assert "Status: OPEN" in s
    assert "F=\\frac{\\overline g}{\\|g\\|_2}" in s
    assert "F\\notin g^\\perp" in s
    assert "|\\langle F,g\\rangle|" in s
    assert "(1-\\epsilon)\\|F\\|_2\\|g\\|_2" in s
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)" in s
    assert "Conditional." in s
    assert "Unrestricted RA1n remains OPEN" in s

def test_ra1n_symbolic_transfer_links_counterexample_exclusion():
    s = Path("docs/math/RA1N_SYMBOLIC_TRANSFER_LEMMA.md").read_text()
    assert "RA1N_STRUCTURAL_COUNTEREXAMPLE_EXCLUSION.md" in s
    assert "RA1N_PROJECTION_ERROR_DOMINATION.md" in s
