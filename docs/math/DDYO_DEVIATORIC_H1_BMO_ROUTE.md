# DDYO Deviatoric H1-BMO Route

## Weakest sufficient remaining lemma

For all dyadic indices with \(|j-k|\le C\),
\[
\left|
\int G_j\cdot
\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}.
\]

Equivalently, it is sufficient to prove the shell-product Hardy estimate
\[
\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1},
\qquad |j-k|\le C,
\]
so that \(H^1\)-BMO duality yields the desired pairing bound.

## Symbol layer

For radial shell kernel and traceless shell multiplier,
\[
e^{(j)}_{ab}(\xi)
=
\chi_j(\xi)\left(\frac{\xi_a\xi_b}{|\xi|^2}-\frac{\delta_{ab}}{3}\right),
\qquad
e^{(j)}_{aa}(\xi)=0.
\]

## Sampled proxy criterion

A deterministic proxy for the missing lemma is:

1. \(e^{(j)}_{ab}(D)\) preserves shell support.
2. The shell product \(G_j\cdot e^{(j)}_{ab}(D)\omega_k\) has zero mean.
3. The shell product has negligible low-frequency mass.

These checks do not prove the lemma, but they test the geometric orthogonality route that would underwrite the \(H^1\)-BMO closure.

## Status

This document records the current frontier route only.
It does not claim theorem-level closure.
