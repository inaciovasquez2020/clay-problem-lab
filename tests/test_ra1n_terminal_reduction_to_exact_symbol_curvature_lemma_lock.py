from pathlib import Path

def test_ra1n_terminal_reduction_to_exact_symbol_curvature_lemma_lock() -> None:
    s = Path("docs/math/RA1N_TERMINAL_REDUCTION_TO_EXACT_SYMBOL_CURVATURE_LEMMA.md").read_text()
    assert "## Status" in s
    assert "CONDITIONAL" in s
    assert "terminal_high_high_resonance_curvature_gain is discharged" in s
    assert "status from OPEN to CLOSED" in s
