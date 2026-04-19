from pathlib import Path
import json

def test_terminal_high_high_resonance_lambda_search_lock() -> None:
    p = Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json")
    d = json.loads(p.read_text())
    assert d["lambda_search"] == 0.0
