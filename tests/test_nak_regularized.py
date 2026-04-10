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
    return np.sum(mag ** 1.5) * (h ** 3)


def matrix_exp_symmetric_field(S, tau):
    A = np.moveaxis(S, (0, 1), (-2, -1))
    flat = A.reshape((-1, 3, 3))
    out = np.zeros_like(flat)
    for m, M in enumerate(flat):
        vals, vecs = np.linalg.eigh(M)
        out[m] = vecs @ np.diag(np.exp(tau * vals)) @ vecs.T
    shp = S.shape[2:]
    return out.reshape(shp + (3, 3)).transpose(3, 4, 0, 1, 2)


def regularized_projector(S, tau=4.0):
    E = matrix_exp_symmetric_field(S, tau=tau)
    tr = np.trace(np.moveaxis(E, (0, 1), (-2, -1)), axis1=-2, axis2=-1)
    return E / np.maximum(tr, 1e-12)


def regularized_alignment_defect(w, S, tau=4.0, eps=1e-12):
    mag = np.sqrt(np.sum(w * w, axis=0))
    what = w / np.maximum(mag, eps)
    P = regularized_projector(S, tau=tau)
    q = np.einsum("i...,ij...,j...->...", what, P, what)
    defect = 1.0 - q
    return np.clip(defect, 0.0, 1.0)


def nak_regularized_residual(w, S, h, tau=4.0):
    mag = np.sqrt(np.sum(w * w, axis=0))
    defect = regularized_alignment_defect(w, S, tau=tau)
    return np.sum(defect * (mag ** 1.5)) * (h ** 3)


def test_regularized_nak_defect_in_unit_interval():
    X, Y, Z, h = make_grid(n=12)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    defect = regularized_alignment_defect(w, S, tau=4.0)
    assert np.min(defect) >= -1e-12
    assert np.max(defect) <= 1.0 + 1e-12


def test_regularized_nak_residual_nonnegative():
    X, Y, Z, h = make_grid(n=16)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    r = nak_regularized_residual(w, S, h, tau=4.0)
    assert r >= 0.0


def test_regularized_nak_residual_bounded_by_drem():
    X, Y, Z, h = make_grid(n=16)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    r_reg = nak_regularized_residual(w, S, h, tau=4.0)
    r_drem = drem_residual(w, h)
    assert r_reg <= r_drem * (1.0 + 1e-9)


def test_regularized_nak_torus_integer_dilation_scales_cubically():
    X, Y, Z, h = make_grid(n=24)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    r1 = nak_regularized_residual(w, S, h, tau=4.0)

    mu = 2.0
    X2, Y2, Z2, h2 = make_grid(n=48)
    u2 = scaled_field_from_base(X2, Y2, Z2, mu=mu)
    w2 = curl(u2, h2)
    S2 = sym_grad(u2, h2)
    r2 = nak_regularized_residual(w2, S2, h2, tau=4.0)

    assert abs(r2 - (mu ** 3) * r1) / max((mu ** 3) * r1, 1e-12) < 8e-2


def test_regularized_projector_trace_one():
    X, Y, Z, h = make_grid(n=10)
    u = velocity_field(X, Y, Z)
    S = sym_grad(u, h)
    P = regularized_projector(S, tau=4.0)
    tr = np.trace(np.moveaxis(P, (0, 1), (-2, -1)), axis1=-2, axis2=-1)
    assert np.max(np.abs(tr - 1.0)) < 1e-10
