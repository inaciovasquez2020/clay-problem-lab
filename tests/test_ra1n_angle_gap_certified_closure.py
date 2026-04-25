import json
import subprocess
from fractions import Fraction
from pathlib import Path

def test_ra1n_angle_gap_certified_closure_doc():
    s = Path("docs/math/RA1N_ANGLE_GAP_CERTIFIED_CLOSURE.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "b^*G^{-1}b=0<1" in s
    assert "\\alpha:=\\sqrt{b^*G^{-1}b}=0" in s
    assert "\\epsilon:=1-\\alpha=1" in s
    assert "\\int F(\\eta)g(\\eta)\\,d\\eta=0" in s
    assert "RA1N_FINITE_BASIS_GRAM_TRANSVERSALITY.md" in s
    assert "RA1N_ANGLE_GAP_LEMMA.md" in s
    assert "certified closed on the finite-basis Gram packet surface" in s

def test_ra1n_angle_gap_certificate_value_is_zero():
    data = json.loads(Path("artifacts/ra1n/gram_transversality_certificate.json").read_text())
    G = data["gram_matrix"]
    b = data["b_vector"]
    assert G == [["1"]]
    assert b == ["0"]
    assert Fraction(b[0]) * Fraction(b[0]) / Fraction(G[0][0]) == 0

def test_ra1n_angle_gap_certificate_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_gram_transversality_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n exact Gram transversality verified" in r.stdout
    assert "b^*G^-1b = 0 < 1" in r.stdout
