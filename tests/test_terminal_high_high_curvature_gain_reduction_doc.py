from pathlib import Path

def test_terminal_high_high_curvature_gain_reduction_doc():
    s = Path("docs/math/TERMINAL_HIGH_HIGH_CURVATURE_GAIN_REDUCTION.md").read_text()
    assert "# Conditional: Terminal High-High Curvature Gain Reduction" in s
    assert "OPEN." in s
    assert "r_k(\\xi,\\eta)" in s
    assert "\\tau(\\xi,\\eta)" in s
    assert "2^{-\\alpha k}" in s
    assert "\\partial_\\perp^2 r_k(\\xi,\\eta)\\big|_{\\xi\\parallel\\eta}" in s
    assert "strict reduction of the terminal theorem closure to one explicit symbol lower bound" in s
    assert "No unconditional proof is claimed here." in s
