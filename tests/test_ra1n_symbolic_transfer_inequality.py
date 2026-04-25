from pathlib import Path

DOC = Path("docs/math/RA1N_SYMBOLIC_TRANSFER_INEQUALITY.md")

def test_ra1n_symbolic_transfer_status_open():
    s = DOC.read_text()
    assert "Status: OPEN." in s

def test_ra1n_symbolic_transfer_target_locked():
    s = DOC.read_text()
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)" in s
    assert "\\mathrm{Curv}_k\\mathrm{Gap}_k" in s
    assert "|\\partial_\\xi\\widehat G_k|" in s
    assert "\\|P_k\\widehat G_k\\|_{\\mathrm{err}}" in s

def test_ra1n_symbolic_transfer_certified_consequence_locked():
    s = DOC.read_text()
    assert "\\mathrm{Curv}_k=2" in s
    assert "\\mathrm{Gap}_k=1" in s
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)\\ge 2>0" in s

def test_ra1n_symbolic_transfer_failure_witness_locked():
    s = DOC.read_text()
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)" in s
    assert "<" in s
    assert "Failure Witness" in s
