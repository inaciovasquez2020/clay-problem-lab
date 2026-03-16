import subprocess
from pathlib import Path

modules = [
    "riemann",
    "navier_stokes",
    "yang_mills",
    "complexity",
    "bsd",
    "hodge"
]

def test_module_runs():
    for m in modules:
        exp = Path(m) / "experiments/core"
        if not exp.exists():
            continue
        for f in exp.glob("*.py"):
            print("testing", f)
            subprocess.run(["python3", str(f)], check=True)

if __name__ == "__main__":
    test_module_runs()
