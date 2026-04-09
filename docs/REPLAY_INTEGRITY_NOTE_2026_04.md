# Replay Integrity Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository is a unified experimental framework for reproducible computational exploration of the Clay Millennium Problems.
It contains:
1. modular experiment runners;
2. tests and scripts;
3. dashboard and framework infrastructure;
4. domain modules for RH, Navier–Stokes, Yang–Mills, P vs NP, BSD, and Hodge.

It does not by itself assert:
1. theorem-level resolution of any Clay problem;
2. theoretical completeness of the experimental search space;
3. validity beyond declared experiments, data, scripts, and tests.

## Weakest structural extension
Let
\[
P
\]
be a declared problem module,
\[
I
\]
a declared experiment input,
\[
E
\]
the pinned environment state,
and
\[
R(P,I,E)
\]
the recorded experiment outcome.

The minimal replay-integrity condition is:
\[
\forall P,I,E,\quad
R(P,I,E)
\]
is deterministically reproduced by rerunning the repository harness with the same
\[
(P,I,E).
\]

## Minimal next artifact
The weakest next artifact is an executable replay audit emitting:
1. experiment outcomes lacking replay metadata;
2. environment drifts changing recorded outcomes;
3. scripts whose summaries are not reconstructible from declared inputs;
4. cross-module runs whose aggregate result is not hash-stable.

## Label
This note is CONDITIONAL.
It preserves the repository's experimental-framework scope.
