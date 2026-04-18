from pathlib import Path

def test_dr33d_step50_stop_rule_lock() -> None:
    s = Path("docs/math/DR33D_STEP_50_STOP_RULE.md").read_text()
    assert "DR33D Step 50 — Stop Rule" in s
    assert "Conditional." in s
    assert r"\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}" in s
    assert r"\mathfrak C(E(u))\le 1-\delta" in s
    assert r"S(E(u))\ge m" in s
    assert "terminal stop rule" in s
