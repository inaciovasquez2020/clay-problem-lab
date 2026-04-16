from pathlib import Path

def test_ra1n_allcertified_depends_on_goodbounds_gate():
    s = Path("docs/status/RA1N_ALLCERTIFIED_FRONTIER.md").read_text()
    assert "# Conditional: RA1n allCertified frontier" in s
    assert "allCertified = true iff every required RA1n certification object is present and verified" in s
    assert "ghat_formula_explicit" in s
    assert "Do not set allCertified = true" in s
