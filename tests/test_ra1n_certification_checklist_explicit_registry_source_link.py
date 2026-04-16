from pathlib import Path

def test_ra1n_certification_checklist_explicit_registry_source_link():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "registry_gate_satisfied" in s
    assert "ClayProblemLab/RA1nL1Registry.lean" in s
