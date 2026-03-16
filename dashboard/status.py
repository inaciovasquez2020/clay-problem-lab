import json
from pathlib import Path

modules = [
    "riemann",
    "navier_stokes",
    "yang_mills",
    "complexity",
    "bsd",
    "hodge"
]

status = []

for m in modules:
    exp = Path(m) / "experiments/core"
    scripts = list(exp.glob("*.py")) if exp.exists() else []
    status.append({
        "module": m,
        "experiments": len(scripts)
    })

print("Clay Problem Lab Status")
print("-----------------------")

for s in status:
    print(f"{s['module']}: {s['experiments']} experiments")
