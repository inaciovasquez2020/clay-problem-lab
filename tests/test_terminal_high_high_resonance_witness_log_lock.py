from pathlib import Path
import json

def test_terminal_high_high_resonance_witness_log_lock() -> None:
    p = Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json")
    d = json.loads(p.read_text())
    w = d["maximizing_witness_log"]
    assert "F_k_xi_eta" in w
    assert "F_k_xi_parallel" in w
    assert "D_kplus1_xi_eta" in w
    assert "D_kplus1_xi_parallel" in w
    assert w["chi_k_xi_plus_eta"] != 0.0
    assert w["kappa_rank_defect_xi_eta"] != 0.0

def test_terminal_high_high_resonance_zero_witness_log_lock() -> None:
    p = Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json")
    d = json.loads(p.read_text())
    z = d.get("first_zero_witness", {})
    assert isinstance(z, dict)
