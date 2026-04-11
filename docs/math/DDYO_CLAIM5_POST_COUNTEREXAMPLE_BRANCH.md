# DDYO Claim 5 Post-Counterexample Branch

## Eliminated route

The route
\[
\nabla\cdot S_k = 0
\]
is false in general, even for incompressible velocity fields.

## Weakest remaining Claim 5 branch

The remaining terminal target is to prove
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\qquad |j-k|\le C,
\]
through the paired shell-cancellation route.

## Frozen auxiliary inputs

### Shell moment input
\[
\int_{\mathbb R^3} S_k(x)\,dx = 0,
\qquad
\int_{\mathbb R^3} \omega_k(x)\,dx = 0.
\]

### Kernel first moment input
\[
\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
\]

### Lower-order routing input
\[
\sum_{|j-k|\le C} |\mathsf R^{\mathrm{lo}}_{j,k}|
\le
C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).
\]

## Next sole reduction

It is sufficient to prove that the first-order Taylor part of the paired remainder has zero shell average, so that the commutator remainder behaves as a dipole and gains the second factor
\[
2^{-k}.
\]

## Consequence

This freezes the shell-moment / dipole-cancellation route as the primary remaining route for Claim 5 after elimination of the divergence-free strain branch.
