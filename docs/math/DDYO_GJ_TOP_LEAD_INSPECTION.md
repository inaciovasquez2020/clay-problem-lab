# DDYO G_j Top Lead Inspection

## Status

Closed at the annular first-moment remainder stage.

## Top lead file

`docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md`

## Leading file head

```text
# Branch B missing math and test

## Sole remaining master key
For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
\]
and
\[
\left|
\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

## Equivalent shell-product \(H^1\) gain
For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
\[
\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

## Equivalent deviatoric coercivity bound
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

## Equivalent absorbability form
For every \(\varepsilon\in(0,1)\),
\[
\left|
\int G_j\cdot
\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
\right|
\le
\varepsilon\,\mathcal D_{j,k}[u]
+
C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.
\]

## Claim 5 / Branch B remainder target
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\qquad |j-k|\le C.
\]

## Pairing IBP frontier
It is sufficient to prove an identity of the form
\[
\int \mathcal H'_\tau(\omega_j)\cdot S_k\!\cdot\nabla(\widetilde P_j\omega_k)\,dx
=
-\int (\nabla \mathcal H'_\tau(\omega_j)) : (S_k\otimes \widetilde P_j\omega_k)\,dx
-\int \mathcal H'_\tau(\omega_j)\cdot ((\nabla\cdot S_k)\widetilde P_j\omega_k)\,dx,
\]
and then show that the antisymmetric contribution cancels in the full paired commutator, leaving only the symmetric-gradient contribution plus lower-order remainder.

## Previously surfaced machine-missing checks
- derivative_commutator_bound
- stress_transport_potential
- s2_defect_budget
- f2_flux_budget
- a2_term
- t_term
- b2_term

## Truthful frontier
- continuum DDYO high-high absorbability: OPEN; conditional on RA1n
- full continuum solve / global regularity closure: open
```

## `G_j` matches

```text
3-## Sole remaining master key
4-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
5-\[
6:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
7-\]
8-and
9-\[
10-\left|
11:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
12-\right|
13-\le
14-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
--
17-## Equivalent shell-product \(H^1\) gain
18-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
19-\[
20:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
21-\le
22-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
23-\]
--
26-For all dyadic indices with \(|j-k|\le C\),
27-\[
28-\left|
29:\int G_j\cdot
30-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
31-\right|
32-\le
--
39-For every \(\varepsilon\in(0,1)\),
40-\[
41-\left|
42:\int G_j\cdot
43-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
44-\right|
45-\le
```

## `Gamma` / kernel matches

```text
NO_GAMMA_KERNEL_MATCHES
```

## dyadic / RA1n matches

```text
11-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
12-\right|
13-\le
14:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
15-\]
16-
17-## Equivalent shell-product \(H^1\) gain
--
19-\[
20-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
21-\le
22:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
23-\]
24-
25-## Equivalent deviatoric coercivity bound
--
30-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
31-\right|
32-\le
33:C\,2^{-j}2^{-k}\,
34-\|\nabla S_k\|_{L^\infty}\,
35-\|\omega_k\|_{L^1}.
36-\]
--
52-\[
53-|\mathsf R_{j,k}|
54-\le
55:C\,2^{-j}2^{-k}\,
56-\|\nabla S_k\|_{L^\infty}\,
57-\|\omega_k\|_{L^1},
58-\qquad |j-k|\le C.
78-- b2_term
79-
80-## Truthful frontier
81:- continuum DDYO high-high absorbability: OPEN; conditional on RA1n
82-- full continuum solve / global regularity closure: open
```
