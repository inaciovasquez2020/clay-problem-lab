from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_ADMISSIBILITY_WEAK_ORTHOGONALITY_THEOREM.md")

def test_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_target():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\forall \\zeta\\in W_{\\mathrm{term}}^\\perp" in s
    assert "\\langle \\chi,\\zeta\\rangle_{L^2}=0" in s

def test_weak_functional():
    s = DOC.read_text()
    assert "\\mathcal W_{\\mathrm{term}}(\\chi)" in s
    assert "\\sup_{\\substack{\\zeta\\in W_{\\mathrm{term}}^\\perp" in s
    assert "\\|\\zeta\\|_2=1" in s

def test_consequence_and_remaining():
    s = DOC.read_text()
    assert "RA1N_TERMINAL_ADMISSIBILITY_ANNIHILATOR_SATURATION_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
    assert "\\mathcal W_{\\mathrm{term}}(\\chi)=0" in s
