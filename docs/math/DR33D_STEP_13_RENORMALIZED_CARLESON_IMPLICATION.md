# DR33D Step 13 — Renormalized Carleson Implication

## Objective
Formulate Carleson control at the renormalized profile level.

## Renormalized profile
For \(\alpha>0\), define
\[
F_j(t):=2^{-\alpha j}E_j(t).
\]

## Renormalized Carleson quantity
Define
\[
\mathfrak C_T^{(\alpha)}(F)
:=
\sup_{I\subset[0,T]}
\frac{1}{|I|}
\sum_j 2^{-j+\alpha j}F_j(t)
\text{ integrated over }I.
\]

## Equivalent form
\[
\mathfrak C_T^{(\alpha)}(F)
=
\sup_{I\subset[0,T]}
\frac{1}{|I|}
\sum_j \int_I 2^{-j}E_j(t)\,dt.
\]

## Target implication
Seek \(\alpha>0,\ \theta\in(0,1)\), \(C>0\) such that
\[
\mathfrak C_T^{(\alpha)}(F)\le C_T
\Longrightarrow
\int_0^T
\left(\sum_j 2^{-j+\alpha j/2}F_j(t)^{1/2}\right)^2 dt
\le
C\int_0^T\sum_j F_j(t)^{1+\theta}dt.
\]

## Status
OPEN — renormalized Carleson bridge not yet established.
