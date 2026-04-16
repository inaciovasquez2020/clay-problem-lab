from pathlib import Path

def test_ra1n_goodbounds_gate_doc():
    s = Path("docs/status/RA1N_GOODBOUNDS_GATE.md").read_text()
    assert "# Conditional: RA1n GoodBounds gate" in s
    assert "GoodBounds" in s
    assert "L^1" in s or "L^1-integrable" in s or "L^1\\text{-integrable}" in s
    assert "C=1" in s or "C = 1" in s
    assert "Do not claim CANONICAL before both local and tail bounds are proved" in s
