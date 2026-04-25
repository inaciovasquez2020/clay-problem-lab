#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECK_DIRS = [
    ROOT / "docs/math",
    ROOT / "docs/status",
]

FORBIDDEN = [
    "Full_RA1n_status: CLOSED",
    "full_ra1n_status: CLOSED",
    "full RA1n is closed",
    "RA1n full promotion is closed unconditionally",
    "unconditional full RA1n closure",
]

REQUIRED = {
    ROOT / "docs/status/RA1N_TERMINAL_FRONTIER_REGISTRY.json": [
        '"full_ra1n_status": "CONDITIONAL"',
        '"unconditional_closure": false',
        '"terminal_frontier": "Weighted Affine-Transfer Cancellation Lemma"',
    ],
    ROOT / "docs/math/RA1N_CONSERVATION_TRANSFER_FRONTIER.md": [
        "Weighted Affine-Transfer Cancellation Lemma",
        r"\Phi_{\xi_{\mathrm{out}}}(\eta)",
        r"F=\frac{\overline g}{\|g\|_2}",
    ],
    ROOT / "docs/status/RA1N_FULL_PROMOTION_STATUS.md": [
        "Full_RA1n_status: CONDITIONAL",
        "Weighted Affine-Transfer Cancellation Lemma",
    ],
}

violations = []

AUDIT_DOC = ROOT / "docs/status/RA1N_UNCONDITIONAL_CLOSURE_AUDIT.md"

for directory in CHECK_DIRS:
    if not directory.exists():
        continue
    for path in directory.rglob("*"):
        if path == AUDIT_DOC:
            continue
        if path.is_file() and path.suffix in {".md", ".json", ".txt"}:
            text = path.read_text(errors="ignore")
            for phrase in FORBIDDEN:
                if phrase in text:
                    violations.append(f"{path.relative_to(ROOT)} contains forbidden phrase: {phrase}")

for path, phrases in REQUIRED.items():
    text = path.read_text(errors="ignore")
    for phrase in phrases:
        if phrase not in text:
            violations.append(f"{path.relative_to(ROOT)} missing required phrase: {phrase}")

if violations:
    raise SystemExit("\n".join(violations))

print("RA1n unconditional closure audit verified")
