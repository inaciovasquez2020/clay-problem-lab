from pathlib import Path

def test_terminal_high_high_resonance_dj_fk_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'def D_j(' in s
    assert 'def F_k(' in s
    assert 'tail = (1.0 / 7.0) * D_j(xi, eta, k + 1)' in s
