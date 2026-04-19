from pathlib import Path
import json

def test_terminal_high_high_resonance_open_gate_lock() -> None:
    p = Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json")
    d = json.loads(p.read_text())
    assert d["missing_input"] == "Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain"
    assert d["status"] == "OPEN"
