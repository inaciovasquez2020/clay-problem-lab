from pathlib import Path

def test_dr33d_step7_counterexample_barrier_lock() -> None:
    s = Path("docs/math/DR33D_STEP_7_COUNTEREXAMPLE_BARRIER.md").read_text()
    assert "DR33D Step 7 — Counterexample Barrier for the Subquartic Bridge" in s
    assert r"E_j^{(N)}" in s
    assert r"\left(\sum_j 2^{-j}\bigl(E_j^{(N)}\bigr)^{1/2}\right)^2" in s
    assert r"\sum_j 2^{-2j}E_j^{(N)}" in s
    assert r"\sum_j 2^{-4j}\bigl(E_j^{(N)}\bigr)^2" in s
    assert "LOCKED BARRIER — new invariant still required." in s
