# Mellin Sobolev Embedding

## Conditional Input

Let
F(t)=M_f\!\left(\tfrac12+it\right)

with
supp(F) ⊂ [-B,B].

Assume Bernstein bounds:
\[
\| t^n F(t)\|_{L^2} \le B^n \|F\|_{L^2}.
\]

## Sobolev Control

For any k ≥ 1:
\[
\|F\|_{H^k(\mathbb R)} \le C_k(B)\|F\|_{L^2}.
\]

## Embedding

By Sobolev embedding on bounded interval:
\[
\sup_{t\in[-B,B]} |F(t)| \le C(B)\|F\|_{L^2}.
\]

## Analytic Extension

Define
F(s)=M_f(s).

Using derivative control:
\[
|\partial_s^n F(s)| \le C(B)^n n! \|F\|_{L^2}.
\]

## Consequence

F extends holomorphically to strip
|\Re s - 1/2| < σ(B)

with exponential type bound:
\[
|F(s)| \le C(B) e^{B|\Im s|}.
\]

## Role

Provides upper-line bound required for three-lines inequality.
