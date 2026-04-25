#!/usr/bin/env python3
from pathlib import Path

REQUIRED = [
    "docs/math/RA1N_TERMINAL_ADMISSIBILITY_ANNIHILATOR_SATURATION_THEOREM.md",
    "docs/math/RA1N_TERMINAL_ADMISSIBILITY_WEAK_ORTHOGONALITY_THEOREM.md",
    "docs/math/RA1N_WEAK_ORTHOGONALITY_FROM_RESIDUAL_NORM_THEOREM.md",
    "docs/math/RA1N_TERMINAL_RESIDUAL_VANISHING_FROM_ADMISSIBILITY_THEOREM.md",
    "docs/math/RA1N_ADMISSIBILITY_RESIDUAL_SATURATION_AXIOM.md",
    "docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md",
]

def require(path: str, needle: str) -> None:
    text = Path(path).read_text()
    assert needle in text, f"{needle!r} missing from {path}"

def main() -> int:
    for path in REQUIRED:
        assert Path(path).exists(), f"missing {path}"

    require("docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md", "Status: FRONTIER CHAIN")
    require("docs/status/RA1N_TERMINAL_FRONTIER_CHAIN.md", "residual-defect saturation")
    require("docs/math/RA1N_ADMISSIBILITY_RESIDUAL_SATURATION_AXIOM.md", "Status: OPEN STRUCTURAL AXIOM")
    require("docs/math/RA1N_TERMINAL_RESIDUAL_VANISHING_FROM_ADMISSIBILITY_THEOREM.md", "Status: CONDITIONAL STRUCTURAL THEOREM")

    print("RA1n terminal frontier chain verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
