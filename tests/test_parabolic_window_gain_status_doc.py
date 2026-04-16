from pathlib import Path

def test_parabolic_window_gain_status_doc_contains_open_terminal_wall():
    s = Path("docs/status/PARABOLIC_WINDOW_GAIN_STATUS.md").read_text()
    assert "# Parabolic Window Gain Status" in s
    assert "Status: OPEN" in s
    assert "single canonical obstruction" in s
    assert "No full solve is claimed." in s
