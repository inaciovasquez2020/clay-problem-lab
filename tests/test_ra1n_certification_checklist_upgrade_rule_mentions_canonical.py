from pathlib import Path

def test_ra1n_certification_checklist_upgrade_rule_mentions_canonical():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "Do not claim CANONICAL" in s
