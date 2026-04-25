import subprocess

def test_ra1n_no_overclaim_frontier_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_no_overclaim_frontier.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n no-overclaim frontier verified." in r.stdout
