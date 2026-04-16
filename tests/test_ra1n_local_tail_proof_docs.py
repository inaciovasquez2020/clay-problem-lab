from pathlib import Path

def test_ra1n_local_tail_proof_docs():
    s1 = Path("docs/math/RA1N_GHAT_LOCAL_BOUND_PROOF.md").read_text()
    s2 = Path("docs/math/RA1N_GHAT_TAIL_BOUND_PROOF.md").read_text()
    assert "# Conditional: RA1n Ghat local bound proof" in s1
    assert "alpha<3" in s1 or "alpha < 3" in s1
    assert "C_0>0" in s1 or "C_0 > 0" in s1
    assert "Do not claim GoodBounds" in s1
    assert "# Conditional: RA1n Ghat tail bound proof" in s2
    assert "varepsilon>0" in s2 or "varepsilon > 0" in s2 or "eps > 0" in s2
    assert "C_\\infty>0" in s2 or "C_\\infty > 0" in s2 or "Cinf > 0" in s2
    assert "Do not claim GoodBounds" in s2
