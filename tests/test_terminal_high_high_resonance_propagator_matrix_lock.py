from pathlib import Path

def test_terminal_high_high_resonance_propagator_matrix_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'def green_hat(vec: tuple[float, float, float]) -> float:' in s
    assert 'def sup_green_hat_k(k: int) -> float:' in s
    assert 'def sigma_eff(k: int, nu: float = 1.0) -> float:' in s
    assert 'def interaction_matrix(' in s
