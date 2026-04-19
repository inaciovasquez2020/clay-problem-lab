from pathlib import Path

def test_terminal_high_high_resonance_bump_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'def h_transition(x: float) -> float:' in s
    assert 'def phi_bump(r: float) -> float:' in s
    assert 'def chi_k(vec: tuple[float, float, float], k: int) -> float:' in s
