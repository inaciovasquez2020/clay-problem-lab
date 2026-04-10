# Variant framework status

## Unified schema

\[
\mathfrak V=(\Phi,R,\Sigma,\mathcal D,\mathcal C)
\]

with target closure form
\[
\frac{d}{dt}(\Phi+\lambda R)+(1-\eta)(\mathcal D+\lambda\mathcal C)
\le
C(\Phi+\lambda R),
\qquad 0\le \eta<1.
\]

## DREM

Residual:
\[
R_{\mathrm{DREM}}[u]=\|\omega\|_{L^{3/2}}^{3/2}.
\]

Status:
- continuum critical residual identified
- positive stretching functional identified
- discrete torus scaling surrogate tested
- interpolation rewrite tested
- coercive closure lemma open

Open obstruction:
\[
\Sigma_{\mathrm{DREM}}
\le
\eta(\mathcal D+\lambda\mathcal C_{\mathrm{DREM}})
+
C(\Phi+\lambda R_{\mathrm{DREM}})
\]
not proved.

## NAK

Residual:
\[
R_{\mathrm{NAK}}[u]
=
\int
\bigl(1-(\widehat\omega\cdot e_1(S))^2\bigr)|\omega|^{3/2}\,dx.
\]

Status:
- alignment-defect residual defined
- discrete residual bounded by DREM tested
- discrete torus cubic law tested
- minimal spectral-gap lemma isolated
- continuum evolution identity conditional on spectral gap

Open obstruction:
uniform lower bound
\[
\lambda_1(S)-\lambda_2(S)\ge \kappa>0
\]
on vorticity support.

## J2B

Current sampled residual:
\[
R_{\mathrm{J2B}}^{\mathrm{test}}
=
\int |\nabla\omega|\,dx.
\]

Status:
- tensor-gradient sampled layer implemented
- discrete torus cubic law tested
- \(L^1\)-\(L^\infty\) sigma reduction tested
- current test residual is not a verified continuum critical residual

Open obstruction:
replace sampled surrogate by a continuum-consistent critical residual and derive its exact residual identity.

## DDYO

Current sampled residual:
\[
R_{\mathrm{DDYO}}^{\mathrm{test}}
=
\sup_j 2^{-j}\|\Delta_j u\|_{L^\infty}.
\]

Status:
- dyadic shell extraction tested
- discrete velocity-envelope invariance tested
- current test layer is a velocity-envelope surrogate
- continuum nonlinear flux closure not proved

Open obstruction:
derive continuum paraproduct closure for the selected critical envelope and isolate the high-high remainder.

## Truthful frontier

Established:
- DREM sampled layer
- NAK sampled layer
- J2B sampled tensor-gradient layer
- DDYO sampled dyadic-envelope layer

Not established:
- continuum closure for any variant
- global regularity consequence
- exact admissible V5 estimate for any variant
