from pathlib import Path

def test_ra1n_conditional_closure_doc_contains_canonical_conditions():
    p = Path("docs/math/DDYO_RA1N_CONDITIONAL_CLOSURE.md")
    s = p.read_text()
    assert "Conditional." in s
    assert r"|F_k(\xi)| \le M_F" in s
    assert r"r_k(\xi) = (1-P_k(\xi))\,\widehat G(\xi)\,\psi_k(\xi)" in s
    assert r"\sup_{\xi\in\mathbb R^3}\sum_k |\psi_k(\xi)| < \infty" in s
    assert r"\widehat G \in L^1(\mathbb R^3)" in s
    assert r"\sum_k a_k" in s
