# DDYO Mollified Skew Cancellation

## Target identity

Let \((\widetilde P_j)_j\) be a smooth positive dyadic family with even real symbol and convolution kernel \(K_j(x-y)\).
Assume \(\Omega_{\sim j}\) is divergence-free and pointwise skew-symmetric.

Prove
\[
\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0.
\]

## Structural expansion

Write
\[
[\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}
=
\widetilde P_j(\Omega_{\sim j}\!\cdot\nabla \omega_{\sim j})
-
\Omega_{\sim j}\!\cdot\nabla(\widetilde P_j\omega_{\sim j}).
\]

Using the kernel representation,
\[
\widetilde P_j f(x)=\int K_j(x-y)f(y)\,dy,
\]
reduce the commutator to an antisymmetric bilinear form in \((x,y)\).

## Required cancellation mechanism

Use simultaneously:

1. evenness of \(K_j(x-y)\),
2. skew-adjointness of \(\Omega_{\sim j}\!\cdot\nabla\),
3. antisymmetry under \((x,y)\leftrightarrow(y,x)\),
4. divergence-free transport:
\[
\nabla\cdot \Omega_{\sim j}=0.
\]

## Weakest sufficient output

It is sufficient to prove that each dyadic summand satisfies
\[
\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0.
\]

## Consequence

This removes the skew part exactly, leaving only the symmetric commutator term for continuum DDYO absorbability.
