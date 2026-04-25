# RA1n Terminal Packet Exhaustion Theorem

Status: CERTIFIED CONDITIONAL THEOREM

## Object

Let

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1\}\subset L^2.
\]

Let

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}\subset L^2
\]

be the terminal RA1n packet class.

## Rank-One Terminal Packet Hypothesis

Assume

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\exists a(F)\in\mathbb C
\quad
F=a(F)\phi_1.
\]

## Theorem

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
\]

Equivalently,

\[
\operatorname{dist}_{L^2}
\left(
F,
V_{\mathrm{RA1n}}
\right)
=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

## Proof

Let

\[
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

By the rank-one terminal packet hypothesis, there exists

\[
a(F)\in\mathbb C
\]

such that

\[
F=a(F)\phi_1.
\]

Since

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1\},
\]

we have

\[
F\in V_{\mathrm{RA1n}}.
\]

Therefore

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
\]

Since \(F\in V_{\mathrm{RA1n}}\), its distance to \(V_{\mathrm{RA1n}}\) is zero:

\[
\operatorname{dist}_{L^2}
\left(
F,
V_{\mathrm{RA1n}}
\right)
=0.
\]

## Certified Consequence

By `RA1N_PACKET_EXHAUSTION_CERTIFIED_CLOSURE.md`,

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}
\Longrightarrow
\text{packet exhaustion}.
\]

By `RA1N_FINAL_CERTIFIED_CONDITIONAL_CLOSURE.md`,

\[
\text{packet exhaustion}
\Longrightarrow
\mathcal T_{\mathrm{RA1n}}(k)\ge c_{\mathrm{RA1n}}>0
\]

on the certified finite-basis RA1n surface.

## Closed Surface

The terminal packet exhaustion theorem is proved conditionally on the rank-one terminal packet hypothesis

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
F=a(F)\phi_1.
\]
