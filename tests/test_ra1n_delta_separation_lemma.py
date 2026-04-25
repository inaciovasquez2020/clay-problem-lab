from pathlib import Path

def test_ra1n_delta_separation_lemma_lock():
    s = Path("docs/math/RA1N_DELTA_SEPARATION_LEMMA.md").read_text()
    assert "Status: OPEN" in s
    assert "B(F,g)=\\int Fg" in s
    assert "h=\\frac{\\overline g}{\\|g\\|_2}" in s
    assert "\\epsilon=\\frac{\\delta^2}{2}" in s
    assert "1-\\frac{\\delta^2}{2}" in s
    assert "\\operatorname{dist}_{L^2/S^1}" in s
    assert ">0" in s
