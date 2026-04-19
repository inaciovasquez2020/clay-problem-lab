from pathlib import Path

def test_admissible_patch_expansion_theorem_lock() -> None:
    s = Path("docs/math/ADMISSIBLE_PATCH_EXPANSION_THEOREM.md").read_text()
    assert "## Status" in s
    assert "CONDITIONAL" in s
    assert "P_{\\mathrm{adm}}" in s
    assert "\\xi \\not\\parallel \\eta" in s
    assert "\\lambda^{\\ast}_{\\mathrm{search}}" in s
    assert "Patch-to-global reduction" in s
    assert "terminal_high_high_resonance_curvature_gain" in s
