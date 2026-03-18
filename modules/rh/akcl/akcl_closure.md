# AKCL Closure

## Inputs

1. Localized coercivity:
E[f] ≥ c0 ∑_{core} |f|^2 w

2. Tail domination:
∑_{tail} |f|^2 w ≤ ε_B(L) ∑_{core} |f|^2 w

3. Decay:
ε_B(L) → 0 exponentially

## Combine

Total mass:
||f||^2
=
∑_{core} |f|^2 w + ∑_{tail} |f|^2 w
≤
(1 + ε_B(L)) ∑_{core} |f|^2 w

## Substitute

E[f] ≥ c0 ∑_{core} |f|^2 w
≥
c0 / (1 + ε_B(L)) ||f||^2

## Limit

As L → ∞:
ε_B(L) → 0

⇒

E[f] ≥ c0 ||f||^2

## Conclusion

Uniform coercivity holds over admissible class.

## Final Reduction

AKCL ⇒ Euler–Gram positivity ⇒ RH

## Status

Conditional.
