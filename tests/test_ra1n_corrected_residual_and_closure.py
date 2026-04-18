from pathlib import Path

def test_ra1n_corrected_residual_and_closure_surface():
    p = Path("docs/math/RA1N_CORRECTED_RESIDUAL_AND_CLOSURE.md")
    text = p.read_text()
    assert "r_k=\\widehat G_k-P_k\\widehat G_k" in text
    assert "is identically zero" in text
    assert "Conditional." in text
    assert "RA1n is not closed by the zero-symbol formula." in text
    assert "The remaining frontier is the exponent-drop shell-sum theorem" in text
