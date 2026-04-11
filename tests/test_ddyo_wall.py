import math
import numpy as np


TWOPI = 2.0 * math.pi


def make_grid(n=24):
    x = np.linspace(0.0, TWOPI, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    h = TWOPI / n
    return X, Y, Z, h


def kgrid(n):
    k = np.fft.fftfreq(n, d=1.0 / n)
    return np.meshgrid(k, k, k, indexing="ij")


def spectral_derivative_scalar(f, axis):
    n = f.shape[0]
    K = kgrid(n)
    F = np.fft.fftn(f)
    return np.fft.ifftn(1j * K[axis] * F).real


def spectral_derivative_vector(v, axis):
    return np.stack([spectral_derivative_scalar(v[c], axis) for c in range(3)], axis=0)


def grad_vector(v):
    return np.stack([spectral_derivative_vector(v, a) for a in range(3)], axis=1)


def curl(v):
    J = grad_vector(v)
    return np.stack(
        [
            J[2, 1] - J[1, 2],
            J[0, 2] - J[2, 0],
            J[1, 0] - J[0, 1],
        ],
        axis=0,
    )


def sym_grad(v):
    J = grad_vector(v)
    return 0.5 * (J + np.swapaxes(J, 0, 1))


def skew_grad(v):
    J = grad_vector(v)
    return 0.5 * (J - np.swapaxes(J, 0, 1))


def bandpass_scalar(f, j):
    n = f.shape[0]
    Kx, Ky, Kz = kgrid(n)
    r = np.sqrt(Kx * Kx + Ky * Ky + Kz * Kz)
    lo = 0.0 if j == 0 else 2.0 ** (j - 1)
    hi = 2.0 ** (j + 1)
    mask = (r >= lo - 1e-12) & (r < hi - 1e-12)
    F = np.fft.fftn(f)
    return np.fft.ifftn(F * mask).real


def bandpass_vector(v, j):
    return np.stack([bandpass_scalar(v[c], j) for c in range(3)], axis=0)


def volume_integral(f, h):
    return float(np.sum(f) * (h**3))


def pointwise_norm(v):
    return np.sqrt(np.sum(v * v, axis=0))


def tensor_pointwise_norm(T):
    return np.sqrt(np.sum(T * T, axis=(0, 1)))


def hprime(v, eps=1e-12):
    mag = np.maximum(pointwise_norm(v), eps)
    return v / np.power(mag, 2.0 / 3.0)


def h_density(v, eps=1e-12):
    mag = np.maximum(pointwise_norm(v), eps)
    return 0.75 * np.power(mag, 4.0 / 3.0)


def lp_norm_vector(v, p, h):
    mag = pointwise_norm(v)
    return float(np.power(np.sum(np.power(mag, p)) * (h**3), 1.0 / p))


def advection(u, w):
    Gw = grad_vector(w)
    return np.einsum("a...,ca...->c...", u, Gw)


def stretch(w, u):
    Ju = grad_vector(u)
    return np.einsum("a...,ca...->c...", w, Ju)


def strain_action(S, w):
    return np.einsum("ab...,b...->a...", S, w)


def skew_action(A, w):
    return np.einsum("ab...,b...->a...", A, w)


def pair_term(uj, wj, uk, wk, k, h):
    integrand = np.sum(hprime(wk) * (-advection(uj, wk) + stretch(wj, uk)), axis=0)
    return (2.0 ** (2 * k)) * volume_integral(integrand, h)


def advective_hh_term(uj, wj, j, h):
    integrand = np.sum(hprime(wj) * (-advection(uj, wj)), axis=0)
    return (2.0 ** (2 * j)) * volume_integral(integrand, h)


def skew_hh_term(Aj, wj, j, h):
    integrand = np.sum(hprime(wj) * skew_action(Aj, wj), axis=0)
    return (2.0 ** (2 * j)) * volume_integral(integrand, h)


def strain_hh_term(Sj, wj, j, h):
    integrand = np.sum(hprime(wj) * strain_action(Sj, wj), axis=0)
    return (2.0 ** (2 * j)) * volume_integral(integrand, h)


def positive_strain_hh_term(Sj, wj, j, h):
    integrand = np.sum(hprime(wj) * strain_action(Sj, wj), axis=0)
    return (2.0 ** (2 * j)) * volume_integral(np.maximum(integrand, 0.0), h)


def shell_residual(wj, j, h):
    return (2.0 ** (2 * j)) * volume_integral(h_density(wj), h)


def max_eigenvalue_field(S):
    M = np.moveaxis(S, (0, 1), (-2, -1))
    return np.linalg.eigvalsh(M)[..., -1]


def active_set_mask(wj, j, h):
    threshold = (2.0 ** (-j)) * lp_norm_vector(wj, 4.0 / 3.0, h)
    return pointwise_norm(wj) >= threshold


def active_lambda_max(Sj, wj, j, h):
    lam = np.maximum(max_eigenvalue_field(Sj), 0.0)
    mask = active_set_mask(wj, j, h)
    if not np.any(mask):
        return 0.0
    return float(np.max(lam[mask]))


def base_velocity_shell(X, Y, Z, k=4):
    return np.stack(
        [
            np.sin(k * Y) + np.cos(k * Z),
            np.sin(k * Z) + np.cos(k * X),
            np.sin(k * X) + np.cos(k * Y),
        ],
        axis=0,
    )


def aligned_multishell_velocity(X, Y, Z):
    return (
        1.00 * base_velocity_shell(X, Y, Z, k=2)
        + 0.70 * base_velocity_shell(X, Y, Z, k=4)
        + 0.35 * base_velocity_shell(X, Y, Z, k=8)
    )


def scaled_field_from_base(X, Y, Z, mu=2.0, k=4):
    return base_velocity_shell(mu * X, mu * Y, mu * Z, k=k)


def shell_index_for_frequency(k):
    return int(round(math.log2(k)))


def test_ddyo_pair_partition_is_exact():
    X, Y, Z, h = make_grid(n=24)
    u = aligned_multishell_velocity(X, Y, Z)
    w = curl(u)

    jmax = 5
    k0 = 2
    us = [bandpass_vector(u, j) for j in range(jmax + 1)]
    ws = [bandpass_vector(w, j) for j in range(jmax + 1)]

    total = 0.0
    ll = 0.0
    lh = 0.0
    hl = 0.0
    hh = 0.0

    for j in range(jmax + 1):
        for k in range(jmax + 1):
            term = pair_term(us[j], ws[j], us[k], ws[k], k, h)
            total += term
            if j <= k - 4:
                if k <= k0:
                    ll += term
                else:
                    lh += term
            elif k <= j - 4:
                hl += term
            else:
                hh += term

    assert abs(total - (ll + lh + hl + hh)) <= 1e-10 * max(1.0, abs(total))


def test_ddyo_hh_advective_cancellation_on_single_shell():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    uj = bandpass_vector(u, j)
    wj = bandpass_vector(curl(u), j)

    lhs = abs(advective_hh_term(uj, wj, j, h))
    rhs = shell_residual(wj, j, h)

    assert lhs <= 1e-10 * max(1.0, rhs)


def test_ddyo_hh_skew_cancellation_on_single_shell():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    uj = bandpass_vector(u, j)
    Aj = skew_grad(uj)
    wj = bandpass_vector(curl(u), j)

    lhs = abs(skew_hh_term(Aj, wj, j, h))
    rhs = shell_residual(wj, j, h)

    assert lhs <= 1e-10 * max(1.0, rhs)


def test_ddyo_hh_positive_strain_is_nontrivial():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    uj = bandpass_vector(u, j)
    Sj = sym_grad(uj)
    wj = bandpass_vector(curl(u), j)

    lhs = positive_strain_hh_term(Sj, wj, j, h)
    rhs = shell_residual(wj, j, h)

    assert lhs > 1e-6 * max(1.0, rhs)


def test_ddyo_full_shell_strain_proxy_controls_positive_hh():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    uj = bandpass_vector(u, j)
    Sj = sym_grad(uj)
    wj = bandpass_vector(curl(u), j)

    lhs = positive_strain_hh_term(Sj, wj, j, h)
    lam = float(np.max(np.maximum(max_eigenvalue_field(Sj), 0.0)))
    rhs = (4.0 / 3.0) * lam * shell_residual(wj, j, h)

    assert lhs <= (1.0 + 1e-9) * max(rhs, 1e-12)


def test_ddyo_normalized_active_lambda_is_integer_dilation_stable():
    X1, Y1, Z1, h1 = make_grid(n=32)
    u1 = base_velocity_shell(X1, Y1, Z1, k=4)
    j1 = shell_index_for_frequency(4)
    u1j = bandpass_vector(u1, j1)
    S1j = sym_grad(u1j)
    w1j = bandpass_vector(curl(u1), j1)
    q1 = active_lambda_max(S1j, w1j, j1, h1) / (2.0**j1)

    mu = 2.0
    X2, Y2, Z2, h2 = make_grid(n=64)
    u2 = scaled_field_from_base(X2, Y2, Z2, mu=mu, k=4)
    j2 = shell_index_for_frequency(8)
    u2j = bandpass_vector(u2, j2)
    S2j = sym_grad(u2j)
    w2j = bandpass_vector(curl(u2), j2)
    q2 = active_lambda_max(S2j, w2j, j2, h2) / (2.0**j2)

    assert abs(q1 - q2) / max(abs(q1), 1e-12) < 5e-2


def active_set_mask_theta(wj, j, h, theta):
    volume = float(np.prod(wj.shape[1:]) * (h**3))
    threshold = (
        theta * (2.0 ** (-j)) * lp_norm_vector(wj, 4.0 / 3.0, h) / (volume**0.75)
    )
    return pointwise_norm(wj) >= threshold


def test_ddyo_theta_active_set_nonempty_single_shell():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    wj = bandpass_vector(curl(u), j)

    mask = active_set_mask_theta(wj, j, h, theta=0.5)

    assert np.any(mask)


def test_ddyo_theta_active_set_nonempty_multishell():
    X, Y, Z, h = make_grid(n=24)
    u = aligned_multishell_velocity(X, Y, Z)

    for k in [2, 4, 8]:
        j = shell_index_for_frequency(k)
        wj = bandpass_vector(curl(u), j)
        mask = active_set_mask_theta(wj, j, h, theta=0.5)
        assert np.any(mask)


def shell_residual_on_mask(wj, j, h, mask):
    return (2.0 ** (2 * j)) * volume_integral(np.where(mask, h_density(wj), 0.0), h)


def positive_strain_hh_term_on_mask(Sj, wj, j, h, mask):
    integrand = np.sum(hprime(wj) * strain_action(Sj, wj), axis=0)
    return (2.0 ** (2 * j)) * volume_integral(
        np.where(mask, np.maximum(integrand, 0.0), 0.0), h
    )


def positive_lambda_sup_on_mask(Sj, mask):
    lam = np.maximum(max_eigenvalue_field(Sj), 0.0)
    if not np.any(mask):
        return 0.0
    return float(np.max(lam[mask]))


def test_ddyo_theta_localized_proxy_split_controls_positive_hh_single_shell():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    uj = bandpass_vector(u, j)
    Sj = sym_grad(uj)
    wj = bandpass_vector(curl(u), j)

    active = active_set_mask_theta(wj, j, h, theta=0.5)
    tail = ~active

    lhs = positive_strain_hh_term(Sj, wj, j, h)

    lam_active = positive_lambda_sup_on_mask(Sj, active)
    lam_tail = positive_lambda_sup_on_mask(Sj, tail)

    rhs_active = (4.0 / 3.0) * lam_active * shell_residual_on_mask(wj, j, h, active)
    rhs_tail = (4.0 / 3.0) * lam_tail * shell_residual_on_mask(wj, j, h, tail)

    assert lhs <= (1.0 + 1e-9) * max(rhs_active + rhs_tail, 1e-12)


def test_ddyo_theta_localized_proxy_split_controls_positive_hh_multishell():
    X, Y, Z, h = make_grid(n=24)
    u = aligned_multishell_velocity(X, Y, Z)

    for k in [2, 4, 8]:
        j = shell_index_for_frequency(k)
        uj = bandpass_vector(u, j)
        Sj = sym_grad(uj)
        wj = bandpass_vector(curl(u), j)

        active = active_set_mask_theta(wj, j, h, theta=0.5)
        tail = ~active

        lhs = positive_strain_hh_term(Sj, wj, j, h)

        lam_active = positive_lambda_sup_on_mask(Sj, active)
        lam_tail = positive_lambda_sup_on_mask(Sj, tail)

        rhs_active = (4.0 / 3.0) * lam_active * shell_residual_on_mask(wj, j, h, active)
        rhs_tail = (4.0 / 3.0) * lam_tail * shell_residual_on_mask(wj, j, h, tail)

        assert lhs <= (1.0 + 1e-9) * max(rhs_active + rhs_tail, 1e-12)


def test_ddyo_theta_tail_ratio_decreases_single_shell():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    wj = bandpass_vector(curl(u), j)

    total = shell_residual(wj, j, h)
    ratios = []

    for theta in [0.25, 0.50, 0.75, 0.90]:
        tail = ~active_set_mask_theta(wj, j, h, theta=theta)
        tail_mass = shell_residual_on_mask(wj, j, h, tail)
        ratios.append(tail_mass / max(total, 1e-12))

    assert ratios[0] <= ratios[1] + 1e-12
    assert ratios[1] <= ratios[2] + 1e-12
    assert ratios[2] <= ratios[3] + 1e-12
    assert ratios[0] < 1.0 - 1e-12
    assert ratios[3] <= 1.0 + 1e-12


def test_ddyo_theta_tail_ratio_decreases_multishell():
    X, Y, Z, h = make_grid(n=24)
    u = aligned_multishell_velocity(X, Y, Z)

    for k in [2, 4, 8]:
        j = shell_index_for_frequency(k)
        wj = bandpass_vector(curl(u), j)

        total = shell_residual(wj, j, h)
        ratios = []

        for theta in [0.25, 0.50, 0.75, 0.90]:
            tail = ~active_set_mask_theta(wj, j, h, theta=theta)
            tail_mass = shell_residual_on_mask(wj, j, h, tail)
            ratios.append(tail_mass / max(total, 1e-12))

        assert ratios[0] <= ratios[1] + 1e-12
        assert ratios[1] <= ratios[2] + 1e-12
        assert ratios[2] <= ratios[3] + 1e-12
        assert ratios[0] < 1.0 - 1e-12
        assert ratios[3] <= 1.0 + 1e-12


def test_ddyo_theta_tail_smallness_gap_single_shell():
    X, Y, Z, h = make_grid(n=24)
    u = base_velocity_shell(X, Y, Z, k=4)
    j = shell_index_for_frequency(4)
    wj = bandpass_vector(curl(u), j)

    total = shell_residual(wj, j, h)
    tail_50 = shell_residual_on_mask(
        wj, j, h, ~active_set_mask_theta(wj, j, h, theta=0.50)
    )
    tail_90 = shell_residual_on_mask(
        wj, j, h, ~active_set_mask_theta(wj, j, h, theta=0.90)
    )

    r50 = tail_50 / max(total, 1e-12)
    r90 = tail_90 / max(total, 1e-12)

    assert r50 < 0.95
    assert r90 >= r50 - 1e-12


def test_ddyo_theta_tail_smallness_gap_multishell():
    X, Y, Z, h = make_grid(n=24)
    u = aligned_multishell_velocity(X, Y, Z)

    for k in [2, 4, 8]:
        j = shell_index_for_frequency(k)
        wj = bandpass_vector(curl(u), j)

        total = shell_residual(wj, j, h)
        tail_50 = shell_residual_on_mask(
            wj, j, h, ~active_set_mask_theta(wj, j, h, theta=0.50)
        )
        tail_90 = shell_residual_on_mask(
            wj, j, h, ~active_set_mask_theta(wj, j, h, theta=0.90)
        )

        r50 = tail_50 / max(total, 1e-12)
        r90 = tail_90 / max(total, 1e-12)

        assert r50 < 0.95
        assert r90 >= r50 - 1e-12
