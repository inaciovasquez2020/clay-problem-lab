from pathlib import Path

def test_hybrid_rk_rescaling_lemma_exists_and_contains_closure_chain():
    p = Path("docs/math/DDYO_HYBRID_RK_RESCALING_LEMMA.md")
    assert p.exists(), "missing hybrid rk rescaling lemma document"
    s = p.read_text()
    assert "r_k(\\xi)=2^{-k}\\rho(2^{-k}\\xi)" in s
    assert "\\partial_\\xi^\\alpha r_k(\\xi)" in s
    assert "\\text{annular fixed-scale kernel bound}" in s
    assert "\\text{RA1n}" in s
    assert "\\text{unconditional DDYO closure}" in s

def test_finished_product_links_hybrid_rk_rescaling_lemma():
    p = Path("docs/math/DDYO_RA1N_FINISHED_PRODUCT.md")
    assert p.exists(), "missing finished product document"
    s = p.read_text()
    assert "DDYO_HYBRID_RK_RESCALING_LEMMA.md" in s
