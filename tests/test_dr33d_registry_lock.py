from pathlib import Path

def test_dr33d_registry_lock() -> None:
    s = Path("docs/math/DR33D_REGISTRY.md").read_text()
    assert "Step 23" in s and "UNRESTRICTED-FALSE" in s
    assert "Step 25A" in s and "FALSE" in s
    assert "Step 25B" in s and "SURVIVING OPEN FRONTIER" in s
    assert "Step 28" in s and "LOCKED REDUCTION" in s
    assert "Step 29" in s and "LOCKED OBSTRUCTION" in s
    assert "Step 30" in s and "LOCKED COUNTEREXAMPLE" in s
    assert "Step 31" in s and "CANDIDATE EXTRA INVARIANT" in s
    assert "CANONICAL REGISTRY — size-controlled frontier isolated after Steps 29–31." in s
