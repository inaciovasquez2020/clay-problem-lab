# DDYO Terminal Frontier Core

## Status

Open.

## Source

Machine-generated from `artifacts/audit/ddyo_open_truth_report.md`.

## Priority terminal markers

- `docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md:464`: Open.
- `docs/math/DDYO_RA1N_PROOF.md:6`: No theorem-level proof is currently present in this repository.
- `docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:36`: Open.
- `docs/math/DDYO_RA1N_OPEN_PROBLEM.md:22`: Open.
- `docs/math/DDYO_RA1N_OPEN_PROBLEM.md:23`: No theorem-level proof is currently present in this repository.
- `docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:18`: Open.
- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:24`: Open.
- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:25`: No theorem-level proof is currently present in this repository.
- `docs/math/DDYO_TERMINAL_OBSTRUCTION.md:39`: Open.
- `docs/math/DDYO_SOLVE_REQUIREMENTS.md:62`: Formally open at the shell-product moment frontier.
- `docs/math/DDYO_RA1N_TARGET_THEOREM.md:22`: Open.
- `docs/math/DDYO_RA1N_TARGET_THEOREM.md:23`: No theorem-level proof is currently present in this repository.
- `docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:110`: Open.
- `docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:17`: Open.

## Residual open markers

- `docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:23`: Open.
- `docs/math/DDYO_MASSIVE_REDUCTION.md:6`: \textbf{DDYO frontier status: Open.}
- `docs/math/DDYO_MASSIVE_REDUCTION.md:177`: \textbf{Open.}
- `docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:6`: \textbf{Open.}
- `docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:67`: Open.
- `docs/math/DDYO_CANONICAL_FRONTIER.md:36`: Open.

## Cardinalities

- priority_markers: 14
- residual_markers: 6
- total_markers: 20


## Current weakest sufficient finalized test

The currently recorded weakest sufficient finalized test for the remaining
gradient obstruction is FsT:

\[
\mathrm{FsT}:=\left\{\,G_j(x)=2^{2j}\Gamma(2^j x)\ \text{for some }\Gamma,\quad
\nabla\!\bigl(x_\ell\Gamma\bigr)\in L^\infty(\mathbb R^3)\,\right\}.
\]

This yields
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
\]
so FsT removes the remaining RA1n gradient obstruction.

Reference:
`docs/math/DDYO_FST_FINALIZED_TEST.md`

Status: Conditional.

