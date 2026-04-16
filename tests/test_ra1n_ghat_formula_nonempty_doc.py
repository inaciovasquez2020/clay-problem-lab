from pathlib import Path

def test_ra1n_ghat_formula_nonempty_doc():
    s = Path("docs/math/RA1N_GHAT_FORMULA.md").read_text()
    # require at least one non-placeholder symbol beyond the equals sign
    assert "\\widehat G(\\xi)=" in s
    rhs = s.split("\\widehat G(\\xi)=",1)[1].strip()
    assert len(rhs) > 0
