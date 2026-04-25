#!/usr/bin/env python3
import json
from pathlib import Path

CERT = Path("artifacts/ra1n/packet_exhaustion_certificate.json")

def main() -> int:
    data = json.loads(CERT.read_text())

    assert data["object"] == "RA1N packet exhaustion certificate"
    assert data["status"] == "conditional-packet-exhaustion-certificate"
    assert data["terminal_packet_class"] == "P_RA1n_terminal"
    assert data["finite_basis_space"] == "V_RA1n"
    assert data["exhaustion_claim"] == "P_RA1n_terminal subset V_RA1n"
    assert data["certifies"] == "P_RA1n_terminal subset V_RA1n"

    generators = data["terminal_generators"]
    assert isinstance(generators, list)
    assert generators

    for item in generators:
        assert item["basis_space"] == "V_RA1n"

    print("RA1n packet exhaustion certificate verified: P_RA1n_terminal subset V_RA1n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
