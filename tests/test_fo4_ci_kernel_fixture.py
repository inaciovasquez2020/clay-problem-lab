from pathlib import Path
import json
import math

def test_fo4_ci_kernel_fixture():
    p = Path("fixtures/fo4/ci_kernel_config.json")
    data = json.loads(p.read_text())
    assert data["R_formula"] == "3*l_avg"
    assert data["delta_sep_formula"] == "2*pi/Lambda"
    assert data["l_avg"] > 0
    assert data["Lambda"] > 0
    R = 3 * data["l_avg"]
    delta_sep = 2 * math.pi / data["Lambda"]
    assert R > 0
    assert delta_sep > 0
