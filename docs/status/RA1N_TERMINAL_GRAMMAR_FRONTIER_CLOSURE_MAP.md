# RA1n Terminal Grammar Frontier Closure Map

Status: CLOSED AS FRONTIER MAP / OPEN AS THEOREM.

## Closed repository-scope object

This document closes the current RA1n terminal-grammar decomposition layer as a repository-scope frontier map.

It does not close the theorem-level RA1n frontier.

It does not prove Navier--Stokes regularity.

## Original theorem-level frontier

\[
\mathcal A_{\mathrm{term}}(\chi)
\iff
\mathcal R_{\mathrm{term}}(\chi)=0.
\]

Equivalently,

\[
\mathcal A_{\mathrm{term}}(\chi)
\iff
(I-\Pi_W)\chi=0.
\]

Equivalently,

\[
\mathcal A_{\mathrm{term}}(\chi)
\iff
\chi\in W_{\mathrm{term}}.
\]

## Direct missing lemma

The direct route is the Terminal Grammar Annihilator Lemma:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\forall \zeta\in W_{\mathrm{term}}^\perp,\quad
\langle \chi,\zeta\rangle_{L^2}=0.
\]

This implies

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\mathcal W_{\mathrm{term}}(\chi)=0
\Longrightarrow
(I-\Pi_W)\chi=0
\Longrightarrow
\mathcal R_{\mathrm{term}}(\chi)=0.
\]

Status: OPEN.

## Grammar-generation route

The grammar-generation route decomposes the same frontier into three open objects.

### 1. Terminal Grammar Atom Span Lemma

\[
\forall \gamma\in\mathfrak G_{\mathrm{atom}},\quad
\gamma\in W_{\mathrm{term}}.
\]

Status: OPEN.

### 2. Terminal Grammar Closure Preservation Lemma

For every operation \(\omega\in\Omega_{\mathrm{term}}\),

\[
\chi_1,\dots,\chi_{q(\omega)}\in W_{\mathrm{term}}
\Longrightarrow
\omega(\chi_1,\dots,\chi_{q(\omega)})\in W_{\mathrm{term}}.
\]

Status: OPEN.

### 3. Terminal Grammar Completeness Lemma

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi\in
\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}}).
\]

Status: OPEN.

## Conditional rebuild

Conditional on the three grammar-generation lemmas,

\[
\mathfrak G_{\mathrm{atom}}\subset W_{\mathrm{term}}
\]

and

\[
\Omega_{\mathrm{term}}\text{ preserves }W_{\mathrm{term}}
\]

give

\[
\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}})
\subset W_{\mathrm{term}}.
\]

Together with grammar completeness,

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi\in W_{\mathrm{term}}
\Longrightarrow
(I-\Pi_W)\chi=0
\Longrightarrow
\mathcal R_{\mathrm{term}}(\chi)=0.
\]

## Final repository-scope closure statement

The current RA1n terminal-grammar decomposition is closed as a dependency map.

The remaining theorem-level input is exactly one of the following:

1. prove the Terminal Grammar Annihilator Lemma directly from the actual RA1n terminal grammar;

or

2. prove all three grammar-generation lemmas:
   - Terminal Grammar Atom Span Lemma;
   - Terminal Grammar Closure Preservation Lemma;
   - Terminal Grammar Completeness Lemma.

No further repository-scope decomposition is admitted without a new actual RA1n terminal grammar definition.
