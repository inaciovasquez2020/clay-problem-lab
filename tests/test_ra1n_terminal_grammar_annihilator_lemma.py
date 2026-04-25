from pathlib import Path

def test_ra1n_terminal_grammar_annihilator_lemma_locked_open():
    p = Path("docs/status/RA1N_TERMINAL_GRAMMAR_ANNIHILATOR_LEMMA.md")
    s = p.read_text()
    assert "Status: OPEN." in s
    assert r"\mathcal A_{\mathrm{term}}(\chi)" in s
    assert r"W_{\mathrm{term}}^\perp" in s
    assert r"\langle \chi,\zeta\rangle_{L^2}=0" in s
    assert r"\mathcal W_{\mathrm{term}}(\chi)=0" in s
    assert r"\mathcal R_{\mathrm{term}}(\chi)=0" in s
    assert "This lemma must be proved from the actual RA1n terminal grammar." in s
    assert "It is not proved here." in s
