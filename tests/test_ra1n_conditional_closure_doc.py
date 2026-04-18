from pathlib import Path

def test_ra1n_conditional_closure_doc():
    s = Path("docs/math/RA1N_CONDITIONAL_CLOSURE.md").read_text()
    assert "Status: CONDITIONAL" in s
    assert "The unconditional frontier is exactly SC\\((A,C_0)\\)." in s
    assert "Membership in \\(\\dot H^s\\) or \\(\\dot B^0_{2,\\infty}\\) alone does not imply SC\\((A,C_0)\\)." in s
    assert "\\mathcal M_k := \\sup_{|j-k|\\le C_0} E_j" in s
    assert "Thus the exact closure alternative is:" in s
