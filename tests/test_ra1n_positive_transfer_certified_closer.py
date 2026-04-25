from pathlib import Path

def test_ra1n_positive_transfer_certified_closer_doc():
    s = Path("docs/math/RA1N_POSITIVE_TRANSFER_CERTIFIED_CLOSER.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md" in s
    assert "epsilon=1" in s
    assert "projection-error strict domination" in s
    assert "c_{\\mathrm{RA1n}}>0" in s
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)" in s
    assert "finite-basis Gram certificate" in s
    assert "structural counterexample exclusion" in s
    assert "certified closed" in s
