#!/usr/bin/env python3
from pathlib import Path

CERTIFIED_CONDITIONAL_DOCS = [
    "docs/math/RA1N_ANGLE_GAP_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md",
    "docs/math/RA1N_POSITIVE_TRANSFER_CERTIFIED_CLOSER.md",
    "docs/math/RA1N_PROJECTION_ERROR_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md",
]

REGISTRY = "docs/status/RA1N_CERTIFIED_CLOSURE_REGISTRY.md"

FORBIDDEN_UNCONDITIONAL_PHRASES = [
    "Status: PROVED UNCONDITIONALLY",
    "Status: UNCONDITIONAL THEOREM",
    "unconditionally closed",
    "unrestricted RA1n is proved unconditionally",
    "full RA1n solved unconditionally",
]

REQUIRED_CONDITIONAL_MARKERS = [
    "Status: CERTIFIED CONDITIONAL THEOREM",
]

def require(path: str, needle: str) -> None:
    text = Path(path).read_text()
    assert needle in text, f"{needle!r} missing from {path}"

def forbid(path: str, needle: str) -> None:
    text = Path(path).read_text()
    assert needle not in text, f"forbidden overclaim {needle!r} found in {path}"

def main() -> int:
    for path in CERTIFIED_CONDITIONAL_DOCS:
        assert Path(path).exists(), f"missing certified conditional RA1n doc: {path}"
        for marker in REQUIRED_CONDITIONAL_MARKERS:
            require(path, marker)
        for phrase in FORBIDDEN_UNCONDITIONAL_PHRASES:
            forbid(path, phrase)

    assert Path(REGISTRY).exists(), f"missing registry: {REGISTRY}"
    require(REGISTRY, "Status: CERTIFIED CONDITIONAL THEOREM REGISTRY")
    require(REGISTRY, "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}")
    require(REGISTRY, "c_{\\mathrm{RA1n}}=2")

    for phrase in FORBIDDEN_UNCONDITIONAL_PHRASES:
        forbid(REGISTRY, phrase)

    print("RA1n certified status truth guard verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
