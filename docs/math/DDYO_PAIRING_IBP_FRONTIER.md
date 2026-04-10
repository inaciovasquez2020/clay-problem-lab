# DDYO Pairing IBP Frontier

## Current formal state

At the current reduction layer, the commutator pairing is not yet resolved by an explicit integration-by-parts identity that isolates the symmetric part of \(\nabla S_k\).

Thus the weakest sufficient next ingredient is to replace the monolithic pairing
\[
\int \mathcal H'_\tau(\omega_j)\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
\]
by an explicit paired decomposition.

## Frozen entropy derivative

\[
\mathcal H_\tau(z)=\sqrt{|z|^2+\tau^2},
\qquad
\mathcal H'_\tau(z)=\frac{z}{\sqrt{|z|^2+\tau^2}}.
\]

## Terminal paired expansion target

Prove that for \(|j-k|\le C\),
\[
\int \mathcal H'_\tau(\omega_j)\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
=
\mathsf I_{j,k}^{\mathrm{sym}}
+
\mathsf R_{j,k},
\]
where
\[
\mathsf I_{j,k}^{\mathrm{sym}}
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

## Weakest sufficient IBP form

It is sufficient to prove an identity of the form
\[
\int \mathcal H'_\tau(\omega_j)\cdot S_k\!\cdot\nabla(\widetilde P_j\omega_k)\,dx
=
-\int (\nabla \mathcal H'_\tau(\omega_j)) : (S_k\otimes \widetilde P_j\omega_k)\,dx
-\int \mathcal H'_\tau(\omega_j)\cdot ((\nabla\cdot S_k)\widetilde P_j\omega_k)\,dx,
\]
and then show that the antisymmetric contribution cancels in the full paired commutator, leaving only the symmetric-gradient contribution plus lower-order remainder.

## Good-unknown branch

If direct IBP is insufficient, the admissible replacement is to define
\[
G_j:=\mathcal H'_\tau(\omega_j),
\]
and prove the commutator pairing identity in the good-unknown form
\[
\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
=
\int \widetilde\Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx
+
\widetilde R_{j,k},
\]
with
\[
|\widetilde R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}.
\]

## Consequence

Any such paired decomposition closes the pairing-level second-gain lemma and completes the DDYO continuum high-high absorbability step.
