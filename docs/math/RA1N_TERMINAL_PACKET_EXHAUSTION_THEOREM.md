# RA1n Terminal Packet Exhaustion Theorem

Status: OPEN.

## Object

Let

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\]

denote the terminal RA1n packet class.

Let

\[
V_{\mathrm{RA1n}}
=
\operatorname{span}\{\phi_1\}
\subset L^2.
\]

## Target Theorem

\[
\boxed{
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
}
\]

Equivalently,

\[
\boxed{
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\quad
\exists a(F)\in\mathbb C
\quad
F=a(F)\phi_1.
}
\]

Equivalently,

\[
\boxed{
\operatorname{dist}_{L^2}
\left(
F,
V_{\mathrm{RA1n}}
\right)
=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
}
\]

## Weakest Sufficient Lemma

Every terminal RA1n packet has zero orthogonal residual against the certified finite-basis surface:

\[
\boxed{
\|(I-\Pi_{V_{\mathrm{RA1n}}})F\|_2=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
}
\]

## Dependency

The Certified Conditional Closure

\[
\mathcal T_{\mathrm{RA1n}}(k)\ge 2>0
\]

becomes unrestricted only after this target theorem is proved.

## Current Status

The theorem is not proved by the finite-basis Gram certificate alone.

The missing object is the packet-exhaustion proof:

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
\operatorname{span}\{\phi_1\}.
\]
