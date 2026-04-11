import math
import numpy as np


def centered_offsets(n):
    idx = np.arange(n)
    return np.where(idx <= n // 2, idx, idx - n)


def make_even_gaussian_kernel(n, sigma_pts):
    m = centered_offsets(n).astype(float)
    K = np.exp(-(m**2) / (2.0 * sigma_pts**2))
    K /= np.sum(K)
    return K


def deriv(f, h):
    return (np.roll(f, -1) - np.roll(f, 1)) / (2.0 * h)


def scalar_hybrid_proxy_l1s(n=384, k=4, sigma_pts=2.0, phase=0.4, wphase=-0.3):
    x = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    h = float(x[1] - x[0])

    s = np.sin(k * x + phase)
    w = np.cos(k * x + wphase)

    sp = deriv(s, h)
    wp = deriv(w, h)

    K = make_even_gaussian_kernel(n, sigma_pts)
    m = centered_offsets(n).astype(float)
    y = np.arange(n)

    raw = np.zeros(n, dtype=float)
    first = np.zeros(n, dtype=float)

    for xi in range(n):
        off = (xi - y) % n
        dx = m[off] * h
        raw[xi] = np.sum(K[off] * (s[xi] - s[y]) * wp[y])
        first[xi] = np.sum(K[off] * (dx * sp[y]) * wp[y])

    raw *= h
    first *= h
    rem = raw - first

    l1_raw = np.sum(np.abs(raw)) * h
    l1_rem = np.sum(np.abs(rem)) * h
    return l1_raw, l1_rem


def test_hybrid_proxy_even_kernel_has_zero_signed_first_moment():
    n = 513
    K = make_even_gaussian_kernel(n, sigma_pts=3.0)
    m = centered_offsets(n).astype(float)
    signed_first_moment = float(np.sum(K * m))
    assert abs(signed_first_moment) < 1e-12


def test_hybrid_proxy_first_order_subtraction_reduces_commutator_l1():
    ratios = []
    for k in [2, 4, 8]:
        l1_raw, l1_rem = scalar_hybrid_proxy_l1s(n=384, k=k, sigma_pts=2.0)
        assert l1_raw > 1e-8
        assert l1_rem < 0.5 * l1_raw
        ratios.append(l1_rem / l1_raw)

    assert max(ratios) < 0.5
