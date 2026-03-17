# Gauge–Fixed Wilson Action: Hessian Structure

## Gauge–Fixed Variables

After axial gauge fixing on block \(B\), variables lie on edges

\[
E_f = E(B) \setminus T_B .
\]

Configuration space

\[
\Omega_B^{fix} = G^{E_f}.
\]

Coordinates: \(U_\ell = \exp(X_\ell)\), \(X_\ell \in \mathfrak{su}(N)\).

---

## Wilson Action

\[
S_B(U)
=
-\beta \sum_{p\subset B} \mathrm{Re}\,\mathrm{Tr}(U_p)
\]

Each plaquette term depends on four links.

---

## First Variation

For link \(\ell\)

\[
\nabla_\ell S_B
=
-\beta
\sum_{p\ni \ell}
\nabla_\ell \mathrm{Re}\,\mathrm{Tr}(U_p)
\]

---

## Hessian

Second variation

\[
\nabla_{\ell_1}\nabla_{\ell_2} S_B
=
-\beta
\sum_{p\ni \ell_1,\ell_2}
\nabla_{\ell_1}\nabla_{\ell_2}
\mathrm{Re}\,\mathrm{Tr}(U_p).
\]

Non-zero only when the two links belong to the same plaquette.

Thus the Hessian matrix has **local plaquette structure**.

---

## Local Positivity

Near identity

\[
U_\ell = \exp(X_\ell)
\]

expand

\[
\mathrm{Re}\,\mathrm{Tr}(U_p)
\approx
N
-
\frac12
\|X_{p}\|^2 .
\]

Hence

\[
S_B(U)
\approx
\frac{\beta}{2}\sum_p \|X_p\|^2 .
\]

This produces a positive quadratic form in the link variables.

---

## Laplacian Structure

The quadratic form corresponds to a **discrete gauge Laplacian** on link variables.

Eigenvalues scale as

\[
\lambda_k \sim L^{-2}.
\]

---

## Target Result

Prove

\[
\nabla^2 S_B(U) \succeq \lambda L^{-2} I
\]

uniformly for all configurations under Dirichlet boundary conditions.

This implies the block spectral gap.

