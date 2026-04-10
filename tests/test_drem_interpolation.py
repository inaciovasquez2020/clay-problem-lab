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


def scalar_lpnorm(f, p, h):
    return (np.sum(np.abs(f) ** p) * (h ** 3)) ** (1.0 / p)


def vector_lpnorm(v, p, h):
    mag = np.sqrt(np.sum(v * v, axis=0))
    return scalar_lpnorm(mag, p, h)


def grad_scalar(f, h):
    gx = grad_periodic(f, h, 0)
    gy = grad_periodic(f, h, 1)
    gz = grad_periodic(f, h, 2)
    return np.stack([gx, gy, gz], axis=0)


def gradient_l2_of_vorticity_power(w, h):
    mag = np.sqrt(np.sum(w * w, axis=0))
    f = np.power(np.maximum(mag, 1e-12), 0.75)
    gf = grad_scalar(f, h)
    return vector_lpnorm(gf, 2.0, h)


def test_drem_exact_rewrite_of_l94_term():
    X, Y, Z, h = make_grid(n=24)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)

    lhs = vector_lpnorm(w, 2.25, h) ** 1.5

    mag = np.sqrt(np.sum(w * w, axis=0))
    rhs = scalar_lpnorm(np.power(mag, 0.75), 3.0, h) ** 2

    assert abs(lhs - rhs) / max(lhs, 1e-12) < 1e-12


def test_drem_theta_is_one_half():
    theta = 0.5
    lhs = 1.0 / 3.0
    rhs = theta * (1.0 / 6.0) + (1.0 - theta) * (1.0 / 2.0)
    assert abs(lhs - rhs) < 1e-15


def test_drem_gn_form_on_torus_sample():
    X, Y, Z, h = make_grid(n=24)
    u = velocity_field(X, Y, Z)
    w = curl(u, h)

    mag = np.sqrt(np.sum(w * w, axis=0))
    f = np.power(np.maximum(mag, 1e-12), 0.75)

    lhs = scalar_lpnorm(f, 3.0, h) ** 2
    a = gradient_l2_of_vorticity_power(w, h)
    b = scalar_lpnorm(f, 2.0, h)

    rhs = (a * b)

    assert lhs <= 10.0 * max(rhs, 1e-12)
