from pathlib import Path
import json
import math

def entropy(x):
    from math import log
    s = sum(x)
    probs = [v / s for v in x if v > 0]
    return -sum(p * log(p, 2) for p in probs)

def transcript_capacity(x):
    return len(tuple(round(v, 6) for v in x))

def obstruction_class(x):
    return 0 if max(x) - min(x) < 1e-9 else 1

def T_R(x, eta):
    mean = sum(x) / len(x)
    return [(1 - eta) * v + eta * mean for v in x]

def test_fo4_eta_tightening_gate():
    data = json.loads(Path("fixtures/fo4/ci_kernel_config.json").read_text())
    eta = data["eta"]
    family = [
        [9.0, 1.0, 1.0, 1.0],
        [8.0, 2.0, 1.0, 1.0],
        [5.0, 1.0, 1.0, 1.0],
    ]
    need_smaller_eta = False
    for x in family:
        y = T_R(x, eta)
        dH = entropy(x) - entropy(y)
        dTC = transcript_capacity(y) - transcript_capacity(x)
        preserved = ((obstruction_class(y) != 0) == (obstruction_class(x) != 0))
        if abs(dH) > 1.0 or dTC > 1.0 or not preserved:
            need_smaller_eta = True
    # Current eta is admissible iff no stress failure occurred.
    assert need_smaller_eta is False
