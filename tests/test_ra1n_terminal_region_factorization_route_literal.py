from pathlib import Path

def test_ra1n_terminal_region_factorization_route_literal():
    text = Path("docs/math/RA1N_TERMINAL_REGION_FACTORIZATION_ROUTE.md").read_text(encoding="utf-8")
    assert "Status: OPEN" in text
    assert r"\Gamma_k^{\mathrm{term}}" in text
    assert r"|\xi\wedge\eta|\ge \varepsilon 2^{2k}" in text
    assert r"g_k(\xi,\eta)=0" in text
    assert r"Z_k:=\{(\xi,\eta):r_k(\xi,\eta)=0\}\subseteq \{(\xi,\eta):g_k(\xi,\eta)=0\}" in text
    assert r"a_k(\xi,\eta):=\frac{r_k(\xi,\eta)}{g_k(\xi,\eta)}" in text
    assert r"\inf_{(\xi,\eta)\in Z_k\cap \Gamma_k^{\mathrm{term}}}|a_k(\xi,\eta)|>0" in text
    assert r"\inf_{(\xi,\eta)\in Z_k\cap \Gamma_k^{\mathrm{term}}}\|\nabla g_k(\xi,\eta)\|>0" in text
    assert r"2^{-\alpha k}|\xi\wedge\eta|^2" in text
