from pathlib import Path

def test_ra1n_ghat_formula_and_goodbounds_pipeline_docs():
    s0 = Path("docs/math/RA1N_GHAT_FORMULA.md").read_text()
    s1 = Path("docs/math/RA1N_GHAT_LOCAL_BOUND_PROOF.md").read_text()
    s2 = Path("docs/math/RA1N_GHAT_TAIL_BOUND_PROOF.md").read_text()
    s3 = Path("docs/math/RA1N_GOODBOUNDS_LEMMAS.md").read_text()

    assert "GHAT_EXPLICIT_FORMULA" in s0
    assert "GHAT_NORMALIZED_PARAMETERS" in s0

    assert "alpha<3" in s1 or "alpha < 3" in s1
    assert "C_0>0" in s1 or "C_0 > 0" in s1
    assert "small-frequency asymptotic" in s1

    assert "varepsilon>0" in s2 or "varepsilon > 0" in s2
    assert "C_\\infty>0" in s2 or "C_\\infty > 0" in s2
    assert "large-frequency decay" in s2

    assert "LocalGoodBound" in s3
    assert "TailGoodBound" in s3
    assert "GoodBounds" in s3
    assert "L^1" in s3 or "L^1\\text{-integrable}" in s3
    assert "C=1" in s3 or "C = 1" in s3
