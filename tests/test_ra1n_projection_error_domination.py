from pathlib import Path

def test_ra1n_projection_error_domination_lock():
    s = Path("docs/math/RA1N_PROJECTION_ERROR_DOMINATION.md").read_text()
    assert "Status: OPEN" in s
    assert "r_k(\\xi)=\\widehat G_k(\\xi)-P_k\\widehat G_k(\\xi)" in s
    assert "\\|P_k\\widehat G_k\\|_{\\mathrm{err}}" in s
    assert "\\mathcal T_{RA1n}(k)" in s
    assert "weakest sufficient missing inequality" in s
