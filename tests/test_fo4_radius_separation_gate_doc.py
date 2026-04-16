from pathlib import Path

def test_fo4_radius_separation_gate_doc():
    s = Path("docs/math/FO4_RADIUS_SEPARATION_GATE.md").read_text()
    assert "# Conditional: FO4 radius-separation gate" in s
    assert "PreserveObstructionClass" in s
    assert "R>\\delta_{\\mathrm{sep}}" in s or "R > \\delta_{\\mathrm{sep}}" in s
    assert "[T_R(z)]\\neq 0 \\iff [z]\\neq 0" in s or "[T_R(z)]" in s
    assert "R\\le \\delta_{\\mathrm{sep}}" in s or "R \\le \\delta_{\\mathrm{sep}}" in s
    assert "Do not claim preservation" in s
