from pathlib import Path

def test_phase_noncancellation_doc_exists_and_is_conditional():
    text = Path("docs/math/PHASE_NONCANCELLATION_LEMMA.md").read_text()
    assert "Phase Noncancellation Lemma" in text
    assert "Status: Conditional." in text
    assert "sectorial trilinear lower bound" in text
