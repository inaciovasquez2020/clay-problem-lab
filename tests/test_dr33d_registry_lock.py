from pathlib import Path

def test_dr33d_registry_lock() -> None:
    s = Path("docs/math/DR33D_REGISTRY.md").read_text()
    assert "DR33D Registry" in s
    assert "Step 23" in s and "UNRESTRICTED-FALSE" in s
    assert "Step 24" in s and "LOCKED IMPOSSIBILITY" in s
    assert "Step 25" in s and "SURVIVING OPEN FRONTIER" in s
    assert "Step 27" in s and "CORRECTED REDUCTION" in s
    assert "Step 28" in s and "LOCKED REDUCTION" in s
    assert r"\left(\sum_{j\in\mathbb Z}2^{-j}E_j^{1/2}\right)^2" in s
    assert r"E_{j+1}\le E_j" in s
    assert r"E_j=0\qquad\text{for all }j<j_0" in s
    assert "CANONICAL REGISTRY — unrestricted falsehood separated from surviving monotone-cutoff frontier." in s
