from pathlib import Path

def test_ra1n_first_order_leakage_locked():
    p = Path("docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md")
    s = p.read_text()
    assert r"\mathsf T^{(1)}_{j,k}" in s
    assert r"=0" in s or "routing bound" in s
