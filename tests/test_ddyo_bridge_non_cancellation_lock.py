from pathlib import Path
import json

DOC = Path("docs/math/DDYO_PACHNER_SYMBOL_LIFT_FRONTIER.md").read_text()
STATUS = Path("docs/status/RA1N_DDYO_PACHNER_BRIDGE_STATUS.md").read_text()
ART = json.loads(Path("artifacts/ra1n_ddyo_pachner_bridge/bridge_summary.json").read_text())

def test_non_cancellation_input_locked() -> None:
    assert "## Non-cancellation lock" in DOC
    assert "\\sigma_{\\mathrm{lower}} = \\varepsilon_{\\gamma}^2 > 0" in DOC
    assert "Uniform non-cancellation input locked" in STATUS
    assert ART["new_required_input"] == "uniform_non_cancellation_on_X_gamma"
    assert ART["certification_formula"] == "sigma_lower = eps_gamma^2"
