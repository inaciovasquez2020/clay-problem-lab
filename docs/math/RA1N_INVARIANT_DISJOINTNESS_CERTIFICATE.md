# RA1n Invariant Disjointness Certificate

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
\ F\neq 0
\right\}
\subset L^2.
\]

Let

\[
h=\frac{\overline g}{\|g\|_2},
\qquad
\mathcal O_h=\{e^{i\theta}h:\theta\in\mathbb R\}.
\]

## Certificate Hypothesis

There exists a phase-invariant RA1n structural functional

\[
\Phi:L^2\setminus\{0\}\to X
\]

such that

\[
\Phi(e^{i\theta}u)=\Phi(u)
\]

for all \(u\neq0\), and there exist disjoint sets \(A,B\subset X\) satisfying

\[
\Phi(K)\subset A,
\qquad
\Phi(h)\in B,
\qquad
A\cap B=\varnothing.
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
\Phi(u)=\Phi(e^{i\theta}h)=\Phi(h).
\]

Since \(u\in K\),

\[
\Phi(u)\in A.
\]

Since \(\Phi(h)\in B\),

\[
\Phi(u)\in B.
\]

Therefore

\[
\Phi(u)\in A\cap B,
\]

contradicting

\[
A\cap B=\varnothing.
\]

Hence

\[
K\cap\mathcal O_h=\varnothing.
\]

## Quadratic Invariant Instantiation

A concrete phase-invariant functional is supplied by `RA1N_QUADRATIC_INVARIANT_CERTIFICATE.md`.

It suffices to find a bounded self-adjoint \(Q:L^2\to L^2\) such that

\[
\sup_{u\in K}
\frac{\langle u,Qu\rangle_{L^2}}{\|u\|_2^2}
<
\frac{\langle h,Qh\rangle_{L^2}}{\|h\|_2^2}.
\]

## Terminal Use

This proves the disjointness input required by `RA1N_COMPACTNESS_TO_DELTA_SEPARATION.md` once a phase-invariant structural RA1n certificate separates the normalized terminal packet set from the aligned obstruction orbit.
