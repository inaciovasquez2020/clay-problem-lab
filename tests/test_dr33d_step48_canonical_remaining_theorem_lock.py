from pathlib import Path

def test_dr33d_step48_canonical_remaining_theorem_lock() -> None:
    s = Path("docs/math/DR33D_STEP_48_CANONICAL_REMAINING_THEOREM.md").read_text()
    assert "DR33D Step 48 — Canonical Remaining Theorem" in s
    assert "Conditional." in s
    assert r"E_{j+1}(u)\le E_j(u)" in s
    assert r"E_j(u)=0\ (j<j_0)" in s
    assert r"\mathfrak C(E(u))\le 1-\delta" in s
    assert r"S(E(u))\ge m" in s
    assert r"A(E(u))^2\le C(\theta,j_0,\delta,m)\,S(E(u))" in s
