# Cross-Module Comparability Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository unifies multiple Clay-problem modules under a common framework.

It does not yet state the exact admissibility condition under which cross-module dashboards or aggregate comparisons are canonical.

## Weakest structural extension
Let
\[
P_1,P_2\in\mathcal P
\]
be declared modules and let
\[
M(P)
\]
denote the module-specific measurement schema used in summaries.

The minimal comparability condition is:
\[
\operatorname{Compare}(P_1,P_2)\text{ is canonical}
\Longrightarrow
M(P_1)\text{ and }M(P_2)\text{ are explicitly normalized into a declared common comparison schema.}
\]

## Minimal next artifact
The weakest next artifact is an executable comparability audit emitting:
1. dashboards comparing incomparable module metrics;
2. aggregate summaries lacking a declared normalization schema;
3. cross-module plots mixing heterogeneous scales without annotation;
4. canonical labels applied to non-normalized cross-module comparisons.

## Label
This note is CONDITIONAL.
It preserves the repository's unified-framework scope.
