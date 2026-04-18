from pathlib import Path

def test_dr33d_step46_shell_exclusion_normal_form_lock() -> None:
    s = Path("docs/math/DR33D_STEP_46_SHELL_EXCLUSION_NORMAL_FORM.md").read_text()
    assert "DR33D Step 46 — Shell-Exclusion Normal Form" in s
    assert "Conditional." in s
    assert r"E_{j+1}(u)\le E_j(u)" in s
    assert r"E_j(u)=0\ (j<j_0)" in s
    assert r"\mathfrak C(E(u))\le 1-\delta" in s
    assert r"S(E(u))\ge m" in s
    assert "one-shell vanishing concentration" in s
    assert "block-monotone vanishing concentration" in s
