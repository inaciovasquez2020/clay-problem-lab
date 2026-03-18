# Core Uniform Lower Bound

## Empirical Law

Let
C(L) = ∫_{Core(L)} |f(x)|^2 w(x) dx

Observed:
C(L) → 1 as L → ∞

## Structural Statement

∃ c(B) > 0 such that:
∫_{Core(L)} |f(x)|^2 w(x) dx ≥ c(B)

for all admissible normalized f.

## Minimal Requirement

c(B) independent of L.

## Consequence

Total mass satisfies:
||f||^2 ≤ (1 + ε_B(L)) ∫_{Core(L)} |f|^2 w

⇒ stable normalization.

## Integration with Tail Domination

Tail/Core → 0
and Core ≥ c(B)

⇒ tail mass ≤ ε_B(L) c(B)

## Closure Chain

Core bound + tail decay ⇒ uniform coercivity.

## Status

Conditional on admissible class regularity.
