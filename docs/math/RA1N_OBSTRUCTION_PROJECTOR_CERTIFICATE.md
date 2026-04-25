# RA1n Obstruction Projector Certificate

Status: PROVED ABSTRACTLY

## Objects

Let

\[
h=\frac{\overline g}{\|g\|_2},
\qquad
\|h\|_2=1.
\]

Let \(V_{\mathrm{RA1n}}\subset L^2\) be a finite-dimensional packet subspace such that

\[
K\subset V_{\mathrm{RA1n}}.
\]

Let \(\Pi_V\) be the orthogonal projection onto \(V_{\mathrm{RA1n}}\).

## Transversality Hypothesis

\[
h\notin V_{\mathrm{RA1n}}.
\]

Equivalently,

\[
\alpha:=\|\Pi_V h\|_2<1.
\]

## Rank-One Certificate

Define

\[
Q_h u=\langle u,h\rangle_{L^2}h.
\]

Then \(Q_h\) is bounded, self-adjoint, positive, and rank one.

Define

\[
\Phi_{Q_h}(u)
=
\frac{\langle u,Q_hu\rangle_{L^2}}{\|u\|_2^2}
=
\frac{|\langle u,h\rangle_{L^2}|^2}{\|u\|_2^2}.
\]

## Packet Bound

For every \(u\in K\),

\[
u\in V_{\mathrm{RA1n}},
\qquad
\|u\|_2=1,
\]

so

\[
|\langle u,h\rangle_{L^2}|
=
|\langle u,\Pi_Vh\rangle_{L^2}|
\le
\|\Pi_Vh\|_2
=
\alpha.
\]

Therefore

\[
\Phi_{Q_h}(u)\le \alpha^2.
\]

## Obstruction Value

\[
\Phi_{Q_h}(h)
=
|\langle h,h\rangle_{L^2}|^2
=
1.
\]

Since \(\alpha<1\),

\[
\sup_{u\in K}\Phi_{Q_h}(u)
\le
\alpha^2
<
1
=
\Phi_{Q_h}(h).
\]

## Consequence

By `RA1N_QUADRATIC_INVARIANT_CERTIFICATE.md`,

\[
K\cap\mathcal O_h=\varnothing.
\]

Moreover,

\[
|\langle u,h\rangle_{L^2}|
\le
\alpha
\qquad
\forall u\in K.
\]

Thus the angle-gap constant may be taken as

\[
\epsilon=1-\alpha.
\]

Equivalently,

\[
|\langle F,g\rangle_{\mathrm{RA1n}}|
\le
\alpha\|F\|_2\|g\|_2
=
(1-\epsilon)\|F\|_2\|g\|_2.
\]

## Terminal Reduction

The RA1n structural counterexample exclusion is solved under the single concrete transversality condition

\[
\frac{\overline g}{\|g\|_2}\notin V_{\mathrm{RA1n}}.
\]
