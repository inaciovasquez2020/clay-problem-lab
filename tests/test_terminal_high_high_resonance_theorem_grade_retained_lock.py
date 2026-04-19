from pathlib import Path

def test_terminal_high_high_resonance_theorem_grade_retained_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'patch_ok = abs(eta) >= 2.0 ** (-k)' in s
    assert 'nontrivial_ok = transverse_gap >= 2.0 ** (-(k + 2))' in s
    assert 'theorem_grade_bounds = abs(xi) >= 2.0 ** (-k) and abs(parallel_eta) >= 2.0 ** (-k)' in s
