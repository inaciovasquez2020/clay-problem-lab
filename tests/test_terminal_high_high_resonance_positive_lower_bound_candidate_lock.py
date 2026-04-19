from pathlib import Path

def test_terminal_high_high_resonance_positive_lower_bound_candidate_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'positive_lower_bound_candidate = max(0.0, min(curvature_lower_bound, transverse_gap * max(abs(derivative), 0.0)))' in s
    assert '"positive_lower_bound_candidate": positive_lower_bound_candidate' in s
