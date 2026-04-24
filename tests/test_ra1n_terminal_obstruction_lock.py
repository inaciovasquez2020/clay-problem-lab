from pathlib import Path

DOC = Path("docs/status/RA1N_TERMINAL_OBSTRUCTION_LOCK_2026_04_24.md").read_text()

def test_ra1n_terminal_obstruction_is_open_and_precise():
    assert "Status: OPEN." in DOC
    assert "RA1n remains the terminal theorem-level obstruction" in DOC
    assert "first-moment shell-product" in DOC
    assert "direct-symbol-derivative" in DOC
    assert "r_k(ξ) = \\widehat G_k(ξ) - P_k \\widehat G_k(ξ)" in DOC
    assert "proposed RA1n proof is not yet a theorem-level closure" in DOC
    assert "No unconditional Navier--Stokes or DDYO continuum closure is claimed" in DOC
    assert "This file does not solve RA1n" in DOC
