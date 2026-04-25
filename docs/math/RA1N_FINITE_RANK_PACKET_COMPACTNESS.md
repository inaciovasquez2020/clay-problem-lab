# RA1n Finite-Rank Packet Compactness Lemma

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

## Hypotheses

There exists a finite-dimensional subspace

\[
V_{\mathrm{RA1n}}\subset L^2
\]

such that

\[
K\subset V_{\mathrm{RA1n}}.
\]

The set \(K\) is closed in \(V_{\mathrm{RA1n}}\).

## Conclusion

\[
K\text{ is compact in }L^2.
\]

## Proof

Every element \(u\in K\) satisfies

\[
\|u\|_2=1.
\]

Hence

\[
K\subset V_{\mathrm{RA1n}}\cap \{u:\|u\|_2=1\}.
\]

Since \(V_{\mathrm{RA1n}}\) is finite-dimensional, its unit sphere is compact.

Since \(K\) is closed in \(V_{\mathrm{RA1n}}\), \(K\) is a closed subset of a compact set.

Therefore

\[
K\text{ is compact in }L^2.
\]

## Terminal Use

This proves the compactness input required by `RA1N_COMPACTNESS_TO_DELTA_SEPARATION.md`, provided the normalized terminal packet class is finite-rank and closed.
