from pathlib import Path

def test_lh_tail_counterexample_doc():
    s = Path("docs/math/LH_TAIL_COUNTEREXAMPLE_AND_MINIMAL_MISSING_INPUT.md").read_text()
    assert "# Conditional: LH tail counterexample and minimal missing input" in s
    assert "Counterexample: fix \\(\\ell\\)" in s
    assert "M^2\\,2^{2N}" in s
    assert "2^{-N}(M\\,2^N)=M" in s
    assert "no inequality controlling the \\(LH\\) tail by \\((D_\\ell,S_\\ell)\\) only is possible" in s
    assert "\\sup_{K,t}" in s
