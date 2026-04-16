from pathlib import Path

def test_ddyo_ra1n_symbol_consistency_blocker_records_kernel_and_symbol_gap():
    s = Path("docs/status/DDYO_RA1N_SYMBOL_CONSISTENCY_BLOCKER.md").read_text()
    assert "Exact DDYO kernel formula" in s
    assert "Exact DDYO remainder-symbol formula" in s
    assert "unsupported replacement" in s
    assert "No further progress possible without new input." in s
