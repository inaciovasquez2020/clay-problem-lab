from pathlib import Path

DOC = Path("docs/status/RA1N_THEOREM_LEVEL_PURSUIT_AUDIT.md")

def test_pursuit_audit_frontier_update():
    s = DOC.read_text()
    assert "Updated Terminal Frontier" in s
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\mathcal R_{\\mathrm{term}}(\\chi)=0" in s
    assert "RA1N_TERMINAL_FRONTIER_CHAIN.md" in s
    assert "RA1N_THEOREM_LEVEL_STOP_RULE.md" in s
