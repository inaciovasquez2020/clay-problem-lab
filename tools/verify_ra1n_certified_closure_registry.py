#!/usr/bin/env python3
from pathlib import Path
import subprocess

ROOT = Path(".")

REQUIRED_DOCS = [
    "docs/math/RA1N_ANGLE_GAP_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md",
    "docs/math/RA1N_PROJECTION_ERROR_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md",
]

REQUIRED_CERTS = [
    "artifacts/ra1n/gram_transversality_certificate.json",
    "artifacts/ra1n/projection_error_domination_certificate.json",
]

def require(path: str, needle: str) -> None:
    text = Path(path).read_text()
    assert needle in text, f"{needle!r} missing from {path}"

def main() -> int:
    registry = Path("docs/status/RA1N_CERTIFIED_CLOSURE_REGISTRY.md")
    assert registry.exists()

    for path in REQUIRED_DOCS + REQUIRED_CERTS:
        assert Path(path).exists(), f"missing required RA1n closure object: {path}"

    require(str(registry), "Status: CERTIFIED CONDITIONAL THEOREM REGISTRY")
    require(str(registry), "c_{\\mathrm{RA1n}}=2")
    require(str(registry), "\\mathcal T_{\\mathrm{RA1n}}(k)\\ge2>0")

    require("docs/math/RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md", "Status: CERTIFIED CONDITIONAL THEOREM")
    require("docs/math/RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md", "c_{\\mathrm{RA1n}}:=2")
    require("docs/math/RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CLOSURE.md", "certified closed on the finite-basis packet-exhausted surface")
    require("docs/math/RA1N_PROJECTION_ERROR_CERTIFIED_CLOSURE.md", "certified closed by exact rational arithmetic")
    require("docs/math/RA1N_ANGLE_GAP_CERTIFIED_CLOSURE.md", "certified closed on the finite-basis Gram packet surface")

    subprocess.run(["python3", "tools/verify_ra1n_gram_transversality_certificate.py"], check=True)
    subprocess.run(["python3", "tools/verify_ra1n_projection_error_domination_certificate.py"], check=True)

    print("RA1n certified closure registry verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
