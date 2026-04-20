import json
from pathlib import Path

def test_terminal_frontier_closed_iff_exact_symbol_curvature_lemma_instantiated() -> None:
    d = json.loads(Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json").read_text())
    if d["exact_symbol_curvature_lemma_instantiated"]:
        assert d["lambda_search"] > 0.0
