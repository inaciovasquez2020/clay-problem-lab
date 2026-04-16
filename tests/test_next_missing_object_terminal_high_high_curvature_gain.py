from pathlib import Path

def test_next_missing_object_terminal_high_high_curvature_gain():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "terminal_high_high_resonance_curvature_gain" in s
    assert "TERMINAL_HIGH_HIGH_RESONANCE_GAIN_ROUTE.md" in s
    assert "r_k(\\xi,\\eta)" in s
    assert "2^{-\\alpha k}|\\xi\\wedge\\eta|^2" in s
    assert "\\mathcal R_K(t)" in s
    assert "\\mathcal E_K(t)^{1+\\theta}" in s
    assert "\\mathcal D_K(t)^{\\frac{1-\\theta}{2}}" in s
