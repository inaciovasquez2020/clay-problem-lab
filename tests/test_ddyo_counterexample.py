import math
import numpy as np


def deriv(f, h, axis):
    return (np.roll(f, -1, axis=axis) - np.roll(f, 1, axis=axis)) / (2.0 * h)


def laplacian(f, h):
    out = np.zeros_like(f)
    for axis in (-3, -2, -1):
        out += (np.roll(f, -1, axis=axis) - 2.0 * f + np.roll(f, 1, axis=axis)) / (
            h * h
        )
    return out


def test_incompressible_velocity_can_have_non_divergence_free_strain():
    n = 48
    grid = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    h = float(grid[1] - grid[0])
    X, Y, Z = np.meshgrid(grid, grid, grid, indexing="ij")

    u = np.stack(
        [
            np.sin(Y),
            np.sin(Z),
            np.sin(X),
        ],
        axis=0,
    )

    grad = np.zeros((3, 3, n, n, n), dtype=float)
    spatial_axes = (-3, -2, -1)
    for a in range(3):
        for b, axis in enumerate(spatial_axes):
            grad[a, b] = deriv(u[a], h, axis)

    div_u = grad[0, 0] + grad[1, 1] + grad[2, 2]
    assert np.max(np.abs(div_u)) < 1e-12

    S = 0.5 * (grad + np.swapaxes(grad, 0, 1))

    div_S = np.zeros((3, n, n, n), dtype=float)
    for a in range(3):
        for b, axis in enumerate(spatial_axes):
            div_S[a] += deriv(S[a, b], h, axis)

    half_lap_u = 0.5 * np.stack([laplacian(u[a], h) for a in range(3)], axis=0)

    assert np.max(np.abs(div_S - half_lap_u)) < 1e-2
    assert np.max(np.abs(div_S)) > 0.2
