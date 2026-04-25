from pathlib import Path

def test_ra1n_terminal_grammar_frontier_closure_map_locked():
    p = Path("docs/status/RA1N_TERMINAL_GRAMMAR_FRONTIER_CLOSURE_MAP.md")
    s = p.read_text()

    assert "Status: CLOSED AS FRONTIER MAP / OPEN AS THEOREM." in s
    assert r"\mathcal A_{\mathrm{term}}(\chi)" in s
    assert r"\mathcal R_{\mathrm{term}}(\chi)=0" in s
    assert r"(I-\Pi_W)\chi=0" in s
    assert r"\chi\in W_{\mathrm{term}}" in s

    assert "Terminal Grammar Annihilator Lemma" in s
    assert r"\forall \zeta\in W_{\mathrm{term}}^\perp" in s
    assert r"\langle \chi,\zeta\rangle_{L^2}=0" in s

    assert "Terminal Grammar Atom Span Lemma" in s
    assert r"\mathfrak G_{\mathrm{atom}}" in s
    assert r"\gamma\in W_{\mathrm{term}}" in s

    assert "Terminal Grammar Closure Preservation Lemma" in s
    assert r"\Omega_{\mathrm{term}}" in s
    assert r"\omega(\chi_1,\dots,\chi_{q(\omega)})\in W_{\mathrm{term}}" in s

    assert "Terminal Grammar Completeness Lemma" in s
    assert r"\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}})" in s

    assert "The current RA1n terminal-grammar decomposition is closed as a dependency map." in s
    assert "No further repository-scope decomposition is admitted without a new actual RA1n terminal grammar definition." in s
    assert "It does not close the theorem-level RA1n frontier." in s
    assert "It does not prove Navier--Stokes regularity." in s
