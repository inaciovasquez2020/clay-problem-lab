from pathlib import Path

def test_ddyo_ra1n_rk_definition_status_is_blocked_until_exact_symbol_is_canonical():
    s = Path("docs/status/DDYO_RA1N_RK_DEFINITION_STATUS.md").read_text()
    assert "BLOCKED PENDING EXACT DDYO SYMBOL FORMULA." in s
