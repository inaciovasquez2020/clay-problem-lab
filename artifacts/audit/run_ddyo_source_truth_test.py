from pathlib import Path
import re
import sys
from datetime import datetime, timezone

CANONICAL = [
    Path("docs/math/DDYO_RA1N_PROOF.md"),
    Path("docs/math/DDYO_RA1N_OPEN_PROBLEM.md"),
    Path("docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md"),
    Path("docs/math/DDYO_RA1N_TARGET_THEOREM.md"),
    Path("docs/math/DDYO_SOLVE_REQUIREMENTS.md"),
    Path("docs/status/DDYO_RA1N_STATUS_2026_04_10.md"),
    Path("docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md"),
    Path("docs/status/DDYO_CHECKPOINT_a641031.md"),
    Path("docs/status/DDYO_COMPLETION_DECLARATION.md"),
    Path("docs/math/DDYO_GJ_EXPLICIT_DEFINITION.md"),
    Path("docs/math/DDYO_GJ_KERNEL_REPRESENTATION.md"),
    Path("docs/math/DDYO_GJ_GRADIENT_PROOF.md"),
]

REQUIRED = [
    ("explicit incomplete declaration", [
        re.compile(r"INCOMPLETE\."),
        re.compile(r"No unconditional closure is declared in this repository\."),
    ]),
    ("explicit theorem missing marker", [
        re.compile(r"No theorem-level proof is currently present in this repository\."),
        re.compile(r"proof sketch only"),
    ]),
    ("open frontier markers present", [
        re.compile(r"No theorem-level proof is currently present in this repository\."),
                        re.compile(r"\bOpen\."),
    ]),
]

FORBIDDEN = [
    ("false completion declaration", re.compile(r"Unconditional closure achieved|Completion status:\s*COMPLETE|\bVERIFIED\b|QED")),
    ("false theorem-complete marker", re.compile(r"Theorem-level proof complete")),
]

OPEN_PAT = re.compile(r"ZZZ_DISABLED_OLD_OPEN_MARKERS")
CLOSED_PAT = re.compile(r"Unconditional closure achieved|Completion status:\s*COMPLETE|Theorem-level proof complete|\bVERIFIED\b|QED")

def read_lines(path: Path):
    try:
        return path.read_text().splitlines()
    except FileNotFoundError:
        return []

def find_matches(rx):
    hits = []
    for p in CANONICAL:
        for i, line in enumerate(read_lines(p), start=1):
            if rx.search(line):
                hits.append((p.as_posix(), i, line))
    return hits

def fmt_hits(hits):
    if not hits:
        return "NONE\n"
    return "".join(f"- `{p}:{i}`: {line}\n" for p, i, line in hits)

sections = []
verdict = "PASS"

sections.append("# DDYO Canonical Source Truth Test\n")
sections.append(f"- UTC: {datetime.now(timezone.utc).isoformat()}\n")
sections.append("- Scope files: {}\n".format(len(CANONICAL)))
sections.append("\n## Canonical source set\n")
for p in CANONICAL:
    sections.append(f"- `{p.as_posix()}`\n")

sections.append("\n## Required markers\n")
for label, regs in REQUIRED:
    all_hits = []
    ok = True
    for rx in regs:
        hits = find_matches(rx)
        all_hits.extend(hits)
        if not hits:
            ok = False
    sections.append(f"\n### {label}\n")
    sections.append("PASS\n" if ok else "FAIL\n")
    sections.append(fmt_hits(all_hits))
    if not ok:
        verdict = "FAIL"

sections.append("\n## Forbidden markers\n")
for label, rx in FORBIDDEN:
    hits = find_matches(rx)
    ok = not hits
    sections.append(f"\n### {label}\n")
    sections.append("PASS\n" if ok else "FAIL\n")
    sections.append(fmt_hits(hits))
    if not ok:
        verdict = "FAIL"

sections.append("\n## Mixed-state contradictions\n")
mixed = []
for p in CANONICAL:
    lines = read_lines(p)
    has_open = any(OPEN_PAT.search(line) for line in lines)
    has_closed = any(CLOSED_PAT.search(line) for line in lines)
    if has_open and has_closed:
        mixed.append((p.as_posix(), 0, "contains both open and closed state markers"))
ok = not mixed
sections.append("\n### simultaneous incomplete and complete markers in canonical source scope\n")
sections.append("PASS\n" if ok else "FAIL\n")
sections.append(fmt_hits(mixed))
if not ok:
    verdict = "FAIL"

sections.append("\n## Verdict\n\n")
sections.append(f"CANONICAL_SOURCE_TRUTH_TEST: {verdict}\n")

out = Path("artifacts/audit/ddyo_canonical_source_truth_report.md")
out.write_text("".join(sections))
print(out.as_posix())
print(f"CANONICAL_SOURCE_TRUTH_TEST: {verdict}")
