from pathlib import Path

def test_ra1n_projector_consistent_kernel_lock():
    s = Path("docs/math/RA1N_PROJECTOR_CONSISTENT_KERNEL.md").read_text()
    assert "\\widehat K_j^{\\mathrm{proj}}(\\xi):=\\psi_j(|\\xi|)" in s
    assert "\\xi_a m^{(j)}_{ab}(\\xi)=0" in s
    assert "\\xi_a \\psi_j(|\\xi|)m^{(j)}_{ab}(\\xi)\\widehat f(\\xi)=0" in s
    assert "r_k^{\\mathrm{proj}}(\\eta,\\zeta)" in s
    assert "|r_{j,k}^{\\mathrm{proj}}(\\eta,\\zeta)|" in s
    assert "[\\widetilde P_j^{\\mathrm{proj}},S_k\\!\\cdot\\nabla]\\omega_k" in s
    assert "\\bigl(\\psi_j(|\\xi|)-\\psi_j(|\\eta|)\\bigr)\\,i\\eta" in s
    assert "\\langle \\widetilde P_j^{\\mathrm{proj}} f,g\\rangle" in s
    assert "\\mathsf T^{(1),\\mathrm{proj}}_{j,k}=0" in s
    assert "|\\mathsf R^{\\mathrm{proj}}_{j,k}|" in s
    assert "2^{-j}2^{-k}" in s
