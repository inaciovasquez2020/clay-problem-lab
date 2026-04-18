from pathlib import Path

def test_next_missing_object_route_status():
    s = Path("docs/status/NEXT_MISSING_OBJECT.md").read_text()
    assert "TERMINAL_HIGH_HIGH_RESONANCE_GAIN_ROUTE.md" in s
    assert "Canonical route status:" in s
    assert "Open." in s
