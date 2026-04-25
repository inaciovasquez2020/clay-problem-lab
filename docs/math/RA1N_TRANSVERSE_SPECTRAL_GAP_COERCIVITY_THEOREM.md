# RA1n Transverse Spectral-Gap Coercivity Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove the transverse coercivity inequality

\[
E_{\perp}(r)\ge \eta\|r\|_2^2
\qquad
\forall r\in V_{\mathrm{RA1n}}^\perp.
\]

## Spectral-Gap Hypothesis

Let

\[
A_{\perp}:V_{\mathrm{RA1n}}^\perp\to V_{\mathrm{RA1n}}^\perp
\]

be the transverse terminal energy operator.

Assume \(A_{\perp}\) is self-adjoint and satisfies the operator lower bound

\[
\langle r,A_{\perp}r\rangle_{L^2}
\ge
\eta\|r\|_2^2
\qquad
\forall r\in V_{\mathrm{RA1n}}^\perp
\]

for some

\[
\eta>0.
\]

Define

\[
E_{\perp}(r):=\langle r,A_{\perp}r\rangle_{L^2}.
\]

## Theorem

For every

\[
r\in V_{\mathrm{RA1n}}^\perp,
\]

one has

\[
E_{\perp}(r)\ge \eta\|r\|_2^2.
\]

## Proof

Let

\[
r\in V_{\mathrm{RA1n}}^\perp.
\]

By definition,

\[
E_{\perp}(r)=\langle r,A_{\perp}r\rangle_{L^2}.
\]

By the spectral-gap hypothesis,

\[
\langle r,A_{\perp}r\rangle_{L^2}
\ge
\eta\|r\|_2^2.
\]

Therefore

\[
E_{\perp}(r)\ge \eta\|r\|_2^2.
\]

## Consequence

By `RA1N_NORMALIZED_TRANSVERSE_COERCIVITY_THEOREM.md`, the transverse energy-gap follows for normalized transverse terminal packets:

\[
\psi\in V_{\mathrm{RA1n}}^\perp,
\qquad
\|\psi\|_2=1
\Longrightarrow
E_{\mathrm{term}}(\psi)\ge E_*+\eta.
\]

## Remaining Non-Conditional Obligation

Prove the spectral-gap lower bound for the actual RA1n transverse terminal energy operator:

\[
A_{\perp}\ge \eta I
\quad
\text{on}
\quad
V_{\mathrm{RA1n}}^\perp.
\]
