# Universal Tail Domination

## Conditional Input

Assume:
1. f ∈ 𝒜_B
2. |f(x)| ≤ C(B) x^{-δ(B)}, δ(B)=1
3. w(x)=e^{-x}

## Tail Bound

∫_L^∞ |f(x)|^2 w(x) dx
≤
C(B)^2 ∫_L^∞ x^{-2} e^{-x} dx
≤
C(B)^2 e^{-L} L^{-2}

## Core Bound

From core lower bound:
∫_{Core(L)} |f|^2 w ≥ c(B) > 0

## Ratio

ε_B(L)
=
∫_{Tail} / ∫_{Core}
≤
(C(B)^2 / c(B)) e^{-L} L^{-2}

## Result

ε_B(L) → 0 exponentially, uniformly over 𝒜_B.

## Closure

Uniform tail domination holds over admissible class.
