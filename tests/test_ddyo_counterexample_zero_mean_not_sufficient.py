import math
import numpy as np


def test_zero_shell_mean_does_not_imply_pairing_cancellation():
    n = 96
    grid = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    h = float(grid[1] - grid[0])
    X, Y, Z = np.meshgrid(grid, grid, grid, indexing="ij")

    u1 = np.zeros_like(X)
    u2 = np.zeros_like(X)
    u3 = np.sin(X)

    d_x_u3 = np.cos(X)

    S13 = 0.5 * d_x_u3
    omega2 = -d_x_u3

    mean_S13 = np.sum(S13) * (h**3)
    mean_omega2 = np.sum(omega2) * (h**3)
    pairing = np.sum(S13 * omega2) * (h**3)

    assert abs(mean_S13) < 1e-12
    assert abs(mean_omega2) < 1e-12
    assert pairing < -1.0

    exact_pairing = -0.5 * math.pi * (2.0 * math.pi) ** 2
    assert abs(pairing - exact_pairing) / abs(exact_pairing) < 5e-3
