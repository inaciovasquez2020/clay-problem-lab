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


def grad_vector(v, h):
    g = np.zeros((3, 3) + v.shape[1:], dtype=float)
    for i in range(3):
        for j in range(3):
            g[i, j] = grad_periodic(v[i], h, j)
    return g


def grad_matrix(M, h):
    g = np.zeros((3, 3, 3) + M.shape[2:], dtype=float)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                g[i, j, k] = grad_periodic(M[i, j], h, k)
    return g


def sym_grad(u, h):
    g = grad_vector(u, h)
    return 0.5 * (g + np.swapaxes(g, 0, 1))


def tensor_pointwise_norm(T):
    component_axes = tuple(range(T.ndim - 3))
    return np.sqrt(np.sum(T * T, axis=component_axes))


def drem_residual(w, h):
    mag = np.sqrt(np.sum(w * w, axis=0))
    return np.sum(mag ** 1.5) * (h ** 3)


def j2b_residual(grad_w, h):
    mag = tensor_pointwise_norm(grad_w)
    return np.sum(mag) * (h ** 3)


def j2b_sigma(grad_S, grad_w, h):
    magS = tensor_pointwise_norm(grad_S)
    magW = tensor_pointwise_norm(grad_w)
    return np.sum(magS * magW) * (h ** 3)


def test_j2b_residual_nonnegative():
    X, Y, Z, h = make_grid(n=16)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    grad_w = grad_vector(w, h)
    r = j2b_residual(grad_w, h)
    assert r >= 0.0


def test_j2b_torus_integer_dilation_scales_cubically():
    X, Y, Z, h = make_grid(n=24)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    grad_w = grad_vector(w, h)
    r1 = j2b_residual(grad_w, h)

    mu = 2.0
    X2, Y2, Z2, h2 = make_grid(n=48)
    u2 = scaled_field_from_base(X2, Y2, Z2, mu=mu)
    w2 = curl(u2, h2)
    grad_w2 = grad_vector(w2, h2)
    r2 = j2b_residual(grad_w2, h2)

    assert abs(r2 - (mu ** 3) * r1) / max((mu ** 3) * r1, 1e-12) < 7e-2


def test_j2b_sigma_holder_l1_linf_form():
    X, Y, Z, h = make_grid(n=20)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    S = sym_grad(u, h)
    grad_w = grad_vector(w, h)
    grad_S = grad_matrix(S, h)

    lhs = j2b_sigma(grad_S, grad_w, h)
    magS = tensor_pointwise_norm(grad_S)
    rhs = np.max(magS) * j2b_residual(grad_w, h) * (1.0 + 1e-9)

    assert lhs <= rhs


def test_j2b_residual_dominates_no_more_than_sampled_higher_norm():
    X, Y, Z, h = make_grid(n=20)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)
    grad_w = grad_vector(w, h)
    mag = tensor_pointwise_norm(grad_w)
    l1 = np.sum(mag) * (h ** 3)
    l12 = (np.sum(mag ** 1.2) * (h ** 3)) ** (1.0 / 1.2)
    volume = (2.0 * math.pi) ** 3
    rhs = (volume ** (1.0 - 1.0 / 1.2)) * l12
    assert l1 <= rhs * (1.0 + 1e-9)
