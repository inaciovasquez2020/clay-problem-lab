from pathlib import Path

def test_ra1n_quadratic_invariant_certificate_doc():
    s = Path("docs/math/RA1N_QUADRATIC_INVARIANT_CERTIFICATE.md").read_text()
    assert "Status: PROVED ABSTRACTLY" in s
    assert "Q:L^2\\to L^2" in s
    assert "\\Phi_Q(u)" in s
    assert "\\Phi_Q(e^{i\\theta}u)" in s
    assert "K\\cap\\mathcal O_h=\\varnothing" in s
    assert "a<b" in s
    assert "\\sup_{u\\in K}\\Phi_Q(u)" in s
    assert "\\Phi_Q(h)" in s
    assert "RA1N_INVARIANT_DISJOINTNESS_CERTIFICATE.md" in s

def test_ra1n_invariant_disjointness_links_quadratic_certificate():
    s = Path("docs/math/RA1N_INVARIANT_DISJOINTNESS_CERTIFICATE.md").read_text()
    assert "RA1N_QUADRATIC_INVARIANT_CERTIFICATE.md" in s
    assert "bounded self-adjoint \\(Q:L^2\\to L^2\\)" in s
    assert "\\sup_{u\\in K}" in s
