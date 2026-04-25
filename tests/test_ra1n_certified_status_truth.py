import subprocess

def test_ra1n_certified_status_truth_guard_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_certified_status_truth.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n certified status truth guard verified." in r.stdout
