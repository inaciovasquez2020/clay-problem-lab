import subprocess

def test_ra1n_terminal_frontier_chain_verifier_runs():
    r = subprocess.run(
        ["python3", "tools/verify_ra1n_terminal_frontier_chain.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "RA1n terminal frontier chain verified." in r.stdout
