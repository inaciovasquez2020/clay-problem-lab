# Pipeline Scope Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository provides a reproducible computational pipeline for exploration and verification.

It does not by itself certify that computational evidence transfers to theorem-level closure for any Clay problem.

## Weakest structural extension
Let
\[
\mathcal H
\]
denote the set of harness-certified computational outputs and
\[
\mathcal T
\]
the set of broader mathematical claims.

The minimal non-overreach condition is:
\[
c\in\mathcal T\setminus\mathcal H
\Longrightarrow
c\text{ must not be presented as certified by this repository.}
\]

## Minimal next artifact
The weakest next artifact is an executable documentation audit emitting:
1. prose upgrading experiment outputs into theorem claims;
2. completeness claims not backed by repository artifacts;
3. release notes silently strengthening certified scope;
4. claims omitting declared repository limits.

## Label
This note is CONDITIONAL.
It preserves the repository's experimental-framework scope.
