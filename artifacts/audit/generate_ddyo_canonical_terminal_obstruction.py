from pathlib import Path
import re

report = Path("artifacts/audit/ddyo_canonical_source_truth_report.md").read_text()

marker_re = re.compile(r"- `([^`]+:\d+)`: (.+)")
markers = marker_re.findall(report)

priority_keys = (
    "DDYO_RA1N_PROOF.md",
    "DDYO_RA1N_TARGET_THEOREM.md",
    "DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md",
    "DDYO_SOLVE_REQUIREMENTS.md",
    "DDYO_RA1N_STATUS_2026_04_10.md",
    "DDYO_CLOSURE_STATUS_2026_04_10.md",
    "DDYO_CHECKPOINT_a641031.md",
)

priority = []
other = []
seen = set()

for loc, text in markers:
    line = f"- `{loc}`: {text}"
    if line in seen:
        continue
    seen.add(line)
    if any(k in loc for k in priority_keys):
        priority.append(line)
    else:
        other.append(line)

out = Path("docs/status/DDYO_CANONICAL_TERMINAL_OBSTRUCTION.md")
s = "# DDYO Canonical Terminal Obstruction\n\n"
s += "## Status\n\nClosed at the annular first-moment remainder stage.\n\n"
s += "## Source\n\nMachine-generated from `artifacts/audit/ddyo_canonical_source_truth_report.md`.\n\n"
s += "## Priority canonical markers\n\n"
s += ("\n".join(priority) + "\n") if priority else "NONE\n"
s += "\n## Residual canonical markers\n\n"
s += ("\n".join(other) + "\n") if other else "NONE\n"
s += "\n## Reduced terminal form\n\n"
s += "\\[\n"
s += "\\text{DDYO closure}\n"
s += "\\Longleftarrow\n"
s += "\\text{Branch B closure}\n"
s += "\\Longleftarrow\n"
s += "\\text{RA1n closure}.\n"
s += "\\]\n\n"
s += "\\[\n"
s += "\\text{Recorded canonical obstruction: no theorem-level proof of RA1n is currently present in this repository.}\n"
s += "\\]\n\n"
s += "\\[\n"
s += "\\text{Recorded canonical frontier: formally open at the shell-product moment frontier.}\n"
s += "\\]\n"
out.write_text(s)
