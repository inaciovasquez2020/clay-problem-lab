from pathlib import Path

def test_parabolic_window_gain_lemma_doc_contains_canonical_object():
    s = Path("docs/math/PARABOLIC_WINDOW_GAIN_LEMMA.md").read_text()
    assert "# Conditional: Parabolic Window Gain Lemma" in s
    assert "\\mathcal A_\\ell(t):=" in s
    assert "\\theta\\in(0,1)" in s
    assert "single canonical obstruction" in s
    assert "No unconditional proof is claimed here." in s
