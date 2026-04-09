# Module Adapter Completeness Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository runs experiments across multiple problem modules.

It does not by itself assert that every declared experiment adapter is total on every declared supported input family.

## Weakest structural extension
Let
\[
\mathcal P
\]
be the declared module set and
\[
\mathcal I_P
\]
the declared supported input family for
\[
P\in\mathcal P.
\]

For each
\[
P\in\mathcal P
\]
and
\[
I\in\mathcal I_P,
\]
let
\[
\operatorname{Run}_P(I)\in\{\mathrm{ok},\mathrm{timeout},\mathrm{error},\mathrm{unsupported}\}.
\]

The minimal completeness condition is:
\[
\forall P\in\mathcal P,\ \forall I\in\mathcal I_P,\quad
\operatorname{Run}_P(I)
\]
is defined and classified.

## Minimal next artifact
The weakest next artifact is an executable adapter audit emitting:
1. undeclared module-input outcomes;
2. unsupported cases lacking explicit classification;
3. crashes without structured status;
4. summary reports built from partial adapter coverage.

## Label
This note is CONDITIONAL.
It preserves the repository's experimental-framework scope.
