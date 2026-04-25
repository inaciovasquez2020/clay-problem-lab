#!/usr/bin/env python3
"""
RA1n numerical transfer sweep.

Status:
    NUMERICAL / NON-PROOF / FRONTIER AID

Runs ra1n_numeric_transfer_probe.run_probe over a finite k-grid.

No theorem-level closure is claimed.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ra1n_numeric_transfer_probe import run_probe


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ks", nargs="+", type=int, default=[4, 6, 8, 10])
    parser.add_argument("--n", type=int, default=257)
    parser.add_argument("--out", default="artifacts/ra1n_numeric/transfer_sweep.json")
    args = parser.parse_args()

    rows = []
    for k in args.ks:
        rows.append(run_probe(args.n, k, "generic"))
        rows.append(run_probe(args.n, k, "even"))

    summary = {
        "status": "NUMERICAL_NON_PROOF",
        "full_ra1n_status": "CONDITIONAL",
        "ks": args.ks,
        "n": args.n,
        "generic_guard_active_all": all(
            row["guard_active"] for row in rows if row["sigma"] == "generic"
        ),
        "generic_projection_success_all": all(
            row["projection_success"] for row in rows if row["sigma"] == "generic"
        ),
        "even_antisymmetry_success_all": all(
            row["relative_antisym_defect"] < 1.0e-12
            for row in rows
            if row["sigma"] == "even"
        ),
        "max_projected_inner_abs": max(float(row["projected_inner_abs"]) for row in rows),
        "max_even_relative_antisym_defect": max(
            float(row["relative_antisym_defect"])
            for row in rows
            if row["sigma"] == "even"
        ),
        "rows": rows,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
