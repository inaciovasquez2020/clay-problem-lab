from pathlib import Path

def test_fo4_obstruction_preservation_gate_doc():
    s = Path("docs/status/FO4_OBSTRUCTION_PRESERVATION_GATE.md").read_text()
    assert "PreserveObstructionClass" in s
    assert "R > \\delta_{\\mathrm{sep}}" in s or "R >" in s
    assert "[T_R(z)]" in s
