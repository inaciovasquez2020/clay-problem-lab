from pathlib import Path
import json

def obstruction_class(x):
    # benchmark nontriviality proxy: imbalance survives iff class is nonzero
    return 0 if max(x) - min(x) < 1e-9 else 1

def T_R(x, eta):
    mean = sum(x) / len(x)
    return [(1 - eta) * v + eta * mean for v in x]

def test_fo4_obstruction_preservation_benchmark():
    data = json.loads(Path("fixtures/fo4/ci_kernel_config.json").read_text())
    eta = data["eta"]
    family = [
        [5.0, 1.0, 1.0, 1.0],
        [4.0, 1.0, 1.0, 1.0],
        [3.0, 1.0, 1.0, 1.0],
    ]
    for x in family:
        before = obstruction_class(x)
        after = obstruction_class(T_R(x, eta))
        assert (after != 0) == (before != 0)
