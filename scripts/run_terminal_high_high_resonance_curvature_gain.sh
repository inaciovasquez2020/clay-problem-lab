#!/usr/bin/env bash
set -euo pipefail
python3 navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py
python3 - <<'PY'
from pathlib import Path
import json

p = Path("artifacts/terminal_high_high_resonance_curvature_gain/frontier_summary.json")
data = json.loads(p.read_text())
print(json.dumps({
    "status": data["status"],
    "obstruction": data["obstruction"],
    "missing_input": data["missing_input"],
    "generation": data["generation"],
    "best_score": data["best_score"],
    "witness_xi": data["witness_xi"],
    "witness_eta": data["witness_eta"],
    "witness_shell": data["witness_shell"],
    "lambda_search": data["lambda_search"],
    "exact_symbol_curvature_lemma_instantiated": data["exact_symbol_curvature_lemma_instantiated"]
}, indent=2))
PY
