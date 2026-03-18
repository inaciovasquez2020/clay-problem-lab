# Epsilon Decay Derivation

## Input

From contour shift:
|f(x)| ≤ C x^{-(1/2+\eta)}

Weight:
w(x) = e^{-x}

## Tail Bound

For L large:

∫_L^∞ |f(x)|^2 w(x) dx
≤
C^2 ∫_L^∞ x^{-1-2\eta} e^{-x} dx

## Estimate

Using monotonicity:

∫_L^∞ x^{-1-2\eta} e^{-x} dx
≤
L^{-1-2\eta} ∫_L^∞ e^{-x} dx
=
L^{-1-2\eta} e^{-L}

## Result

∫_Tail |f|^2 w
≤
C^2 e^{-L} L^{-1-2\eta}

## Core Lower Bound

∫_Core |f|^2 w ≥ c(B) > 0

## Epsilon

ε_B(L) = O(e^{-L} L^{-1-2\eta})

## Limit

ε_B(L) → 0 exponentially
