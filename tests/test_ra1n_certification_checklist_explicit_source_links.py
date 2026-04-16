from pathlib import Path

def test_ra1n_certification_checklist_explicit_source_links():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "docs/math/RA1N_GHAT_FORMULA.md" in s
    assert "docs/math/RA1N_GHAT_LOCAL_BOUND_PROOF.md" in s
    assert "docs/math/RA1N_GHAT_TAIL_BOUND_PROOF.md" in s
    assert "docs/status/RA1N_GOODBOUNDS_GATE.md" in s
