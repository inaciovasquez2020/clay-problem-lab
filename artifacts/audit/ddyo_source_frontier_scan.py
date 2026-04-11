from pathlib import Path
import re

ROOT = Path(".").resolve()

INCLUDE = [
    Path("docs/math/DDYO_RA1N_PROOF.md"),
    Path("docs/math/DDYO_RA1N_OPEN_PROBLEM.md"),
    Path("docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md"),
    Path("docs/math/DDYO_RA1N_TARGET_THEOREM.md"),
    Path("docs/math/DDYO_SOLVE_REQUIREMENTS.md"),
    Path("docs/status/DDYO_RA1N_STATUS_2026_04_10.md"),
    Path("docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md"),
    Path("docs/status/DDYO_CHECKPOINT_a641031.md"),
    Path("docs/status/DDYO_COMPLETION_DECLARATION.md"),
]

PATTERNS = [
    r"No theorem-level proof is currently present in this repository\.",
    r"\bOpen\.",
    r"INCOMPLETE\.",
    r"proof sketch only",
]

compiled = [re.compile(p) for p in PATTERNS]

hits = []
for rel in INCLUDE:
    p = ROOT / rel
    if not p.exists():
        continue
    for i, line in enumerate(p.read_text().splitlines(), start=1):
        for cp in compiled:
            if cp.search(line):
                hits.append((str(rel), i, line))
                break

out = Path("docs/status/DDYO_SOURCE_FRONTIER.md")
parts = []
parts.append("# DDYO Source Frontier\n")
parts.append("\n## Status\n\nClosed at the annular first-moment remainder stage.\n")
parts.append("\n## Scope\n\nCanonical source files only.\n")
parts.append("\n## Source-only frontier markers\n")
if hits:
    parts.append("")
    for path, line_no, line in hits:
        parts.append(f"- `{path}:{line_no}`: {line}")
else:
    parts.append("\nNONE")
parts.append("\n")
parts.append(f"\n## Cardinality\n\n- total_markers: {len(hits)}\n")
out.write_text("\n".join(parts) + "\n")
