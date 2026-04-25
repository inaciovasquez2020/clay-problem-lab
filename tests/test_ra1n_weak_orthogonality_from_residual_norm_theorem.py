from pathlib import Path

DOC = Path("docs/math/RA1N_WEAK_ORTHOGONALITY_FROM_RESIDUAL_NORM_THEOREM.md")

def test_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_target():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\mathcal W_{\\mathrm{term}}(\\chi)=0" in s

def test_residual_norm_identity():
    s = DOC.read_text()
    assert "r_W(\\chi):=(I-\\Pi_W)\\chi" in s
    assert "\\mathcal W_{\\mathrm{term}}(\\chi)=\\|r_W(\\chi)\\|_2" in s

def test_consequence_remaining():
    s = DOC.read_text()
    assert "RA1N_TERMINAL_ADMISSIBILITY_WEAK_ORTHOGONALITY_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
    assert "\\|r_W(\\chi)\\|_2=0" in s
