# DDYO critical envelope

## Continuum candidate

\[
R_{\mathrm{DDYO}}[u]
:=
\sup_{j\in\mathbb Z} 2^{-j}\|\Delta_j u\|_{L^\infty(\mathbb R^3)}
=
\|u\|_{\dot B^{-1}_{\infty,\infty}}.
\]

This is the natural critical dyadic envelope for velocity.

## Navier--Stokes scaling

\[
u_\mu(x,t)=\mu u(\mu x,\mu^2 t).
\]

For dyadic integer dilation \(\mu=2^{j_0}\),
\[
\Delta_j u_\mu(x,t)=\mu\,(\Delta_{j+j_0}u)(\mu x,\mu^2 t),
\]
hence
\[
2^{-j}\|\Delta_j u_\mu\|_{L^\infty}
=
2^{-(k-j_0)}\mu\,\|\Delta_k u\|_{L^\infty}
=
2^{-k}\|\Delta_k u\|_{L^\infty},
\qquad k=j+j_0.
\]

Therefore
\[
R_{\mathrm{DDYO}}[u_\mu]=R_{\mathrm{DDYO}}[u].
\]

## Sampled torus layer

The current test file `tests/test_ddyo_residual.py` implements the periodic sampled analogue
\[
R_{\mathrm{DDYO}}^{\mathrm{test}}
=
\sup_j 2^{-j}\|\Delta_j u\|_{L^\infty},
\]
using discrete Fourier shell extraction.

This sampled layer checks:
- shell localization
- nonnegativity
- integer-dilation invariance of the weighted sup structure

## Frontier

The remaining continuum step is to estimate the nonlinear dyadic flux
\[
\Sigma_{\mathrm{DDYO}}[u]
\]
through a paraproduct decomposition and prove a closure bound of the form
\[
\Sigma_{\mathrm{DDYO}}[u]
\le
\eta(\mathcal D[u]+\lambda \mathcal C_{\mathrm{DDYO}}[u])
+
C(\Phi[u]+\lambda R_{\mathrm{DDYO}}[u]),
\qquad 0\le \eta<1.
\]

The explicit obstruction is the high-high interaction remainder.
