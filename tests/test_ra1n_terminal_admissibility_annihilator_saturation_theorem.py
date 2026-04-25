from pathlib import Path

DOC = Path("docs/math/RA1N_TERMINAL_ADMISSIBILITY_ANNIHILATOR_SATURATION_THEOREM.md")

def test_ra1n_terminal_admissibility_annihilator_saturation_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_terminal_admissibility_annihilator_saturation_target():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "(I-\\Pi_W)\\chi=0" in s

def test_ra1n_terminal_admissibility_annihilator_saturation_hypothesis():
    s = DOC.read_text()
    assert "W_{\\mathrm{term}}^\\perp" in s
    assert "\\forall \\zeta\\in W_{\\mathrm{term}}^\\perp" in s
    assert "\\langle \\chi,\\zeta\\rangle_{L^2}=0" in s
    assert "annihilator-saturation hypothesis" in s

def test_ra1n_terminal_admissibility_annihilator_saturation_proof_core():
    s = DOC.read_text()
    assert "r:=(I-\\Pi_W)\\chi" in s
    assert "\\zeta=r" in s
    assert "\\langle \\chi,r\\rangle_{L^2}=0" in s
    assert "\\|r\\|_2^2" in s
    assert "r=0" in s

def test_ra1n_terminal_admissibility_annihilator_saturation_consequence():
    s = DOC.read_text()
    assert "RA1N_TERMINAL_ADMISSIBILITY_FINITE_COORDINATE_THEOREM.md" in s
    assert "a(\\chi)\\phi_1" in s
    assert "\\sum_{j=1}^m c_j(\\chi)\\psi_j" in s
    assert "Remaining Non-Conditional Obligation" in s
