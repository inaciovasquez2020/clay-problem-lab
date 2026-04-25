# RA1n Angle-Gap Certified Closure

Status: CERTIFIED CONDITIONAL THEOREM

## Objects

Let

\[
g\neq0,
\qquad
h:=\frac{\overline g}{\|g\|_2}.
\]

Let

\[
V_{\mathrm{RA1n}}
=
\operatorname{span}\{\phi_1,\dots,\phi_m\}
\subset L^2.
\]

Define

\[
G_{ij}:=\langle \phi_j,\phi_i\rangle_{L^2},
\qquad
b_i:=\langle h,\phi_i\rangle_{L^2}.
\]

## Certified Input

The executable certificate `artifacts/ra1n/gram_transversality_certificate.json` verifies exactly that

\[
b^*G^{-1}b=0<1.
\]

Thus

\[
\alpha:=\sqrt{b^*G^{-1}b}=0.
\]

Set

\[
\epsilon:=1-\alpha=1.
\]

## Theorem

For every

\[
F\in V_{\mathrm{RA1n}},
\]

one has

\[
\left|\int F(\eta)g(\eta)\,d\eta\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

With the certified value \(\epsilon=1\), this becomes

\[
\left|\int F(\eta)g(\eta)\,d\eta\right|
\le
0.
\]

Equivalently,

\[
\int F(\eta)g(\eta)\,d\eta=0
\qquad
\forall F\in V_{\mathrm{RA1n}}.
\]

## Proof

By `RA1N_FINITE_BASIS_GRAM_TRANSVERSALITY.md`,

\[
b^*G^{-1}b<1
\Longrightarrow
h\notin V_{\mathrm{RA1n}}.
\]

By `RA1N_ANGLE_GAP_LEMMA.md`, if

\[
h\notin V_{\mathrm{RA1n}},
\]

then

\[
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2
\]

with

\[
\epsilon=1-\sqrt{b^*G^{-1}b}.
\]

The executable certificate verifies

\[
b^*G^{-1}b=0.
\]

Therefore

\[
\epsilon=1.
\]

Hence

\[
\left|\int Fg\right|
\le
0
\]

for every \(F\in V_{\mathrm{RA1n}}\), so

\[
\int Fg=0.
\]

## Closed Surface

The RA1n angle-gap lemma is certified closed on the finite-basis Gram packet surface verified by

\[
b^*G^{-1}b=0<1.
\]
