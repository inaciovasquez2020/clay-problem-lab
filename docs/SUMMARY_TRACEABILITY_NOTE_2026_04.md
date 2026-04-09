# Summary Traceability Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository emits aggregate summaries across experiments and modules.

It does not yet state the full summary-to-artifact traceability condition as a repository-level boundary theorem.

## Weakest structural extension
Let
\[
S
\]
be a reported summary item.

The minimal traceability requirement is the existence of a unique quadruple
\[
(P,I,E,A)
\]
such that:
\[
P=\text{problem module},\quad
I=\text{experiment input},\quad
E=\text{pinned environment},\quad
A=\text{replay artifact bundle},
\]
and
\[
S=\operatorname{Summarize}(P,I,E,A).
\]

## Minimal next artifact
The weakest next artifact is an executable traceability audit emitting:
1. summary items lacking concrete \((P,I,E,A)\) witnesses;
2. duplicate summaries mapping to inconsistent witness tuples;
3. replay bundles missing for reported outcomes;
4. summary files not reconstructible from stored artifacts.

## Label
This note is CONDITIONAL.
It preserves the repository's experimental-framework scope.
