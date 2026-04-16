from pathlib import Path

def test_renormalized_flux_route_doc_contains_conditional_frontier():
    p = Path("docs/math/RENORMALIZED_FLUX_ROUTE.md")
    s = p.read_text()
    assert "# Conditional: renormalized flux route" in s
    assert "\widetilde{\mathrm{Flux}}_\ell" in s
    assert "\mathcal D_K(t)" in s
    assert "\mathcal Q_K(t)" in s
    assert "Weakest remaining object:" in s
