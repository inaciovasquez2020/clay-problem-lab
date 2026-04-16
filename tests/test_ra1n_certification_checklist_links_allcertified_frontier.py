from pathlib import Path

def test_ra1n_certification_checklist_links_allcertified_frontier():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "RA1N_ALLCERTIFIED_FRONTIER.md" in s or "allCertified = true" in s
