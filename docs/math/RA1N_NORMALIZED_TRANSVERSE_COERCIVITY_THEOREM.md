# RA1n Normalized Transverse Coercivity Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove the transverse energy-gap hypothesis

\[
\psi\in V_{\mathrm{RA1n}}^\perp,
\qquad
\psi\neq0
\Longrightarrow
E_{\mathrm{term}}(\psi)\ge E_*+\eta.
\]

## Required Normalization

A uniform transverse gap is admissible only on the normalized terminal transverse class:

\[
\psi\in V_{\mathrm{RA1n}}^\perp,
\qquad
\|\psi\|_2=1.
\]

## Coercive Energy Decomposition

Assume

\[
E_{\mathrm{term}}(F)
=
E_{\parallel}(\Pi_VF)
+
E_{\perp}((I-\Pi_V)F),
\]

and assume there exists

\[
\eta>0
\]

such that

\[
E_{\perp}(r)\ge \eta\|r\|_2^2
\qquad
\forall r\in V_{\mathrm{RA1n}}^\perp.
\]

Assume also

\[
E_{\parallel}(0)\ge E_*.
\]

## Theorem

For every normalized transverse packet

\[
\psi\in V_{\mathrm{RA1n}}^\perp,
\qquad
\|\psi\|_2=1,
\]

one has

\[
E_{\mathrm{term}}(\psi)\ge E_*+\eta.
\]

## Proof

Let

\[
\psi\in V_{\mathrm{RA1n}}^\perp,
\qquad
\|\psi\|_2=1.
\]

Then

\[
\Pi_V\psi=0
\]

and

\[
(I-\Pi_V)\psi=\psi.
\]

Therefore

\[
E_{\mathrm{term}}(\psi)
=
E_{\parallel}(0)
+
E_{\perp}(\psi).
\]

By the baseline bound,

\[
E_{\parallel}(0)\ge E_*.
\]

By transverse coercivity,

\[
E_{\perp}(\psi)\ge \eta\|\psi\|_2^2=\eta.
\]

Thus

\[
E_{\mathrm{term}}(\psi)
\ge
E_*+\eta.
\]

## Consequence

By `RA1N_TRANSVERSE_ENERGY_GAP_EXCLUSION_THEOREM.md`,

\[
E_{\mathrm{term}}(\psi)\ge E_*+\eta
\]

excludes every normalized nonzero transverse terminal generator.

## Remaining Non-Conditional Obligation

Prove the coercive energy decomposition and transverse coercivity inequality from the actual RA1n terminal construction:

\[
E_{\mathrm{term}}(F)
=
E_{\parallel}(\Pi_VF)
+
E_{\perp}((I-\Pi_V)F),
\]

\[
E_{\perp}(r)\ge \eta\|r\|_2^2.
\]
