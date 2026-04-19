from pathlib import Path

def test_terminal_high_high_resonance_eigen_lock() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'def eigenvalue_pair_vieta(' in s
    assert 'def kappa_rank_defect(' in s
