from pathlib import Path

def test_exact_ddyo_symbol_curvature_lemma_lock() -> None:
    s = Path("docs/math/EXACT_DDYO_SYMBOL_CURVATURE_LEMMA.md").read_text()
    assert "# Exact DDYO Symbol Curvature Lemma" in s
    assert "**Status: OPEN**" in s
    assert "terminal_high_high_resonance_curvature_gain" in s
    assert "lambda_{\\mathrm{search}}" in s
    assert "\\lambda_{\\mathrm{search}} > 0" in s
    assert "Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain" in s
