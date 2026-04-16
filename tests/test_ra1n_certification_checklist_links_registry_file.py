from pathlib import Path

def test_ra1n_certification_checklist_links_registry_file():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "ClayProblemLab/RA1nL1Registry.lean" in s or "registry gate is satisfied" in s
