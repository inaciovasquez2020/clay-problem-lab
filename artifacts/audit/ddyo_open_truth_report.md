# DDYO Open Frontier Truth Test

- UTC: 2026-04-11T13:04:21.335656+00:00
- Spec: `artifacts/audit/ddyo_open_truth_spec.json`
- Scope files: 60


## Required files

PASS

## Required commands

### `./artifacts/audit/ddyo_status_consistency_2026_04_11.sh`
- rc: 0

```text
DDYO_STATUS_CONSISTENCY: PASS

EXPECTED_OPEN_FRONTIER_MARKERS:
docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:25:No theorem-level proof is currently present in this repository.
docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
docs/math/DDYO_RA1N_PROOF.md:6:No theorem-level proof is currently present in this repository.
docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:5:- Formally open at the shell-product moment frontier
docs/math/DDYO_RA1N_OPEN_PROBLEM.md:23:No theorem-level proof is currently present in this repository.
docs/math/DDYO_RA1N_TARGET_THEOREM.md:23:No theorem-level proof is currently present in this repository.
docs/status/DDYO_CHECKPOINT_a641031.md:5:- Formally open at the shell-product moment frontier
docs/math/DDYO_SOLVE_REQUIREMENTS.md:62:Formally open at the shell-product moment frontier.

```
### `python3 -m pytest -q`
- rc: 0

```text
...............................................................          [100%]
63 passed in 24.95s

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
- `docs/math/DDYO_MASSIVE_REDUCTION.md:6`: \textbf{DDYO frontier status: Open.}
- `docs/math/DDYO_MASSIVE_REDUCTION.md:177`: \textbf{Open.}
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
- `docs/math/DDYO_CANONICAL_FRONTIER.md:36`: Open.
- `docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:17`: Open.
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38`: - Formally conditional on RA1n
- `docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:5`: - Formally open at the shell-product moment frontier

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
