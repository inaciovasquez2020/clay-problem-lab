from pathlib import Path
import json

def test_terminal_high_high_resonance_issue_output_lock() -> None:
    p = Path("artifacts/terminal_high_high_resonance_curvature_gain/issue_012.json")
    d = json.loads(p.read_text())
    assert d["issue"] == "simulation_cannot_upgrade_placeholder_to_theorem_without_exact_symbol_curvature_lemma"
    assert d["needed_information"]["name"] == "Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain"
    assert d["needed_information"]["reduction_doc"] == "docs/math/RA1N_TERMINAL_REDUCTION_TO_EXACT_SYMBOL_CURVATURE_LEMMA.md"
