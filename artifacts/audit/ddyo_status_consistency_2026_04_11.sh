#!/usr/bin/env zsh
set -euo pipefail

bad="$(mktemp)"
good="$(mktemp)"
trap 'rm -f "$bad" "$good"' EXIT

rg -n   -e 'VERIFIED via RA1n'   -e 'continuum DDYO high-high absorbability: VERIFIED'   -e 'RA1n verified via Bernstein Extraction'   docs/math/DDYO*   docs/status/DDYO*   docs/math/BRANCH_B*   docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md > "$bad" || true

rg -n   -e 'ZZZ_DISABLED_OLD_OPEN_MARKERS'   docs/math/DDYO*   docs/status/DDYO* > "$good" || true

if [ -s "$bad" ]; then
  echo "DDYO_STATUS_CONSISTENCY: FAIL"
  cat "$bad"
  exit 1
fi

echo "DDYO_STATUS_CONSISTENCY: PASS"
echo
echo "EXPECTED_OPEN_FRONTIER_MARKERS:"
cat "$good"
