from pathlib import Path

def test_exact_ddyo_symbol_curvature_lemma_finish_condition_lock() -> None:
    s = Path("docs/math/EXACT_DDYO_SYMBOL_CURVATURE_LEMMA.md").read_text()
    assert "## Status" in s
    assert "OPEN" in s
    assert "lambda_{\\mathrm{search}} > 0" in s
    assert "uniform positive lower bound" in s
    assert "No further theorem-level progress is possible without a new invariant, estimate, or exact formula" in s
