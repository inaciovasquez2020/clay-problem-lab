#!/usr/bin/env python3
from pathlib import Path

FORBIDDEN = [
    "Terminal Generator Classification Theorem: PROVED",
    "RA1n theorem-level closure: PROVED",
    "Navier-Stokes solved",
    "Navier--Stokes solved",
    "Clay problem solved",
]

REQUIRED_OPEN = [
    "docs/math/RA1N_ADMISSIBILITY_RESIDUAL_SATURATION_AXIOM.md",
    "docs/status/RA1N_THEOREM_LEVEL_STOP_RULE.md",
    "docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md",
]

def main() -> int:
    for path in REQUIRED_OPEN:
        text = Path(path).read_text()
        for bad in FORBIDDEN:
            assert bad not in text, f"forbidden overclaim {bad!r} in {path}"

    stop = Path("docs/status/RA1N_THEOREM_LEVEL_STOP_RULE.md").read_text()
    assert "No further progress possible without new input." in stop
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in stop
    assert "\\mathcal R_{\\mathrm{term}}(\\chi)=0" in stop

    print("RA1n no-overclaim frontier verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
