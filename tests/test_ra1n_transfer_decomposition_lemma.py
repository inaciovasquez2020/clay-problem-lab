from pathlib import Path

DOC = Path("docs/math/RA1N_TRANSFER_DECOMPOSITION_LEMMA.md")

def test_transfer_decomposition_status_open():
    s = DOC.read_text()
    assert "Status: OPEN." in s

def test_transfer_decomposition_identity_locked():
    s = DOC.read_text()
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)=M_k-E_k" in s

def test_transfer_decomposition_main_bound_locked():
    s = DOC.read_text()
    assert "M_k\\ge" in s
    assert "\\mathrm{Curv}_k\\mathrm{Gap}_k|\\partial_\\xi\\widehat G_k|" in s

def test_transfer_decomposition_error_bound_locked():
    s = DOC.read_text()
    assert "E_k\\le" in s
    assert "\\|P_k\\widehat G_k\\|_{\\mathrm{err}}" in s

def test_transfer_decomposition_consequence_locked():
    s = DOC.read_text()
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)\\ge 2>0" in s
    assert "definition-level identity" in s
