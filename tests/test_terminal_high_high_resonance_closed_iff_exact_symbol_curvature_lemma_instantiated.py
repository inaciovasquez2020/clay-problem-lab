from pathlib import Path
import json

def test_terminal_high_high_resonance_closed_iff_exact_symbol_curvature_lemma_instantiated() -> None:
    p = Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json")
    d = json.loads(p.read_text())
    assert (d["status"] == "CLOSED") == (
        d["exact_symbol_curvature_lemma_instantiated"] and d["lambda_search"] > 0.0
    )
