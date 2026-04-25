# RA1n Weak Orthogonality from Residual Norm Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\mathcal W_{\mathrm{term}}(\chi)=0.
\]

## Residual Norm Identity

Let

\[
r_W(\chi):=(I-\Pi_W)\chi.
\]

Assume

\[
\mathcal W_{\mathrm{term}}(\chi)=\|r_W(\chi)\|_2.
\]

## Residual Vanishing Hypothesis

Assume terminal admissibility forces

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\|r_W(\chi)\|_2=0.
\]

## Theorem

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\mathcal W_{\mathrm{term}}(\chi)=0.
\]

## Proof

Assume

\[
\mathcal A_{\mathrm{term}}(\chi).
\]

By residual vanishing,

\[
\|r_W(\chi)\|_2=0.
\]

By the residual norm identity,

\[
\mathcal W_{\mathrm{term}}(\chi)
=
\|r_W(\chi)\|_2
=
0.
\]

## Consequence

By `RA1N_TERMINAL_ADMISSIBILITY_WEAK_ORTHOGONALITY_THEOREM.md`,

\[
\mathcal W_{\mathrm{term}}(\chi)=0
\Longrightarrow
\forall \zeta\in W_{\mathrm{term}}^\perp,
\quad
\langle \chi,\zeta\rangle_{L^2}=0.
\]

## Remaining Non-Conditional Obligation

Prove terminal residual vanishing:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\|r_W(\chi)\|_2=0.
\]
