# RA1n Quadratic Invariant Certificate

Status: PROVED ABSTRACTLY

## Objects

Let

\[
K
=
\left\{
\frac{F}{\|F\|_2}
:
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\ F\neq0
\right\}
\subset L^2.
\]

Let

\[
h=\frac{\overline g}{\|g\|_2}.
\]

Let \(Q:L^2\to L^2\) be bounded and self-adjoint.

Define

\[
\Phi_Q(u)
=
\frac{\langle u,Qu\rangle_{L^2}}{\|u\|_2^2}.
\]

## Phase Invariance

For every \(u\neq0\) and every \(\theta\in\mathbb R\),

\[
\Phi_Q(e^{i\theta}u)
=
\Phi_Q(u).
\]

## Separation Hypothesis

There exist real numbers \(a,b\) with

\[
a<b
\]

such that

\[
\Phi_Q(u)\le a
\qquad
\forall u\in K,
\]

and

\[
\Phi_Q(h)\ge b.
\]

## Conclusion

\[
K\cap\mathcal O_h=\varnothing.
\]

## Proof

Assume for contradiction that

\[
u\in K\cap\mathcal O_h.
\]

Then for some \(\theta\in\mathbb R\),

\[
u=e^{i\theta}h.
\]

By phase invariance,

\[
\Phi_Q(u)=\Phi_Q(h).
\]

Since \(u\in K\),

\[
\Phi_Q(u)\le a.
\]

Since \(\Phi_Q(h)\ge b\),

\[
\Phi_Q(u)\ge b.
\]

Thus

\[
b\le \Phi_Q(u)\le a,
\]

contradicting

\[
a<b.
\]

Therefore

\[
K\cap\mathcal O_h=\varnothing.
\]

## Terminal Use

This instantiates the phase-invariant structural functional required by `RA1N_INVARIANT_DISJOINTNESS_CERTIFICATE.md`.

The remaining concrete certificate is a bounded self-adjoint \(Q\) satisfying

\[
\sup_{u\in K}\Phi_Q(u)
<
\Phi_Q(h).
\]

## Rank-One Obstruction Projector Instantiation

A concrete quadratic certificate is supplied by `RA1N_OBSTRUCTION_PROJECTOR_CERTIFICATE.md`.

If

\[
h=rac{\overline g}{\|g\|_2}
otin V_{\mathrm{RA1n}},
\]

then \(Q_hu=\langle u,h\rangle h\) separates the normalized terminal packet set from the obstruction orbit.
