from pathlib import Path

def test_ra1n_terminal_grammar_closure_preservation_lemma_locked_open():
    p = Path("docs/status/RA1N_TERMINAL_GRAMMAR_CLOSURE_PRESERVATION_LEMMA.md")
    s = p.read_text()
    assert "Status: OPEN." in s
    assert r"\Omega_{\mathrm{term}}" in s
    assert r"\omega\in\Omega_{\mathrm{term}}" in s
    assert r"\chi_1,\dots,\chi_{q(\omega)}\in W_{\mathrm{term}}" in s
    assert r"\omega(\chi_1,\dots,\chi_{q(\omega)})\in W_{\mathrm{term}}" in s
    assert r"(I-\Pi_W)\omega(\chi_1,\dots,\chi_{q(\omega)})=0" in s
    assert r"\mathcal R_{\mathrm{term}}" in s
    assert "This document does not identify the actual RA1n grammar operations." in s
    assert "This document does not prove closure preservation." in s
