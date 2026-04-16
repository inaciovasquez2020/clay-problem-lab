from pathlib import Path

def test_ra1n_certification_checklist_links_gate():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "RA1N_GOODBOUNDS_GATE.md" in s or "GoodBounds gate" in s
