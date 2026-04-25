from pathlib import Path

def test_ra1n_compactness_to_delta_separation_doc():
    s = Path("docs/math/RA1N_COMPACTNESS_TO_DELTA_SEPARATION.md").read_text()
    assert "Status: PROVED ABSTRACTLY" in s
    assert "K \\text{ is compact in } L^2" in s
    assert "K\\cap \\mathcal O_h=\\varnothing" in s
    assert "\\delta" in s
    assert ">0" in s
    assert "\\epsilon=\\frac{\\delta^2}{2}" in s
    assert "RA1N_DELTA_SEPARATION_LEMMA.md" in s

def test_ra1n_delta_separation_links_compactness_source():
    s = Path("docs/math/RA1N_DELTA_SEPARATION_LEMMA.md").read_text()
    assert "RA1N_COMPACTNESS_TO_DELTA_SEPARATION.md" in s
    assert "normalized terminal packet set is compact" in s
    assert "disjoint from the obstruction orbit" in s
