# RA1n Terminal Grammar Completeness Lemma

Status: OPEN.

## Lemma

Let \(\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}})\) denote the smallest class containing the terminal grammar atoms and closed under the actual RA1n terminal grammar operations.

\[
\forall \chi\in L^2,\quad
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi\in
\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}}).
\]

## Rebuild target

If

\[
\mathfrak G_{\mathrm{atom}}\subset W_{\mathrm{term}}
\]

and every operation in \(\Omega_{\mathrm{term}}\) preserves \(W_{\mathrm{term}}\), then

\[
\operatorname{Cl}_{\Omega_{\mathrm{term}}}(\mathfrak G_{\mathrm{atom}})
\subset W_{\mathrm{term}}.
\]

Therefore this lemma gives

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi\in W_{\mathrm{term}}
\Longrightarrow
\mathcal R_{\mathrm{term}}(\chi)=0.
\]

## No-overclaim lock

This document does not identify the actual terminal grammar closure.
This document does not prove grammar completeness.
It records the next weakest sufficient admissibility-to-grammar object.
