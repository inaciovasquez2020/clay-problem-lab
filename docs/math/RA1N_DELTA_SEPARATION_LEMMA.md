# RA1n Delta-Separation Lemma

Status: OPEN

## Pairing Convention

Let the RA1n transfer pairing be

\[
B(F,g)=\int Fg.
\]

Let

\[
h=\frac{\overline g}{\|g\|_2}.
\]

Then

\[
\frac{B(F,g)}{\|F\|_2\|g\|_2}
=
\left\langle
\frac{F}{\|F\|_2},
h
\right\rangle_{L^2},
\]

where

\[
\langle u,v\rangle_{L^2}=\int u\overline v.
\]

## Delta-Separation Hypothesis

There exists \(\delta>0\) such that

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

## Angle-Gap Consequence

For every nonzero \(F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}\),

\[
\left|
\left\langle
\frac{F}{\|F\|_2},
\frac{\overline g}{\|g\|_2}
\right\rangle_{L^2}
\right|
\le
1-\frac{\delta^2}{2}.
\]

Hence

\[
|B(F,g)|
\le
\left(1-\frac{\delta^2}{2}\right)\|F\|_2\|g\|_2.
\]

Equivalently,

\[
|\langle F,g\rangle_{\mathrm{RA1n}}|
\le
(1-\epsilon)\|F\|_2\|g\|_2,
\qquad
\epsilon=\frac{\delta^2}{2}.
\]

## Terminal Reduction

The RA1n structural counterexample exclusion reduces to proving the positive separation

\[
\operatorname{dist}_{L^2/S^1}
\left(
\frac{\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}}{\|\cdot\|_2},
\frac{\overline g}{\|g\|_2}
\right)
>0.
\]

## Compactness Source

The positive separation \(\delta>0\) follows from `RA1N_COMPACTNESS_TO_DELTA_SEPARATION.md` once the normalized terminal packet set is compact in \(L^2\) and disjoint from the obstruction orbit.
