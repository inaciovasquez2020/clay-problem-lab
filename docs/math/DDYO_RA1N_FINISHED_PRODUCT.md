# DDYO / RA1n Finished Product

## Theorem 1 (Intrinsic annular gradient-moment estimate)

Let
\[
\widehat{G_j}(\xi)=\frac{\varphi(2^{-j}\xi)}{|\xi|^4},
\qquad
\varphi\in C_c^\infty(\mathbb R^3),
\qquad
\operatorname{supp}\varphi\subset\left\{\tfrac12\le |\xi|\le 2\right\}.
\]
Then for each \(\ell\in\{1,2,3\}\),
\[
\|\nabla(x_\ell G_j)\|_{L^\infty(\mathbb R^3)}\le C\,2^{-j}.
\]

### Proof
Set
\[
\widetilde G:=\mathcal F^{-1}\!\left(\frac{\varphi(\eta)}{|\eta|^4}\right).
\]
Since \(\varphi(\eta)/|\eta|^4\) is smooth and compactly supported away from \(0\), \(\widetilde G\in\mathcal S(\mathbb R^3)\).

By the change of variables \(\xi=2^j\eta\),
\[
G_j(x)
=
\int_{\mathbb R^3}\frac{\varphi(2^{-j}\xi)}{|\xi|^4}e^{ix\cdot \xi}\,d\xi
=
2^{-j}\widetilde G(2^j x).
\]
Hence
\[
|G_j(x)|\le 2^{-j}\|\widetilde G\|_{L^\infty}.
\]

Also,
\[
\nabla G_j(x)=2^{-j}\cdot 2^j(\nabla \widetilde G)(2^j x)
=
(\nabla \widetilde G)(2^j x).
\]
Therefore, with \(y=2^j x\),
\[
|x_\ell \nabla G_j(x)|
=
2^{-j}|y_\ell|\,|(\nabla \widetilde G)(y)|
\le
2^{-j}\|y_\ell \nabla \widetilde G(y)\|_{L^\infty_y}.
\]
Since \(y_\ell\nabla \widetilde G(y)\in\mathcal S(\mathbb R^3)\), the right-hand side is \(O(2^{-j})\).

Using
\[
\nabla(x_\ell G_j)=e_\ell G_j+x_\ell \nabla G_j,
\]
we obtain
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}
\le
\|G_j\|_{L^\infty}
+
\|x_\ell\nabla G_j\|_{L^\infty}
\le
C2^{-j}.
\qquad\blacksquare
\]

---

## Proposition 2 (Exact remaining obstruction)

Let \(r_k(\xi)\) denote the exact DDYO / RA1n remainder symbol appearing in the repository source of truth.

If
\[
\forall \alpha\in\mathbb N^3,\qquad
\sup_{k\ge 0}\sup_{|\xi|\sim 2^k}
2^{k(1+|\alpha|)}
\bigl|\partial_\xi^\alpha r_k(\xi)\bigr|
<\infty,
\]
then the prior conditional RA1n closure becomes unconditional.

### Proof
This is exactly the missing hypothesis previously isolated for closure. Once it is derived from the exact repository formula for \(r_k\), the shell-product moment frontier closes. \(\blacksquare\)

---

## Corollary 3 (What is proved here)

The intrinsic annular bi-Laplacian scaling proves the full gradient-moment estimate
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\lesssim 2^{-j}
\]
with no external symbol assumptions.

---

## Open Item

Unconditional closure is reduced to one exact formula-level task:

\[
\forall \alpha\in\mathbb N^3,\qquad
\sup_{k\ge 0}\sup_{|\xi|\sim 2^k}
2^{k(1+|\alpha|)}
\bigl|\partial_\xi^\alpha r_k(\xi)\bigr|
<\infty
\]
for the actual repository remainder \(r_k\).

The unsupported replacement
\[
r_k=\widehat G_k-P_k\widehat G_k
\]
is not used here.

The unsupported annular “volume absorption” step is not used here.

Status: Conditional at the exact \(r_k\)-symbol stage.
