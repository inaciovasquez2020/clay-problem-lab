from pathlib import Path

DOC = Path("docs/math/RA1N_QK_DINI_REDUCTION.md").read_text()

def test_qk_definition_present():
    assert "Q_k(t):=\\frac{\\mathcal M_k(t)}{E_k(t)}" in DOC

def test_dini_energy_bounds_present():
    assert "D^+E_k(t)\\ge -a_kE_k(t)-b_k\\mathcal M_k(t)." in DOC
    assert "D^+\\mathcal M_k(t)\\le \\alpha_k\\mathcal M_k(t)+\\beta_kE_k(t)." in DOC

def test_qk_inequality_present():
    assert "D^+Q_k(t)" in DOC
    assert "\\le\n\\beta_k+(\\alpha_k+a_k)Q_k(t)+b_kQ_k(t)^2." in DOC

def test_uniform_mu_conditions_present():
    assert "\\beta_k+b_k\\le \\mu," in DOC
    assert "\\alpha_k+a_k\\le -\\mu" in DOC
    assert "-\\mu\\bigl(Q_k(t)-1\\bigr)." in DOC

def test_lyapunov_and_ra1n_substitution_present():
    assert "L(t):=\\sup_k(Q_k(t)-1)\\ge 0." in DOC
    assert "D^+L(t)\\le -\\mu L(t)\\le 0" in DOC
    assert "A:=1+L(0)." in DOC
    assert "2^{\\beta k}E_k(t)^{3/2}" in DOC
