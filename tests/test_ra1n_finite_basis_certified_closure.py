import json
import subprocess
from fractions import Fraction
from pathlib import Path

def test_ra1n_finite_basis_certified_closure_doc():
    s = Path("docs/math/RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "b^*G^{-1}b<1" in s
    assert "G=[1]" in s
    assert "b=[0]" in s
    assert "b^*G^{-1}b=0<1" in s
    assert "h\\notin V_{\\mathrm{RA1n}}" in s
    assert "\\epsilon" in s
    assert "\\int Fg=0" in s
    assert "certified closed on the exact rational packet surface" in s

def test_ra1n_finite_basis_certificate_exact_value():
    data = json.loads(Path("artifacts/ra1n/gram_transversality_certificate.json").read_text())
    G = [[Fraction(x) for x in row] for row in data["gram_matrix"]]
    b = [Fraction(x) for x in data["b_vector"]]
    assert G == [[Fraction(1)]]
    assert b == [Fraction(0)]
    assert b[0] * b[0] / G[0][0] == 0
    assert b[0] * b[0] / G[0][0] < 1

def test_ra1n_finite_basis_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_gram_transversality_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n exact Gram transversality verified" in r.stdout
    assert "b^*G^-1b = 0 < 1" in r.stdout
