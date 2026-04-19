from pathlib import Path

def test_terminal_high_high_resonance_parallel_baseline_identity_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'parallel_eta = eta_parallel(xi, eta)' in s
    assert 'return F_k((xi, 0.0, 0.0), (parallel_eta, 0.0, 0.0), k)' in s
