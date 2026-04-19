from pathlib import Path

def test_dr33d_registry_lock() -> None:
    s = Path("docs/math/DR33D_REGISTRY.md").read_text()
    assert "Step 32" in s and "LOCKED NORMALIZATION" in s
    assert "Step 33" in s and "CANDIDATE CONCENTRATION INVARIANT" in s
    assert "The exact surviving frontier is Step 25B" in s
    assert r"S=\sum_j E_j^{1+\theta}\to0" in s
    assert "CANONICAL REGISTRY — normalization and concentration diagnostic added after Steps 32–33." in s
