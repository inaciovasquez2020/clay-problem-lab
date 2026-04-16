from pathlib import Path

def test_ra1n_certification_checklist_upgrade_rule_mentions_allcertified():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "allCertified = true" in s
