from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(".").resolve()
LOGDIR = ROOT / "artifacts" / "max_fight"
LOGDIR.mkdir(parents=True, exist_ok=True)

EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    "node_modules",
    "dist",
    "build",
    "artifacts",
    ".lake",
}

RUN_KEYWORDS = {
    "sim",
    "simulate",
    "simulation",
    "sweep",
    "counterexample",
    "proxy",
    "verify",
    "verification",
    "sample",
    "experiment",
    "benchmark",
}

SAFE_FORMATTERS = [
    ["ruff", "check", "--fix", "."],
    ["ruff", "format", "."],
    ["black", "."],
    ["isort", "."],
]


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", text)[:180]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def iter_py_files() -> Iterable[Path]:
    for path in ROOT.rglob("*.py"):
        parts = set(path.parts)
        if parts & EXCLUDE_DIRS:
            continue
        yield path


def has_main_guard(path: Path) -> bool:
    try:
        s = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False
    return "__main__" in s


def is_standalone_candidate(path: Path) -> bool:
    name = path.name.lower()
    parts = [p.lower() for p in path.parts]
    if "tests" in parts:
        return False
    if any(k in name for k in RUN_KEYWORDS):
        return True
    if has_main_guard(path):
        return True
    return False


def run(cmd: list[str], label: str, timeout: int = 600) -> dict:
    log = LOGDIR / f"{slug(label)}.log"
    text = []
    text.append("$ " + " ".join(shlex.quote(c) for c in cmd))
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        )
        text.append("\n[stdout]\n")
        text.append(proc.stdout)
        text.append("\n[stderr]\n")
        text.append(proc.stderr)
        text.append(f"\n[returncode]\n{proc.returncode}\n")
        write_text(log, "".join(text))
        return {
            "label": label,
            "cmd": cmd,
            "returncode": proc.returncode,
            "log": str(log.relative_to(ROOT)),
        }
    except subprocess.TimeoutExpired as e:
        text.append("\n[timeout]\n")
        text.append(f"{timeout}\n")
        text.append("\n[stdout]\n")
        text.append((e.stdout or ""))
        text.append("\n[stderr]\n")
        text.append((e.stderr or ""))
        write_text(log, "".join(text))
        return {
            "label": label,
            "cmd": cmd,
            "returncode": 124,
            "log": str(log.relative_to(ROOT)),
        }
    except Exception as e:
        text.append("\n[exception]\n")
        text.append(repr(e) + "\n")
        write_text(log, "".join(text))
        return {
            "label": label,
            "cmd": cmd,
            "returncode": 1,
            "log": str(log.relative_to(ROOT)),
        }


def phase_commands() -> list[tuple[str, list[str], int]]:
    cmds: list[tuple[str, list[str], int]] = []
    cmds.append(("compileall", [sys.executable, "-m", "compileall", "."], 1200))
    cmds.append(("pytest", [sys.executable, "-m", "pytest", "-q"], 1800))
    cmds.append(
        (
            "unittest_discover",
            [sys.executable, "-m", "unittest", "discover", "-v"],
            1800,
        )
    )
    return cmds


def standalone_commands() -> list[tuple[str, list[str], int]]:
    cmds: list[tuple[str, list[str], int]] = []
    seen: set[Path] = set()
    for path in sorted(iter_py_files()):
        if path in seen:
            continue
        if is_standalone_candidate(path):
            seen.add(path)
            rel = path.relative_to(ROOT)
            if rel.as_posix() == "tools/max_fight.py":
                continue
            cmds.append((f"standalone::{rel}", [sys.executable, str(rel)], 300))
    return cmds


def apply_safe_formatters() -> list[dict]:
    out = []
    for cmd in SAFE_FORMATTERS:
        if have(cmd[0]):
            out.append(run(cmd, f"autofix::{cmd[0]}", timeout=1800))
    return out


def normalize_newlines_and_trailing_space() -> None:
    for path in iter_py_files():
        try:
            s = path.read_text(encoding="utf-8")
        except Exception:
            continue
        s2 = s.replace("\r\n", "\n")
        s2 = "\n".join(line.rstrip() for line in s2.split("\n"))
        if s2 != s:
            path.write_text(s2, encoding="utf-8")


def main() -> int:
    normalize_newlines_and_trailing_space()

    all_results: list[dict] = []
    rounds = []

    initial = []
    for label, cmd, timeout in phase_commands():
        initial.append(run(cmd, label, timeout))
    for label, cmd, timeout in standalone_commands():
        initial.append(run(cmd, label, timeout))
    all_results.extend(initial)
    rounds.append({"round": "initial", "results": initial})

    initial_failures = [r for r in initial if r["returncode"] != 0]

    autofix = []
    if initial_failures:
        autofix = apply_safe_formatters()
        all_results.extend(autofix)
        rounds.append({"round": "autofix", "results": autofix})

        retry = []
        for label, cmd, timeout in phase_commands():
            retry.append(run(cmd, f"retry::{label}", timeout))
        for label, cmd, timeout in standalone_commands():
            retry.append(run(cmd, f"retry::{label}", timeout))
        all_results.extend(retry)
        rounds.append({"round": "retry", "results": retry})

    summary = {
        "cwd": str(ROOT),
        "initial_failures": [r["label"] for r in initial_failures],
        "all_results": all_results,
        "remaining_failures": [
            r["label"]
            for r in all_results
            if r["label"].startswith("retry::") and r["returncode"] != 0
        ]
        or [r["label"] for r in initial if r["returncode"] != 0 and not autofix],
    }
    write_text(LOGDIR / "summary.json", json.dumps(summary, indent=2))
    write_text(
        LOGDIR / "SUMMARY.txt",
        "\n".join(
            [f"{r['label']}: rc={r['returncode']} log={r['log']}" for r in all_results]
        )
        + "\n",
    )

    print("=== MAX_FIGHT_SUMMARY ===")
    for r in all_results:
        print(f"{r['label']}: rc={r['returncode']} log={r['log']}")
    print("=== REMAINING_FAILURES ===")
    if summary["remaining_failures"]:
        for x in summary["remaining_failures"]:
            print(x)
    else:
        print("NONE")

    return 0 if not summary["remaining_failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
