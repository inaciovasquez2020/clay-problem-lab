# DR33D Step 25 — Exact Monotone-Cutoff Frontier Lemma

## Frontier statement

Let \(0<\theta<1\). Determine whether there exists \(C=C(\theta,j_0)<\infty\) such that for every nonnegative sequence \((E_j)_{j\in\mathbb Z}\) satisfying
\[
E_{j+1}\le E_j\qquad\text{for all }j,
\qquad
E_j=0\qquad\text{for all }j<j_0,
\]
one has
\[
\boxed{
\left(\sum_{j\in\mathbb Z}2^{-j}E_j^{1/2}\right)^2
\le
C\sum_{j\in\mathbb Z}E_j^{1+\theta}.
}
\]

## Equivalent invariant form

With
\[
\mathfrak I(E):=\left(\sum_{j\in\mathbb Z}2^{-j}E_j^{1/2}\right)^2,
\]
the frontier asks whether
\[
\mathfrak I(E)\le C\|E\|_{\ell^{1+\theta}}^{\,1+\theta}
\]
holds under monotonicity plus lower-shell cutoff.

## Logical role

Step 24 shows unrestricted Step 23 is false on arbitrary nonnegative
\(\ell^{1+\theta}\) sequences.

Therefore this monotone-cutoff form is the exact surviving frontier after the unrestricted impossibility result.

## Status

OPEN FRONTIER LEMMA — unrestricted form is false; monotone-cutoff form remains unresolved.
