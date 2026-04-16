from pathlib import Path

def test_ddyo_terminal_window_gain_status_doc_contains_open_missing_object():
    s = Path("docs/status/DDYO_TERMINAL_WINDOW_GAIN_STATUS.md").read_text()
    assert "Status: OPEN" in s
    assert "Canonical missing object:" in s
    assert "\\mathcal R_K(t)\\le \\mathcal D_K(t)" in s
    assert "2^{2\\ell}" in s
    assert "2^{(2+\\sigma)\\ell}" in s
