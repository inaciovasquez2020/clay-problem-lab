from pathlib import Path

def test_ddyo_ra1n_canonical_derivative_theorem_is_blocked():
    s = Path("docs/math/DDYO_RA1N_CANONICAL_DERIVATIVE_THEOREM_BLOCKED.md").read_text()
    assert "Blocked until the exact DDYO symbol is canonical." in s
    assert "partial_{\\xi_\\ell}" in s
