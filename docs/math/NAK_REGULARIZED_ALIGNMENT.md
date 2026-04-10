# NAK regularized alignment

## Spectral-gap-free replacement

For symmetric strain
\[
S=\frac{\nabla u+(\nabla u)^\top}{2},
\]
define the soft projector
\[
P_\tau(S):=\frac{e^{\tau S}}{\operatorname{tr}(e^{\tau S})},
\qquad \tau>0.
\]

Then
\[
P_\tau(S)\ge 0,
\qquad
\operatorname{tr}(P_\tau(S))=1,
\]
and \(P_\tau(S)\) is smooth in \(S\) with no eigenvalue-crossing singularity.

## Regularized alignment defect

Let
\[
\omega=\nabla\times u,
\qquad
\widehat\omega=\frac{\omega}{|\omega|}.
\]

Define
\[
A_\tau:=1-\widehat\omega\cdot P_\tau(S)\widehat\omega.
\]

Then
\[
0\le A_\tau\le 1.
\]

## Regularized NAK residual

\[
R_{\mathrm{NAK},\tau}[u]
:=
\int_{\mathbb R^3} A_\tau\,|\omega|^{3/2}\,dx.
\]

Under Navier--Stokes scaling on \(\mathbb R^3\),
\[
u_\mu(x,t)=\mu u(\mu x,\mu^2 t),
\qquad
\omega_\mu(x,t)=\mu^2\omega(\mu x,\mu^2 t),
\qquad
S_\mu(x,t)=\mu^2 S(\mu x,\mu^2 t).
\]

The fixed-\(\tau\) regularized residual is not scale-invariant on \(\mathbb R^3\).
The sampled torus tests only verify:
- nonnegativity
- \(R_{\mathrm{NAK},\tau}\le R_{\mathrm{DREM}}\)
- fixed-domain integer-dilation cubic law for the sampled quadrature layer

## Frontier

A scale-consistent regularized NAK variant requires either:
\[
\tau=\tau[u]
\]
with critical scaling, or a different smooth spectral functional replacing \(P_\tau(S)\).
