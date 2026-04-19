from pathlib import Path

def test_symbolic_placeholder_blocked_until_exact_ddyo_symbol_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    t = Path("docs/math/EXACT_DDYO_SYMBOL_CURVATURE_LEMMA.md").read_text()
    assert ("symbolic_placeholder" in s) or ("simulation_cannot_upgrade_placeholder_to_theorem_without_exact_symbol_curvature_lemma" in s)
    assert "OPEN" in t
