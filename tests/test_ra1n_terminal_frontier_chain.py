from pathlib import Path

DOC = Path("docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md")

def test_status():
    s = DOC.read_text()
    assert "Status: FRONTIER CHAIN" in s

def test_chain():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\mathcal R_{\\mathrm{term}}(\\chi)=0" in s
    assert "\\|r_W(\\chi)\\|_2=0" in s
    assert "\\mathcal W_{\\mathrm{term}}(\\chi)=0" in s
    assert "(I-\\Pi_W)\\chi=0" in s

def test_frontier():
    s = DOC.read_text()
    assert "remaining non-conditional input" in s
    assert "residual-defect saturation" in s
