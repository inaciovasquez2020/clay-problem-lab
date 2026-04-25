# RA1n Structural Counterexample Exclusion

Status: OPEN

## Object

Let \(g\in L^2\) and \(g\neq 0\). The unrestricted RA1n symbolic transfer route is blocked by the aligned packet

\[
F=\frac{\overline g}{\|g\|_2}.
\]

Indeed,

\[
\langle F,g\rangle
=
\int \frac{\overline g}{\|g\|_2}\,g
=
\|g\|_2
\neq 0,
\]

so

\[
F\notin g^\perp.
\]

## Weakest Missing Lemma

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
F\neq \frac{\overline g}{\|g\|_2}.
\]

## Stronger Angle-Gap Form

There exists \(\epsilon>0\) such that

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
|\langle F,g\rangle|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

## Projection-Error Positivity Requirement

Assume

\[
\mathcal T_{\mathrm{RA1n}}(k)
\ge
\mathrm{Curv}_k\,\mathrm{Gap}_k\,|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}.
\]

If

\[
\mathrm{Curv}_k\,\mathrm{Gap}_k\,|\partial_\xi\widehat G_k|
>
\|P_k\widehat G_k\|_{\mathrm{err}},
\]

then

\[
\mathcal T_{\mathrm{RA1n}}(k)\ge c_{\mathrm{RA1n}}>0.
\]

## Conditional Closure

The unrestricted RA1n symbolic transfer lemma follows conditionally from:

1. Structural counterexample exclusion.
2. Angle-gap domination.
3. Projection-error positivity.

## Terminal Status

Conditional.

Unrestricted RA1n remains OPEN until structural counterexample exclusion is proved.
