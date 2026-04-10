import math
import numpy as np


TWOPI = 2.0 * math.pi


def _j2b_make_grid(n=48):
    x = np.linspace(0.0, TWOPI, n, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    h = TWOPI / n
    return X, Y, Z, h


def _j2b_kgrid(n):
    k = np.fft.fftfreq(n, d=1.0 / n)
    return np.meshgrid(k, k, k, indexing="ij")


def _j2b_d1_scalar(f, axis):
    n = f.shape[0]
    K = _j2b_kgrid(n)
    F = np.fft.fftn(f)
    return np.fft.ifftn(1j * K[axis] * F).real


def _j2b_grad_vector(v):
    return np.stack(
        [np.stack([_j2b_d1_scalar(v[c], a) for a in range(3)], axis=0) for c in range(3)],
        axis=0,
    )


def _j2b_grad_matrix(M):
    return np.stack(
        [
            np.stack(
                [np.stack([_j2b_d1_scalar(M[a, b], k) for k in range(3)], axis=0) for b in range(3)],
                axis=0,
            )
            for a in range(3)
        ],
        axis=0,
    )


def _j2b_grad_tensor2(T):
    return np.stack(
        [
            np.stack(
                [np.stack([_j2b_d1_scalar(T[a, b], k) for k in range(3)], axis=0) for b in range(3)],
                axis=0,
            )
            for a in range(3)
        ],
        axis=0,
    )


def _j2b_curl(v):
    J = _j2b_grad_vector(v)
    return np.stack(
        [
            J[2, 1] - J[1, 2],
            J[0, 2] - J[2, 0],
            J[1, 0] - J[0, 1],
        ],
        axis=0,
    )


def _j2b_sym_grad(v):
    J = _j2b_grad_vector(v)
    return 0.5 * (J + np.swapaxes(J, 0, 1))


def _j2b_skew_grad(v):
    J = _j2b_grad_vector(v)
    return 0.5 * (J - np.swapaxes(J, 0, 1))


def _j2b_tensor_vec(T, v):
    return np.einsum("ab...,b...->a...", T, v)


def _j2b_tensor_tensor(T, Q):
    return np.einsum("ab...,bc...->ac...", T, Q)


def _j2b_product_rule_left(gradS, q, S, gradq):
    return np.einsum("abk...,bc...->ack...", gradS, q) + np.einsum("ab...,bck...->ack...", S, gradq)


def _j2b_vec_norm(v):
    return np.sqrt(np.sum(v * v, axis=0))


def _j2b_mat_norm(M):
    return np.sqrt(np.sum(M * M, axis=(0, 1)))


def _j2b_tensor3_norm(T):
    return np.sqrt(np.sum(T * T, axis=(0, 1, 2)))


def _j2b_l1_scalar(f, h):
    return float(np.sum(np.abs(f)) * (h ** 3))


def _j2b_l1_vec(v, h):
    return float(np.sum(_j2b_vec_norm(v)) * (h ** 3))


def _j2b_l1_mat(M, h):
    return float(np.sum(_j2b_mat_norm(M)) * (h ** 3))


def _j2b_l1_tensor3(T, h):
    return float(np.sum(_j2b_tensor3_norm(T)) * (h ** 3))


def _j2b_linf_mat(M):
    return float(np.max(_j2b_mat_norm(M)))


def _j2b_linf_tensor3(T):
    return float(np.max(_j2b_tensor3_norm(T)))


def _j2b_base_velocity_shell(X, Y, Z, k=2):
    return np.stack(
        [
            np.sin(k * Y) + np.cos(k * Z),
            np.sin(k * Z) + np.cos(k * X),
            np.sin(k * X) + np.cos(k * Y),
        ],
        axis=0,
    )


def _j2b_multishell_velocity(X, Y, Z):
    return (
        1.00 * _j2b_base_velocity_shell(X, Y, Z, k=2)
        + 0.40 * _j2b_base_velocity_shell(X, Y, Z, k=4)
    )


def _j2b_shear_shell(X, Y, Z, k=4):
    return np.stack(
        [
            np.sin(k * Z),
            np.zeros_like(X),
            np.zeros_like(X),
        ],
        axis=0,
    )


def test_j2b_stretch_gradient_split_is_exact():
    X, Y, Z, _ = _j2b_make_grid(n=48)
    u = _j2b_multishell_velocity(X, Y, Z)
    w = _j2b_curl(u)

    J = _j2b_grad_vector(u)
    S = 0.5 * (J + np.swapaxes(J, 0, 1))
    A = 0.5 * (J - np.swapaxes(J, 0, 1))

    lhs = _j2b_grad_vector(_j2b_tensor_vec(J, w))
    rhs = _j2b_grad_vector(_j2b_tensor_vec(S, w) + _j2b_tensor_vec(A, w))

    err = float(np.max(np.abs(lhs - rhs)))
    ref = max(1.0, float(np.max(np.abs(lhs))))
    assert err <= 1e-10 * ref


def test_j2b_skew_term_vanishes_on_shear_shell():
    X, Y, Z, _ = _j2b_make_grid(n=48)
    u = _j2b_shear_shell(X, Y, Z, k=4)
    w = _j2b_curl(u)
    A = _j2b_skew_grad(u)

    Aw = _j2b_tensor_vec(A, w)
    grad_Aw = _j2b_grad_vector(Aw)

    assert float(np.max(np.abs(Aw))) <= 1e-10
    assert float(np.max(np.abs(grad_Aw))) <= 1e-10


def test_j2b_strain_product_rule_bound():
    X, Y, Z, h = _j2b_make_grid(n=48)
    u = _j2b_multishell_velocity(X, Y, Z)

    w = _j2b_curl(u)
    q = _j2b_grad_vector(w)
    S = _j2b_sym_grad(u)
    gradS = _j2b_grad_matrix(S)
    gradq = _j2b_grad_tensor2(q)

    strain_q = _j2b_tensor_tensor(S, q)
    grad_strain_q = _j2b_grad_tensor2(strain_q)

    lhs = _j2b_l1_tensor3(grad_strain_q, h)
    rhs = _j2b_linf_tensor3(gradS) * _j2b_l1_mat(q, h) + _j2b_linf_mat(S) * _j2b_l1_tensor3(gradq, h)

    assert lhs <= (1.0 + 1e-9) * max(rhs, 1e-12)
