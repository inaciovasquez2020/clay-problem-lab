import subprocess

experiments = [
    "riemann/experiments/core/zero_spacing.py",
    "navier_stokes/experiments/core/enstrophy_growth.py",
    "yang_mills/experiments/core/transfer_gap.py",
    "complexity/experiments/core/entropy_depth.py",
    "bsd/experiments/core/rank_sample.py",
    "hodge/experiments/core/hodge_numbers.py",
]

for exp in experiments:
    print("\nRunning:", exp)
    subprocess.run(["python3", exp])
