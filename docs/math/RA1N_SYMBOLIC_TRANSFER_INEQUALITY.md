# RA1n Symbolic Transfer Inequality

Status: OPEN.

## Object

Let

\[
\mathcal T_{\mathrm{RA1n}}(k)
\]

denote the RA1n transfer quantity.

Let

\[
\mathrm{Curv}_k,\qquad
\mathrm{Gap}_k,\qquad
|\partial_\xi\widehat G_k|,
\qquad
\|P_k\widehat G_k\|_{\mathrm{err}}
\]

be the certified curvature, transverse gap, symbolic derivative, and projection-error terms.

## Target Theorem

\[
\boxed{
\mathcal T_{\mathrm{RA1n}}(k)
\ge
\mathrm{Curv}_k\mathrm{Gap}_k
|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}.
}
\]

## Certified Consequence

Using the certified values

\[
\mathrm{Curv}_k=2,
\qquad
\mathrm{Gap}_k=1,
\qquad
|\partial_\xi\widehat G_k|=1,
\qquad
\|P_k\widehat G_k\|_{\mathrm{err}}=0,
\]

the target theorem gives

\[
\mathcal T_{\mathrm{RA1n}}(k)\ge 2>0.
\]

## Weakest Missing Object

A symbolic lower-bound proof converting the certified curvature-gap margin into the RA1n transfer lower bound:

\[
\mathrm{Curv}_k\mathrm{Gap}_k
|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}
\le
\mathcal T_{\mathrm{RA1n}}(k).
\]

## Failure Witness

The theorem fails if there exists an admissible certified packet configuration such that

\[
\mathcal T_{\mathrm{RA1n}}(k)
<
\mathrm{Curv}_k\mathrm{Gap}_k
|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}.
\]
