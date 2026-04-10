import math
import numpy as np


def make_grid(n=64, L=2.0 * math.pi):
    x = np.linspace(0.0, L, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    return X, Y, Z, L / n


def base_velocity_shell(X, Y, Z, k=4):
    u1 = np.sin(k * Y)
    u2 = np.sin(k * Z)
    u3 = np.sin(k * X)
    return np.stack([u1, u2, u3], axis=0)


def scaled_field_from_base(X, Y, Z, mu=2.0, k=4):
    return mu * base_velocity_shell(mu * X, mu * Y, mu * Z, k=k)


def fftfreq_integer(n):
    return np.fft.fftfreq(n, d=1.0 / n)


def shell_mask(n, j):
    freq = fftfreq_integer(n)
    KX, KY, KZ = np.meshgrid(freq, freq, freq, indexing="ij")
    M = np.maximum.reduce([np.abs(KX), np.abs(KY), np.abs(KZ)])
    lo = 2 ** j
    hi = 2 ** (j + 1)
    return (M >= lo) & (M < hi)


def bandpass(u, j):
    n = u.shape[1]
    mask = shell_mask(n, j)
    out = np.zeros_like(u, dtype=float)
    for c in range(3):
        uh = np.fft.fftn(u[c])
        bh = uh * mask
        out[c] = np.fft.ifftn(bh).real
    return out


def vector_linf(v):
    mag = np.sqrt(np.sum(v * v, axis=0))
    return float(np.max(mag))


def ddyo_residual_velocity(u):
    n = u.shape[1]
    jmax = int(math.log2(n // 2))
    vals = []
    for j in range(jmax + 1):
        dj = bandpass(u, j)
        vals.append((2.0 ** (-j)) * vector_linf(dj))
    return max(vals) if vals else 0.0


def test_ddyo_residual_nonnegative():
    X, Y, Z, _ = make_grid(n=32)
    u = base_velocity_shell(X, Y, Z, k=4)
    r = ddyo_residual_velocity(u)
    assert r >= 0.0


def test_ddyo_single_shell_localization():
    X, Y, Z, _ = make_grid(n=64)
    u = base_velocity_shell(X, Y, Z, k=4)

    ref = vector_linf(bandpass(u, 2))
    assert ref > 1e-6

    for j in [0, 1, 3, 4, 5]:
        err = vector_linf(bandpass(u, j))
        assert err <= 1e-10 * ref + 1e-12


def test_ddyo_velocity_envelope_torus_integer_dilation_invariant():
    X, Y, Z, _ = make_grid(n=64)
    u = base_velocity_shell(X, Y, Z, k=4)
    r1 = ddyo_residual_velocity(u)

    mu = 2.0
    X2, Y2, Z2, _ = make_grid(n=128)
    u2 = scaled_field_from_base(X2, Y2, Z2, mu=mu, k=4)
    r2 = ddyo_residual_velocity(u2)

    assert abs(r1 - r2) / max(r1, 1e-12) < 1e-10
