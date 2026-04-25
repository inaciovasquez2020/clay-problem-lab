# RA1n Exact Gram Computation Certificate

Status: EXECUTABLE CERTIFICATE SURFACE

## Certified Object

For

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1,\dots,\phi_m\},
\qquad
h=\frac{\overline g}{\|g\|_2},
\]

define

\[
G_{ij}:=\langle \phi_j,\phi_i\rangle_{L^2},
\qquad
b_i:=\langle h,\phi_i\rangle_{L^2}.
\]

The certified transversality inequality is

\[
b^*G^{-1}b<1.
\]

## Exact Rational Certificate

A certificate is admissible only if it contains exact rational data for \(G\) and \(b\), and the verifier recomputes

\[
b^*G^{-1}b=\frac ND
\]

directly from that data.

The inequality is accepted exactly when

\[
0\le N<D.
\]

## Angle-Gap Constant

If

\[
b^*G^{-1}b=\frac ND<1,
\]

then

\[
\alpha=\sqrt{\frac ND}<1,
\qquad
\epsilon=1-\sqrt{\frac ND}>0.
\]

Thus

\[
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2
\qquad
\forall F\in V_{\mathrm{RA1n}}.
\]

## Dependency

This supplies the executable computation layer for `RA1N_FINITE_BASIS_GRAM_TRANSVERSALITY.md`.
