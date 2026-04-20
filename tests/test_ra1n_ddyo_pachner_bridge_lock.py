from pathlib import Path
import json

DOC = Path("docs/math/DDYO_PACHNER_SYMBOL_LIFT_FRONTIER.md").read_text()
SNAP = Path("docs/status/RA1N_DDYO_PACHNER_BRIDGE_STATUS.md").read_text()
ART = json.loads(Path("artifacts/ra1n_ddyo_pachner_bridge/bridge_summary.json").read_text())

def test_status_lock() -> None:
    assert "## Status" in DOC
    assert "CONDITIONAL" in DOC
    assert "Status: CONDITIONAL" in SNAP
    assert ART["status"] == "CONDITIONAL"

def test_rank_lock() -> None:
    assert "rank_F2(F6) = 5" in DOC
    assert "rank_F2(F7) = 25" in DOC
    assert ART["verified_discrete_input"]["rank_F2_F6"] == 5
    assert ART["verified_discrete_input"]["rank_F2_F7"] == 25

def test_missing_bridge_lock() -> None:
    assert "Phi_{6,7}" in DOC
    assert "V_{\\mathrm{out}}" in DOC
    assert "E_{\\mathrm{out}}" in DOC
    assert ART["missing_map"] == "Phi_6,7"
    assert ART["missing_data"] == ["V_out", "E_out", "X_gamma"]

def test_nonimplication_lock() -> None:
    assert "\\centernot\\Longrightarrow" in DOC
