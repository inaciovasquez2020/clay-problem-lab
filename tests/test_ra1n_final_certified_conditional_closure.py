import subprocess
from pathlib import Path

def test_ra1n_final_certified_conditional_closure_doc():
    s = Path("docs/math/RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md").read_text()
    assert "Status: CERTIFIED CONDITIONAL THEOREM" in s
    assert "\\mathcal P_{\\mathrm{RA1n}}^{\\mathrm{terminal}}" in s
    assert "b^*G^{-1}b=0<1" in s
    assert "\\epsilon=1" in s
    assert "\\int Fg=0" in s
    assert "c_{\\mathrm{RA1n}}:=2" in s
    assert "\\mathcal T_{\\mathrm{RA1n}}(k)" in s
    assert "RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CLOSURE.md" in s
    assert "RA1n is certified closed on the conditional finite-basis packet-exhausted surface" in s

def test_ra1n_final_certified_closure_verifiers_run():
    gram = subprocess.run(
        ["python3", "tools/verify_ra1n_gram_transversality_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    proj = subprocess.run(
        ["python3", "tools/verify_ra1n_projection_error_domination_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "b^*G^-1b = 0 < 1" in gram.stdout
    assert "margin = 2 > 0" in proj.stdout
