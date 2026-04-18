# DDYO Canonical Source Truth Test
- UTC: 2026-04-18T02:37:16.131717+00:00
- Scope files: 12

## Canonical source set
- `docs/math/DDYO_RA1N_PROOF.md`
- `docs/math/DDYO_RA1N_OPEN_PROBLEM.md`
- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md`
- `docs/math/DDYO_RA1N_TARGET_THEOREM.md`
- `docs/math/DDYO_SOLVE_REQUIREMENTS.md`
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md`
- `docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md`
- `docs/status/DDYO_CHECKPOINT_a641031.md`
- `docs/status/DDYO_COMPLETION_DECLARATION.md`
- `docs/math/DDYO_GJ_EXPLICIT_DEFINITION.md`
- `docs/math/DDYO_GJ_KERNEL_REPRESENTATION.md`
- `docs/math/DDYO_GJ_GRADIENT_PROOF.md`

## Required markers

### explicit incomplete declaration
PASS
- `docs/status/DDYO_COMPLETION_DECLARATION.md:5`: INCOMPLETE.
- `docs/status/DDYO_COMPLETION_DECLARATION.md:15`: - No unconditional closure is declared in this repository.

### explicit theorem missing marker
FAIL
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:39`: - RA1n open; proof sketch only in DDYO_RA1N_MOMENT_BOUND_PROOF.md

### open frontier markers present
FAIL
NONE

## Forbidden markers

### false completion declaration
PASS
NONE

### false theorem-complete marker
PASS
NONE

## Mixed-state contradictions

### simultaneous incomplete and complete markers in canonical source scope
PASS
NONE

## Verdict

CANONICAL_SOURCE_TRUTH_TEST: FAIL
