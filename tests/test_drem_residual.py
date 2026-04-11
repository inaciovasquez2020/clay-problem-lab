import math
import numpy as np


def make_grid(n=24, L=2.0 * math.pi):
    x = np.linspace(0.0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    return X, Y, Z, L / n


def velocity_field(X, Y, Z):
    u1 = np.sin(Y) + 0.5 * np.cos(Z)
    u2 = np.sin(Z) + 0.5 * np.cos(X)
    u3 = np.sin(X) + 0.5 * np.cos(Y)
    return np.stack([u1, u2, u3], axis=0)


def grad_periodic(f, h, axis):
    return (np.roll(f, -1, axis=axis) - np.roll(f, 1, axis=axis)) / (2.0 * h)


def curl(u, h):
    u1, u2, u3 = u
    w1 = grad_periodic(u3, h, 1) - grad_periodic(u2, h, 2)
    w2 = grad_periodic(u1, h, 2) - grad_periodic(u3, h, 0)
    w3 = grad_periodic(u2, h, 0) - grad_periodic(u1, h, 1)
    return np.stack([w1, w2, w3], axis=0)


def sym_grad(u, h):
    g = np.zeros((3, 3) + u.shape[1:], dtype=float)
    for i in range(3):
        for j in range(3):
            g[i, j] = grad_periodic(u[i], h, j)
    return 0.5 * (g + np.swapaxes(g, 0, 1))


def lpnorm_scalar(f, p, h):
    return (np.sum(np.abs(f) ** p) * (h**3)) ** (1.0 / p)


def lpnorm_tensor(T, p, h):
    mag = np.sqrt(np.sum(T * T, axis=tuple(range(2))))
    return lpnorm_scalar(mag, p, h)


def lpnorm_vector(v, p, h):
    mag = np.sqrt(np.sum(v * v, axis=0))
    return lpnorm_scalar(mag, p, h)


def drem_residual(w, h):
    mag = np.sqrt(np.sum(w * w, axis=0))
    return np.sum(np.abs(mag) ** 1.5) * (h**3)


def stretch_positive_sigma(S, w, h, eps=1e-12):
    mag = np.sqrt(np.sum(w * w, axis=0))
    what = w / np.maximum(mag, eps)
    quad = np.einsum("i...,ij...,j...->...", what, S, what)
    pos = np.maximum(quad, 0.0)
    return np.sum(pos * (mag**1.5)) * (h**3)


def scaled_field_from_base(X, Y, Z, mu):
    return mu * velocity_field(mu * X, mu * Y, mu * Z)


def test_drem_torus_integer_dilation_scales_cubically():
    X, Y, Z, h = make_grid(n=24)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    r1 = drem_residual(w, h)

    mu = 2.0
    X2, Y2, Z2, h2 = make_grid(n=48)
    u2 = scaled_field_from_base(X2, Y2, Z2, mu=mu)
    w2 = curl(u2, h2)
    r2 = drem_residual(w2, h2)

    assert abs(r2 - (mu**3) * r1) / max((mu**3) * r1, 1e-12) < 5e-2


def test_drem_holder_structure():
    X, Y, Z, h = make_grid(n=24)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)

    sigma = stretch_positive_sigma(S, w, h)
    lhs = sigma
    rhs = lpnorm_tensor(S, 3.0, h) * (lpnorm_vector(w, 2.25, h) ** 1.5)

    assert lhs <= rhs * (1.0 + 1e-9)


def test_drem_residual_nonnegative():
    X, Y, Z, h = make_grid(n=16)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    r = drem_residual(w, h)
    assert r >= 0.0
