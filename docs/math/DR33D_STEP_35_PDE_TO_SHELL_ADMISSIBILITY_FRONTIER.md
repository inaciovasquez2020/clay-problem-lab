# DR33D Step 35 — PDE-to-Shell Admissibility Frontier

## Status
Conditional.

## Shell map

Let \(u\) be an admissible PDE state and let
\[
E_j(u)\ge 0
\]
denote its shell-energy profile.

Define
\[
A(E(u)):=\sum_{j\in\mathbb Z}2^{-j}E_j(u)^{1/2},
\qquad
S(E(u)):=\sum_{j\in\mathbb Z}E_j(u)^{1+\theta},
\qquad
\mathfrak C(E(u)):=\frac{\sup_j E_j(u)^{1+\theta}}{S(E(u))}.
\]

Assume the shell support normalization
\[
E_j(u)=0\qquad (j<j_0).
\]

## Target PDE-to-shell theorem

The surviving linear frontier is reduced to the following implication:

\[
\boxed{
\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}
}
\]
for some parameters
\[
\delta\in(0,1),\qquad m>0,
\]
where
\[
\mathcal A_{\delta,m}
:=
\left\{
E:\ 
E_j\ge 0,\ 
E_j=0\ (j<j_0),\
E_{j+1}\le E_j,\
\mathfrak C(E)\le 1-\delta,\
S(E)\ge m
\right\}.
\]

Equivalently, it is enough to prove

\[
\boxed{
\mathcal P(u)\Longrightarrow
\Bigl(
E_{j+1}(u)\le E_j(u),\ 
\mathfrak C(E(u))\le 1-\delta,\
S(E(u))\ge m
\Bigr).
}
\]

## Consequence of Step 34

By the locked Step 34 frontier object, if
\[
E(u)\in\mathcal A_{\delta,m},
\]
then
\[
A(E(u))^2\le C(\theta,j_0,\delta,m)\,S(E(u)).
\]

Therefore
\[
\boxed{
\mathcal P(u)\Longrightarrow A(E(u))^2\le C(\theta,j_0,\delta,m)\,S(E(u)).
}
\]

## Weakest remaining PDE object

The weakest remaining PDE-level ingredient is a shell-exclusion mechanism implying both:

1. non-concentration
\[
\mathfrak C(E(u))\le 1-\delta,
\]

2. positive size floor
\[
S(E(u))\ge m>0.
\]

## Canonical frontier sentence

The remaining wall is no longer Hölder reduction or normalization.
It is the derivation of admissibility:
\[
\mathcal P(u)\Longrightarrow E(u)\in\mathcal A_{\delta,m}.
\]

## Lock sentence

Step 35 records the exact PDE-to-shell frontier:
prove one admissibility theorem sending PDE states into the Step 34 class.
