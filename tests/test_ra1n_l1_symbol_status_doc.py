from pathlib import Path

def test_ra1n_l1_symbol_status_doc():
    s = Path("docs/status/RA1N_L1_SYMBOL_STATUS.md").read_text()
    assert "Status: CONDITIONAL" in s
    assert "RA1N_L1_SYMBOL_WALL" in s
    assert "allCertified = true" in s
    assert "C = 1" in s
    assert "Do not promote to CANONICAL" in s
