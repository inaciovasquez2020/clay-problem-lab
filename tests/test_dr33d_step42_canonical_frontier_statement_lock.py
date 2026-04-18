from pathlib import Path

def test_dr33d_step42_canonical_frontier_statement_lock() -> None:
    s = Path("docs/math/DR33D_STEP_42_CANONICAL_FRONTIER_STATEMENT.md").read_text()
    assert "DR33D Step 42 — Canonical Frontier Statement" in s
    assert "Conditional." in s
    assert r"E_{j+1}(u)\le E_j(u)" in s
    assert r"E_j(u)=0\ (j<j_0)" in s
    assert r"\mathfrak C(E(u))\le 1-\delta" in s
    assert r"S(E(u))\ge m" in s
    assert "canonical exact wording of the remaining frontier" in s
