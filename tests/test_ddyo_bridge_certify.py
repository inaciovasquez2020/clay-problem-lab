import json
import subprocess

def test_certify_analytic():
    out = subprocess.check_output(
        ["python3","src/ddyo/certify_from_pachner_graph.py","artifacts/pachner_outbound/sample_outbound.json"]
    )
    data = json.loads(out)

    assert data["c0"] > 0
    assert data["a_curv"] > 0
    assert data["kappa_lower"] > 0
    assert data["D_lower"] > 0
    assert data["certified"] is True
