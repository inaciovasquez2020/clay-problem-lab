from pathlib import Path

def test_ddyo_terminal_window_gain_frontier_doc_contains_canonical_object():
    s = Path("docs/math/DDYO_TERMINAL_WINDOW_GAIN_FRONTIER.md").read_text()
    assert "Conditional: DDYO terminal window-gain frontier" in s
    assert "\\mathcal A_\\ell(t):=" in s
    assert "\\mathcal R_K(t)\\le \\mathcal D_K(t)" in s
    assert "Open Problem." in s
    assert "2^{(2+\\sigma)\\ell}" in s
