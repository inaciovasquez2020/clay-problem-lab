from pathlib import Path

def test_dr33d_step43_proof_obligation_lock() -> None:
    s = Path("docs/math/DR33D_STEP_43_PROOF_OBLIGATION.md").read_text()
    assert "DR33D Step 43 — Proof Obligation" in s
    assert "Conditional." in s
    assert r"\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}" in s
    assert r"E_{j+1}(u)\le E_j(u)" in s
    assert r"\mathfrak C(E(u))\le 1-\delta" in s
    assert r"S(E(u))\ge m" in s
