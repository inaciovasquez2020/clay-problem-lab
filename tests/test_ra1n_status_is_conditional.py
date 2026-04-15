from pathlib import Path

def test_ra1n_status_is_conditional():
    p = Path("docs/status/RA1N_STATUS.md")
    s = p.read_text()
    assert "Status: CONDITIONAL" in s
    assert "Minimal missing verification:" in s
    assert r"\widehat G \in L^1(\mathbb R^3)" in s
