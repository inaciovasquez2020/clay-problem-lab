# DR33D Step 36 — PDE Shell-Exclusion Axiom

## Status
Conditional.

## Purpose

This step isolates the weakest PDE-level assumption currently sufficient to close the
Step 35 admissibility frontier.

## Shell profile

Let \(u\) be an admissible PDE state with shell energies
\[
E_j(u)\ge 0.
\]

Define
\[
S(E(u)):=\sum_{j\in\mathbb Z}E_j(u)^{1+\theta},
\qquad
\mathfrak C(E(u)):=\frac{\sup_j E_j(u)^{1+\theta}}{S(E(u))},
\qquad 0<\theta<1.
\]

Assume
\[
E_j(u)=0\qquad (j<j_0).
\]

## PDE shell-exclusion axiom

There exist constants
\[
\delta\in(0,1),\qquad m>0
\]
such that every PDE state \(u\) in the target class satisfies
\[
E_{j+1}(u)\le E_j(u),
\qquad
\mathfrak C(E(u))\le 1-\delta,
\qquad
S(E(u))\ge m.
\]

Equivalently,
\[
\boxed{
\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}.
}
\]

## Closure consequence

By Step 34 and Step 35, the PDE shell-exclusion axiom implies
\[
A(E(u))^2\le C(\theta,j_0,\delta,m)\,S(E(u)).
\]

Hence the full surviving linear frontier closes under this axiom.

## Canonical minimal form

The minimal remaining PDE object is exactly:

\[
\boxed{
\exists\,\delta\in(0,1),\ m>0
\text{ such that }
\mathcal P(u)\Longrightarrow
\bigl(\mathfrak C(E(u))\le 1-\delta \ \wedge\ S(E(u))\ge m\bigr).
}
\]

with monotonicity
\[
E_{j+1}(u)\le E_j(u)
\]
included as part of admissibility.

## Lock sentence

Step 36 records the exact PDE shell-exclusion axiom whose proof is equivalent to
closing the current DR33D surviving frontier.
