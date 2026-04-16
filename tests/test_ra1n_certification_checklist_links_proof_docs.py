from pathlib import Path

def test_ra1n_certification_checklist_links_proof_docs():
    s = Path("docs/status/RA1N_CERTIFICATION_CHECKLIST.md").read_text()
    assert "RA1N_GHAT_LOCAL_BOUND_PROOF.md" in s or "local bound is proved" in s
    assert "RA1N_GHAT_TAIL_BOUND_PROOF.md" in s or "tail bound is proved" in s
