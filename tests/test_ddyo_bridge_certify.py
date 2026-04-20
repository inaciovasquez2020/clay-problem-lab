import json
import subprocess


def test_certify_non_cancellation_squared_modulus():
    out = subprocess.check_output(
        ["python3", "src/ddyo/certify_from_pachner_graph.py", "artifacts/pachner_outbound/sample_outbound.json"]
    )
    data = json.loads(out)

    assert data["Gamma_term_sharp_excludes_cancellation_loci"] is True
    assert data["x_gamma_min_abs"] == 0.25
    assert data["sigma_lower"] == 0.0625
    assert data["kappa_lower"] > 0
    assert data["D_lower"] > 0
    assert data["a_curv"] > 0
    assert data["certified"] is True
