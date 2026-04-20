import json
import subprocess

def test_certify():
    out = subprocess.check_output(
        ["python3","src/ddyo/certify_from_pachner_graph.py","artifacts/pachner_outbound/sample_outbound.json"]
    )
    data = json.loads(out)
    assert "a_curv" in data
    assert data["certified"] in [True, False]
