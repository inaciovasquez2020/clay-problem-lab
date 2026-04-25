from pathlib import Path

DOC = Path("docs/math/RA1N_ADMISSIBILITY_RESIDUAL_SATURATION_AXIOM.md")

def test_status():
    s = DOC.read_text()
    assert "Status: OPEN STRUCTURAL AXIOM" in s

def test_axiom():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\iff" in s
    assert "\\mathcal R_{\\mathrm{term}}(\\chi)=0" in s

def test_status_rule():
    s = DOC.read_text()
    assert "repository defines terminal admissibility by residual-defect saturation" in s
    assert "Remaining Non-Conditional Obligation" in s
