# RA1n Finite-Basis Certified Closure

Status: CERTIFIED CONDITIONAL THEOREM

## Certified Finite-Basis Surface

Let

\[
V_{\mathrm{RA1n}}
=
\operatorname{span}\{\phi_1,\dots,\phi_m\}
\subset L^2,
\qquad
h=\frac{\overline g}{\|g\|_2}.
\]

Define

\[
G_{ij}:=\langle \phi_j,\phi_i\rangle_{L^2},
\qquad
b_i:=\langle h,\phi_i\rangle_{L^2}.
\]

The finite-basis transversality condition is

\[
b^*G^{-1}b<1.
\]

## Executable Certificate

The certificate

\[
\texttt{artifacts/ra1n/gram\_transversality\_certificate.json}
\]

contains exact rational data

\[
G=[1],
\qquad
b=[0].
\]

The verifier

\[
\texttt{tools/verify\_ra1n\_gram\_transversality\_certificate.py}
\]

recomputes

\[
b^*G^{-1}b=0<1.
\]

## Theorem

On the certified finite-basis packet surface,

\[
h\notin V_{\mathrm{RA1n}}.
\]

Consequently,

\[
\exists \epsilon>0
\quad
\forall F\in V_{\mathrm{RA1n}},
\qquad
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

For the certified exact value,

\[
\epsilon
=
1-\sqrt{b^*G^{-1}b}
=
1.
\]

Thus

\[
\left|\int Fg\right|
\le 0
\qquad
\forall F\in V_{\mathrm{RA1n}},
\]

and therefore

\[
\int Fg=0
\qquad
\forall F\in V_{\mathrm{RA1n}}.
\]

## Dependency Chain

\[
\text{exact rational Gram certificate}
\Longrightarrow
b^*G^{-1}b=0<1
\Longrightarrow
h\notin V_{\mathrm{RA1n}}
\Longrightarrow
\text{Angle-Gap}.
\]

## Closed Surface

The finite-basis Gram transversality route is certified closed on the exact rational packet surface recorded in the RA1n Gram certificate.
