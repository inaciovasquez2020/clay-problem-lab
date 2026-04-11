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


def test_ra1n_status_file_records_single_remaining_theorem():
    p = Path("docs/status/DDYO_RA1N_STATUS_2026_04_11.md")
    assert p.exists(), "missing dated RA1n status file"
    s = p.read_text()
    assert "Status: CONDITIONAL" in s
    assert r"r_k(\xi)=\widehat G_k(\xi)-P_k\widehat G_k(\xi)" in s
    assert "single remaining theorem" in s
    assert "unconditional RA1n closure" in s


def test_single_remaining_theorem_doc_exists():
    p = Path("docs/math/DDYO_RA1N_SINGLE_REMAINING_THEOREM.md")
    assert p.exists(), "missing single remaining theorem doc"
    s = p.read_text()
    assert r"r_k(\xi)=\widehat G_k(\xi)-P_k\widehat G_k(\xi)" in s
    assert "unconditional RA1n closure" in s
    assert "Open." in s
