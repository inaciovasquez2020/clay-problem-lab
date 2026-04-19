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
    "witness_shell": data["witness_shell"]
}, indent=2))
PY
