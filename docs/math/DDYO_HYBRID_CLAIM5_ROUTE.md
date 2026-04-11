# DDYO Hybrid Claim 5 Route

## Hybrid terminal route

The remaining Claim 5 branch is the hybrid route:

1. paired decomposition at the \(\mathcal H'_\tau\)-level,
2. first-order Taylor extraction of the shell difference,
3. kernel symmetrization to remove the first-order paired leakage,
4. dipole-type second gain on the post-symmetrized remainder,
5. lower-order routing through the existing
\[
\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u].
\]

## Frozen target

For \(|j-k|\le C\),
\[
\int \mathcal H'_\tau(\omega_j)\cdot[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
=
\mathsf I^{\mathrm{sym}}_{j,k}+\mathsf R_{j,k},
\]
with
\[
\mathsf I^{\mathrm{sym}}_{j,k}
=
\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx,
\]
and
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\qquad |j-k|\le C.
\]

## Hybrid mechanism

The first factor \(2^{-j}\) is supplied by the kernel first moment:
\[
\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
\]

The second factor \(2^{-k}\) is not taken from:
\[
\nabla\cdot S_k=0
\quad\text{or}\quad
\int S_k=0,\ \int \omega_k=0
\]
alone.

It is taken from the post-symmetrized first-order Taylor cancellation of the paired shell interaction.

## Proxy status

The accompanying test file is a sampled scalar proxy only.
It tests the hybrid mechanism
\[
\text{raw commutator} \;\to\; \text{first-order subtraction} \;\to\; \text{smaller remainder},
\]
without claiming the continuum DDYO lemma is proved.
