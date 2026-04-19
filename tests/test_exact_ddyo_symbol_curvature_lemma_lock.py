from pathlib import Path

def test_exact_ddyo_symbol_curvature_lemma_lock() -> None:
    s = Path("docs/math/EXACT_DDYO_SYMBOL_CURVATURE_LEMMA.md").read_text()
    assert "## Status" in s
    assert "OPEN" in s
    assert "m_k^{\\mathrm{DDYO}}(\\xi,\\eta)" in s
    assert "\\partial_\\perp^2 r_k^{\\mathrm{DDYO}}(\\xi,\\eta)\\big|_{\\xi\\parallel\\eta}\\ge c\\,2^{-\\alpha k}" in s
    assert "|r_k^{\\mathrm{DDYO}}(\\xi,\\eta)|\\ge c\\,2^{-\\alpha k}|\\xi\\wedge\\eta|^2" in s
    assert "terminal_high_high_resonance_curvature_gain" in s
