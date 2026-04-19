# Exact DDYO Symbol Curvature Lemma

**Status: OPEN**

## Purpose

This note records the exact missing theorem-level input for the terminal frontier
`terminal_high_high_resonance_curvature_gain`.

## Lemma (target statement)

Let
\[
r_k(\xi,\eta)
=
F_k(\xi,\eta)-F_k(\xi,\eta_{\parallel}),
\]
where \(\eta_{\parallel}\) denotes the projection of \(\eta\) onto the \(\xi\)-axis,
and let the admissible DDYO retained class be the repository-native class enforced by
`terminal_high_high_resonance_curvature_gain_sim.py`.

Then there exist explicit constants \(c_0>0\), \(k_0\in\mathbb{N}\), and an admissible
open region
\[
\mathcal U \subset \{(\xi,\eta,k): k\ge k_0,\ \chi_k(\xi+\eta)>0\}
\]
such that for every \((\xi,\eta,k)\in\mathcal U\),
\[
|r_k(\xi,\eta)| \ge c_0.
\]

Equivalently, on the retained admissible DDYO class there exists a witness with
strictly positive transverse exact symbol curvature:
\[
\lambda_{\mathrm{search}}
=
\sup_{(\xi,\eta,k)\in\mathcal U} |r_k(\xi,\eta)|
>0.
\]

## Repository-native closure consequence

If this lemma is proved and instantiated in the simulator, then the frontier
`terminal_high_high_resonance_curvature_gain` closes at theorem level by replacing the
current zero witness
\[
\lambda_{\mathrm{search}}=0
\]
with a certified positive lower bound.

## Current blocking status

The repository currently records the exact missing input literal
`Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain`.

The repository currently records:
\[
\texttt{status}=\mathrm{OPEN},\qquad
\texttt{missing\_input}=\texttt{Exact Symbol Curvature Lemma for terminal\_high\_high\_resonance\_curvature\_gain}.
\]

## Finish condition

Replace this OPEN statement by a proved exact lower-bound theorem with explicit
hypotheses and constants sufficient to force
\[
\lambda_{\mathrm{search}} > 0
\]
in the retained admissible class.

