# RA1n Compactness-to-Delta Separation Lemma

Status: PROVED ABSTRACTLY

## Normalized Terminal Packet Set

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

## Hypotheses

\[
K \text{ is compact in } L^2,
\]

and

\[
K\cap \mathcal O_h=\varnothing.
\]

## Conclusion

There exists \(\delta>0\) such that

\[
\forall u\in K,
\qquad
\inf_{\theta\in\mathbb R}
\|u-e^{i\theta}h\|_2
\ge \delta.
\]

Equivalently,

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\inf_{\theta\in\mathbb R}
\left\|
\frac{F}{\|F\|_2}
-
e^{i\theta}\frac{\overline g}{\|g\|_2}
\right\|_2
\ge \delta.
\]

## Proof

The orbit \(\mathcal O_h\) is compact because it is the continuous image of the compact circle \(S^1\).

Since \(K\) and \(\mathcal O_h\) are compact and disjoint subsets of the metric space \(L^2\),

\[
\delta
=
\inf_{u\in K}
\inf_{\theta\in\mathbb R}
\|u-e^{i\theta}h\|_2
>0.
\]

Thus the RA1n delta-separation hypothesis follows.

## Angle-Gap Output

By `RA1N_DELTA_SEPARATION_LEMMA.md`,

\[
|\langle F,g\rangle_{\mathrm{RA1n}}|
\le
\left(1-\frac{\delta^2}{2}\right)
\|F\|_2\|g\|_2.
\]

Hence

\[
\epsilon=\frac{\delta^2}{2}.
\]

## Finite-Rank Compactness Source

The compactness hypothesis for \(K\) follows from `RA1N_FINITE_RANK_PACKET_COMPACTNESS.md` if the normalized terminal packet set is contained in a finite-dimensional RA1n packet subspace and is closed there.
