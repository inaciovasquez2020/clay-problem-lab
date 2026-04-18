from pathlib import Path

def test_dr33d_step29_power_gap_obstruction_lock() -> None:
    s = Path("docs/math/DR33D_STEP_29_POWER_GAP_OBSTRUCTION.md").read_text()
    assert "DR33D Step 29 — Exact Power-Gap Obstruction Lemma" in s
    assert r"S^{1/(1+\theta)}\le C\,S" in s
    assert r"E^{(a)}_j" in s
    assert r"S(a)=a^{1+\theta}" in s
    assert r"a^{-\theta}\to\infty" in s
    assert "LOCKED OBSTRUCTION — Step 28 stops exactly at the power gap \\(S^{1/(1+\\theta)}\\not\\Rightarrow S\\)." in s
