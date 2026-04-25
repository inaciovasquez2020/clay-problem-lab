# RA1n Terminal Packet Normal-Form Criterion

Status: OPEN.

## Object

Let

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\]

be the terminal RA1n packet class.

Let

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1\}.
\]

## Target Criterion

\[
\boxed{
\forall F\in \mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\quad
\exists a(F)\in\mathbb C
\quad
F=a(F)\phi_1.
}
\]

## Consequence

\[
\boxed{
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
}
\]

## Weakest Missing Object

A definition-level normal form for terminal RA1n packets:

\[
\boxed{
F(\eta)=a(F)\phi_1(\eta)
\qquad
\forall F\in \mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
}
\]

## Halt Condition

If terminal RA1n packets admit any independent residual mode

\[
r(F):=F-\Pi_{V_{\mathrm{RA1n}}}F
\neq 0,
\]

then terminal packet exhaustion fails.
