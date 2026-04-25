# RA1n Finite-Basis Gram Transversality Certificate

Status: PROVED ABSTRACTLY

## Objects

Let

\[
g\neq0,
\qquad
h:=\frac{\overline g}{\|g\|_2}.
\]

Let

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1,\dots,\phi_m\}
\subset L^2
\]

with linearly independent basis \(\phi_1,\dots,\phi_m\).

Define the Gram matrix

\[
G_{ij}:=\langle \phi_j,\phi_i\rangle_{L^2}
\]

and the coefficient vector

\[
b_i:=\langle h,\phi_i\rangle_{L^2}.
\]

## Projection Formula

The orthogonal projection

\[
\Pi_Vh=\sum_{j=1}^m c_j\phi_j
\]

has coefficients satisfying

\[
Gc=b.
\]

Hence

\[
c=G^{-1}b.
\]

Moreover,

\[
\|\Pi_Vh\|_2^2
=
b^*G^{-1}b.
\]

## Transversality Criterion

If

\[
b^*G^{-1}b<1,
\]

then

\[
h\notin V_{\mathrm{RA1n}}.
\]

## Proof

Since \(\|h\|_2=1\), if \(h\in V_{\mathrm{RA1n}}\), then

\[
\Pi_Vh=h.
\]

Therefore

\[
\|\Pi_Vh\|_2^2=\|h\|_2^2=1.
\]

But the projection formula gives

\[
\|\Pi_Vh\|_2^2=b^*G^{-1}b.
\]

Thus

\[
b^*G^{-1}b<1
\]

implies

\[
h\notin V_{\mathrm{RA1n}}.
\]

## Angle-Gap Output

Set

\[
\alpha:=\sqrt{b^*G^{-1}b}.
\]

If

\[
\alpha<1,
\]

then by `RA1N_ANGLE_GAP_LEMMA.md`,

\[
\epsilon:=1-\alpha>0
\]

and

\[
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2
\qquad
\forall F\in V_{\mathrm{RA1n}}.
\]

## Terminal Form

\[
b^*G^{-1}b<1
\Longrightarrow
\text{Angle-Gap}.
\]
