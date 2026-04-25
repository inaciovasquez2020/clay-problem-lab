#!/usr/bin/env python3
import subprocess

COMMANDS = [
    ["python3", "tools/verify_ra1n_packet_exhaustion_certificate.py"],
    ["python3", "tools/verify_ra1n_gram_transversality_certificate.py"],
    ["python3", "tools/verify_ra1n_projection_error_domination_certificate.py"],
    ["python3", "tools/verify_ra1n_certified_closure_registry.py"],
    ["python3", "tools/verify_ra1n_all_certified_surfaces.py"],
    ["python3", "tools/verify_ra1n_certified_status_truth.py"],
]

def main() -> int:
    for cmd in COMMANDS:
        subprocess.run(cmd, check=True)
    print("RA1n certified conditional pipeline verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
