import json
import subprocess

with open("framework/problem_registry.json") as f:
    data = json.load(f)

for p in data["problems"]:
    module = p["module"]
    print("Running module:", module)
    subprocess.run(["python3", f"{module}/experiments/core",], check=False)
