from pathlib import Path

def test_ra1n_certification_checklist_links_formula_doc():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "RA1N_GHAT_FORMULA.md" in s or "ghat_formula_explicit" in s
