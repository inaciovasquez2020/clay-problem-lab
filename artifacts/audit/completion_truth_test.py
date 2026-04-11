#!/usr/bin/env python3
import argparse
import glob
import json
import re
import subprocess
import sys
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

def uniq_paths(items):
    out = []
    seen = set()
    for x in items:
        p = str(Path(x))
        if p not in seen:
            seen.add(p)
            out.append(Path(p))
    return out

def expand(patterns):
    hits = []
    for pat in patterns:
        matches = [Path(p) for p in glob.glob(pat, recursive=True)]
        if not matches and Path(pat).exists():
            matches = [Path(pat)]
        for m in matches:
            if m.is_file():
                hits.append(m)
    return uniq_paths(hits)

def read_lines(path):
    try:
        return path.read_text(errors="ignore").splitlines()
    except Exception:
        return []

def grep(pattern, files):
    rx = re.compile(pattern)
    out = []
    for fp in files:
        for i, line in enumerate(read_lines(fp), start=1):
            if rx.search(line):
                out.append((str(fp), i, line.strip()))
    return out

def section(title):
    return ["", f"## {title}", ""]

def trim(s, n=40):
    lines = s.splitlines()
    if len(lines) <= n:
        return s
    return "\n".join(lines[:n] + ["...[truncated]..."])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    spec_path = Path(args.spec)
    out_path = Path(args.out)
    spec = json.loads(spec_path.read_text())

    name = spec.get("name", spec_path.stem)
    scope = expand(spec.get("scope", []))

    ok = True
    report = [
        f"# {name}",
        "",
        f"- UTC: {datetime.now(timezone.utc).isoformat()}",
        f"- Spec: `{spec_path}`",
        f"- Scope files: {len(scope)}",
        ""
    ]

    report += section("Required files")
    missing = []
    for item in spec.get("must_exist", []):
        if not Path(item).exists():
            missing.append(item)
    if missing:
        ok = False
        report.append("FAIL")
        for item in missing:
            report.append(f"- missing: `{item}`")
    else:
        report.append("PASS")

    report += section("Required commands")
    for cmd in spec.get("must_run", []):
        proc = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        report.append(f"### `{cmd}`")
        report.append(f"- rc: {proc.returncode}")
        if proc.stdout.strip():
            report.append("")
            report.append("```text")
            report.append(trim(proc.stdout))
            report.append("```")
        if proc.stderr.strip():
            report.append("")
            report.append("```text")
            report.append(trim(proc.stderr))
            report.append("```")
        if proc.returncode != 0:
            ok = False

    report += section("Required markers")
    for rule in spec.get("must_find", []):
        label = rule["label"]
        paths = expand(rule.get("paths", spec.get("scope", [])))
        hits = grep(rule["pattern"], paths)
        report.append(f"### {label}")
        if hits:
            report.append("PASS")
            for fp, ln, text in hits[:20]:
                report.append(f"- `{fp}:{ln}`: {text}")
        else:
            ok = False
            report.append("FAIL")

    report += section("Forbidden markers")
    for rule in spec.get("must_not_find", []):
        label = rule["label"]
        paths = expand(rule.get("paths", spec.get("scope", [])))
        hits = grep(rule["pattern"], paths)
        report.append(f"### {label}")
        if hits:
            ok = False
            report.append("FAIL")
            for fp, ln, text in hits[:40]:
                report.append(f"- `{fp}:{ln}`: {text}")
        else:
            report.append("PASS")

    report += section("Mixed-state contradictions")
    for rule in spec.get("forbid_mixed_states", []):
        label = rule["label"]
        paths = expand(rule.get("paths", spec.get("scope", [])))
        open_hits = grep(rule["open_pattern"], paths)
        closed_hits = grep(rule["closed_pattern"], paths)
        report.append(f"### {label}")
        if open_hits and closed_hits:
            ok = False
            report.append("FAIL")
            report.append("#### open")
            for fp, ln, text in open_hits[:20]:
                report.append(f"- `{fp}:{ln}`: {text}")
            report.append("#### closed")
            for fp, ln, text in closed_hits[:20]:
                report.append(f"- `{fp}:{ln}`: {text}")
        else:
            report.append("PASS")

    report += section("Verdict")
    report.append("COMPLETION_TRUTH_TEST: PASS" if ok else "COMPLETION_TRUTH_TEST: FAIL")

    out_path.write_text("\n".join(report) + "\n")
    print(out_path.read_text())
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
