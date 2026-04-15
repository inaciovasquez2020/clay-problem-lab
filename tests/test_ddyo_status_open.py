from pathlib import Path

def test_ddyo_status_open():
    p = Path("docs/status/DDYO_STATUS.md")
    s = p.read_text()
    assert "Status: OPEN" in s
    assert "No unconditional DDYO closure is claimed here." in s
