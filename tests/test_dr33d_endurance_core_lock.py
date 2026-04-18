from pathlib import Path

def test_dr33d_endurance_core_locked() -> None:
    s = Path("docs/math/DR33D_ENDURANCE_CORE.md").read_text()
    assert "DR33D — Endurance Core (Unassigned)" in s
    assert r"\Theta(b,T):=\inf_u \mathcal E_T[u,b]" in s
    assert "Conditional monotonicity" in s
    assert r"\mathcal P_T[b]=\infty" in s
    assert "DR33D provisional wall" in s
