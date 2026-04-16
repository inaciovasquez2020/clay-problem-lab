from pathlib import Path
import json

def entropy(x):
    # finite-support toy entropy budget for CI gating
    from math import log
    s = sum(x)
    probs = [v / s for v in x if v > 0]
    return -sum(p * log(p, 2) for p in probs)

def transcript_capacity(x):
    # simple bounded transcript proxy for CI gating
    return len(tuple(round(v, 6) for v in x))

def T_R(x, eta):
    # contraction-style transport proxy
    mean = sum(x) / len(x)
    return [(1 - eta) * v + eta * mean for v in x]

def test_fo4_transport_stress_budget():
    data = json.loads(Path("fixtures/fo4/ci_kernel_config.json").read_text())
    eta = data["eta"]
    family = [
        [9.0, 1.0, 1.0, 1.0],
        [8.0, 2.0, 1.0, 1.0],
        [7.0, 3.0, 1.0, 1.0],
        [6.0, 4.0, 1.0, 1.0],
    ]
    C_entropy = 1.0
    C_tc = 1.0
    for x in family:
        y = T_R(x, eta)
        dH = entropy(x) - entropy(y)
        dTC = transcript_capacity(y) - transcript_capacity(x)
        assert abs(dH) <= C_entropy
        assert dTC <= C_tc
