#!/usr/bin/env python3
from pathlib import Path
import subprocess

REQUIRED = [
    "docs/math/RA1N_PACKET_EXHAUSTION_CERTIFIED_CLOSURE.md",
    "artifacts/ra1n/packet_exhaustion_certificate.json",
    "tools/verify_ra1n_packet_exhaustion_certificate.py",
    "docs/math/RA1N_ANGLE_GAP_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md",
    "docs/math/RA1N_POSITIVE_TRANSFER_CERTIFIED_CLOSER.md",
    "docs/math/RA1N_PROJECTION_ERROR_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CLOSURE.md",
    "docs/math/RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md",
    "docs/status/RA1N_CERTIFIED_CLOSURE_REGISTRY.md",
    "artifacts/ra1n/gram_transversality_certificate.json",
    "artifacts/ra1n/projection_error_domination_certificate.json",
    "tools/verify_ra1n_gram_transversality_certificate.py",
    "tools/verify_ra1n_projection_error_domination_certificate.py",
    "tools/verify_ra1n_certified_closure_registry.py",
]

NEEDLES = {
    "docs/math/RA1N_PACKET_EXHAUSTION_CERTIFIED_CLOSURE.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}",
        "\\subset",
        "V_{\\mathrm{RA1n}}",
        "Packet exhaustion is certified closed",
    ],
    "docs/math/RA1N_ANGLE_GAP_CERTIFIED_CLOSURE.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "b^*G^{-1}b=0<1",
        "\\epsilon:=1-\\alpha=1",
        "\\int F(\\eta)g(\\eta)\\,d\\eta=0",
    ],
    "docs/math/RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "b^*G^{-1}b=0<1",
        "h\\notin V_{\\mathrm{RA1n}}",
        "\\int Fg=0",
    ],
    "docs/math/RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}",
        "\\epsilon=1",
        "\\int Fg=0",
    ],
    "docs/math/RA1N_POSITIVE_TRANSFER_CERTIFIED_CLOSER.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "c_{\\mathrm{RA1n}}>0",
        "\\mathcal T_{\\mathrm{RA1n}}(k)",
    ],
    "docs/math/RA1N_PROJECTION_ERROR_CERTIFIED_CLOSURE.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "c_{\\mathrm{RA1n}}:=2",
        "certified closed by exact rational arithmetic",
    ],
    "docs/math/RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CLOSURE.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "c_{\\mathrm{RA1n}}:=2",
        "\\mathcal T_{\\mathrm{RA1n}}(k)",
    ],
    "docs/math/RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM",
        "c_{\\mathrm{RA1n}}:=2",
        "\\mathcal T_{\\mathrm{RA1n}}(k)",
    ],
    "docs/status/RA1N_CERTIFIED_CLOSURE_REGISTRY.md": [
        "Status: CERTIFIED CONDITIONAL THEOREM REGISTRY",
        "c_{\\mathrm{RA1n}}=2",
        "\\mathcal T_{\\mathrm{RA1n}}(k)\\ge2>0",
    ],
}

def require(path: str, needle: str) -> None:
    text = Path(path).read_text()
    assert needle in text, f"{needle!r} missing from {path}"

def main() -> int:
    for path in REQUIRED:
        assert Path(path).exists(), f"missing certified RA1n surface object: {path}"

    for path, needles in NEEDLES.items():
        for needle in needles:
            require(path, needle)

    subprocess.run(["python3", "tools/verify_ra1n_packet_exhaustion_certificate.py"], check=True)
    subprocess.run(["python3", "tools/verify_ra1n_gram_transversality_certificate.py"], check=True)
    subprocess.run(["python3", "tools/verify_ra1n_projection_error_domination_certificate.py"], check=True)
    subprocess.run(["python3", "tools/verify_ra1n_certified_closure_registry.py"], check=True)

    print("RA1n all certified surfaces verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
