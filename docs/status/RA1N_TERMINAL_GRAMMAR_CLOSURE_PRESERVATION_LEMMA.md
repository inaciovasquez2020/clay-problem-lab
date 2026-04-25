# RA1n Terminal Grammar Closure Preservation Lemma

Status: OPEN.

## Lemma

Let \(\Omega_{\mathrm{term}}\) be the set of operations in the actual RA1n terminal grammar.

For every operation

\[
\omega\in\Omega_{\mathrm{term}},
\]

with arity \(q(\omega)\),

\[
\chi_1,\dots,\chi_{q(\omega)}\in W_{\mathrm{term}}
\Longrightarrow
\omega(\chi_1,\dots,\chi_{q(\omega)})\in W_{\mathrm{term}}.
\]

Equivalently,

\[
(I-\Pi_W)\omega(\chi_1,\dots,\chi_{q(\omega)})=0.
\]

Equivalently,

\[
\mathcal R_{\mathrm{term}}
\bigl(\omega(\chi_1,\dots,\chi_{q(\omega)})\bigr)=0.
\]

## Rebuild target

Together with the Terminal Grammar Atom Span Lemma,

\[
\forall \gamma\in\mathfrak G_{\mathrm{atom}},
\qquad
\gamma\in W_{\mathrm{term}},
\]

this lemma implies that every finite grammar-generated terminal object lies in \(W_{\mathrm{term}}\).

## No-overclaim lock

This document does not identify the actual RA1n grammar operations.
This document does not prove closure preservation.
It records the next weakest sufficient grammar-level object.
