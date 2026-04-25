from pathlib import Path

DOC = Path("docs/math/RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CONDITIONAL_CLOSURE.md")

def test_symbolic_transfer_conditional_status_locked():
    s = DOC.read_text()
    assert "Status: Certified Conditional Theorem." in s

def test_symbolic_transfer_assumption_locked():
    s = DOC.read_text()
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)" in s
    assert "\\mathrm{Curv}_k\\mathrm{Gap}_k|\\partial_\\xi\\widehat G_k|" in s
    assert "\\|P_k\\widehat G_k\\|_{\\mathrm{err}}" in s

def test_symbolic_transfer_conclusion_locked():
    s = DOC.read_text()
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)\\ge 2>0" in s

def test_symbolic_transfer_remaining_object_locked():
    s = DOC.read_text()
    assert "prove the symbolic transfer inequality itself" in s
