# RA1n Canonical Status Snapshot — 2026-04-25

Status: CANONICAL SNAPSHOT

Full_RA1n_status: CONDITIONAL

## Locked chain

1. Unary normalized derivative obstruction: CLOSED inside the unary lane.
2. Conservation-transfer frontier: LOCKED.
3. Terminal frontier registry: LOCKED.
4. Unconditional-promotion audit: ACTIVE.
5. \(g^\perp\) terminal assumption: LOCKED.
6. Terminal frontier chain: LOCKED.

## Active terminal dependency

\[
F\in g^\perp
\]

or

\[
g\equiv0.
\]

## Required parametrization

\[
\Phi_{\xi_{\mathrm{out}}}(\eta)
=
(\xi_{\mathrm{out}}-\eta,\eta).
\]

## Counterexample guard

\[
g(\eta)
=
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
J_{k,\omega}(\eta).
\]

If

\[
g\not\equiv0,
\]

then

\[
F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}
\]

violates weighted FM-1 transfer.

## Promotion rule

Full RA1n promotion requires:

\[
\text{unary closure lane}
+
\text{Weighted Affine-Transfer Cancellation Lemma}
+
(F\in g^\perp\ \text{or}\ g\equiv0).
\]

## Current repository status

\[
\boxed{
\text{RA1n is conditionally frontier-locked, not promoted beyond the terminal dependency.}
}
\]
