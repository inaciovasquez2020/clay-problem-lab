from pathlib import Path

def test_ra1n_kernel_parity_normal_form_lock():
    s = Path("docs/math/RA1N_KERNEL_PARITY_NORMAL_FORM.md").read_text()
    assert "K_j^{\\mathrm{sym}}" in s
    assert "K_j^{\\mathrm{asym}}" in s
    assert "\\mathcal B_{j,k}[H]=\\mathcal B_{j,k}[H\\circ\\sigma]" in s
    assert "H^{(1)}_{j,k}(y,x)=-H^{(1)}_{j,k}(x,y)" in s
    assert "\\mathsf T^{(1),\\mathrm{sym}}_{j,k}=0" in s
    assert "\\langle \\mathcal H'(\\omega_j),\\mathcal C^{(1),\\mathrm{sym}}_{j,k}\\omega_k\\rangle=0" in s
    assert "|\\mathsf R^{\\mathrm{sym}}_{j,k}|" in s
    assert "2^{-j}2^{-k}" in s
