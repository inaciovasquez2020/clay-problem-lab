from pathlib import Path

def test_ra1n_terminal_grammar_completeness_lemma_locked_open():
    p = Path("docs/status/RA1N_TERMINAL_GRAMMAR_COMPLETENESS_LEMMA.md")
    s = p.read_text()
    assert "Status: OPEN." in s
    assert r"\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}})" in s
    assert r"\mathcal A_{\mathrm{term}}(\chi)" in s
    assert r"\chi\in" in s
    assert r"\mathfrak G_{\mathrm{atom}}\subset W_{\mathrm{term}}" in s
    assert r"\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}})" in s
    assert r"\subset W_{\mathrm{term}}" in s
    assert r"\mathcal R_{\mathrm{term}}(\chi)=0" in s
    assert "This document does not identify the actual terminal grammar closure." in s
    assert "This document does not prove grammar completeness." in s
