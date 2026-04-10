# J2B critical residual

## Corrected continuum candidate

\[
R_{\mathrm{J2B}}[u]:=\|\nabla\omega\|_{L^1(\mathbb R^3)},
\qquad
\omega=\nabla\times u.
\]

## Navier--Stokes scaling

\[
u_\mu(x,t)=\mu u(\mu x,\mu^2 t).
\]

Then
\[
\omega_\mu(x,t)=\mu^2\omega(\mu x,\mu^2 t),
\qquad
\nabla\omega_\mu(x,t)=\mu^3(\nabla\omega)(\mu x,\mu^2 t).
\]

Therefore
\[
R_{\mathrm{J2B}}[u_\mu]
=
\int_{\mathbb R^3}\mu^3|(\nabla\omega)(\mu x,\mu^2 t)|\,dx
=
R_{\mathrm{J2B}}[u].
\]

## Sampled torus test law

For the current periodic sampled test layer,
integer-frequency dilation on the fixed torus obeys
\[
R_{\mathrm{J2B}}^{\mathrm{test}}[u_\mu]\approx \mu^3 R_{\mathrm{J2B}}^{\mathrm{test}}[u].
\]

This is the fixed-domain torus law used in `tests/test_j2b_residual.py`,
not the \(\mathbb R^3\) Navier--Stokes scaling law.

## Frontier

The remaining step is to derive a continuum residual identity for
\[
\frac{d}{dt}\|\nabla\omega\|_{L^1}
\]
from the differentiated vorticity equation and identify a coercive dissipation term.
