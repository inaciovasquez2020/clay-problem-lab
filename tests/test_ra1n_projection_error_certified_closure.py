import json
import subprocess
from fractions import Fraction
from pathlib import Path

def test_ra1n_projection_error_certified_closure_doc():
    s = Path("docs/math/RA1N_PROJECTION_ERROR_CERTIFIED_CLOSURE.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "projection-error domination condition" in s
    assert "\\mathrm{Curv}_k=2" in s
    assert "\\mathrm{Gap}_k=1" in s
    assert "\\|P_k\\widehat G_k\\|_{\\mathrm{err}}=0" in s
    assert "c_{\\mathrm{RA1n}}:=2" in s
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)\\ge c_{\\mathrm{RA1n}}>0" in s
    assert "certified closed by exact rational arithmetic" in s

def test_ra1n_projection_error_certificate_exact_margin():
    data = json.loads(Path("artifacts/ra1n/projection_error_domination_certificate.json").read_text())
    curvature = Fraction(data["curvature"])
    gap = Fraction(data["gap"])
    derivative_abs = Fraction(data["derivative_abs"])
    projection_error = Fraction(data["projection_error"])
    assert curvature * gap * derivative_abs - projection_error == 2
    assert curvature * gap * derivative_abs > projection_error

def test_ra1n_projection_error_certificate_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_projection_error_domination_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n projection-error domination verified" in r.stdout
    assert "margin = 2 > 0" in r.stdout
