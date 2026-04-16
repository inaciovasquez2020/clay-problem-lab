from pathlib import Path

def test_lh_tail_terminal_obstruction_doc():
    s = Path("docs/status/LH_TAIL_TERMINAL_OBSTRUCTION.md").read_text()
    assert "HL piece: harmless at \\(\\theta=0\\)" in s
    assert "HH piece: harmless at \\(\\theta=0\\)" in s
    assert "LH piece: terminal obstruction" in s
    assert "\\sum_{m\\ge \\ell+4}2^{-m}D_m^{1/2}" in s
    assert "\\exists\\,U_\\ell\\ge 0" in s
