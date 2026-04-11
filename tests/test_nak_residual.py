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


def scaled_field_from_base(X, Y, Z, mu):
    return mu * velocity_field(mu * X, mu * Y, mu * Z)


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


def drem_residual(w, h):
    mag = np.sqrt(np.sum(w * w, axis=0))
    return np.sum(mag**1.5) * (h**3)


def principal_eigenvector_field(S):
    A = np.moveaxis(S, (0, 1), (-2, -1))
    flat = A.reshape((-1, 3, 3))
    vals, vecs = np.linalg.eigh(flat)
    e1 = vecs[:, :, -1]
    shp = S.shape[2:]
    return e1.reshape(shp + (3,)).transpose(3, 0, 1, 2)


def alignment_defect(w, S, eps=1e-12):
    mag = np.sqrt(np.sum(w * w, axis=0))
    what = w / np.maximum(mag, eps)
    e1 = principal_eigenvector_field(S)
    dot = np.sum(what * e1, axis=0)
    defect = 1.0 - dot**2
    return np.clip(defect, 0.0, 1.0)


def nak_residual(w, S, h):
    mag = np.sqrt(np.sum(w * w, axis=0))
    defect = alignment_defect(w, S)
    return np.sum(defect * (mag**1.5)) * (h**3)


def test_nak_residual_nonnegative():
    X, Y, Z, h = make_grid(n=16)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    r = nak_residual(w, S, h)
    assert r >= 0.0


def test_nak_residual_bounded_by_drem():
    X, Y, Z, h = make_grid(n=16)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    r_nak = nak_residual(w, S, h)
    r_drem = drem_residual(w, h)
    assert r_nak <= r_drem * (1.0 + 1e-9)


def test_nak_alignment_defect_in_unit_interval():
    X, Y, Z, h = make_grid(n=12)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    defect = alignment_defect(w, S)
    assert np.min(defect) >= -1e-12
    assert np.max(defect) <= 1.0 + 1e-12


def test_nak_torus_integer_dilation_scales_cubically():
    X, Y, Z, h = make_grid(n=24)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    r1 = nak_residual(w, S, h)

    mu = 2.0
    X2, Y2, Z2, h2 = make_grid(n=48)
    u2 = scaled_field_from_base(X2, Y2, Z2, mu=mu)
    w2 = curl(u2, h2)
    S2 = sym_grad(u2, h2)
    r2 = nak_residual(w2, S2, h2)

    assert abs(r2 - (mu**3) * r1) / max((mu**3) * r1, 1e-12) < 7e-2
