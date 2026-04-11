# Completion Truth Test

## Purpose

This test is a completion verifier, not a consistency-only verifier.

## Exit semantics

- `COMPLETION_TRUTH_TEST: PASS`
  means the repository satisfies the declared completion specification.

- `COMPLETION_TRUTH_TEST: FAIL`
  means at least one completion requirement is missing or at least one open-frontier marker remains.

## Interpretation rule

A FAIL is a correct outcome whenever the repository is still formally open.

## Minimal usage

```zsh
./artifacts/audit/run_completion_truth_test.sh SPEC_JSON OUT_MD
Required structure for a true PASS
theorem-level proof files exist;
completion declaration exists;
required completion markers are present;
forbidden open-frontier markers are absent;
no mixed open/complete state exists.
