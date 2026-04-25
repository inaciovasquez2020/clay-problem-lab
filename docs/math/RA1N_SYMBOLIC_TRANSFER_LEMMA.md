# RA1n Symbolic Transfer Lemma

Status: OPEN

## Object

Let

\[
r_k(\xi)=\widehat G_k(\xi)-P_k\widehat G_k(\xi).
\]

## Target Lemma

On the terminal high-high resonance packet class, the locked curvature-gain hypotheses imply a strictly positive lower bound for the RA1n residual transfer:

\[
\mathcal T_{RA1n}(k) \ge c_{RA1n} > 0.
\]

## Required Inputs

1. Exact packet normalization.
2. Exact curvature lower bound.
3. Exact transverse-gap lower bound.
4. Exact derivative-size compatibility.
5. Projection-error control for \(P_k\widehat G_k\).

## Missing Step

Prove that the numerical transfer registry is a consequence of the symbolic inequalities above, not an independent empirical assumption.

## Frontier Status

This is the weakest theorem-grade bridge between the current numerical RA1n evidence registry and the full RA1n terminal obstruction.

## Required Structural Counterexample Exclusion

The unrestricted symbolic transfer route additionally requires

\[
orall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
F
eq rac{\overline g}{\|g\|_2}.
\]

See `RA1N_STRUCTURAL_COUNTEREXAMPLE_EXCLUSION.md`.

## Required Projection-Error Positivity

The transfer lower bound also requires the strict domination inequality recorded in `RA1N_PROJECTION_ERROR_DOMINATION.md`.
