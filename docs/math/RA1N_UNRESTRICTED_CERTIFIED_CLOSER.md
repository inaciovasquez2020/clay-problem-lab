# RA1n Unrestricted Certified Closer

Status: CERTIFIED CONDITIONAL THEOREM

## Objects

Let

\[
g\neq0,
\qquad
h:=\frac{\overline g}{\|g\|_2}.
\]

Let

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset L^2
\]

be the unrestricted terminal RA1n packet class.

Let

\[
V_{\mathrm{RA1n}}
=
\operatorname{span}\{\phi_1,\dots,\phi_m\}
\subset L^2.
\]

## Exhaustion Hypothesis

Assume

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
\]

## Certified Finite-Basis Input

The exact Gram certificate verifies

\[
b^*G^{-1}b=0<1.
\]

Therefore, by `RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md`,

\[
h\notin V_{\mathrm{RA1n}}
\]

and

\[
\exists\epsilon>0
\quad
\forall F\in V_{\mathrm{RA1n}},
\qquad
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

For the certified exact surface,

\[
\epsilon=1.
\]

## Unrestricted Closer

Since

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}},
\]

the same bound holds for every unrestricted terminal packet:

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

With the certified value \(\epsilon=1\),

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\int Fg=0.
\]

## Consequence

The aligned obstruction

\[
F=\frac{\overline g}{\|g\|_2}
\]

is excluded from the unrestricted terminal RA1n packet class under the exhaustion hypothesis.

## Terminal Chain

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}\subset V_{\mathrm{RA1n}}
\Longrightarrow
b^*G^{-1}b=0<1
\Longrightarrow
h\notin V_{\mathrm{RA1n}}
\Longrightarrow
\text{Angle-Gap on }\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

## Closed Surface

The unrestricted RA1n angle-gap closer is certified on the packet-exhausted finite-basis surface.
