#!/usr/bin/env zsh
set -euo pipefail

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "usage: $0 SPEC_JSON [OUT_MD]" >&2
  exit 2
fi

SPEC="$1"
OUT="${2:-artifacts/audit/completion_truth_report.md}"

if [ ! -f "$SPEC" ]; then
  echo "missing spec: $SPEC" >&2
  exit 2
fi

python3 artifacts/audit/completion_truth_test.py \
  --spec "$SPEC" \
  --out "$OUT"
