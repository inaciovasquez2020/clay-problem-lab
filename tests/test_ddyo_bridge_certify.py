import json
import subprocess
import tempfile
from pathlib import Path


def run_certify(payload):
    with tempfile.TemporaryDirectory() as td:
        fp = Path(td) / "payload.json"
        fp.write_text(json.dumps(payload))
        out = subprocess.check_output(
            ["python3", "src/ddyo/certify_from_pachner_graph.py", str(fp)]
        )
        return json.loads(out)


def test_certify_non_cancellation_squared_modulus():
    payload = {
        "Gamma_term_sharp_excludes_cancellation_loci": True,
        "epsilon_gamma": 0.25,
        "c0": 0.00018310546875,
        "a_curv": 1.52587890625e-05,
        "V_out": [1, 2, 3, 4],
        "E_out": [0.5, 0.25, 0.125, 0.0625],
        "X_gamma": [0.25, -0.5, 0.75, -1.0]
    }
    data = run_certify(payload)

    assert data["Gamma_term_sharp_excludes_cancellation_loci"] is True
    assert data["epsilon_gamma"] == 0.25
    assert data["sigma_lower"] == 0.0625
    assert data["kappa_lower"] > 0
    assert data["D_lower"] > 0
    assert data["a_curv"] > 0
    assert data["certified"] is True


def test_certify_fails_when_epsilon_gamma_zero():
    payload = {
        "Gamma_term_sharp_excludes_cancellation_loci": True,
        "epsilon_gamma": 0.0,
        "c0": 0.00018310546875,
        "a_curv": 1.52587890625e-05,
        "V_out": [1, 2, 3, 4],
        "E_out": [0.5, 0.25, 0.125, 0.0625],
        "X_gamma": [0.25, -0.5, 0.75, -1.0]
    }
    data = run_certify(payload)

    assert data["epsilon_gamma"] == 0.0
    assert data["sigma_lower"] == 0.0
    assert data["certified"] is False
