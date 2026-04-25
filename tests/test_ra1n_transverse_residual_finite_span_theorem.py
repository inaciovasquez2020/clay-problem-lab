from pathlib import Path

DOC = Path("docs/math/RA1N_TRANSVERSE_RESIDUAL_FINITE_SPAN_THEOREM.md")

def test_ra1n_transverse_residual_finite_span_status():
    s = DOC.read_text()
    assert "Status: CONDITIONAL STRUCTURAL THEOREM" in s

def test_ra1n_transverse_residual_finite_span_target():
    s = DOC.read_text()
    assert "r=(I-\\Pi_V)F" in s
    assert "F\\in\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "r\\in W_{\\perp}" in s

def test_ra1n_transverse_residual_finite_span_hypothesis():
    s = DOC.read_text()
    assert "finite residual expansion" in s
    assert "(I-\\Pi_V)F" in s
    assert "\\sum_{j=1}^m c_j(F)\\psi_j" in s
    assert "c_j(F)\\in\\mathbb C" in s

def test_ra1n_transverse_residual_finite_span_consequence():
    s = DOC.read_text()
    assert "RA1N_TRANSVERSE_RAYLEIGH_GAP_CERTIFICATE_THEOREM.md" in s
    assert "RA1N_TRANSVERSE_SPECTRAL_GAP_COERCIVITY_THEOREM.md" in s
    assert "RA1N_NORMALIZED_TRANSVERSE_COERCIVITY_THEOREM.md" in s
    assert "RA1N_TRANSVERSE_ENERGY_GAP_EXCLUSION_THEOREM.md" in s
    assert "Remaining Non-Conditional Obligation" in s
