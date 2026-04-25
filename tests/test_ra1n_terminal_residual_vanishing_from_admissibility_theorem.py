from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_RESIDUAL_VANISHING_FROM_ADMISSIBILITY_THEOREM.md")

def test_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_target():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\|r_W(\\chi)\\|_2=0" in s

def test_residual_functional():
    s = DOC.read_text()
    assert "\\mathcal R_{\\mathrm{term}}(\\chi):=\\|r_W(\\chi)\\|_2^2" in s
    assert "\\mathcal R_{\\mathrm{term}}(\\chi)=0" in s

def test_consequence_remaining():
    s = DOC.read_text()
    assert "RA1N_WEAK_ORTHOGONALITY_FROM_RESIDUAL_NORM_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
