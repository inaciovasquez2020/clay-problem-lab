from pathlib import Path

def test_ra1n_theorem_level_pursuit_audit_doc():
    s = Path("docs/status/RA1N_THEOREM_LEVEL_PURSUIT_AUDIT.md").read_text()
    assert "Status: PURSUIT TEST" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "(I-\\Pi_V)F=0" in s
    assert "F=a(F)\\phi_1" in s
    assert "Terminal generator normal form" in s
    assert "Residual-zero identity" in s
    assert "No transverse witness" in s
    assert "Rank-one packet classification" in s
    assert "genuine structural normal-form mechanism" in s
