import subprocess

def test_ra1n_all_certified_surfaces_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_all_certified_surfaces.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n all certified surfaces verified." in r.stdout
