from pathlib import Path

def test_ra1n_terminal_grammar_atom_span_lemma_locked_open():
    p = Path("docs/status/RA1N_TERMINAL_GRAMMAR_ATOM_SPAN_LEMMA.md")
    s = p.read_text()
    assert "Status: OPEN." in s
    assert r"\mathfrak G_{\mathrm{atom}}" in s
    assert r"\gamma\in W_{\mathrm{term}}" in s
    assert r"(I-\Pi_W)\gamma=0" in s
    assert r"\mathcal R_{\mathrm{term}}(\gamma)=0" in s
    assert "This document does not identify the actual grammar atoms." in s
    assert "This document does not prove the lemma." in s
