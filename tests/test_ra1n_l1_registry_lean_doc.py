from pathlib import Path

def test_ra1n_l1_registry_lean_doc():
    s = Path("ClayProblemLab/RA1nL1Registry.lean").read_text()
    assert "def GoodBounds : Prop :=" in s
    assert "axiom goodBounds_imply_L1 : GoodBounds → L1_integrable" in s
    assert "axiom C_eq_one_of_L1 : L1_integrable → C = 1" in s
    assert 'ra1nUpgradeIfCanonical.status = "CANONICAL"' in s
