import math
import numpy as np


TWOPI = 2.0 * math.pi


def _dc_make_grid(n=48):
    x = np.linspace(0.0, TWOPI, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    h = TWOPI / n
    return X, Y, Z, h


def _dc_kgrid(n):
    k = np.fft.fftfreq(n, d=1.0 / n)
    return np.meshgrid(k, k, k, indexing="ij")


def _dc_d1_scalar(f, axis):
    n = f.shape[0]
    K = _dc_kgrid(n)
    F = np.fft.fftn(f)
    return np.fft.ifftn(1j * K[axis] * F).real


def _dc_grad_vector(v):
    return np.stack(
        [np.stack([_dc_d1_scalar(v[c], a) for a in range(3)], axis=0) for c in range(3)],
        axis=0,
    )


def _dc_curl(v):
    J = _dc_grad_vector(v)
    return np.stack(
        [
            J[2, 1] - J[1, 2],
            J[0, 2] - J[2, 0],
            J[1, 0] - J[0, 1],
        ],
        axis=0,
    )


def _dc_sym_grad(v):
    J = _dc_grad_vector(v)
    return 0.5 * (J + np.swapaxes(J, 0, 1))


def _dc_skew_grad(v):
    J = _dc_grad_vector(v)
    return 0.5 * (J - np.swapaxes(J, 0, 1))


def _dc_bandpass_scalar(f, j):
    n = f.shape[0]
    Kx, Ky, Kz = _dc_kgrid(n)
    r = np.sqrt(Kx * Kx + Ky * Ky + Kz * Kz)
    lo = 0.0 if j == 0 else 2.0 ** (j - 1)
    hi = 2.0 ** (j + 1)
    mask = (r >= lo - 1e-12) & (r < hi - 1e-12)
    F = np.fft.fftn(f)
    return np.fft.ifftn(F * mask).real


def _dc_bandpass_vector(v, j):
    return np.stack([_dc_bandpass_scalar(v[c], j) for c in range(3)], axis=0)


def _dc_advection(u, w):
    Gw = _dc_grad_vector(w)
    return np.einsum("a...,ca...->c...", u, Gw)


def _dc_hprime(v, eps=1e-12):
    mag = np.maximum(np.sqrt(np.sum(v * v, axis=0)), eps)
    return v / np.power(mag, 2.0 / 3.0)


def _dc_tensor_vec(T, v):
    return np.einsum("ab...,b...->a...", T, v)


def _dc_vec_norm(v):
    return np.sqrt(np.sum(v * v, axis=0))


def _dc_mat_norm(M):
    return np.sqrt(np.sum(M * M, axis=(0, 1)))


def _dc_l1_vec(v, h):
    return float(np.sum(_dc_vec_norm(v)) * (h ** 3))


def _dc_l1_scalar(f, h):
    return float(np.sum(np.abs(f)) * (h ** 3))


def _dc_linf_mat(M):
    return float(np.max(_dc_mat_norm(M)))


def _dc_volume_integral(f, h):
    return float(np.sum(f) * (h ** 3))


def _dc_shell_index(k):
    return int(round(math.log2(k)))


def _dc_base_velocity_shell(X, Y, Z, k=4):
    return np.stack(
        [
            np.sin(k * Y) + np.cos(k * Z),
            np.sin(k * Z) + np.cos(k * X),
            np.sin(k * X) + np.cos(k * Y),
        ],
        axis=0,
    )


def _dc_multishell_velocity(X, Y, Z):
    return (
        1.00 * _dc_base_velocity_shell(X, Y, Z, k=2)
        + 0.70 * _dc_base_velocity_shell(X, Y, Z, k=4)
        + 0.35 * _dc_base_velocity_shell(X, Y, Z, k=8)
    )


def _dc_scaled_field_from_base(X, Y, Z, mu=2.0, k=4):
    return _dc_base_velocity_shell(mu * X, mu * Y, mu * Z, k=k)


def _dc_commutator(u, w, j):
    return _dc_bandpass_vector(_dc_advection(u, w), j) - _dc_advection(u, _dc_bandpass_vector(w, j))


def test_ddyo_commutator_split_is_exact():
    X, Y, Z, _ = _dc_make_grid(n=48)
    u = _dc_multishell_velocity(X, Y, Z)
    w = _dc_curl(u)
    j = _dc_shell_index(4)

    lhs = _dc_bandpass_vector(_dc_advection(u, w), j)
    rhs = _dc_advection(u, _dc_bandpass_vector(w, j)) + _dc_commutator(u, w, j)

    err = float(np.max(np.abs(lhs - rhs)))
    ref = max(1.0, float(np.max(np.abs(lhs))))
    assert err <= 1e-10 * ref


def test_ddyo_same_scale_commutator_bound_single_shell():
    X, Y, Z, h = _dc_make_grid(n=48)
    u = _dc_base_velocity_shell(X, Y, Z, k=4)
    w = _dc_curl(u)
    j = _dc_shell_index(4)

    uj = _dc_bandpass_vector(u, j)
    wj = _dc_bandpass_vector(w, j)
    comm = _dc_commutator(uj, wj, j)

    lhs = _dc_l1_vec(comm, h)
    rhs = (2.0 ** (-j)) * _dc_linf_mat(_dc_grad_vector(uj)) * _dc_l1_vec(_dc_grad_vector(wj), h)

    assert lhs <= 8.0 * max(rhs, 1e-12)


def test_ddyo_rotation_part_cancels_against_hprime():
    X, Y, Z, h = _dc_make_grid(n=48)
    u = _dc_base_velocity_shell(X, Y, Z, k=4)
    j = _dc_shell_index(4)

    uj = _dc_bandpass_vector(u, j)
    wj = _dc_bandpass_vector(_dc_curl(u), j)
    Aj = _dc_skew_grad(uj)

    integrand = np.sum(_dc_hprime(wj) * _dc_tensor_vec(Aj, wj), axis=0)
    lhs = abs(_dc_volume_integral(integrand, h))
    rhs = _dc_l1_vec(wj, h)

    assert lhs <= 1e-10 * max(rhs, 1.0)


def test_ddyo_normalized_commutator_ratio_integer_dilation_stable():
    X1, Y1, Z1, h1 = _dc_make_grid(n=48)
    u1 = _dc_base_velocity_shell(X1, Y1, Z1, k=4)
    w1 = _dc_curl(u1)
    j1 = _dc_shell_index(4)

    u1j = _dc_bandpass_vector(u1, j1)
    w1j = _dc_bandpass_vector(w1, j1)
    lhs1 = _dc_l1_vec(_dc_commutator(u1j, w1j, j1), h1)
    rhs1 = (2.0 ** (-j1)) * _dc_linf_mat(_dc_grad_vector(u1j)) * _dc_l1_vec(_dc_grad_vector(w1j), h1)
    q1 = lhs1 / max(rhs1, 1e-12)

    mu = 2.0
    X2, Y2, Z2, h2 = _dc_make_grid(n=96)
    u2 = _dc_scaled_field_from_base(X2, Y2, Z2, mu=mu, k=4)
    w2 = _dc_curl(u2)
    j2 = _dc_shell_index(8)

    u2j = _dc_bandpass_vector(u2, j2)
    w2j = _dc_bandpass_vector(w2, j2)
    lhs2 = _dc_l1_vec(_dc_commutator(u2j, w2j, j2), h2)
    rhs2 = (2.0 ** (-j2)) * _dc_linf_mat(_dc_grad_vector(u2j)) * _dc_l1_vec(_dc_grad_vector(w2j), h2)
    q2 = lhs2 / max(rhs2, 1e-12)

    assert abs(q1 - q2) / max(abs(q1), 1e-12) < 1.5e-1

def _dc_bandpass_matrix(M, j):
    return np.stack(
        [np.stack([_dc_bandpass_scalar(M[a, b], j) for b in range(3)], axis=0) for a in range(3)],
        axis=0,
    )


def _dc_bandpass_tensor2(T, j):
    return np.stack(
        [np.stack([_dc_bandpass_scalar(T[a, b], j) for b in range(3)], axis=0) for a in range(3)],
        axis=0,
    )


def _dc_grad_matrix(M):
    return np.stack(
        [
            np.stack(
                [np.stack([_dc_d1_scalar(M[a, b], k) for k in range(3)], axis=0) for b in range(3)],
                axis=0,
            )
            for a in range(3)
        ],
        axis=0,
    )


def _dc_grad_tensor2(T):
    return np.stack(
        [
            np.stack(
                [np.stack([_dc_d1_scalar(T[a, b], k) for k in range(3)], axis=0) for b in range(3)],
                axis=0,
            )
            for a in range(3)
        ],
        axis=0,
    )


def _dc_mat_tensor2(M, Q):
    return np.einsum("ab...,bk...->ak...", M, Q)


def _dc_tensor2_norm(Q):
    return np.sqrt(np.sum(Q * Q, axis=(0, 1)))


def _dc_tensor3_norm(T):
    return np.sqrt(np.sum(T * T, axis=(0, 1, 2)))


def _dc_l1_tensor2(Q, h):
    return float(np.sum(_dc_tensor2_norm(Q)) * (h ** 3))


def _dc_l2_matrix(M, h):
    return float(np.sqrt(np.sum(M * M) * (h ** 3)))


def _dc_l2_tensor2(Q, h):
    return float(np.sqrt(np.sum(Q * Q) * (h ** 3)))


def _dc_l2_tensor3(T, h):
    return float(np.sqrt(np.sum(T * T) * (h ** 3)))


def _dc_linf_tensor3(T):
    return float(np.max(_dc_tensor3_norm(T)))


def _dc_commutator_mat_tensor2(M, Q, j):
    return _dc_bandpass_tensor2(_dc_mat_tensor2(M, Q), j) - _dc_mat_tensor2(M, _dc_bandpass_tensor2(Q, j))


def _dc_commutator_epsilon_proxy(M, Q, j, h):
    gradM = _dc_grad_matrix(M)
    gradQ = _dc_grad_tensor2(Q)
    lhs = _dc_l1_tensor2(_dc_commutator_mat_tensor2(M, Q, j), h)
    rhs = (2.0 ** (-j)) * (
        _dc_l2_tensor3(gradM, h) * _dc_l2_tensor2(Q, h)
        + _dc_l2_matrix(M, h) * _dc_l2_tensor3(gradQ, h)
    )
    return lhs / max(64.0 * rhs, 1e-12)


def test_ddyo_strain_rotation_commutator_split_is_exact():
    X, Y, Z, _ = _dc_make_grid(n=48)
    u = _dc_multishell_velocity(X, Y, Z)
    w = _dc_curl(u)
    j = _dc_shell_index(4)

    uj = _dc_bandpass_vector(u, j)
    Jj = _dc_grad_vector(uj)
    Sj = _dc_sym_grad(uj)
    Aj = _dc_skew_grad(uj)
    qj = _dc_grad_vector(_dc_bandpass_vector(w, j))

    lhs = _dc_commutator_mat_tensor2(Jj, qj, j)
    rhs = _dc_commutator_mat_tensor2(Sj, qj, j) + _dc_commutator_mat_tensor2(Aj, qj, j)

    err = float(np.max(np.abs(lhs - rhs)))
    ref = max(1.0, float(np.max(np.abs(lhs))))
    assert err <= 1e-10 * ref


def test_ddyo_strain_commutator_kato_ponce_proxy_bound():
    X, Y, Z, h = _dc_make_grid(n=48)
    u = _dc_multishell_velocity(X, Y, Z)
    w = _dc_curl(u)
    j = _dc_shell_index(4)

    uj = _dc_bandpass_vector(u, j)
    Sj = _dc_sym_grad(uj)
    qj = _dc_grad_vector(_dc_bandpass_vector(w, j))
    gradSj = _dc_grad_matrix(Sj)
    gradqj = _dc_grad_tensor2(qj)

    lhs = _dc_l1_tensor2(_dc_commutator_mat_tensor2(Sj, qj, j), h)
    rhs = (2.0 ** (-j)) * (
        _dc_l2_tensor3(gradSj, h) * _dc_l2_tensor2(qj, h)
        + _dc_l2_matrix(Sj, h) * _dc_l2_tensor3(gradqj, h)
    )

    assert lhs <= 64.0 * max(rhs, 1e-12)


def test_ddyo_rotation_commutator_lower_order_proxy_bound():
    X, Y, Z, h = _dc_make_grid(n=48)
    u = _dc_multishell_velocity(X, Y, Z)
    w = _dc_curl(u)
    j = _dc_shell_index(4)

    uj = _dc_bandpass_vector(u, j)
    Aj = _dc_skew_grad(uj)
    qj = _dc_grad_vector(_dc_bandpass_vector(w, j))
    gradAj = _dc_grad_matrix(Aj)

    lhs = _dc_l1_tensor2(_dc_commutator_mat_tensor2(Aj, qj, j), h)
    rhs = (2.0 ** (-j)) * _dc_linf_tensor3(gradAj) * _dc_l1_tensor2(qj, h)

    assert lhs <= 64.0 * max(rhs, 1e-12)


def test_ddyo_commutator_epsilon_proxy_integer_dilation_stable():
    X1, Y1, Z1, h1 = _dc_make_grid(n=48)
    u1 = _dc_base_velocity_shell(X1, Y1, Z1, k=4)
    w1 = _dc_curl(u1)
    j1 = _dc_shell_index(4)

    u1j = _dc_bandpass_vector(u1, j1)
    S1j = _dc_sym_grad(u1j)
    q1 = _dc_grad_vector(_dc_bandpass_vector(w1, j1))
    e1 = _dc_commutator_epsilon_proxy(S1j, q1, j1, h1)

    mu = 2.0
    X2, Y2, Z2, h2 = _dc_make_grid(n=96)
    u2 = _dc_scaled_field_from_base(X2, Y2, Z2, mu=mu, k=4)
    w2 = _dc_curl(u2)
    j2 = _dc_shell_index(8)

    u2j = _dc_bandpass_vector(u2, j2)
    S2j = _dc_sym_grad(u2j)
    q2 = _dc_grad_vector(_dc_bandpass_vector(w2, j2))
    e2 = _dc_commutator_epsilon_proxy(S2j, q2, j2, h2)

    assert e1 < 0.5
    assert e2 < 0.5
    assert abs(e1 - e2) / max(abs(e1), 1e-12) < 2.0e-1
