#!/usr/bin/env zsh
set -euo pipefail
rg -n   -e 'VERIFIED via RA1n'   -e 'continuum DDYO high-high absorbability: VERIFIED'   -e 'RA1n verified via Bernstein Extraction'   -e 'No theorem-level proof is currently present in this repository'   -e 'Formally conditional on RA1n'   -e 'Formally open at the shell-product moment frontier'   docs/math/DDYO*   docs/status/DDYO*   docs/math/BRANCH_B*   docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md
