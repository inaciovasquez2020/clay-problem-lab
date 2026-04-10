# DREM residual status

## Canonical residual
\[
R_{\mathrm{DREM}}[u]=\|\omega\|_{L^{3/2}(\mathbb{R}^3)}^{3/2},\qquad \omega=\nabla\times u.
\]

## Continuum scaling on \(\mathbb{R}^3\)
For
\[
u_\mu(x,t)=\mu u(\mu x,\mu^2 t),\qquad \omega_\mu(x,t)=\mu^2\omega(\mu x,\mu^2 t),
\]
one has
\[
R_{\mathrm{DREM}}[u_\mu]=R_{\mathrm{DREM}}[u].
\]

## Fixed-torus discrete test law
For periodic sampled fields on a fixed torus, integer-frequency dilation obeys
\[
R_{\mathrm{DREM}}[u_\mu]\approx \mu^3 R_{\mathrm{DREM}}[u]
\]
under the discrete quadrature used in `tests/test_drem_residual.py`.

## Positive stretching functional
\[
\Sigma_{\mathrm{DREM}}[u]
=
\int (\widehat\omega\cdot S\widehat\omega)_+\,|\omega|^{3/2}\,dx,
\qquad
S=\frac{\nabla u+(\nabla u)^\top}{2}.
\]

Using
\[
(\widehat\omega\cdot S\widehat\omega)_+\le |S|
\]
and Hölder,
\[
\Sigma_{\mathrm{DREM}}[u]
\le
\|S\|_{L^3}\|\omega\|_{L^{9/4}}^{3/2}.
\]

## Remaining obstruction
The missing closure lemma is an estimate of the form
\[
\|S\|_{L^3}\|\omega\|_{L^{9/4}}^{3/2}
\le
\eta\,\mathcal D_{\mathrm{DREM}}[u]+C\,\Phi[u]+C\,R_{\mathrm{DREM}}[u],
\qquad
0\le \eta<1.
\]

Status:
- residual chosen
- continuum criticality identified
- discrete torus law tested
- Hölder reduction identified
- coercive closure still open
