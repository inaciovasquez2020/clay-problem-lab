# RA1n Terminal Residual-Zero Certified Closure

Status: CERTIFIED CONDITIONAL THEOREM

## Objects

Let

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1\}\subset L^2.
\]

Let

\[
\Pi_V:L^2\to V_{\mathrm{RA1n}}
\]

be the orthogonal projection.

Let

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}\subset L^2
\]

be the terminal RA1n packet class.

Define the terminal residual

\[
R(F):=(I-\Pi_V)F.
\]

## Certified Packet Exhaustion Input

The executable packet exhaustion certificate verifies

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
\]

Equivalently,

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
F\in V_{\mathrm{RA1n}}.
\]

## Theorem

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
R(F)=0.
\]

Equivalently,

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
(I-\Pi_V)F=0.
\]

## Proof

Let

\[
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

By certified packet exhaustion,

\[
F\in V_{\mathrm{RA1n}}.
\]

Since \(\Pi_V\) is the orthogonal projection onto \(V_{\mathrm{RA1n}}\),

\[
\Pi_VF=F.
\]

Therefore

\[
R(F)
=
(I-\Pi_V)F
=
F-\Pi_VF
=
F-F
=
0.
\]

Hence

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
(I-\Pi_V)F=0.
\]

## Distance Form

Since \(R(F)=0\),

\[
\operatorname{dist}_{L^2}(F,V_{\mathrm{RA1n}})
=
\|(I-\Pi_V)F\|_2
=
0.
\]

## Closed Surface

The terminal residual-zero theorem is certified closed on the packet-exhausted finite-basis RA1n surface.
