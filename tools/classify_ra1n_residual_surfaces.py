#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOTS = [Path("docs/math"), Path("docs/status")]
OUT = Path("artifacts/ra1n_residual_surface_classification.json")

PATTERNS = {
    "unary": [
        "r_k(ξ)",
        "r_k(\\xi)",
        "r_k = \\widehat G_k",
        "r_k=\\widehat G_k",
        "\\widehat G_k(ξ)",
        "\\widehat G_k(\\xi)",
        "P_k\\widehat G_k(ξ)",
        "P_k\\widehat G_k(\\xi)",
    ],
    "binary": [
        "r_k(ξ,η)",
        "r_k(\\xi,\\eta)",
        "r_k(η,ζ)",
        "r_k(\\eta,\\zeta)",
    ],
    "ternary": [
        "r_k(ξ,η,ζ)",
        "r_k(\\xi,\\eta,\\zeta)",
    ],
    "transverse_high_high": [
        "transverse",
        "high-high",
        "ξ ∥ η",
        "\\xi\\parallel\\eta",
        "\\xi \\parallel \\eta",
        "\\xi\\wedge\\eta",
        "\\xi \\wedge \\eta",
    ],
    "sampled_surrogate": [
        "sampled",
        "surrogate",
        "periodic sampled",
    ],
    "conditional_symbolic": [
        "(1−P_k",
        "(1-P_k",
        "conditional",
        "CONDITIONAL",
    ],
}

def classify(text: str) -> list[str]:
    hits: list[str] = []
    for label, patterns in PATTERNS.items():
        if any(pattern in text for pattern in patterns):
            hits.append(label)
    return hits

def main() -> int:
    records = []
    for root in ROOTS:
        for path in sorted(root.rglob("*.md")):
            text = path.read_text(errors="ignore")
            if "r_k" not in text and "RA1n" not in text and "RA1N" not in text:
                continue
            labels = classify(text)
            if labels:
                records.append({
                    "path": str(path),
                    "labels": labels,
                })

    summary = {}
    for record in records:
        for label in record["labels"]:
            summary[label] = summary.get(label, 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "status": "classification_only",
        "closure_claim": False,
        "canonical_unary_surface": r"r_k(ξ)=\widehat G_k(ξ)−P_k\widehat G_k(ξ)",
        "summary": summary,
        "records": records,
    }, indent=2, sort_keys=True) + "\n")

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
