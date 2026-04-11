#!/usr/bin/env zsh
set -euo pipefail
rg -n   -e 'verified|VERIFIED'   -e 'proof sketch only'   -e 'No theorem-level proof is currently present in this repository'   -e 'Formally conditional on RA1n'   -e 'Formally open at the shell-product moment frontier'   docs/math docs/status
