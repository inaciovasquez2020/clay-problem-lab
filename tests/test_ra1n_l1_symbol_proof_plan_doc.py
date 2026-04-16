from pathlib import Path

def test_ra1n_l1_symbol_proof_plan_doc():
    s = Path("docs/math/RA1N_L1_SYMBOL_PROOF_PLAN.md").read_text()
    assert "# Conditional: RA1n L1 symbol proof plan" in s
    assert "Prove GoodBounds for the actual Fourier kernel Ghat" in s
    assert "alpha < 3" in s
    assert "eps > 0" in s
    assert "GoodBounds -> L1_integrable -> C = 1" in s
    assert "Do not claim CANONICAL" in s
