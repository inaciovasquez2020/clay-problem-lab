# DDYO Open Frontier Truth Test

- UTC: 2026-04-11T13:20:15.531325+00:00
- Spec: `artifacts/audit/ddyo_source_truth_spec.json`
- Scope files: 66


## Required files

PASS

## Required commands

### `./artifacts/audit/ddyo_status_consistency_2026_04_11.sh`
- rc: 0

```text
DDYO_STATUS_CONSISTENCY: PASS

EXPECTED_OPEN_FRONTIER_MARKERS:
docs/status/DDYO_CHECKPOINT_a641031.md:5:- Formally open at the shell-product moment frontier
docs/status/DDYO_FRONTIER_REGISTRY.md:13:- `docs/math/DDYO_RA1N_PROOF.md:6`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_FRONTIER_REGISTRY.md:18:- `docs/math/DDYO_RA1N_OPEN_PROBLEM.md:23`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_FRONTIER_REGISTRY.md:21:- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:25`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_FRONTIER_REGISTRY.md:25:- `docs/math/DDYO_SOLVE_REQUIREMENTS.md:62`: Formally open at the shell-product moment frontier.
docs/status/DDYO_FRONTIER_REGISTRY.md:27:- `docs/math/DDYO_RA1N_TARGET_THEOREM.md:23`: No theorem-level proof is currently present in this repository.
docs/math/DDYO_GJ_CONTEXT_EXTRACT_CLEAN.md:2716:./docs/math/DDYO_RA1N_PROOF.md-6-No theorem-level proof is currently present in this repository.
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:2375:./artifacts/branch_b/branch_b_open_hits.log-24-docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:3870:./artifacts/branch_b/branch_b_open_hits.log-15-docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:34:- Formally open at the shell-product moment frontier
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:3879:./artifacts/branch_b/branch_b_open_hits.log-24-docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:4140:./docs/math/DDYO_RA1N_PROOF.md-6-No theorem-level proof is currently present in this repository.
docs/status/DDYO_SOURCE_FRONTIER.md:17:- `docs/math/DDYO_RA1N_PROOF.md:6`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_SOURCE_FRONTIER.md:20:- `docs/math/DDYO_RA1N_OPEN_PROBLEM.md:23`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_SOURCE_FRONTIER.md:22:- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:25`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_SOURCE_FRONTIER.md:24:- `docs/math/DDYO_RA1N_TARGET_THEOREM.md:23`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_SOURCE_FRONTIER.md:25:- `docs/math/DDYO_SOLVE_REQUIREMENTS.md:62`: Formally open at the shell-product moment frontier.
docs/status/DDYO_SOURCE_FRONTIER.md:26:- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38`: - Formally conditional on RA1n
docs/status/DDYO_SOURCE_FRONTIER.md:28:- `docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:5`: - Formally open at the shell-product moment frontier
docs/status/DDYO_SOURCE_FRONTIER.md:29:- `docs/status/DDYO_CHECKPOINT_a641031.md:5`: - Formally open at the shell-product moment frontier
docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
docs/math/DDYO_RA1N_OPEN_PROBLEM.md:23:No theorem-level proof is currently present in this repository.
docs/math/DDYO_RA1N_PROOF.md:6:No theorem-level proof is currently present in this repository.
docs/status/DDYO_TERMINAL_FRONTIER_CORE.md:14:- `docs/math/DDYO_RA1N_PROOF.md:6`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_TERMINAL_FRONTIER_CORE.md:17:- `docs/math/DDYO_RA1N_OPEN_PROBLEM.md:23`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_TERMINAL_FRONTIER_CORE.md:20:- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:25`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_TERMINAL_FRONTIER_CORE.md:22:- `docs/math/DDYO_SOLVE_REQUIREMENTS.md:62`: Formally open at the shell-product moment frontier.
docs/status/DDYO_TERMINAL_FRONTIER_CORE.md:24:- `docs/math/DDYO_RA1N_TARGET_THEOREM.md:23`: No theorem-level proof is currently present in this repository.
docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:5:- Formally open at the shell-product moment frontier
docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:25:No theorem-level proof is currently present in this repository.
docs/math/DDYO_RA1N_TARGET_THEOREM.md:23:No theorem-level proof is currently present in this repository.
docs/math/DDYO_SOLVE_REQUIREMENTS.md:62:Formally open at the shell-product moment frontier.

```
### `python3 -m pytest -q`
- rc: 0

```text
...............................................................          [100%]
63 passed in 26.10s

```

## Required markers

### explicit incomplete declaration
PASS
- `docs/status/DDYO_COMPLETION_DECLARATION.md:5`: INCOMPLETE.
- `docs/status/DDYO_COMPLETION_DECLARATION.md:15`: - No unconditional closure is declared in this repository.
### explicit theorem missing marker
PASS
- `docs/math/DDYO_RA1N_PROOF.md:6`: No theorem-level proof is currently present in this repository.
- `docs/math/DDYO_RA1N_PROOF.md:21`: The existing Bernstein-extraction file is a proof sketch only and does not establish the missing \(2^{-k}\) gain at theorem level.
### open frontier markers present
PASS
- `docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md:464`: Open.
- `docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:23`: Open.
- `docs/math/DDYO_RA1N_PROOF.md:6`: No theorem-level proof is currently present in this repository.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:227`: ./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-17-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:392`: ./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-110-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:520`: ./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-23-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:1133`: ./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-39-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:1150`: ./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-18-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:1975`: ./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-18-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:2375`: ./artifacts/branch_b/branch_b_open_hits.log-24-docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:3870`: ./artifacts/branch_b/branch_b_open_hits.log-15-docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:34:- Formally open at the shell-product moment frontier
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:3879`: ./artifacts/branch_b/branch_b_open_hits.log-24-docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:4140`: ./docs/math/DDYO_RA1N_PROOF.md-6-No theorem-level proof is currently present in this repository.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:5152`: ./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-18-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:5188`: ./docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md-464-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:5205`: ./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-36-Open.
- `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:5221`: Open.
- `docs/math/DDYO_MASSIVE_REDUCTION.md:6`: \textbf{DDYO frontier status: Open.}
- `docs/math/DDYO_MASSIVE_REDUCTION.md:177`: \textbf{Open.}
- `docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:36`: Open.

## Forbidden markers

### false completion declaration
PASS
### false theorem-complete marker
PASS

## Mixed-state contradictions

### simultaneous incomplete and complete markers in DDYO frontier scope
PASS

## Verdict

COMPLETION_TRUTH_TEST: PASS
