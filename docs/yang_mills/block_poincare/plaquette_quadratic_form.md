# Plaquette Quadratic Form and Discrete Gauge Laplacian

## Linearization

Let

\[
U_\ell = \exp(X_\ell), \qquad X_\ell \in \mathfrak{su}(N).
\]

For small fluctuations,

\[
U_p = U_{\ell_1}U_{\ell_2}U_{\ell_3}^{-1}U_{\ell_4}^{-1}.
\]

Using BCH expansion,

\[
U_p \approx \exp(X_{\ell_1}+X_{\ell_2}-X_{\ell_3}-X_{\ell_4}).
\]

---

## Quadratic Expansion of Wilson Action

Wilson action

\[
S_B(U) = -\beta \sum_{p\subset B}\mathrm{Re}\,\mathrm{Tr}(U_p).
\]

Expand near identity:

\[
\mathrm{Re}\,\mathrm{Tr}(U_p)
\approx
N - \frac12 \|X_{\ell_1}+X_{\ell_2}-X_{\ell_3}-X_{\ell_4}\|^2 .
\]

Thus

\[
S_B(U)
\approx
\frac{\beta}{2}
\sum_{p}
\|X_{\ell_1}+X_{\ell_2}-X_{\ell_3}-X_{\ell_4}\|^2 .
\]

---

## Matrix Form

Define vector

\[
X = (X_\ell)_{\ell\in E_f}.
\]

Let \(A\) be the plaquette–edge incidence matrix.

Then

\[
S_B(U)
\approx
\frac{\beta}{2} X^T A^T A X.
\]

---

## Discrete Gauge Laplacian

The operator

\[
\Delta_g = A^T A
\]

acts as a Laplacian on link variables.

Properties

- positive semidefinite
- kernel removed by axial gauge fixing
- smallest eigenvalue scales as

\[
\lambda_{min}(\Delta_g) \sim L^{-2}.
\]

---

## Convexity Consequence

Quadratic approximation implies

\[
\nabla^2 S_B(U)
\succeq
\beta \Delta_g.
\]

Thus

\[
\nabla^2 S_B(U)
\succeq
c L^{-2} I .
\]

---

## Resulting Spectral Gap

Brascamp–Lieb inequality yields

\[
\operatorname{Var}_{\mu_B}(g)
\le
C L^2
\sum_{\ell\subset B}
\|\nabla_\ell g\|^2 .
\]

This gives the block spectral gap.

