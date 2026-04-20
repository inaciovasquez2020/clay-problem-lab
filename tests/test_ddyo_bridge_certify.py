import json
import subprocess

def test_certify_uniform():
    out = subprocess.check_output(
        ["python3","src/ddyo/certify_from_pachner_graph.py","artifacts/pachner_outbound/sample_outbound.json"]
    )
    data = json.loads(out)

    assert data["sigma_lower"] > 0
    assert data["kappa_rank"] > 0
    assert data["D_lower"] > 0
    assert data["a_curv"] > 0
    assert data["certified"] is True
