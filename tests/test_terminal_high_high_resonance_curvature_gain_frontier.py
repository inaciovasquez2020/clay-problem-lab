from pathlib import Path
import json

def test_symbol_assumption_lock() -> None:
    s = Path("docs/math/TERMINAL_HIGH_HIGH_RESONANCE_SYMBOL_ASSUMPTION.md").read_text()
    assert "exact closed-form formula" in s or "exact closed-form" in s
    assert "|r_k(\\xi,\\eta)|\\ge c\\,2^{-\\alpha k}|\\xi\\wedge\\eta|^2" in s

def test_frontier_simulator_writes_summary() -> None:
    p = Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json")
    assert p.exists()
    data = json.loads(p.read_text())
    assert data["obstruction"] == "terminal_high_high_resonance_curvature_gain"
    assert data["missing_input"] == "Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain"
    assert data["status"] == "OPEN"
