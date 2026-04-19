from pathlib import Path

def test_exact_ddyo_symbol_formula_fk_open_input_lock() -> None:
    s = Path("docs/math/EXACT_DDYO_SYMBOL_FORMULA_FK.md").read_text()
    assert "## Status" in s
    assert "OPEN" in s
    assert "F_k(\\xi,\\eta)" in s
    assert "m_k(\\xi,\\eta)=F_k(\\xi,\\eta)" in s
    assert "NotImplementedError" in s
