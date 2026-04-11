from pathlib import Path
import re

report = Path("artifacts/audit/ddyo_open_truth_report.md").read_text()

m = re.search(
    r"### open frontier markers present\nPASS\n(?P<body>(?:- `.*\n)+)",
    report
)
body = m.group("body") if m else ""

markers = [line.strip() for line in body.splitlines() if line.strip().startswith("- `")]

priority_keys = (
    "GRADIENT_BOUND",
    "GJ_",
    "G_j",
    "RA1N",
    "TERMINAL_OBSTRUCTION",
    "SHELL_PRODUCT",
    "SOLVE_REQUIREMENTS",
    "CLOSURE_STATUS",
    "CHECKPOINT_a641031",
)

priority = []
other = []
seen = set()

for line in markers:
    if line in seen:
        continue
    seen.add(line)
    if any(key in line for key in priority_keys):
        priority.append(line)
    else:
        other.append(line)

out = Path("docs/status/DDYO_TERMINAL_FRONTIER_CORE.md")
text = "# DDYO Terminal Frontier Core\n\n"
text += "## Status\n\n"
text += "Open.\n\n"
text += "## Source\n\n"
text += "Machine-generated from `artifacts/audit/ddyo_open_truth_report.md`.\n\n"
text += "## Priority terminal markers\n\n"
text += (("\n".join(priority) + "\n") if priority else "NONE\n")
text += "\n## Residual open markers\n\n"
text += (("\n".join(other) + "\n") if other else "NONE\n")
text += f"\n## Cardinalities\n\n- priority_markers: {len(priority)}\n- residual_markers: {len(other)}\n- total_markers: {len(priority) + len(other)}\n"
out.write_text(text)
