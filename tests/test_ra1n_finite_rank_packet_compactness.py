from pathlib import Path

def test_ra1n_finite_rank_packet_compactness_doc():
    s = Path("docs/math/RA1N_FINITE_RANK_PACKET_COMPACTNESS.md").read_text()
    assert "Status: PROVED ABSTRACTLY" in s
    assert "V_{\\mathrm{RA1n}}\\subset L^2" in s
    assert "K\\subset V_{\\mathrm{RA1n}}" in s
    assert "K\\text{ is compact in }L^2" in s
    assert "finite-dimensional" in s
    assert "closed subset of a compact set" in s
    assert "RA1N_COMPACTNESS_TO_DELTA_SEPARATION.md" in s

def test_ra1n_compactness_links_finite_rank_source():
    s = Path("docs/math/RA1N_COMPACTNESS_TO_DELTA_SEPARATION.md").read_text()
    assert "RA1N_FINITE_RANK_PACKET_COMPACTNESS.md" in s
    assert "finite-dimensional RA1n packet subspace" in s
    assert "closed there" in s
