from pathlib import Path

def test_ra1n_unrestricted_certified_closer_doc():
    s = Path("docs/math/RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "\\subset\nV_{\\mathrm{RA1n}}" in s
    assert "b^*G^{-1}b=0<1" in s
    assert "RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md" in s
    assert "\\epsilon=1" in s
    assert "\\int Fg=0" in s
    assert "aligned obstruction" in s
    assert "packet-exhausted finite-basis surface" in s
