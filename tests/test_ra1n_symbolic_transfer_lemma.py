from pathlib import Path

def test_ra1n_symbolic_transfer_lemma_status():
    s = Path("docs/math/RA1N_SYMBOLIC_TRANSFER_LEMMA.md").read_text()
    assert "Status: OPEN" in s
    assert "r_k(\\xi)=\\widehat G_k(\\xi)-P_k\\widehat G_k(\\xi)" in s
    assert "\\mathcal T_{RA1n}(k) \\ge c_{RA1n} > 0" in s
    assert "not an independent empirical assumption" in s
