# DDYO Paired Decomposition Lemma

## Terminal paired lemma

For \(|j-k|\le C\), prove
\[
\int \mathcal H'_\tau(\omega_j)\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
=
\mathsf I^{\mathrm{sym}}_{j,k}+\mathsf R_{j,k},
\]
where
\[
\mathsf I^{\mathrm{sym}}_{j,k}
=
\int \Gamma_{j,k}(x):\operatorname{Sym}\nabla S_k(x)\,dx,
\]
and
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\]
up to summable lower-order terms.

## Frozen entropy derivative

\[
\mathcal H_\tau(z)=\sqrt{|z|^2+\tau^2},
\qquad
\mathcal H'_\tau(z)=\frac{z}{\sqrt{|z|^2+\tau^2}}.
\]

## Weakest sufficient structural identity

It is sufficient to prove
\[
\int \mathcal H'_\tau(\omega_j)\cdot S_k\!\cdot\nabla(\widetilde P_j\omega_k)\,dx
=
-\int \nabla \mathcal H'_\tau(\omega_j):(S_k\otimes \widetilde P_j\omega_k)\,dx
-\int (\nabla\cdot S_k)\,\mathcal H'_\tau(\omega_j)\cdot \widetilde P_j\omega_k\,dx,
\]
and to combine this with the corresponding expansion of
\[
\int \mathcal H'_\tau(\omega_j)\cdot \widetilde P_j(S_k\!\cdot\nabla\omega_k)\,dx
\]
so that antisymmetric contributions cancel and only the symmetric-gradient term remains at top order.

## Good-unknown equivalent form

Equivalently, with
\[
G_j:=\mathcal H'_\tau(\omega_j),
\]
it is sufficient to prove
\[
\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
=
\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx
+
\mathsf R_{j,k},
\]
with the same remainder bound above.

## Consequence

This lemma implies the pairing-level second-gain estimate and closes the DDYO continuum high-high absorbability step.
