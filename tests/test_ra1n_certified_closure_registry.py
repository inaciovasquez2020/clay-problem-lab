import subprocess
from pathlib import Path

def test_ra1n_certified_closure_registry_doc():
    s = Path("docs/status/RA1N_CERTIFIED_CLOSURE_REGISTRY.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM REGISTRY" in s
    assert "RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md" in s
    assert "gram_transversality_certificate.json" in s
    assert "projection_error_domination_certificate.json" in s
    assert "c_{\\mathrm{RA1n}}=2" in s
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)\\ge2>0" in s

def test_ra1n_certified_closure_registry_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_certified_closure_registry.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n certified closure registry verified." in r.stdout
