from pathlib import Path

def test_terminal_high_high_resonance_eta_parallel_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'def eta_parallel(xi: float, eta: float) -> float:' in s
    assert 'return xi' in s
