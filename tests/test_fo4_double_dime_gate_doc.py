from pathlib import Path

def test_fo4_double_dime_gate_doc():
    s = Path("docs/status/FO4_DOUBLE_DIME_GATE.md").read_text()
    assert "Double Dime admissibility" in s
    assert "R > \\delta_{\\mathrm{sep}}" in s or "R >" in s
    assert "Do not claim Double Dime admissibility" in s
