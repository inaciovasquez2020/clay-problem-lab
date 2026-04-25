import subprocess

def test_ra1n_certified_pipeline_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_certified_pipeline.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n certified conditional pipeline verified." in r.stdout
