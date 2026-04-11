import subprocess
import sys
import json
from pathlib import Path

REGISTRY = Path("framework/problem_registry.json")


def load_registry():
    with open(REGISTRY) as f:
        return json.load(f)["problems"]


def list_problems():
    for p in load_registry():
        print(p["module"], "-", p["name"])


def run_problem(module):
    exp = Path(module) / "experiments/core"
    if not exp.exists():
        print("no experiments found for", module)
        return
    for f in exp.glob("*.py"):
        print("running", f)
        subprocess.run(["python3", str(f)])


def main():
    if len(sys.argv) < 2:
        print("usage: clay list | clay run <module>")
        return

    cmd = sys.argv[1]

    if cmd == "list":
        list_problems()

    elif cmd == "run":
        if len(sys.argv) < 3:
            print("specify module")
            return
        run_problem(sys.argv[2])


if __name__ == "__main__":
    main()
