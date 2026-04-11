from pathlib import Path

def test_canonical_rk_definition_exists():
    p = Path("docs/math/DDYO_RA1N_CANONICAL_RK_DEFINITION.md")
    assert p.exists(), "missing canonical rk definition doc"
    s = p.read_text()
    assert "r_k=\\widehat G_k-P_k\\widehat G_k" in s
    assert "docs/math/DDYO_RA1N_EXACT_MISSING_LEMMA.md" in s
    assert "does not by itself yield unconditional RA1n closure" in s

def test_rk_definition_status_is_extracted():
    p = Path("docs/status/DDYO_RA1N_RK_DEFINITION_STATUS.md")
    assert p.exists(), "missing rk definition status doc"
    s = p.read_text()
    assert "Status: EXTRACTED" in s
    assert "r_k=\\widehat G_k-P_k\\widehat G_k" in s
    assert "Derive the exact theorem-level symbol derivative estimate" in s
