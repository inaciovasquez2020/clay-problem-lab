from pathlib import Path

def test_terminal_high_high_resonance_sim_requires_fk() -> None:
    s = Path("navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py").read_text()
    assert 'def F_k(xi: float, eta: float, k: int) -> float:' in s
    assert 'raise NotImplementedError("Provide the explicit closed-form DDYO symbol formula m_k(xi,eta)=F_k(xi,eta).")' in s
