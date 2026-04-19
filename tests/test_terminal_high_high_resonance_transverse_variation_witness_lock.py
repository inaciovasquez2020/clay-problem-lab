from pathlib import Path

def test_terminal_high_high_resonance_transverse_variation_witness_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'def transverse_variation_nonvanishing(xi: float, eta: float, k: int, h: float = 1.0e-6) -> float:' in s
    assert '"transverse_variation_nonzero": abs(derivative) > 0.0' in s
