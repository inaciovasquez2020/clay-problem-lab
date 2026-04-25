from pathlib import Path

DOC = Path("docs/status/RA1N_NEXT_TERMINAL_DECISION.md").read_text()

def test_ra1n_next_terminal_decision_status():
    assert "Status: OPEN." in DOC
    assert "RA1n has a closed unary closure lane." in DOC
    assert "Full RA1n remains conditional." in DOC

def test_ra1n_next_terminal_decision_binary():
    assert "next terminal decision is binary" in DOC
    assert "uses only the unary closure lane" in DOC
    assert "separate theorem frontiers" in DOC

def test_ra1n_next_terminal_decision_promotion_theorem():
    assert "RA1n first-moment shell-product surface = RA1n-unary-closure-lane." in DOC
    assert "then the current unary closure lane promotes to full RA1n closure" in DOC
    assert "If this identity is not proved, no full RA1n closure claim is admissible." in DOC
