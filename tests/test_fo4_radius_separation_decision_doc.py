from pathlib import Path

def test_fo4_radius_separation_decision_doc():
    s = Path("docs/status/FO4_RADIUS_SEPARATION_DECISION.md").read_text()
    assert "R_EXTRACTED_VALUE" in s
    assert "DELTA_SEP_EXTRACTED_VALUE" in s
    assert "R > \\delta_{\\mathrm{sep}}" in s or "R >" in s
    assert "R \\le \\delta_{\\mathrm{sep}}" in s or "R <=" in s
