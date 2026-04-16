from pathlib import Path

def test_ra1n_certification_checklist_consistency():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "terminal_symbol_registered" in s
    assert "ghat_formula_explicit" in s
    assert "local_bound_proved" in s
    assert "tail_bound_proved" in s
    assert "goodbounds_assembled" in s
    assert "allCertified = true" in s
