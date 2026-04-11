import numpy as np


def integer_freqs(n: int) -> np.ndarray:
    return np.fft.fftfreq(n, d=1.0 / n)


def freq_mesh(n: int):
    k = integer_freqs(n)
    return np.meshgrid(k, k, k, indexing="ij")


def exact_shell_mask(n: int, r2: int) -> np.ndarray:
    KX, KY, KZ = freq_mesh(n)
    return ((KX * KX + KY * KY + KZ * KZ) == r2).astype(float)


def deviatoric_multiplier(n: int, a: int, b: int, r2: int) -> np.ndarray:
    KX, KY, KZ = freq_mesh(n)
    ks = [KX, KY, KZ]
    denom = KX * KX + KY * KY + KZ * KZ
    out = np.zeros_like(KX, dtype=float)
    nz = denom > 0
    out[nz] = (ks[a][nz] * ks[b][nz]) / denom[nz]
    if a == b:
        out[nz] -= 1.0 / 3.0
    out *= exact_shell_mask(n, r2)
    return out


def apply_multiplier(f: np.ndarray, m: np.ndarray) -> np.ndarray:
    return np.fft.ifftn(m * np.fft.fftn(f)).real


def low_frequency_energy_ratio(f: np.ndarray, cutoff2: int) -> float:
    F = np.fft.fftn(f)
    KX, KY, KZ = freq_mesh(f.shape[0])
    low = (KX * KX + KY * KY + KZ * KZ) <= cutoff2
    num = float(np.sum(np.abs(F[low]) ** 2))
    den = float(np.sum(np.abs(F) ** 2))
    return 0.0 if den == 0.0 else num / den


def shell_fields(n: int = 64, k0: int = 4):
    x = 2.0 * np.pi * np.arange(n) / n
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    G = np.sin(k0 * (X - Y))
    omega = np.cos(k0 * (X + Y))
    return G, omega


def shell_support_ratio(f: np.ndarray, r2: int) -> float:
    F = np.fft.fftn(f)
    mask = exact_shell_mask(f.shape[0], r2).astype(bool)
    num = float(np.sum(np.abs(F[~mask]) ** 2))
    den = float(np.sum(np.abs(F) ** 2))
    return 0.0 if den == 0.0 else num / den


def test_deviatoric_multiplier_preserves_exact_shell_support():
    n = 64
    k0 = 4
    r2 = 2 * k0 * k0
    _, omega = shell_fields(n=n, k0=k0)
    m = deviatoric_multiplier(n, 0, 1, r2)
    zeta = apply_multiplier(omega, m)
    assert shell_support_ratio(zeta, r2) < 1e-24


def test_shell_product_has_zero_mean_for_off_diagonal_deviatoric_piece():
    n = 64
    k0 = 4
    r2 = 2 * k0 * k0
    G, omega = shell_fields(n=n, k0=k0)
    m = deviatoric_multiplier(n, 0, 1, r2)
    zeta = apply_multiplier(omega, m)
    product = G * zeta
    assert abs(float(np.mean(product))) < 1e-14
    assert low_frequency_energy_ratio(product, cutoff2=1) < 1e-24


def test_shell_product_has_zero_mean_for_diagonal_deviatoric_piece():
    n = 64
    k0 = 4
    r2 = 2 * k0 * k0
    G, omega = shell_fields(n=n, k0=k0)
    m = deviatoric_multiplier(n, 0, 0, r2)
    zeta = apply_multiplier(omega, m)
    product = G * zeta
    assert abs(float(np.mean(product))) < 1e-14
    assert low_frequency_energy_ratio(product, cutoff2=1) < 1e-24
