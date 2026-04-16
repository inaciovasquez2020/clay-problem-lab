from pathlib import Path

def test_fo4_radius_separation_status_doc():
    s = Path("docs/status/FO4_RADIUS_SEPARATION_STATUS.md").read_text()
    assert "# Conditional: FO4 radius versus separation status" in s
    assert "SIMULATED_RADIUS" in s
    assert "CERTIFIED_DELTA_SEP" in s
    assert "R>\\delta_{\\mathrm{sep}}" in s or "R > \\delta_{\\mathrm{sep}}" in s
    assert "R\\le \\delta_{\\mathrm{sep}}" in s or "R \\le \\delta_{\\mathrm{sep}}" in s
    assert "Do not claim Double Dime admissibility" in s
    assert "Conditional." in s
