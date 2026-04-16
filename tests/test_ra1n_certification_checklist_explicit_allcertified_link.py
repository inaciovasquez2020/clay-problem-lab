from pathlib import Path

def test_ra1n_certification_checklist_explicit_allcertified_link():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "docs/status/RA1N_ALLCERTIFIED_FRONTIER.md" in s
