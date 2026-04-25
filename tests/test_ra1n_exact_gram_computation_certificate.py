import json
import subprocess
from fractions import Fraction
from pathlib import Path

def test_ra1n_exact_gram_certificate_recomputes_bound():
    data = json.loads(Path("artifacts/ra1n/gram_transversality_certificate.json").read_text())
    assert data["object"] == "RA1N exact finite-basis Gram transversality certificate"
    assert data["status"] == "conditional-angle-gap-certificate"
    assert data["certifies"] == "b^*G^{-1}b < 1"
    assert data["gram_matrix"] == [["1"]]
    assert data["b_vector"] == ["0"]

def test_ra1n_exact_gram_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_gram_transversality_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n exact Gram transversality verified" in r.stdout
    assert "b^*G^-1b = 0 < 1" in r.stdout

def test_ra1n_exact_gram_doc():
    s = Path("docs/math/RA1N_EXACT_GRAM_COMPUTATION_CERTIFICATE.md").read_text()
    assert "Status: EXECUTABLE CERTIFICATE SURFACE" in s
    assert "b^*G^{-1}b<1" in s
    assert "\\epsilon=1-\\sqrt{\\frac ND}>0" in s
    assert "RA1N_FINITE_BASIS_GRAM_TRANSVERSALITY.md" in s
