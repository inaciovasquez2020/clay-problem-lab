from pathlib import Path
import json
import subprocess

COERC = json.loads(Path("artifacts/ra1n_ddyo_coercivity/frontier_summary.json").read_text())
BRIDGE = json.loads(Path("artifacts/ra1n_ddyo_pachner_bridge/bridge_summary.json").read_text())
DOC = Path("docs/math/DDYO_PACHNER_SYMBOL_LIFT_FRONTIER.md").read_text()

def test_sigma_lower_formula_literal() -> None:
    assert COERC["sigma_lower_formula"] == "epsilon_gamma**2"

def test_bridge_status_literal() -> None:
    assert BRIDGE["status"] == "CONDITIONAL"

def test_piecewise_rule_and_finish_condition_locked() -> None:
    assert "## Piecewise sigma_lower rule" in DOC
    assert "\\sigma_{\\mathrm{lower}}=" in DOC
    assert "\\varepsilon_{\\gamma}^{2}" in DOC
    assert "\\inf_{(\\xi,\\eta)\\in\\Gamma_{\\mathrm{term}}^{\\sharp}} |X_{\\gamma}(\\xi,\\eta)| \\ge \\varepsilon_{\\gamma}>0" in DOC

def test_no_x_gamma_min_abs_repo_wide() -> None:
    import subprocess

    proc = subprocess.run(["git", "grep", "-n", "x_gamma_min_abs", "--", ":!tests/test_ddyo_bridge_literal_locks.py"], capture_output=True, text=True)
    assert proc.returncode == 1
    assert proc.stdout.strip() == ""
