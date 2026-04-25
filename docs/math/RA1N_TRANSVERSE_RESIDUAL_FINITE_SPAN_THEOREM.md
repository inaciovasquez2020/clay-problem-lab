# RA1n Transverse Residual Finite-Span Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove

\[
r=(I-\Pi_V)F,
\qquad
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\Longrightarrow
r\in W_{\perp}.
\]

## Objects

Let

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1\}.
\]

Let

\[
\Pi_V:L^2\to V_{\mathrm{RA1n}}
\]

be the orthogonal projection.

Let

\[
W_{\perp}
=
\operatorname{span}\{\psi_1,\dots,\psi_m\}
\subset
V_{\mathrm{RA1n}}^\perp.
\]

Define the terminal transverse residual

\[
r(F):=(I-\Pi_V)F.
\]

## Finite Transverse Generator Hypothesis

Assume every terminal packet admits the finite residual expansion

\[
(I-\Pi_V)F
=
\sum_{j=1}^m c_j(F)\psi_j
\]

for some coefficients

\[
c_j(F)\in\mathbb C.
\]

## Theorem

For every

\[
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\]

one has

\[
r(F)\in W_{\perp}.
\]

## Proof

Let

\[
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

By the finite transverse generator hypothesis,

\[
r(F)
=
(I-\Pi_V)F
=
\sum_{j=1}^m c_j(F)\psi_j.
\]

Since

\[
W_{\perp}
=
\operatorname{span}\{\psi_1,\dots,\psi_m\},
\]

it follows that

\[
r(F)\in W_{\perp}.
\]

Therefore

\[
r=(I-\Pi_V)F,
\qquad
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\Longrightarrow
r\in W_{\perp}.
\]

## Consequence

By `RA1N_TRANSVERSE_RAYLEIGH_GAP_CERTIFICATE_THEOREM.md`,

\[
r\in W_{\perp}
\Longrightarrow
\langle r,A_{\perp}r\rangle_{L^2}
\ge
\eta\|r\|_2^2.
\]

By `RA1N_TRANSVERSE_SPECTRAL_GAP_COERCIVITY_THEOREM.md`, this gives

\[
E_{\perp}(r)\ge \eta\|r\|_2^2.
\]

By `RA1N_NORMALIZED_TRANSVERSE_COERCIVITY_THEOREM.md`, normalized nonzero transverse residuals satisfy

\[
E_{\mathrm{term}}(r)\ge E_*+\eta.
\]

By `RA1N_TRANSVERSE_ENERGY_GAP_EXCLUSION_THEOREM.md`, nonzero transverse terminal residuals are excluded.

## Remaining Non-Conditional Obligation

Prove the finite transverse generator hypothesis from the actual terminal packet grammar:

\[
(I-\Pi_V)F
=
\sum_{j=1}^m c_j(F)\psi_j
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]
