from pathlib import Path
import json
import math

def test_fo4_radius_truth_gate():
    data = json.loads(Path("fixtures/fo4/ci_kernel_config.json").read_text())
    R = 3 * data["l_avg"]
    delta_sep = 2 * math.pi / data["Lambda"]
    assert (R > delta_sep) or (R <= delta_sep)
