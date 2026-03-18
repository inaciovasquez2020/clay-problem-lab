# Mellin Three-Lines Inequality

## Conditional Statement

Let
F(s) = M_f(s)

assume:
1. F holomorphic in strip
   a ≤ Re(s) ≤ b
2. Boundary L^2 bounds:
   ∫ |F(a+it)|^2 dt ≤ A
   ∫ |F(b+it)|^2 dt ≤ B

## Three-Lines Inequality (L^2 form)

For θ ∈ [0,1], set
σ = (1-θ)a + θ b.

Then:
\[
\int_{\mathbb R} |F(\sigma+it)|^2 dt
\le
A^{1-\theta} B^{\theta}.
\]

## Application

Take:
a = 1/2
b = 1/2 + σ₀

Assume boundary control at both lines.

## Target

Extend control from Re(s)=1/2 to Re(s)=1/2+σ.

## Required Input

Upper boundary estimate:
∫ |F(1/2+σ₀+it)|^2 dt ≤ C(B)

## Consequence

Interpolation yields:
∫ |F(1/2+σ+it)|^2 dt ≤ C(B)

## Role

Provides Hardy-strip control from two boundary lines.

## Status

Conditional on upper-line bound.
