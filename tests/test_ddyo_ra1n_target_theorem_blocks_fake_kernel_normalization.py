from pathlib import Path

def test_ddyo_ra1n_target_theorem_blocks_fake_kernel_normalization():
    s = Path("docs/math/DDYO_RA1N_TARGET_THEOREM.md").read_text()
    assert "Do not use" in s
    assert "exact DDYO kernel formula" in s
    assert "dyadic scaling" in s
