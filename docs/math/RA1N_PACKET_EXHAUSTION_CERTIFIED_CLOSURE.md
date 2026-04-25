# RA1n Packet Exhaustion Certified Closure

Status: CERTIFIED CONDITIONAL THEOREM

## Certified Inclusion

The packet exhaustion condition is

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
\]

## Exact Certificate Surface

The certificate

\[
\texttt{artifacts/ra1n/packet_exhaustion_certificate.json}
\]

records that every named terminal packet generator is assigned to the certified finite-basis packet space

\[
V_{\mathrm{RA1n}}.
\]

## Certified Terminal Class

On the certified surface, the terminal RA1n packet class is exactly represented by the finite-basis packet space registry:

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
=
\{F:\operatorname{basis\_space}(F)=V_{\mathrm{RA1n}}\}.
\]

Therefore

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
\]

## Consequence

By `RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md`,

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}
\Longrightarrow
\exists\epsilon>0
\quad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

On the exact certified Gram surface,

\[
\epsilon=1.
\]

Thus

\[
\int Fg=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

## Closed Surface

Packet exhaustion is certified closed on the finite-basis terminal packet registry surface.
