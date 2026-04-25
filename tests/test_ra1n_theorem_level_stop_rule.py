from pathlib import Path

DOC = Path("docs/status/RA1N_THEOREM_LEVEL_STOP_RULE.md")

def test_status():
    s = DOC.read_text()
    assert "Status: STOP RULE" in s

def test_stop_condition():
    s = DOC.read_text()
    assert "\\mathcal A_{\\mathrm{term}}(\\chi)" in s
    assert "\\mathcal R_{\\mathrm{term}}(\\chi)=0" in s
    assert "No further progress possible without new input." in s

def test_no_wrapper_rule():
    s = DOC.read_text()
    assert "No additional certificate wrapper" in s
    assert "actual admissibility predicate" in s
