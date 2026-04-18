from pathlib import Path

def test_ra1n_projector_paired_symmetry_lock():
    s = Path("docs/math/RA1N_PROJECTOR_PAIRED_SYMMETRY.md").read_text()
    assert "K_j^{\\mathrm{proj}}(x-y)=K_j^{\\mathrm{proj}}(y-x)" in s
    assert "r_k(\\eta,\\zeta)=r_k(\\zeta,\\eta)" in s
    assert "e^{-i(x-y)\\cdot(\\eta+\\zeta)}" in s
    assert "\\Gamma_{j,k}(y,x)=\\Gamma_{j,k}(x,y)" in s
    assert "\\mathsf T^{(1),\\mathrm{proj}}_{j,k}=0" in s
    assert "|\\mathsf R^{\\mathrm{proj}}_{j,k}|" in s
    assert "2^{-j}2^{-k}" in s
