from pathlib import Path

def test_next_missing_object_terminal_symbol_lower_bound():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "terminal_high_high_symbol_lower_bound" in s
    assert "TERMINAL_HIGH_HIGH_CURVATURE_GAIN_REDUCTION.md" in s
    assert "r_k(\\xi,\\eta)" in s
    assert "\\tau(\\xi,\\eta)=\\frac{|\\xi\\wedge\\eta|}{|\\xi|\\,|\\eta|}" in s
    assert "2^{-\\alpha k}" in s
    assert "single explicit missing object" in s
