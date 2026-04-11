# DDYO G_j Context Extract Clean

## Target

Filtered repository context for the theorem-level target
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]

Generated DDYO artifacts and audit/status outputs are excluded.

## Context windows for `G_j`

```text
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-36-\]
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-37-
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-38-Combined with
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-39-\[
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:40:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-41-\]
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-42-it implies
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-43-\[
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-44-\left|
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:45:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-46-\right|
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-47-\le
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-48-C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-49-\]
--
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-4-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-5-For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-6-\[
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-7-\left|
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:8:\int G_j\cdot
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-9-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-10-\right|
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-11-\le
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-12-C\,2^{-j}2^{-k}\,
--
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-15-\]
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-16-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-17-Equivalently, it is sufficient to prove the shell-product Hardy estimate
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-18-\[
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:19:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-20-\le
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-21-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1},
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-22-\qquad |j-k|\le C,
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-23-\]
--
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-38-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-39-A deterministic proxy for the missing lemma is:
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-40-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-41-1. \(e^{(j)}_{ab}(D)\) preserves shell support.
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:42:2. The shell product \(G_j\cdot e^{(j)}_{ab}(D)\omega_k\) has zero mean.
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-43-3. The shell product has negligible low-frequency mass.
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-44-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-45-These checks do not prove the lemma, but they test the geometric orthogonality route that would underwrite the \(H^1\)-BMO closure.
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-46-
--
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-4-
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-5-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-6-\[
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-7-\left|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:8:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-9-\right|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-10-\le
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-11-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-12-\]
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-13-
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-14-Together with the zeroth-moment identity
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-15-\[
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:16:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-17-\]
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-18-this is sufficient to recover the shell-product \(H^1\) gain and hence
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-19-\[
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-20-\left|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:21:\int G_j\cdot
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-22-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-23-\right|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-24-\le
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-25-C\,2^{-j}2^{-k}\,
--
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-32-
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-33-It is equivalently sufficient to prove that for every \(\varepsilon\in(0,1)\),
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-34-\[
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-35-\left|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:36:\int G_j\cdot
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-37-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-38-\right|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-39-\le
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-40-\varepsilon\,\mathcal D_{j,k}[u]
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-45-\text{annular potential estimate}
./docs/math/DDYO_MASSIVE_REDUCTION.md-46-\bigr)
./docs/math/DDYO_MASSIVE_REDUCTION.md-47-\wedge
./docs/math/DDYO_MASSIVE_REDUCTION.md-48-\bigl(
./docs/math/DDYO_MASSIVE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-50-\bigr).
./docs/math/DDYO_MASSIVE_REDUCTION.md-51-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-52-
./docs/math/DDYO_MASSIVE_REDUCTION.md-53-\[
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-82-
./docs/math/DDYO_MASSIVE_REDUCTION.md-83-The RA1n first-moment estimate reduces to the conjunction
./docs/math/DDYO_MASSIVE_REDUCTION.md-84-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md-85-\left|
./docs/math/DDYO_MASSIVE_REDUCTION.md:86:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_MASSIVE_REDUCTION.md-87-\right|
./docs/math/DDYO_MASSIVE_REDUCTION.md-88-\le
./docs/math/DDYO_MASSIVE_REDUCTION.md-89-C\,2^{-j}2^{-k}\|\omega_k\|_{L^1},
./docs/math/DDYO_MASSIVE_REDUCTION.md-90-\]
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-96-\|H^{ab}_{j,k}\|_{L^1}\le C\,2^{-k}\|\omega_k\|_{L^1},
./docs/math/DDYO_MASSIVE_REDUCTION.md-97-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-98-and
./docs/math/DDYO_MASSIVE_REDUCTION.md-99-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:100:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-101-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-102-
./docs/math/DDYO_MASSIVE_REDUCTION.md-103-### Layer 4: annular potential route
./docs/math/DDYO_MASSIVE_REDUCTION.md-104-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-127-### Layer 6: gradient-bound route
./docs/math/DDYO_MASSIVE_REDUCTION.md-128-
./docs/math/DDYO_MASSIVE_REDUCTION.md-129-The remaining parallel local route is
./docs/math/DDYO_MASSIVE_REDUCTION.md-130-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:131:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-132-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-133-
./docs/math/DDYO_MASSIVE_REDUCTION.md:134:The repository-wide provenance audit has been introduced precisely because theorem-level closure of this bound requires the exact structural construction of \(G_j\).
./docs/math/DDYO_MASSIVE_REDUCTION.md-135-
./docs/math/DDYO_MASSIVE_REDUCTION.md-136-## Massive reduction conclusion
./docs/math/DDYO_MASSIVE_REDUCTION.md-137-
./docs/math/DDYO_MASSIVE_REDUCTION.md-138-All currently recorded DDYO frontier documents collapse to the following single conditional statement:
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-143-Q_m\in \mathcal S(\mathbb R^3)
./docs/math/DDYO_MASSIVE_REDUCTION.md-144-\bigr]
./docs/math/DDYO_MASSIVE_REDUCTION.md-145-\wedge
./docs/math/DDYO_MASSIVE_REDUCTION.md-146-\bigl[
./docs/math/DDYO_MASSIVE_REDUCTION.md:147:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-148-\bigr]
./docs/math/DDYO_MASSIVE_REDUCTION.md-149-\Longrightarrow
./docs/math/DDYO_MASSIVE_REDUCTION.md-150-\text{RA1n}
./docs/math/DDYO_MASSIVE_REDUCTION.md-151-\Longrightarrow
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-165-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-166-and
./docs/math/DDYO_MASSIVE_REDUCTION.md-167-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md-168-\text{(B)}\quad
./docs/math/DDYO_MASSIVE_REDUCTION.md:169:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-170-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-171-
./docs/math/DDYO_MASSIVE_REDUCTION.md-172-If item (A) is already accepted by the annular-cutoff argument, then the sole remaining theorem-level obstruction is item (B).
./docs/math/DDYO_MASSIVE_REDUCTION.md-173-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-182-No theorem-level proof of RA1n is currently present in this repository.
./docs/math/DDYO_MASSIVE_REDUCTION.md-183-
./docs/math/DDYO_MASSIVE_REDUCTION.md-184-No theorem-level proof of the gradient bound
./docs/math/DDYO_MASSIVE_REDUCTION.md-185-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:186:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-187-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-188-is currently recorded in this repository.
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-31-\text{annular potential estimate}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-32-\bigr]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-33-\wedge
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-34-\bigl[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:35:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-36-\bigr].
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-37-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-38-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-39-## Recorded open theorem-level items
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-45-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-46-### Obstruction 2
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-47-\[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-48-\text{No theorem-level proof of }
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-50-\text{ is currently present in this repository.}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-51-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-52-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-53-### Obstruction 3
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-58-## Reduced canonical form
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-59-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-60-If the annular fixed-scale Schwartz-kernel route is accepted, then the sole remaining terminal obstruction is
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-61-\[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:62:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-63-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-64-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-65-## Status
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-66-
--
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-4-
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-5-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-6-\[
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-7-\left|
./docs/math/DDYO_RA1N_TARGET_THEOREM.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-9-\right|
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-10-\le
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-11-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-12-\]
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:1:# DDYO RA1n G_j Provenance Audit
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-2-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-3-## Purpose
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-4-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:5:Search the repository for the exact construction of \(G_j\) needed for the remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-6-\[
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-8-\]
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-9-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:10:## Raw repository hits for \(G_j\)
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-11-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-12-```text
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:13:./docs/status/DDYO_RA1N_STATUS_2026_04_10.md:21:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:14:./docs/status/DDYO_RA1N_STATUS_2026_04_10.md:26:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:15:./docs/status/SCIENTIFIC_MATURITY_CHECKPOINT_2026_04_11.md:12:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:16:./docs/status/SCIENTIFIC_MATURITY_CURRENT.md:15:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:17:./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:52:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:18:./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:57:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:19:./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:67:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:20:./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:40:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:21:./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:45:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:22:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:34:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:23:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:36:-\int_{\mathbb R^3}\partial_m\!\bigl(x_\ell G_j(x)\bigr)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:24:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:41:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:25:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:44:\|\nabla(x_\ell G_j)\|_{L^\infty}\,\|H^{ab}_{j,k}\|_{L^1}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:26:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:27:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:54:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:28:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:64:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:29:./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:10:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:30:./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:15:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:31:./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:25:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:32:./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:33:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:33:./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:8:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:34:./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:19:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:35:./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:42:2. The shell product \(G_j\cdot e^{(j)}_{ab}(D)\omega_k\) has zero mean.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:36:./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:37:./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:16:\int_{\mathbb R^3} G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:38:./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:9:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:39:./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:17:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:40:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:41:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:42:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:21:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:43:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:25:\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:44:./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:45:./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:58:\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:46:./docs/math/BRANCH_B_FINAL_FRONTIER.md:16:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:47:./docs/math/BRANCH_B_FINAL_FRONTIER.md:24:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:48:./docs/math/BRANCH_B_FINAL_FRONTIER.md:41:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:49:./docs/math/BRANCH_B_FINAL_FRONTIER.md:49:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:50:./docs/math/BRANCH_B_FINAL_FRONTIER.md:54:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:51:./docs/math/BRANCH_B_FINAL_FRONTIER.md:76:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:52:./docs/math/BRANCH_B_FINAL_FRONTIER.md:142:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:53:./docs/math/BRANCH_B_FINAL_FRONTIER.md:149:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:54:./docs/math/BRANCH_B_FINAL_FRONTIER.md:158:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:55:./docs/math/BRANCH_B_FINAL_FRONTIER.md:167:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:56:./docs/math/BRANCH_B_FINAL_FRONTIER.md:178:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:57:./docs/math/BRANCH_B_FINAL_FRONTIER.md:211:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:58:./docs/math/BRANCH_B_FINAL_FRONTIER.md:216:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:59:./docs/math/BRANCH_B_FINAL_FRONTIER.md:233:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:60:./docs/math/BRANCH_B_FINAL_FRONTIER.md:241:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:61:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:62:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:14:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:63:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:19:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:64:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:31:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:65:./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:8:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:66:./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:22:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:67:./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:35:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:68:./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:43:\int (\partial_b S_k^a)\,\bigl(G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:69:./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:47:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:70:./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:71:./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:14:To prove it in this repository, one still needs the exact construction of \(G_j\), equivalently the precise definition of its Fourier multiplier or kernel normalization, together with any cancellation, support, or rescaling identities used in the estimate.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:72:./docs/math/DDYO_RA1N_PROOF.md:13:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:73:./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:6:\left| \int x_\ell \, G_j(x) \, e^{(j)}_{ab}(D) \omega_k(x) \, dx \right| \le C \, 2^{-j} 2^{-k} \|\omega_k\|_{L^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:74:./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:10:1. **Fourier Representation**: Let K(x) = G_j(x)\,[e^{(j)}_{ab}(D)\omega_k](x). The first moment is:
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:75:./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:20:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:76:./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:30:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:77:./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:8:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:78:./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:16:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:79:./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:21:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:80:./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:36:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:81:./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:6:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:82:./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:11:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:83:./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:20:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:84:./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:29:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:85:./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:42:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:86:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:1:# DDYO RA1n G_j Provenance Audit
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:87:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:5:Search the repository for the exact construction of \(G_j\) needed for the remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:88:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:89:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:10:## Raw repository hits for \(G_j\)
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:90:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:16:./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:91:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:17:./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:62:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:92:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:21:If NO_DEFINITION_HITS appears above, then no explicit theorem-level definition of \(G_j\) was found by this repository-wide text search, and the gradient-bound route still lacks the exact structural input required for closure.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:93:./docs/math/DDYO_RA1N_TARGET_THEOREM.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:94:./docs/math/DDYO_CANONICAL_FRONTIER.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:95:./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:62:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:96:./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:66:\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:97:./docs/math/DDYO_SOLVE_REQUIREMENTS.md:8:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:98:./docs/math/DDYO_SOLVE_REQUIREMENTS.md:15:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:99:./docs/math/DDYO_SOLVE_REQUIREMENTS.md:24:\bigl\|G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:100:./docs/math/DDYO_SOLVE_REQUIREMENTS.md:33:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-101-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-102-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-103-Candidate definition hits
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:104:./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:105:./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:62:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:106:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:16:./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:107:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:17:./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:62:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-108-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-109-Status
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-110-Closed at the annular first-moment remainder stage.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:111:If NO_DEFINITION_HITS appears above, then no explicit theorem-level definition of \(G_j\) was found by this repository-wide text search, and the gradient-bound route still lacks the exact structural input required for closure.
--
./docs/math/DDYO_RA1N_PROOF.md-9-
./docs/math/DDYO_RA1N_PROOF.md-10-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_PROOF.md-11-\[
./docs/math/DDYO_RA1N_PROOF.md-12-\left|
./docs/math/DDYO_RA1N_PROOF.md:13:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_PROOF.md-14-\right|
./docs/math/DDYO_RA1N_PROOF.md-15-\le
./docs/math/DDYO_RA1N_PROOF.md-16-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_PROOF.md-17-\]
--
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-30-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-31-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-32-Hence
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-33-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:34:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-35-=
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:36:-\int_{\mathbb R^3}\partial_m\!\bigl(x_\ell G_j(x)\bigr)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-37-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-38-and therefore
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-39-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-40-\left|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:41:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-42-\right|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-43-\le
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:44:\|\nabla(x_\ell G_j)\|_{L^\infty}\,\|H^{ab}_{j,k}\|_{L^1}.
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-45-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-46-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-47-Consequently, if
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-48-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-50-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-51-then
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-52-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-53-\left|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:54:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-55-\right|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-56-\le
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-57-C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-58-\]
--
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-60-## Status
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-61-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-62-This reduces RA1n to the annular divergence-potential estimate together with the bound
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-63-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:64:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-65-\]
--
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-5-Find a proof that there exists \(C<\infty\) such that for all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-6-all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-7-\[
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-8-\left|
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:9:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-10-\right|
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-11-\le
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-12-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-13-\]
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-14-
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-15-Together with
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-16-\[
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:17:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-18-\]
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-19-this implies the shell-product \(H^1\) gain, the deviatoric coercivity estimate,
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-20-Claim 5, and final DDYO continuum closure.
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-21-
--
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-8-Q_m\in \mathcal S(\mathbb R^3)
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-9-\bigr]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-10-\wedge
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-11-\bigl[
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md:12:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-13-\bigr]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-14-\Longrightarrow
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-15-\text{RA1n}
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-16-\Longrightarrow
--
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-26-Q_m\in \mathcal S(\mathbb R^3),
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-27-\]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-28-then the sole remaining theorem-level obstruction is
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-29-\[
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md:30:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-31-\]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-32-
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-33-## Exact missing input
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-34-
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md:35:To prove the terminal obstruction, the repository still requires the exact theorem-level construction of \(G_j\) sufficient to derive the scale-sharp gradient estimate.
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-36-
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-37-## Status
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-38-
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-39-Closed at the annular first-moment remainder stage.
--
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-4-
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-5-For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-6-\[
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-7-\left|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:8:\int G_j\cdot
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-9-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-10-\right|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-11-\le
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-12-C\,2^{-j}2^{-k}\,
--
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-18-
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-19-It is equivalently sufficient to prove that for every \(\varepsilon\in(0,1)\),
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-20-\[
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-21-\left|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:22:\int G_j\cdot
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-23-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-24-\right|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-25-\le
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-26-\varepsilon\,\mathcal D_{j,k}[u]
--
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-31-## Equivalent Hardy-space route
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-32-
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-33-A sufficient route is the shell-product estimate
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-34-\[
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:35:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-36-\le
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-37-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1},
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-38-\qquad |j-k|\le C,
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-39-\]
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-40-combined with
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-41-\[
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-42-\left|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:43:\int (\partial_b S_k^a)\,\bigl(G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr)\,dx
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-44-\right|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-45-\le
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-46-\|\partial_b S_k^a\|_{BMO}\,
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:47:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}.
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-48-\]
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-49-
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-50-## Status
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-51-
--
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:1:# DDYO RA1n G_j Definition Status
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-2-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-3-## Result
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-4-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:5:Repository-wide literal search found references to \(G_j\) but no explicit theorem-level construction of \(G_j\).
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-6-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-7-## Consequence
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-8-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-9-The remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-10-\[
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:11:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-12-\]
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-13-still lacks the exact structural input required for proof.
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-14-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-15-## Status
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-16-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-17-Closed at the annular first-moment remainder stage.
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-18-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:19:No explicit theorem-level definition of \(G_j\) is currently recorded in this repository.
--
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-58-## Good-unknown branch
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-59-
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-60-If direct IBP is insufficient, the admissible replacement is to define
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-61-\[
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:62:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-63-\]
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-64-and prove the commutator pairing identity in the good-unknown form
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-65-\[
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:66:\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-67-=
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-68-\int \widetilde\Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-69-+
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-70-\widetilde R_{j,k},
--
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-4-
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-5-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-6-\[
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-7-\left|
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-9-\right|
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-10-\le
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-11-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-12-\]
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-13-
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-14-Together with
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-15-\[
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:16:\int_{\mathbb R^3} G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-17-\]
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-18-this yields the shell-product \(H^1\) gain, the deviatoric coercivity estimate, Claim 5 / paired remainder closure, and final DDYO continuum closure.
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-19-
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-20-## Status
--
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-48-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-49-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-50-Combined with
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-51-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:52:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-53-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-54-it yields
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-55-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-56-\left|
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:57:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-58-\right|
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-59-\le
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-60-C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-61-\]
--
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-63-## Status
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-64-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-65-Conditional on the gradient bound
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-66-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:67:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-68-\]
--
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-6-## Verified Lemma
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-7-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-8-Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-9-\[
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:10:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-11-\]
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-12-and
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-13-\[
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-14-\left|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:15:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-16-\right|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-17-\le
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-18-C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-19-\]
--
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-21-## Consequences
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-22-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-23-RA1n implies the shell-product \(H^1\) gain
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-24-\[
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:25:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-26-\le
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-27-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-28-\]
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-29-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-30-Hence RA1n implies the deviatoric coercivity estimate
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-31-\[
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-32-\left|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:33:\int G_j\cdot
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-34-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-35-\right|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-36-\le
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-37-C\,2^{-j}2^{-k}\,
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-50-## Good-unknown equivalent form
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-51-
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-52-Equivalently, with
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-53-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-55-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-56-it is sufficient to prove
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-57-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:58:\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-59-=
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-60-\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-61-+
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-62-\mathsf R_{j,k},
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-1-# DDYO RA1n Gradient Bound
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-2-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-3-## Target lemma
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-9-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-10-## RA1n consequence
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-11-
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-17-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-18-then
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-19-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-20-\left|
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:21:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-22-\right|
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-23-=
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-24-\left|
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:25:\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-26-\right|
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-27-\le
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-28-C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-29-\]
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-3-## Open theorem-level target
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-5-The remaining local theorem-level target is
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-9-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-10-## Minimal missing input
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-11-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-12-No theorem-level proof of this bound is presently recorded.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-13-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:14:To prove it in this repository, one still needs the exact construction of \(G_j\), equivalently the precise definition of its Fourier multiplier or kernel normalization, together with any cancellation, support, or rescaling identities used in the estimate.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-15-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-16-## Status
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-17-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-18-Closed at the annular first-moment remainder stage.
--
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-2-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-3-## Sole remaining master key
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-4-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-5-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:6:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-7-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-8-and
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-9-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-10-\left|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:11:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-12-\right|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-13-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-14-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-15-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-16-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-17-## Equivalent shell-product \(H^1\) gain
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-18-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-19-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:20:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-21-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-22-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-23-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-24-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-25-## Equivalent deviatoric coercivity bound
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-26-For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-27-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-28-\left|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:29:\int G_j\cdot
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-30-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-31-\right|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-32-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-33-C\,2^{-j}2^{-k}\,
--
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-38-## Equivalent absorbability form
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-39-For every \(\varepsilon\in(0,1)\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-40-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-41-\left|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:42:\int G_j\cdot
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-43-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-44-\right|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-45-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-46-\varepsilon\,\mathcal D_{j,k}[u]
--
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-4-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-5-### 1. Zeroth-moment shell-product identity
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-6-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-7-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:8:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-9-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-10-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-11-### 2. First-moment shell-product control
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-12-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-13-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-14-\left|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:15:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-16-\right|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-17-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-18-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-19-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-20-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-21-### 3. Shell-product Hardy gain
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-22-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-23-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:24:\bigl\|G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr\|_{H^1}
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-25-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-26-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-27-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-28-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-29-### 4. Deviatoric coercivity / absorption
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-30-For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-31-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-32-\left|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:33:\int G_j\cdot
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-34-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-35-\right|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-36-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-37-C\,2^{-j}2^{-k}\,
--
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-16-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-17-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-18-Assume also the gradient bound:
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-19-\[
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:20:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-21-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-22-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-23-Then for
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-24-\[
--
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-26-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-27-one has
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-28-\[
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-29-\left|
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:30:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-31-\right|
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-32-\le
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-33-C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-34-\]
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-12-Find a proof that there exists C < infinity such that for all dyadic indices with |j-k| <= C,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-13-all tensor indices a,b, and all coordinate indices l,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-14-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-15-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:16:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-17-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-18-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-19-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-20-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-21-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-22-Together with
./docs/math/BRANCH_B_FINAL_FRONTIER.md-23-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md:24:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-25-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-26-this implies the shell-product H^1 gain, the deviatoric coercivity estimate,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-27-Claim 5, and final DDYO continuum closure.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-28-
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-37-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-38-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-39-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-40-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:41:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-42-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-43-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-44-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-45-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-46-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-47-Together with the zeroth-moment identity
./docs/math/BRANCH_B_FINAL_FRONTIER.md-48-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md:49:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-50-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-51-this is sufficient to recover the shell-product \(H^1\) gain and hence
./docs/math/BRANCH_B_FINAL_FRONTIER.md-52-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-53-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:54:\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-55-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-56-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-57-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-58-C\,2^{-j}2^{-k}\,
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-72-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-73-For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-74-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-75-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:76:\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-77-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-78-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-79-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-80-C\,2^{-j}2^{-k}\,
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-138-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-139-### 1. Zeroth-moment shell-product identity
./docs/math/BRANCH_B_FINAL_FRONTIER.md-140-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-141-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md:142:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-143-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-144-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-145-### 2. First-moment shell-product control
./docs/math/BRANCH_B_FINAL_FRONTIER.md-146-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-147-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-148-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:149:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-150-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-151-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-152-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-153-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-154-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-155-### 3. Shell-product Hardy gain
./docs/math/BRANCH_B_FINAL_FRONTIER.md-156-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-157-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md:158:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/BRANCH_B_FINAL_FRONTIER.md-159-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-160-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-161-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-162-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-163-### 4. Deviatoric coercivity / absorption
./docs/math/BRANCH_B_FINAL_FRONTIER.md-164-For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-165-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-166-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:167:\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-168-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-169-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-170-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-171-C\,2^{-j}2^{-k}\,
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-174-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-175-or equivalently, for every \(\varepsilon\in(0,1)\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-176-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-177-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:178:\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-179-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-180-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-181-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-182-\varepsilon\,\mathcal D_{j,k}[u]
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-207-## Verified Statement
./docs/math/BRANCH_B_FINAL_FRONTIER.md-208-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-209-Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-210-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md:211:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-212-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-213-and
./docs/math/BRANCH_B_FINAL_FRONTIER.md-214-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-215-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:216:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-217-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-218-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-219-C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-220-\]
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-229-## Current weakest sufficient remaining lemma
./docs/math/BRANCH_B_FINAL_FRONTIER.md-230-For all dyadic indices with |j-k| <= C, all tensor indices a,b, and all coordinate indices l,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-231-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-232-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md:233:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-234-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-235-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-236-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-237-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-238-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-239-Together with the zeroth-moment identity
./docs/math/BRANCH_B_FINAL_FRONTIER.md-240-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md:241:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-242-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-243-this is sufficient to recover the shell-product H^1 gain and the target deviatoric coercivity bound.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-244-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-245-```
--
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-1-# DDYO Minimal Missing Lemma
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-2-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-3-## Conditional
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-4-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:5:Assume there exists an explicit theorem-level construction of \(G_j\) such that
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-6-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:7:G_j(x)=2^{2j}\Gamma(2^j x)
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-8-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-9-for some fixed kernel \(\Gamma\) satisfying
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-10-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-11-\nabla(x_\ell \Gamma)\in L^\infty(\mathbb R^3).
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-12-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-13-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-14-Then
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-15-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:16:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-17-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-18-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-19-Consequently, together with the recorded annular-potential route, one obtains RA1n, hence Branch B closure, hence DDYO shell-product frontier closure.
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-20-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-21-## Status
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-22-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-23-Closed at the annular first-moment remainder stage.
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-24-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:25:No theorem-level proof of the required explicit construction of \(G_j\) is currently present in this repository.
--
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-2-
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-3-## Objective
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-4-Establish that the first moment of the shell-product interaction satisfies:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-5-\[
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:6:\left| \int x_\ell \, G_j(x) \, e^{(j)}_{ab}(D) \omega_k(x) \, dx \right| \le C \, 2^{-j} 2^{-k} \|\omega_k\|_{L^1}
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-7-\]
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-8-
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-9-## Proof: Bernstein Extraction via Fourier Derivative
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:10:1. **Fourier Representation**: Let K(x) = G_j(x)\,[e^{(j)}_{ab}(D)\omega_k](x). The first moment is:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-11-   \[ M_{1,\ell} = \int x_\ell K(x) \, dx = i \left. \frac{\partial}{\partial \xi_\ell} \widehat{K}(\xi) \right|_{\xi=0} \]
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-12-2. **Symbol Decomposition**: The symbol of the product is the convolution of the symbols:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-13-   \[ \widehat{K}(\xi) = \left( \hat{G}_j * \left[ \text{symb}(e^{(j)}_{ab}) \cdot \hat{\omega}_k \right] \right)(\xi) \]
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-14-3. **Derivative Application**: By the properties of convolution:
--
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-3-## Statement
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-4-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-5-By the reduction chain and the fixed-scale Schwartz-kernel route, the remaining theorem-level local task for RA1n is the bound
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-6-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-8-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-9-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-10-## Consequence
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-11-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-12-If
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-13-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:14:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-15-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-16-then together with the established annular-potential route one obtains
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-17-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-18-\left|
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:19:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-20-\right|
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-21-\le
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-22-C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-23-\]
--
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-27-## Frontier form
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-28-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-29-The DDYO shell-product frontier is reduced to the theorem-level proof of
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-30-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:31:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-32-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-33-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-34-## Status
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-35-
--
./docs/math/DDYO_CANONICAL_FRONTIER.md-4-
./docs/math/DDYO_CANONICAL_FRONTIER.md-5-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_CANONICAL_FRONTIER.md-6-\[
./docs/math/DDYO_CANONICAL_FRONTIER.md-7-\left|
./docs/math/DDYO_CANONICAL_FRONTIER.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_CANONICAL_FRONTIER.md-9-\right|
./docs/math/DDYO_CANONICAL_FRONTIER.md-10-\le
./docs/math/DDYO_CANONICAL_FRONTIER.md-11-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_CANONICAL_FRONTIER.md-12-\]
```

## Context windows for kernel / `Gamma` candidates

```text
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-3-## Conditional
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-4-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-5-Assume there exists an explicit theorem-level construction of \(G_j\) such that
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-6-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:7:G_j(x)=2^{2j}\Gamma(2^j x)
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-8-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:9:for some fixed kernel \(\Gamma\) satisfying
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-10-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:11:\nabla(x_\ell \Gamma)\in L^\infty(\mathbb R^3).
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-12-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-13-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-14-Then
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-15-\[
--
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-31-where
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-32-\[
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-33-\mathsf I_{j,k}^{\mathrm{sym}}
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-34-=
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:35:\int \Gamma_{j,k}(x):\operatorname{Sym}\nabla S_k(x)\,dx,
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-36-\]
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-37-and
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-38-\[
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-39-|\mathsf R_{j,k}|
--
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-64-and prove the commutator pairing identity in the good-unknown form
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-65-\[
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-66-\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-67-=
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:68:\int \widetilde\Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-69-+
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-70-\widetilde R_{j,k},
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-71-\]
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-72-with
--
./docs/math/DDYO_CLAIM5_TARGET.md-5-For \(|j-k|\le C\), prove
./docs/math/DDYO_CLAIM5_TARGET.md-6-\[
./docs/math/DDYO_CLAIM5_TARGET.md-7-\int \mathcal H'_\tau(\omega_j)\cdot[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_CLAIM5_TARGET.md-8-=
./docs/math/DDYO_CLAIM5_TARGET.md:9:\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx+\mathsf R_{j,k},
./docs/math/DDYO_CLAIM5_TARGET.md-10-\]
./docs/math/DDYO_CLAIM5_TARGET.md-11-with
./docs/math/DDYO_CLAIM5_TARGET.md-12-\[
./docs/math/DDYO_CLAIM5_TARGET.md-13-|\mathsf R_{j,k}|
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-15-with
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-16-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-17-\mathsf I^{\mathrm{sym}}_{j,k}
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-18-=
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md:19:\int \Gamma_{j,k}(x):\operatorname{Sym}\nabla S_k(x)\,dx,
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-20-\qquad
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-21-|\mathsf R_{j,k}|
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-22-\le
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-23-C\,2^{-j}2^{-k}\,
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-52-Show the remaining top-order term can be written as
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-53-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-54-\mathsf I^{\mathrm{sym}}_{j,k}
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-55-=
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md:56:\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx.
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-57-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-58-
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-59-### Claim 5: dyadic remainder gain
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-60-Prove the remainder satisfies
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-11-where
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-12-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-13-\mathsf I^{\mathrm{sym}}_{j,k}
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-14-=
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:15:\int \Gamma_{j,k}(x):\operatorname{Sym}\nabla S_k(x)\,dx,
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-16-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-17-and
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-18-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-19-|\mathsf R_{j,k}|
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-56-it is sufficient to prove
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-57-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-58-\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-59-=
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:60:\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-61-+
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-62-\mathsf R_{j,k},
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-63-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-64-with the same remainder bound above.
--
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-24-with
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-25-\[
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-26-\mathsf I^{\mathrm{sym}}_{j,k}
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-27-=
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:28:\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx,
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-29-\]
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-30-and
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-31-\[
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-32-|\mathsf R_{j,k}|
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-3-## Conditional
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-4-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-5-Assume there exists an explicit theorem-level construction of \(G_j\) such that
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-6-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:7:G_j(x)=2^{2j}\Gamma(2^j x)
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-8-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-9-for some fixed kernel \(\Gamma\) satisfying
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-10-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-11-\nabla(x_\ell \Gamma)\in L^\infty(\mathbb R^3).
./modules/rh/akcl/akcl_uniformization.md-27-E[f] ≥ c0 D(L) ||f||^2
./modules/rh/akcl/akcl_uniformization.md-28-
./modules/rh/akcl/akcl_uniformization.md-29-## New Invariant
./modules/rh/akcl/akcl_uniformization.md-30-
./modules/rh/akcl/akcl_uniformization.md:31:D(L) captures kernel mass growth.
./modules/rh/akcl/akcl_uniformization.md-32-
./modules/rh/akcl/akcl_uniformization.md-33-Uniform coercivity ⇔ controlled growth of D(L).
--
./modules/rh/experiments/akcl_normalized_scan.py-4-def weight(x):
./modules/rh/experiments/akcl_normalized_scan.py-5-    return np.exp(-x)
./modules/rh/experiments/akcl_normalized_scan.py-6-
./modules/rh/experiments/akcl_normalized_scan.py-7-
./modules/rh/experiments/akcl_normalized_scan.py:8:def kernel(x, y):
./modules/rh/experiments/akcl_normalized_scan.py-9-    return (x - y) ** 2
./modules/rh/experiments/akcl_normalized_scan.py-10-
./modules/rh/experiments/akcl_normalized_scan.py-11-
./modules/rh/experiments/akcl_normalized_scan.py-12-def energy(xs):
./modules/rh/experiments/akcl_normalized_scan.py-13-    E = 0.0
./modules/rh/experiments/akcl_normalized_scan.py-14-    for x in xs:
./modules/rh/experiments/akcl_normalized_scan.py-15-        for y in xs:
./modules/rh/experiments/akcl_normalized_scan.py:16:            E += kernel(x, y) * weight(x) * weight(y)
./modules/rh/experiments/akcl_normalized_scan.py-17-    return E
./modules/rh/experiments/akcl_normalized_scan.py-18-
./modules/rh/experiments/akcl_normalized_scan.py-19-
./modules/rh/experiments/akcl_normalized_scan.py-20-def D(xs):
./modules/rh/experiments/akcl_normalized_scan.py-21-    vals = []
./modules/rh/experiments/akcl_normalized_scan.py-22-    for x in xs:
./modules/rh/experiments/akcl_normalized_scan.py-23-        s = 0.0
./modules/rh/experiments/akcl_normalized_scan.py-24-        for y in xs:
./modules/rh/experiments/akcl_normalized_scan.py:25:            s += kernel(x, y) * weight(y)
./modules/rh/experiments/akcl_normalized_scan.py-26-        vals.append(s)
./modules/rh/experiments/akcl_normalized_scan.py-27-    return max(vals)
./modules/rh/experiments/akcl_normalized_scan.py-28-
./modules/rh/experiments/akcl_normalized_scan.py-29-
--
./tests/test_ddyo_hybrid_proxy.py-6-    idx = np.arange(n)
./tests/test_ddyo_hybrid_proxy.py-7-    return np.where(idx <= n // 2, idx, idx - n)
./tests/test_ddyo_hybrid_proxy.py-8-
./tests/test_ddyo_hybrid_proxy.py-9-
./tests/test_ddyo_hybrid_proxy.py:10:def make_even_gaussian_kernel(n, sigma_pts):
./tests/test_ddyo_hybrid_proxy.py-11-    m = centered_offsets(n).astype(float)
./tests/test_ddyo_hybrid_proxy.py-12-    K = np.exp(-(m**2) / (2.0 * sigma_pts**2))
./tests/test_ddyo_hybrid_proxy.py-13-    K /= np.sum(K)
./tests/test_ddyo_hybrid_proxy.py-14-    return K
--
./tests/test_ddyo_hybrid_proxy.py-27-
./tests/test_ddyo_hybrid_proxy.py-28-    sp = deriv(s, h)
./tests/test_ddyo_hybrid_proxy.py-29-    wp = deriv(w, h)
./tests/test_ddyo_hybrid_proxy.py-30-
./tests/test_ddyo_hybrid_proxy.py:31:    K = make_even_gaussian_kernel(n, sigma_pts)
./tests/test_ddyo_hybrid_proxy.py-32-    m = centered_offsets(n).astype(float)
./tests/test_ddyo_hybrid_proxy.py-33-    y = np.arange(n)
./tests/test_ddyo_hybrid_proxy.py-34-
./tests/test_ddyo_hybrid_proxy.py-35-    raw = np.zeros(n, dtype=float)
--
./tests/test_ddyo_hybrid_proxy.py-49-    l1_rem = np.sum(np.abs(rem)) * h
./tests/test_ddyo_hybrid_proxy.py-50-    return l1_raw, l1_rem
./tests/test_ddyo_hybrid_proxy.py-51-
./tests/test_ddyo_hybrid_proxy.py-52-
./tests/test_ddyo_hybrid_proxy.py:53:def test_hybrid_proxy_even_kernel_has_zero_signed_first_moment():
./tests/test_ddyo_hybrid_proxy.py-54-    n = 513
./tests/test_ddyo_hybrid_proxy.py:55:    K = make_even_gaussian_kernel(n, sigma_pts=3.0)
./tests/test_ddyo_hybrid_proxy.py-56-    m = centered_offsets(n).astype(float)
./tests/test_ddyo_hybrid_proxy.py-57-    signed_first_moment = float(np.sum(K * m))
./tests/test_ddyo_hybrid_proxy.py-58-    assert abs(signed_first_moment) < 1e-12
./tests/test_ddyo_hybrid_proxy.py-59-
--
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-82-
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-83-Properties
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-84-
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-85-- positive semidefinite
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md:86:- kernel removed by axial gauge fixing
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-87-- smallest eigenvalue scales as
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-88-
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-89-\[
./docs/yang_mills/block_poincare/plaquette_quadratic_form.md-90-\lambda_{min}(\Delta_g) \sim L^{-2}.
--
./docs/math/DDYO_COUNTEREXAMPLE_ZERO_SHELL_MEAN_NOT_SUFFICIENT.md-51-\int S_k=0,
./docs/math/DDYO_COUNTEREXAMPLE_ZERO_SHELL_MEAN_NOT_SUFFICIENT.md-52-\qquad
./docs/math/DDYO_COUNTEREXAMPLE_ZERO_SHELL_MEAN_NOT_SUFFICIENT.md-53-\int \omega_k=0
./docs/math/DDYO_COUNTEREXAMPLE_ZERO_SHELL_MEAN_NOT_SUFFICIENT.md-54-\]
./docs/math/DDYO_COUNTEREXAMPLE_ZERO_SHELL_MEAN_NOT_SUFFICIENT.md:55:without an additional dipole / Taylor / kernel cancellation mechanism is false.
--
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-1-# DDYO Kernel First Moment Lemma
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-2-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md:3:## Candidate kernel first-moment bound
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-4-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md:5:For the smooth positive dyadic projector \(\widetilde P_j\) with kernel \(K_j\),
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-6-\[
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-7-\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-8-\]
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-9-
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-10-## Minimal missing input
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-11-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-12-No theorem-level proof of this bound is presently recorded.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-13-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:14:To prove it in this repository, one still needs the exact construction of \(G_j\), equivalently the precise definition of its Fourier multiplier or kernel normalization, together with any cancellation, support, or rescaling identities used in the estimate.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-15-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-16-## Status
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-17-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-18-Closed at the annular first-moment remainder stage.
--
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-5-Assume there exists an explicit theorem-level construction of \(G_j\) such that
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-6-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-7-G_j(x)=2^{2j}\Gamma(2^j x)
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-8-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:9:for some fixed kernel \(\Gamma\) satisfying
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-10-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-11-\nabla(x_\ell \Gamma)\in L^\infty(\mathbb R^3).
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-12-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-13-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-52-
./docs/math/DDYO_MASSIVE_REDUCTION.md-53-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md-54-\text{annular potential estimate}
./docs/math/DDYO_MASSIVE_REDUCTION.md-55-\Longleftarrow
./docs/math/DDYO_MASSIVE_REDUCTION.md:56:\text{fixed-scale Schwartz-kernel bound}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-57-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-58-
./docs/math/DDYO_MASSIVE_REDUCTION.md-59-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:60:\text{fixed-scale Schwartz-kernel bound}
./docs/math/DDYO_MASSIVE_REDUCTION.md-61-\Longleftarrow
./docs/math/DDYO_MASSIVE_REDUCTION.md-62-Q_m\in \mathcal S(\mathbb R^3).
./docs/math/DDYO_MASSIVE_REDUCTION.md-63-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-64-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-101-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-102-
./docs/math/DDYO_MASSIVE_REDUCTION.md-103-### Layer 4: annular potential route
./docs/math/DDYO_MASSIVE_REDUCTION.md-104-
./docs/math/DDYO_MASSIVE_REDUCTION.md:105:The annular potential estimate reduces to the fixed-scale multiplier-kernel route:
./docs/math/DDYO_MASSIVE_REDUCTION.md-106-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md-107-q_{k,m}(\xi)=2^{-k}Q_m(2^{-k}\xi),
./docs/math/DDYO_MASSIVE_REDUCTION.md-108-\qquad
./docs/math/DDYO_MASSIVE_REDUCTION.md-109-\|\mathcal F^{-1}q_{k,m}\|_{L^1}=2^{-k}\|K_m\|_{L^1},
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-121-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-122-
./docs/math/DDYO_MASSIVE_REDUCTION.md-123-### Layer 5: fixed-scale cutoff statement
./docs/math/DDYO_MASSIVE_REDUCTION.md-124-
./docs/math/DDYO_MASSIVE_REDUCTION.md:125:At fixed scale, the annular cutoff removes the origin singularity, so the multiplier is smooth and compactly supported away from the singular point. This is the recorded local route to the \(L^1\) kernel bound.
./docs/math/DDYO_MASSIVE_REDUCTION.md-126-
./docs/math/DDYO_MASSIVE_REDUCTION.md-127-### Layer 6: gradient-bound route
./docs/math/DDYO_MASSIVE_REDUCTION.md-128-
./docs/math/DDYO_MASSIVE_REDUCTION.md-129-The remaining parallel local route is
--
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-5-For \(|j-k|\le C\), let
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-6-\[
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-7-\mathsf T^{(1)}_{j,k}
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-8-\]
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-10-
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-11-The sole next target is to prove either
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-12-\[
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-13-\mathsf T^{(1)}_{j,k}=0,
--
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-33-up to summable lower-order terms.
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-34-
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-35-## Status
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-36-
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:37:This isolates the only unresolved first-order leakage object in the hybrid paired/Taylor/kernel route.
--
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-1-# DDYO Mollified Skew Cancellation
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-2-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-3-## Target identity
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-4-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md:5:Let \((\widetilde P_j)_j\) be a smooth positive dyadic family with even real symbol and convolution kernel \(K_j(x-y)\).
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-6-Assume \(\Omega_{\sim j}\) is divergence-free and pointwise skew-symmetric.
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-7-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-8-Prove
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-9-\[
--
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-20--
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-21-\Omega_{\sim j}\!\cdot\nabla(\widetilde P_j\omega_{\sim j}).
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-22-\]
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-23-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md:24:Using the kernel representation,
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-25-\[
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-26-\widetilde P_j f(x)=\int K_j(x-y)f(y)\,dy,
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-27-\]
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-28-reduce the commutator to an antisymmetric bilinear form in \((x,y)\).
--
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-1-# DDYO Almost-Orthogonality Gain
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-2-
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-3-## Remaining shellwise ingredient
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-4-
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md:5:After the kernel first-moment estimate
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-6-\[
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-7-\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j},
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-8-\]
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-9-the remaining task is to extract one further effective \(2^{-j}\) from shell localization / almost-orthogonality.
--
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-5-The remaining Claim 5 branch is the hybrid route:
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-6-
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-7-1. paired decomposition at the \(\mathcal H'_\tau\)-level,
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-8-2. first-order Taylor extraction of the shell difference,
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:9:3. kernel symmetrization to remove the first-order paired leakage,
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-10-4. dipole-type second gain on the post-symmetrized remainder,
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-11-5. lower-order routing through the existing
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-12-\[
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-13-\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u].
--
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-38-\]
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-39-
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-40-## Hybrid mechanism
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-41-
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:42:The first factor \(2^{-j}\) is supplied by the kernel first moment:
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-43-\[
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-44-\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-45-\]
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-46-
--
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-9-with \(\chi_k\) supported in
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-10-\[
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-11-\{\xi\in\mathbb R^3:c\,2^k\le |\xi|\le C\,2^k\},
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-12-\]
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md:13:the desired annular potential estimate follows from the kernel bound
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-14-\[
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-15-\|\mathcal F^{-1}q_{k,m}\|_{L^1}\le C\,2^{-k}.
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-16-\]
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-17-
--
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-59-Prove
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-60-\[
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-61-Q_m\in \mathcal S(\mathbb R^3),
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-62-\]
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md:63:equivalently that the annular cutoff removes the origin singularity and yields an \(L^1\) Schwartz kernel at unit scale.
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-64-
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-65-## Status
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-66-
./docs/math/DDYO_RA1N_MULTIPLIER_KERNEL_ROUTE.md-67-Open reduction target.
--
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-1-# DDYO RA1n Sole Remaining Local Task
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-2-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-3-## Statement
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-4-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:5:By the reduction chain and the fixed-scale Schwartz-kernel route, the remaining theorem-level local task for RA1n is the bound
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-6-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-7-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-8-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-9-
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-56-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-57-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-58-## Reduced canonical form
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-59-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:60:If the annular fixed-scale Schwartz-kernel route is accepted, then the sole remaining terminal obstruction is
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-61-\[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-62-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-63-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-64-
--
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-24-so that \(H^1\)-BMO duality yields the desired pairing bound.
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-25-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-26-## Symbol layer
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-27-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:28:For radial shell kernel and traceless shell multiplier,
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-29-\[
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-30-e^{(j)}_{ab}(\xi)
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-31-=
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-32-\chi_j(\xi)\left(\frac{\xi_a\xi_b}{|\xi|^2}-\frac{\delta_{ab}}{3}\right),
--
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-45-\int_0^1 \nabla S_{\sim j}(y+\theta(x-y))\,d\theta
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-46-\right)\nabla g(y)\,dy.
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-47-\]
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-48-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:49:## Required kernel gain
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-50-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-51-The terminal estimate is to prove
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-52-\[
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-53-\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j},
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-1-# DDYO RA1n Gradient Bound
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-2-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-3-## Target lemma
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-7-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-9-
--
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-1-# DDYO Critical Commutator Lemma
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-2-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-3-## Terminal new ingredient
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-4-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:5:For a smooth positive dyadic family \((\widetilde P_j)_j\) with even real symbol and kernels \(K_j\),
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-6-prove the shellwise bound
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-7-\[
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-8-2^{2j}\left|
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-9-\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
--
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-11-alone do not imply cancellation of the paired remainder.
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-12-
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-13-## Sole remaining Claim 5 route
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-14-
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md:15:The remaining terminal target is to prove that the first-order Taylor contribution in the paired remainder is itself orthogonal to the shell interaction after kernel symmetrization, so that the remainder behaves as a dipole and gains the second factor
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-16-\[
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-17-2^{-k}.
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-18-\]
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-19-
--
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-26-C\,2^{-j}2^{-k}\,
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-27-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-28-\|\omega_k\|_{L^1},
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-29-\]
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md:30:where the first \(2^{-j}\) comes from the kernel first moment and the second \(2^{-k}\) comes from genuine paired dipole / Taylor / kernel cancellation.
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-31-
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-32-## Weakest sufficient structural lemma
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-33-
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-34-It is sufficient to prove that the first-order Taylor piece
--
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-38-of the paired commutator remainder satisfies
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-39-\[
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-40-\mathsf T^{(1)}_{j,k}=0
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-41-\]
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md:42:after shell-frequency localization and kernel symmetrization, leaving only a second-order remainder with net gain
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-43-\[
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-44-2^{-j}2^{-k}.
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-45-\]
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-46-
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-36-./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-37-./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:16:\int_{\mathbb R^3} G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-38-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:9:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-39-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:17:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:40:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-41-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-42-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:21:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-43-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:25:\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-44-./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-67-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:35:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-68-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:43:\int (\partial_b S_k^a)\,\bigl(G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-69-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:47:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-70-./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:71:./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:14:To prove it in this repository, one still needs the exact construction of \(G_j\), equivalently the precise definition of its Fourier multiplier or kernel normalization, together with any cancellation, support, or rescaling identities used in the estimate.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-72-./docs/math/DDYO_RA1N_PROOF.md:13:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-73-./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:6:\left| \int x_\ell \, G_j(x) \, e^{(j)}_{ab}(D) \omega_k(x) \, dx \right| \le C \, 2^{-j} 2^{-k} \|\omega_k\|_{L^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-74-./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:10:1. **Fourier Representation**: Let K(x) = G_j(x)\,[e^{(j)}_{ab}(D)\omega_k](x). The first moment is:
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-75-./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:20:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-33-\int \mathcal H'_\tau(\omega_j)\cdot \widetilde P_j(S_k\!\cdot\nabla\omega_k)\,dx
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-34--
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-35-\int \mathcal H'_\tau(\omega_j)\cdot S_k\!\cdot\nabla(\widetilde P_j\omega_k)\,dx
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-36-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md:37:into kernel form with \(K_j(x-y)\).
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-38-
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-39-### Claim 2: symmetrization in \((x,y)\)
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md:40:Rewrite the kernel pairing as a sum of terms symmetric and antisymmetric under
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-41-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-42-(x,y)\leftrightarrow(y,x).
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-43-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-44-
./modules/rh/akcl/mellin_contour_shift.md-12-
./modules/rh/akcl/mellin_contour_shift.md-13-## Shift
./modules/rh/akcl/mellin_contour_shift.md-14-
./modules/rh/akcl/mellin_contour_shift.md-15-For 0 < \eta < \sigma,
./modules/rh/akcl/mellin_contour_shift.md:16:apply the inverse Fourier formula on the line \Im u = \eta.
./modules/rh/akcl/mellin_contour_shift.md-17-
./modules/rh/akcl/mellin_contour_shift.md-18-Then
./modules/rh/akcl/mellin_contour_shift.md-19-|g(u)| \le C_{\sigma,\eta}(B)e^{- \eta u}
./modules/rh/akcl/mellin_contour_shift.md-20-for u \to +\infty.
```

## Context windows for dyadic scaling candidates

```text
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-3-## Conditional
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-4-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-5-Assume there exists an explicit theorem-level construction of \(G_j\) such that
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-6-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:7:G_j(x)=2^{2j}\Gamma(2^j x)
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-8-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-9-for some fixed kernel \(\Gamma\) satisfying
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-10-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-11-\nabla(x_\ell \Gamma)\in L^\infty(\mathbb R^3).
--
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-13-For
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-14-\[
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-15-B_j[u]
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-16-:=
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md:17:2^{2j}\!\int \mathcal H'(\omega_j)\cdot
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-18-[\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx,
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-19-\]
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-20-prove a decomposition
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-21-\[
--
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-115-- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:14:### Branch B: lower-order routing`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-116-- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:18:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr)_{j,k}.`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-117-- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:35:This is the minimal remaining object for hybrid DDYO Claim 5 after first-order post-symmetrization.`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-118-- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:1:# DDYO Dyadic Gain Extraction`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md:119:- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:11:extract the exact shellwise gain needed to offset the DDYO weight \(2^{2j}\).`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-120-- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:25:\varepsilon\,\lambda^{-1}\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-121-- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:27:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-122-
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-123-## Missing machine checks
--
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-5-For a smooth positive dyadic family \((\widetilde P_j)_j\),
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-6-prove
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-7-\[
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-8-\left|
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:9:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-10-\right|
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-11-\le
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-12-\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-13-+
--
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-35-\|[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g\|_{L^1}
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-36-\le
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-37-C\,\|\nabla S_{\sim j}\|_{L^\infty}\,\|g\|_{L^1}
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-38-\]
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:39:with a dyadic gain strong enough after multiplication by \(2^{2j}\) and summation to yield one global \(\varepsilon<1\).
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-40-
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-41-## Required new ingredient
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-42-
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-43-A Coifman--Meyer / Constantin--E--Titi type commutator estimate at the exact DDYO critical weights.
--
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-7-[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g(x)
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-8-=
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-9-\int K_j(x-y)\bigl(S_{\sim j}(x)-S_{\sim j}(y)\bigr)\cdot \nabla g(y)\,dy,
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-10-\]
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:11:extract the exact shellwise gain needed to offset the DDYO weight \(2^{2j}\).
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-12-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-13-## Weakest sufficient shellwise bound
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-14-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-15-It is sufficient to prove
--
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-57-## Consequence
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-58-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-59-This shellwise gain closes the weighted summation
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-60-\[
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:61:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-62-[\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-63-\]
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-64-with one global \(\varepsilon<1\), completing the DDYO continuum high-high absorbability step.
--
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-4-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-5-For a smooth positive dyadic family \((\widetilde P_j)_j\) with even real symbol and kernels \(K_j\),
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-6-prove the shellwise bound
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-7-\[
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:8:2^{2j}\left|
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-9-\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-10-\right|
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-11-\le
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-12-\varepsilon_j\bigl(\mathcal D_j[u]+\lambda\mathcal C_j[u]\bigr)
--
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-51-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-52-This lemma, together with mollified skew cancellation and lower-order projector replacement, yields
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-53-\[
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-54-\left|
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:55:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-56-\right|
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-57-\le
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-58-\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-59-+
--
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-25-## Consequence
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-26-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-27-If this reduction holds, the continuum DDYO symmetric commutator pairing frontier reduces to the mollified identity/bound pair:
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-28-\[
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md:29:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0,
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-30-\]
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-31-and
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-32-\[
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-33-\left|
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md:34:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-35-\right|
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-36-\le
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-37-\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-38-+
--
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-20-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-21-## Weakest remaining lemma
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-22-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-23-\[
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:24:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-25-\]
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-26-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-27-and
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-28-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-29-\[
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-30-\left|
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:31:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-32-\right|
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-33-\le
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-34-\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-35-+
--
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-64-## Weakest sufficient conditional closure
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-65-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-66-There exists a smooth positive dyadic family \((\widetilde P_j)_j\) such that, for every \(0<\varepsilon<1\),
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-67-\[
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:68:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0,
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-69-\]
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-70-and
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-71-\[
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-72-\left|
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:73:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-74-\right|
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-75-\le
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-76-\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-77-+
--
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-72-## Consequence
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-73-
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-74-Any one of Routes A--C is sufficient to close
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-75-\[
./docs/math/DDYO_SECOND_GAIN_ROUTE.md:76:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-77-[\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-78-\]
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-79-with one global \(\varepsilon<1\).
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-80-
--
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-6-Assume \(\Omega_{\sim j}\) is divergence-free and pointwise skew-symmetric.
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-7-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-8-Prove
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-9-\[
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md:10:\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0.
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-11-\]
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-12-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-13-## Structural expansion
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-14-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-3-## Conditional
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-4-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-5-Assume there exists an explicit theorem-level construction of \(G_j\) such that
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-6-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:7:G_j(x)=2^{2j}\Gamma(2^j x)
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-8-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-9-for some fixed kernel \(\Gamma\) satisfying
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-10-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-11-\nabla(x_\ell \Gamma)\in L^\infty(\mathbb R^3).
./docs/math/DDYO_CRITICAL_ENVELOPE.md-4-
./docs/math/DDYO_CRITICAL_ENVELOPE.md-5-\[
./docs/math/DDYO_CRITICAL_ENVELOPE.md-6-R_{\mathrm{DDYO}}[u]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-7-:=
./docs/math/DDYO_CRITICAL_ENVELOPE.md:8:\sup_{j\in\mathbb Z} 2^{-j}\|\Delta_j u\|_{L^\infty(\mathbb R^3)}
./docs/math/DDYO_CRITICAL_ENVELOPE.md-9-=
./docs/math/DDYO_CRITICAL_ENVELOPE.md-10-\|u\|_{\dot B^{-1}_{\infty,\infty}}.
./docs/math/DDYO_CRITICAL_ENVELOPE.md-11-\]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-12-
--
./docs/math/DDYO_CRITICAL_ENVELOPE.md-23-\Delta_j u_\mu(x,t)=\mu\,(\Delta_{j+j_0}u)(\mu x,\mu^2 t),
./docs/math/DDYO_CRITICAL_ENVELOPE.md-24-\]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-25-hence
./docs/math/DDYO_CRITICAL_ENVELOPE.md-26-\[
./docs/math/DDYO_CRITICAL_ENVELOPE.md:27:2^{-j}\|\Delta_j u_\mu\|_{L^\infty}
./docs/math/DDYO_CRITICAL_ENVELOPE.md-28-=
./docs/math/DDYO_CRITICAL_ENVELOPE.md-29-2^{-(k-j_0)}\mu\,\|\Delta_k u\|_{L^\infty}
./docs/math/DDYO_CRITICAL_ENVELOPE.md-30-=
./docs/math/DDYO_CRITICAL_ENVELOPE.md-31-2^{-k}\|\Delta_k u\|_{L^\infty},
--
./docs/math/DDYO_CRITICAL_ENVELOPE.md-42-The current test file `tests/test_ddyo_residual.py` implements the periodic sampled analogue
./docs/math/DDYO_CRITICAL_ENVELOPE.md-43-\[
./docs/math/DDYO_CRITICAL_ENVELOPE.md-44-R_{\mathrm{DDYO}}^{\mathrm{test}}
./docs/math/DDYO_CRITICAL_ENVELOPE.md-45-=
./docs/math/DDYO_CRITICAL_ENVELOPE.md:46:\sup_j 2^{-j}\|\Delta_j u\|_{L^\infty},
./docs/math/DDYO_CRITICAL_ENVELOPE.md-47-\]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-48-using discrete Fourier shell extraction.
./docs/math/DDYO_CRITICAL_ENVELOPE.md-49-
./docs/math/DDYO_CRITICAL_ENVELOPE.md-50-This sampled layer checks:
--
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-24-If the post-symmetrized first-order leakage vanishes or routes to lower order, then the remaining paired remainder satisfies
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-25-\[
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-26-|\mathsf R_{j,k}|
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-27-\le
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:28:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-29-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-30-\|\omega_k\|_{L^1},
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-31-\qquad |j-k|\le C,
./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md-32-\]
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-3-## Open theorem-level target
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-5-The remaining local theorem-level target is
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-9-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-10-## Minimal missing input
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-11-
--
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-36-\]
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-37-
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-38-Combined with
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-39-\[
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:40:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-41-\]
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-42-it implies
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-43-\[
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-44-\left|
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-45-\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-46-\right|
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-47-\le
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:48:C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-49-\]
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-50-
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-51-## Status
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-52-
--
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-3-## Statement
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-4-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-5-By the reduction chain and the fixed-scale Schwartz-kernel route, the remaining theorem-level local task for RA1n is the bound
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-6-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-8-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-9-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-10-## Consequence
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-11-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-12-If
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-13-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:14:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-15-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-16-then together with the established annular-potential route one obtains
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-17-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-18-\left|
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-19-\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-20-\right|
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-21-\le
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:22:C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-23-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-24-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-25-Hence RA1n follows.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-26-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-27-## Frontier form
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-28-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-29-The DDYO shell-product frontier is reduced to the theorem-level proof of
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-30-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:31:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-32-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-33-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-34-## Status
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-35-
--
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-15-If the terminal paired remainder satisfies
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-16-\[
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-17-|\mathsf R_{j,k}|
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-18-\le
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md:19:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-20-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-21-\|\omega_k\|_{L^1},
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-22-\]
./docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md-23-and all lower-order terms route into
--
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-45-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-46-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-47-Consequently, if
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-48-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-50-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-51-then
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-52-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-53-\left|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-54-\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-55-\right|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-56-\le
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:57:C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-58-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-59-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-60-## Status
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-61-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-62-This reduces RA1n to the annular divergence-potential estimate together with the bound
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-63-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:64:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-65-\]
--
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-30-and
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-31-\[
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-32-|\mathsf R_{j,k}|
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-33-\le
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:34:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-35-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-36-\|\omega_k\|_{L^1},
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-37-\qquad |j-k|\le C.
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-38-\]
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-39-
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-40-## Hybrid mechanism
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-41-
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:42:The first factor \(2^{-j}\) is supplied by the kernel first moment:
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-43-\[
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:44:\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-45-\]
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-46-
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-47-The second factor \(2^{-k}\) is not taken from:
./docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md-48-\[
--
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-3-## Candidate kernel first-moment bound
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-4-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-5-For the smooth positive dyadic projector \(\widetilde P_j\) with kernel \(K_j\),
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-6-\[
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md:7:\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-8-\]
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-9-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-10-## Weakest sufficient usage
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-11-
--
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-7-\left|
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-8-\int \mathcal H'_\tau(\omega_j)\cdot[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-9-\right|
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-10-\le
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md:11:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-12-\|\nabla S_k\|_{\mathrm{BMO}}\,
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-13-\|\omega_k\|_{H^1},
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-14-\]
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-15-or an equivalent shell-localized \(H^1\)-BMO paracommutator bound implying
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-16-\[
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-17-|\mathsf R_{j,k}|
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-18-\le
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md:19:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-20-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-21-\|\omega_k\|_{L^1}.
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-22-\]
./docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md-23-
--
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-14-\left|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-15-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-16-\right|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-17-\le
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:18:C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-19-\]
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-20-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-21-## Consequences
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-22-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-23-RA1n implies the shell-product \(H^1\) gain
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-24-\[
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-25-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-26-\le
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:27:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-28-\]
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-29-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-30-Hence RA1n implies the deviatoric coercivity estimate
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-31-\[
--
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-33-\int G_j\cdot
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-34-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-35-\right|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-36-\le
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:37:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-38-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-39-\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-40-\]
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-41-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-42-Hence RA1n implies Claim 5 / paired remainder closure
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-43-\[
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-44-|\mathsf R_{j,k}|
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-45-\le
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:46:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-47-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-48-\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-49-\]
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-50-
--
./docs/math/DDYO_RA1N_PROOF.md-12-\left|
./docs/math/DDYO_RA1N_PROOF.md-13-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_PROOF.md-14-\right|
./docs/math/DDYO_RA1N_PROOF.md-15-\le
./docs/math/DDYO_RA1N_PROOF.md:16:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_PROOF.md-17-\]
./docs/math/DDYO_RA1N_PROOF.md-18-
./docs/math/DDYO_RA1N_PROOF.md-19-## Current state
./docs/math/DDYO_RA1N_PROOF.md-20-
--
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-48-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-49-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-50-Combined with
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-51-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:52:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-53-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-54-it yields
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-55-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-56-\left|
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-57-\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-58-\right|
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-59-\le
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:60:C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-61-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-62-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-63-## Status
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-64-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-65-Conditional on the gradient bound
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-66-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:67:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-68-\]
--
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-7-\left|
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-8-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-9-\right|
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-10-\le
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:11:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-12-\]
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-13-
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-14-Together with
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-15-\[
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-3-## Target lemma
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-5-For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-9-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-10-## RA1n consequence
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-11-
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-24-\left|
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-25-\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-26-\right|
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-27-\le
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:28:C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-29-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-30-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-31-## Status
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-32-
--
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-16-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-17-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-18-Assume also the gradient bound:
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-19-\[
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:20:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-21-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-22-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-23-Then for
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-24-\[
--
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-29-\left|
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-30-\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-31-\right|
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-32-\le
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:33:C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-34-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-35-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-36-## Consequence
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-37-
--
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-3-## Remaining shellwise ingredient
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-4-
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-5-After the kernel first-moment estimate
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-6-\[
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md:7:\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j},
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-8-\]
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md:9:the remaining task is to extract one further effective \(2^{-j}\) from shell localization / almost-orthogonality.
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-10-
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-11-## Terminal shellwise target
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-12-
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-13-For
--
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-48-with
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-49-\[
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-50-\|T_{j,k}(\nabla S_k,\omega_k)\|_{L^1}
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-51-\le
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md:52:C\,2^{-j}2^{-k}\,\|\nabla S_k\|_{L^\infty}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-53-\]
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-54-
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-55-## Consequence
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-56-
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md:57:This produces the second effective \(2^{-j}\), closes
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-58-\[
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-59-\sum_j B_j[u],
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-60-\]
./docs/math/DDYO_ALMOST_ORTHOGONALITY_GAIN.md-61-and therefore completes the DDYO continuum high-high absorbability step.
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-45-\text{annular potential estimate}
./docs/math/DDYO_MASSIVE_REDUCTION.md-46-\bigr)
./docs/math/DDYO_MASSIVE_REDUCTION.md-47-\wedge
./docs/math/DDYO_MASSIVE_REDUCTION.md-48-\bigl(
./docs/math/DDYO_MASSIVE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-50-\bigr).
./docs/math/DDYO_MASSIVE_REDUCTION.md-51-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-52-
./docs/math/DDYO_MASSIVE_REDUCTION.md-53-\[
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-85-\left|
./docs/math/DDYO_MASSIVE_REDUCTION.md-86-\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_MASSIVE_REDUCTION.md-87-\right|
./docs/math/DDYO_MASSIVE_REDUCTION.md-88-\le
./docs/math/DDYO_MASSIVE_REDUCTION.md:89:C\,2^{-j}2^{-k}\|\omega_k\|_{L^1},
./docs/math/DDYO_MASSIVE_REDUCTION.md-90-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-91-obtained from:
./docs/math/DDYO_MASSIVE_REDUCTION.md-92-
./docs/math/DDYO_MASSIVE_REDUCTION.md-93-\[
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-96-\|H^{ab}_{j,k}\|_{L^1}\le C\,2^{-k}\|\omega_k\|_{L^1},
./docs/math/DDYO_MASSIVE_REDUCTION.md-97-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-98-and
./docs/math/DDYO_MASSIVE_REDUCTION.md-99-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:100:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-101-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-102-
./docs/math/DDYO_MASSIVE_REDUCTION.md-103-### Layer 4: annular potential route
./docs/math/DDYO_MASSIVE_REDUCTION.md-104-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-127-### Layer 6: gradient-bound route
./docs/math/DDYO_MASSIVE_REDUCTION.md-128-
./docs/math/DDYO_MASSIVE_REDUCTION.md-129-The remaining parallel local route is
./docs/math/DDYO_MASSIVE_REDUCTION.md-130-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:131:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-132-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-133-
./docs/math/DDYO_MASSIVE_REDUCTION.md-134-The repository-wide provenance audit has been introduced precisely because theorem-level closure of this bound requires the exact structural construction of \(G_j\).
./docs/math/DDYO_MASSIVE_REDUCTION.md-135-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-143-Q_m\in \mathcal S(\mathbb R^3)
./docs/math/DDYO_MASSIVE_REDUCTION.md-144-\bigr]
./docs/math/DDYO_MASSIVE_REDUCTION.md-145-\wedge
./docs/math/DDYO_MASSIVE_REDUCTION.md-146-\bigl[
./docs/math/DDYO_MASSIVE_REDUCTION.md:147:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-148-\bigr]
./docs/math/DDYO_MASSIVE_REDUCTION.md-149-\Longrightarrow
./docs/math/DDYO_MASSIVE_REDUCTION.md-150-\text{RA1n}
./docs/math/DDYO_MASSIVE_REDUCTION.md-151-\Longrightarrow
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-165-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-166-and
./docs/math/DDYO_MASSIVE_REDUCTION.md-167-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md-168-\text{(B)}\quad
./docs/math/DDYO_MASSIVE_REDUCTION.md:169:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-170-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-171-
./docs/math/DDYO_MASSIVE_REDUCTION.md-172-If item (A) is already accepted by the annular-cutoff argument, then the sole remaining theorem-level obstruction is item (B).
./docs/math/DDYO_MASSIVE_REDUCTION.md-173-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-182-No theorem-level proof of RA1n is currently present in this repository.
./docs/math/DDYO_MASSIVE_REDUCTION.md-183-
./docs/math/DDYO_MASSIVE_REDUCTION.md-184-No theorem-level proof of the gradient bound
./docs/math/DDYO_MASSIVE_REDUCTION.md-185-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:186:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-187-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-188-is currently recorded in this repository.
--
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-12-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-13-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-14-Then
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-15-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:16:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-17-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-18-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-19-Consequently, together with the recorded annular-potential route, one obtains RA1n, hence Branch B closure, hence DDYO shell-product frontier closure.
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-20-
--
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-8-\int G_j\cdot
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-9-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-10-\right|
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-11-\le
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:12:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-13-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-14-\|\omega_k\|_{L^1}.
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-15-\]
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-16-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-17-Equivalently, it is sufficient to prove the shell-product Hardy estimate
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-18-\[
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-19-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-20-\le
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:21:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1},
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-22-\qquad |j-k|\le C,
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-23-\]
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-24-so that \(H^1\)-BMO duality yields the desired pairing bound.
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-25-
--
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-13-The remaining terminal target is to prove
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-14-\[
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-15-|\mathsf R_{j,k}|
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-16-\le
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md:17:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-18-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-19-\|\omega_k\|_{L^1},
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-20-\qquad |j-k|\le C,
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-21-\]
--
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-31-\]
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-32-
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-33-### Kernel first moment input
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-34-\[
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md:35:\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-36-\]
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-37-
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-38-### Lower-order routing input
./docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md-39-\[
--
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-3-## New ingredient
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-4-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-5-Construct a smooth positive dyadic family \((\widetilde P_j)_j\) with symbol
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-6-\[
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md:7:\widetilde m_j(\xi)=\rho(2^{-j}\xi),
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-8-\]
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-9-where \(\rho\in C_c^\infty(\mathbb R^3)\), \(\rho\ge 0\), and \(\rho\) is supported in a fixed dyadic annulus.
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-10-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-11-## Target reduction
--
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-17-is lower-order in the sense that
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-18-\[
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-19-\left\|([P_j,f]-[\widetilde P_j,f])g\right\|_{L^1}
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-20-\le
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md:21:C\,2^{-j}\|\nabla f\|_{L^\infty}\|g\|_{L^1}
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-22-\]
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-23-up to an admissible summable dyadic remainder.
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-24-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-25-## Consequence
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-3-## Purpose
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-4-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-5-Search the repository for the exact construction of \(G_j\) needed for the remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-6-\[
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-8-\]
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-9-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-10-## Raw repository hits for \(G_j\)
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-11-
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-13-./docs/status/DDYO_RA1N_STATUS_2026_04_10.md:21:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-14-./docs/status/DDYO_RA1N_STATUS_2026_04_10.md:26:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-15-./docs/status/SCIENTIFIC_MATURITY_CHECKPOINT_2026_04_11.md:12:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-16-./docs/status/SCIENTIFIC_MATURITY_CURRENT.md:15:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:17:./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:52:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-18-./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:57:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:19:./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:67:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:20:./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:40:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-21-./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:45:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-22-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:34:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-23-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:36:-\int_{\mathbb R^3}\partial_m\!\bigl(x_\ell G_j(x)\bigr)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-24-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:41:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-25-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:44:\|\nabla(x_\ell G_j)\|_{L^\infty}\,\|H^{ab}_{j,k}\|_{L^1}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:26:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-27-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:54:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:28:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:64:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-29-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:10:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-30-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:15:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-31-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:25:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-32-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:33:\int G_j\cdot
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-37-./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:16:\int_{\mathbb R^3} G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-38-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:9:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-39-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:17:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-40-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:41:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-42-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:21:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-43-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:25:\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-44-./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-45-./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:58:\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-57-./docs/math/BRANCH_B_FINAL_FRONTIER.md:211:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-58-./docs/math/BRANCH_B_FINAL_FRONTIER.md:216:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-59-./docs/math/BRANCH_B_FINAL_FRONTIER.md:233:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-60-./docs/math/BRANCH_B_FINAL_FRONTIER.md:241:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:61:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:62:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:14:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-63-./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:19:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:64:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:31:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-65-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:8:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-66-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:22:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-67-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:35:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-68-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:43:\int (\partial_b S_k^a)\,\bigl(G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-69-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:47:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:70:./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-71-./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:14:To prove it in this repository, one still needs the exact construction of \(G_j\), equivalently the precise definition of its Fourier multiplier or kernel normalization, together with any cancellation, support, or rescaling identities used in the estimate.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-72-./docs/math/DDYO_RA1N_PROOF.md:13:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:73:./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:6:\left| \int x_\ell \, G_j(x) \, e^{(j)}_{ab}(D) \omega_k(x) \, dx \right| \le C \, 2^{-j} 2^{-k} \|\omega_k\|_{L^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-74-./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:10:1. **Fourier Representation**: Let K(x) = G_j(x)\,[e^{(j)}_{ab}(D)\omega_k](x). The first moment is:
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:75:./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:20:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-76-./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:30:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-77-./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:8:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-78-./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:16:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-79-./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:21:\int G_j\cdot
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-84-./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:29:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-85-./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:42:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-86-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:1:# DDYO RA1n G_j Provenance Audit
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-87-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:5:Search the repository for the exact construction of \(G_j\) needed for the remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:88:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-89-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:10:## Raw repository hits for \(G_j\)
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-90-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:16:./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-91-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:17:./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:62:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-92-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:21:If NO_DEFINITION_HITS appears above, then no explicit theorem-level definition of \(G_j\) was found by this repository-wide text search, and the gradient-bound route still lacks the exact structural input required for closure.
--
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-37-and
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-38-\[
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-39-|\mathsf R_{j,k}|
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-40-\le
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:41:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-42-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-43-\|\omega_k\|_{L^1},
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-44-\]
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-45-up to summable lower-order terms.
--
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-72-with
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-73-\[
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-74-|\widetilde R_{j,k}|
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-75-\le
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:76:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-77-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-78-\|\omega_k\|_{L^1}.
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-79-\]
./docs/math/DDYO_PAIRING_IBP_FRONTIER.md-80-
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-19-\int \Gamma_{j,k}(x):\operatorname{Sym}\nabla S_k(x)\,dx,
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-20-\qquad
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-21-|\mathsf R_{j,k}|
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-22-\le
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md:23:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-24-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-25-\|\omega_k\|_{L^1}.
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-26-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-27-
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-60-Prove the remainder satisfies
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-61-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-62-|\mathsf R_{j,k}|
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-63-\le
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md:64:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-65-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-66-\|\omega_k\|_{L^1},
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-67-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-68-up to summable lower-order terms.
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-31-\text{annular potential estimate}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-32-\bigr]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-33-\wedge
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-34-\bigl[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:35:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-36-\bigr].
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-37-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-38-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-39-## Recorded open theorem-level items
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-45-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-46-### Obstruction 2
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-47-\[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-48-\text{No theorem-level proof of }
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-50-\text{ is currently present in this repository.}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-51-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-52-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-53-### Obstruction 3
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-58-## Reduced canonical form
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-59-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-60-If the annular fixed-scale Schwartz-kernel route is accepted, then the sole remaining terminal obstruction is
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-61-\[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:62:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-63-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-64-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-65-## Status
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-66-
--
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-30-\int \mathcal H'(\omega_j)\cdot
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-31-[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-32-\right|
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-33-\le
./docs/math/DDYO_SECOND_GAIN_ROUTE.md:34:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-35-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-36-\|\omega_k\|_{L^1}\,
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-37-\|\mathcal H'(\omega_j)\|_{L^\infty},
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-38-\qquad |j-k|\le C.
--
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-51-with
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-52-\[
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-53-\|[\widetilde P_j,[Q_k,S_k]]g\|_{L^1}
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-54-\le
./docs/math/DDYO_SECOND_GAIN_ROUTE.md:55:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-56-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-57-\|g\|_{L^1}.
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-58-\]
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-59-
--
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-65-(x-y)\cdot \int_0^1 \nabla S_k(y+\theta(x-y))\,d\theta,
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-66-\]
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-67-prove that the first-order contribution vanishes after pairing with \(\mathcal H'(\omega_j)\), leaving only a remainder with net gain
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-68-\[
./docs/math/DDYO_SECOND_GAIN_ROUTE.md:69:2^{-j}2^{-k}.
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-70-\]
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-71-
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-72-## Consequence
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-73-
--
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-7-\left|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-8-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-9-\right|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-10-\le
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:11:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-12-\]
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-13-
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-14-Together with the zeroth-moment identity
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-15-\[
--
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-21-\int G_j\cdot
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-22-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-23-\right|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-24-\le
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:25:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-26-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-27-\|\omega_k\|_{L^1},
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-28-\qquad |j-k|\le C.
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-29-\]
--
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-10-\left|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-11-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-12-\right|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-13-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:14:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-15-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-16-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-17-## Equivalent shell-product \(H^1\) gain
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-18-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-19-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-20-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-21-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:22:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-23-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-24-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-25-## Equivalent deviatoric coercivity bound
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-26-For all dyadic indices with \(|j-k|\le C\),
--
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-29-\int G_j\cdot
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-30-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-31-\right|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-32-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:33:C\,2^{-j}2^{-k}\,
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-34-\|\nabla S_k\|_{L^\infty}\,
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-35-\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-36-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-37-
--
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-51-## Claim 5 / Branch B remainder target
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-52-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-53-|\mathsf R_{j,k}|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-54-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:55:C\,2^{-j}2^{-k}\,
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-56-\|\nabla S_k\|_{L^\infty}\,
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-57-\|\omega_k\|_{L^1},
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-58-\qquad |j-k|\le C.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-59-\]
--
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-49-## Required kernel gain
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-50-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-51-The terminal estimate is to prove
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-52-\[
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:53:\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j},
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-54-\]
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:55:and recover one additional effective \(2^{-j}\) from the shell localization / almost-orthogonality structure, yielding net \(2^{-2j}\).
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-56-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-57-## Consequence
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-58-
./docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md-59-This shellwise gain closes the weighted summation
--
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-22-For \(|j-k|\le C\),
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-23-\[
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-24-|\mathsf R_{j,k}|
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-25-\le
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md:26:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-27-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-28-\|\omega_k\|_{L^1},
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-29-\]
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md:30:where the first \(2^{-j}\) comes from the kernel first moment and the second \(2^{-k}\) comes from genuine paired dipole / Taylor / kernel cancellation.
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-31-
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-32-## Weakest sufficient structural lemma
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-33-
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-34-It is sufficient to prove that the first-order Taylor piece
--
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-40-\mathsf T^{(1)}_{j,k}=0
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-41-\]
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-42-after shell-frequency localization and kernel symmetrization, leaving only a second-order remainder with net gain
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-43-\[
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md:44:2^{-j}2^{-k}.
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-45-\]
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-46-
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-47-## Consequence
./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-48-
--
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-14-These vanishing-moment identities are admissible inputs for the paired remainder gain:
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-15-\[
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-16-|\mathsf R_{j,k}|
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-17-\le
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md:18:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-19-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-20-\|\omega_k\|_{L^1}.
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-21-\]
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-22-
--
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-7-\left|
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-8-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-9-\right|
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-10-\le
./docs/math/DDYO_RA1N_TARGET_THEOREM.md:11:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-12-\]
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-13-
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-14-## Role
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-15-
--
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-8-\left|
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-9-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-10-\right|
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-11-\le
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:12:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-13-\]
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-14-
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-15-Together with
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-16-\[
--
./docs/math/DDYO_CANONICAL_FRONTIER.md-7-\left|
./docs/math/DDYO_CANONICAL_FRONTIER.md-8-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_CANONICAL_FRONTIER.md-9-\right|
./docs/math/DDYO_CANONICAL_FRONTIER.md-10-\le
./docs/math/DDYO_CANONICAL_FRONTIER.md:11:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_CANONICAL_FRONTIER.md-12-\]
./docs/math/DDYO_CANONICAL_FRONTIER.md-13-
./docs/math/DDYO_CANONICAL_FRONTIER.md-14-## Dependency chain
./docs/math/DDYO_CANONICAL_FRONTIER.md-15-
--
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-22-Either branch implies that the remaining paired remainder satisfies
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-23-\[
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-24-|\mathsf R_{j,k}|
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-25-\le
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:26:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-27-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-28-\|\omega_k\|_{L^1},
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-29-\qquad |j-k|\le C,
./docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md-30-\]
--
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-85-\int \mathcal H_\tau'(\omega_j)\cdot
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-86-[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-87-\right|
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-88-\le
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md:89:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-90-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-91-\|\omega_k\|_{L^1},
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-92-\qquad |j-k|\le C,
./docs/math/DDYO_H_PRIME_ROUTE_CRITERION.md-93-\]
--
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-7-## Consequence
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-8-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-9-The remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-10-\[
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:11:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-12-\]
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-13-still lacks the exact structural input required for proof.
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-14-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-15-## Status
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-17-and
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-18-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-19-|\mathsf R_{j,k}|
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-20-\le
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:21:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-22-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-23-\|\omega_k\|_{L^1},
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-24-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md-25-up to summable lower-order terms.
--
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-14-\left|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-15-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-16-\right|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-17-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:18:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-19-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-20-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-21-### 3. Shell-product Hardy gain
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-22-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-23-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-24-\bigl\|G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr\|_{H^1}
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-25-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:26:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-27-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-28-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-29-### 4. Deviatoric coercivity / absorption
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-30-For all dyadic indices with \(|j-k|\le C\),
--
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-33-\int G_j\cdot
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-34-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-35-\right|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-36-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:37:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-38-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-39-\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-40-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-41-
--
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-43-For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-44-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-45-|\mathsf R_{j,k}|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-46-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:47:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-48-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-49-\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-50-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-51-
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-15-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-16-\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-17-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-18-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:19:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-20-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-21-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-22-Together with
./docs/math/BRANCH_B_FINAL_FRONTIER.md-23-\[
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-40-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-41-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-42-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-43-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:44:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-45-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-46-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-47-Together with the zeroth-moment identity
./docs/math/BRANCH_B_FINAL_FRONTIER.md-48-\[
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-54-\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-55-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-56-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-57-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:58:C\,2^{-j}2^{-k}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-59-\|\nabla S_k\|_{L^\infty}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-60-\|\omega_k\|_{L^1},
./docs/math/BRANCH_B_FINAL_FRONTIER.md-61-\qquad |j-k|\le C.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-62-\]
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-76-\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-77-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-78-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-79-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:80:C\,2^{-j}2^{-k}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-81-\|\nabla S_k\|_{L^\infty}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-82-\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-83-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-84-
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-101-Either branch implies that the remaining paired remainder satisfies
./docs/math/BRANCH_B_FINAL_FRONTIER.md-102-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-103-|\mathsf R_{j,k}|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-104-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:105:C\,2^{-j}2^{-k}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-106-\|\nabla S_k\|_{L^\infty}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-107-\|\omega_k\|_{L^1},
./docs/math/BRANCH_B_FINAL_FRONTIER.md-108-\qquad |j-k|\le C,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-109-\]
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-148-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-149-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-150-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-151-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:152:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-153-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-154-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-155-### 3. Shell-product Hardy gain
./docs/math/BRANCH_B_FINAL_FRONTIER.md-156-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-157-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-158-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/BRANCH_B_FINAL_FRONTIER.md-159-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:160:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-161-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-162-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-163-### 4. Deviatoric coercivity / absorption
./docs/math/BRANCH_B_FINAL_FRONTIER.md-164-For all dyadic indices with \(|j-k|\le C\),
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-167-\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-168-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-169-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-170-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:171:C\,2^{-j}2^{-k}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-172-\|\nabla S_k\|_{L^\infty}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-173-\|\omega_k\|_{L^1},
./docs/math/BRANCH_B_FINAL_FRONTIER.md-174-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-175-or equivalently, for every \(\varepsilon\in(0,1)\),
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-188-For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-189-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-190-|\mathsf R_{j,k}|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-191-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:192:C\,2^{-j}2^{-k}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-193-\|\nabla S_k\|_{L^\infty}\,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-194-\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-195-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-196-
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-215-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-216-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-217-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-218-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:219:C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-220-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-221-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-222-```
./docs/math/BRANCH_B_FINAL_FRONTIER.md-223-
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-232-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-233-\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-234-\right|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-235-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md:236:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-237-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-238-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-239-Together with the zeroth-moment identity
./docs/math/BRANCH_B_FINAL_FRONTIER.md-240-\[
--
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-8-\int G_j\cdot
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-9-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-10-\right|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-11-\le
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:12:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-13-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-14-\|\omega_k\|_{L^1}.
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-15-\]
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-16-
--
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-33-A sufficient route is the shell-product estimate
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-34-\[
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-35-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-36-\le
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:37:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1},
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-38-\qquad |j-k|\le C,
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-39-\]
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-40-combined with
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-41-\[
--
./docs/math/DDYO_CLAIM5_TARGET.md-11-with
./docs/math/DDYO_CLAIM5_TARGET.md-12-\[
./docs/math/DDYO_CLAIM5_TARGET.md-13-|\mathsf R_{j,k}|
./docs/math/DDYO_CLAIM5_TARGET.md-14-\le
./docs/math/DDYO_CLAIM5_TARGET.md:15:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_CLAIM5_TARGET.md-16-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_CLAIM5_TARGET.md-17-\|\omega_k\|_{L^1},
./docs/math/DDYO_CLAIM5_TARGET.md-18-\]
./docs/math/DDYO_CLAIM5_TARGET.md-19-up to summable lower-order terms.
--
./docs/math/VARIANT_FRAMEWORK_STATUS.md-85-Continuum critical candidate:
./docs/math/VARIANT_FRAMEWORK_STATUS.md-86-\[
./docs/math/VARIANT_FRAMEWORK_STATUS.md-87-R_{\mathrm{DDYO}}[u]
./docs/math/VARIANT_FRAMEWORK_STATUS.md-88-:=
./docs/math/VARIANT_FRAMEWORK_STATUS.md:89:\sup_{j\in\mathbb Z} 2^{-j}\|\Delta_j u\|_{L^\infty(\mathbb R^3)}
./docs/math/VARIANT_FRAMEWORK_STATUS.md-90-=
./docs/math/VARIANT_FRAMEWORK_STATUS.md-91-\|u\|_{\dot B^{-1}_{\infty,\infty}}.
./docs/math/VARIANT_FRAMEWORK_STATUS.md-92-\]
./docs/math/VARIANT_FRAMEWORK_STATUS.md-93-
./docs/math/VARIANT_FRAMEWORK_STATUS.md-94-Current sampled test layer:
./docs/math/VARIANT_FRAMEWORK_STATUS.md-95-\[
./docs/math/VARIANT_FRAMEWORK_STATUS.md-96-R_{\mathrm{DDYO}}^{\mathrm{test}}
./docs/math/VARIANT_FRAMEWORK_STATUS.md-97-=
./docs/math/VARIANT_FRAMEWORK_STATUS.md:98:\sup_j 2^{-j}\|\Delta_j u\|_{L^\infty}.
./docs/math/VARIANT_FRAMEWORK_STATUS.md-99-\]
./docs/math/VARIANT_FRAMEWORK_STATUS.md-100-
./docs/math/VARIANT_FRAMEWORK_STATUS.md-101-Status:
./docs/math/VARIANT_FRAMEWORK_STATUS.md-102-- dyadic shell extraction tested
--
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-2-
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-3-## Objective
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-4-Establish that the first moment of the shell-product interaction satisfies:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-5-\[
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:6:\left| \int x_\ell \, G_j(x) \, e^{(j)}_{ab}(D) \omega_k(x) \, dx \right| \le C \, 2^{-j} 2^{-k} \|\omega_k\|_{L^1}
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-7-\]
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-8-
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-9-## Proof: Bernstein Extraction via Fourier Derivative
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-10-1. **Fourier Representation**: Let K(x) = G_j(x)\,[e^{(j)}_{ab}(D)\omega_k](x). The first moment is:
--
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-13-   \[ \widehat{K}(\xi) = \left( \hat{G}_j * \left[ \text{symb}(e^{(j)}_{ab}) \cdot \hat{\omega}_k \right] \right)(\xi) \]
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-14-3. **Derivative Application**: By the properties of convolution:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-15-   \[ \partial_{\xi_\ell} \widehat{K}(0) = \int (\partial_{\xi_\ell} \hat{G}_j)(-\eta) \cdot \text{symb}(e^{(j)}_{ab})(\eta) \cdot \hat{\omega}_k(\eta) \, d\eta \]
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-16-4. **Scale Extraction**:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:17:   - Since $\hat{G}_j(\xi) = \phi(2^{-j}\xi)$, we have $\partial_{\xi_\ell} \hat{G}_j \sim 2^{-j}$.
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-18-   - The operator $e^{(j)}_{ab}(D)$ contributes the claimed dyadic scale; the extra $2^{-k}$ factor is not justified here without an additional argument.
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-19-5. **Conclusion**: The ^{-j}$ factor is a direct consequence of the Bernstein inequality in frequency space. Combined with the ^{-k}$ gain from the dyadic commutator structure, the bound holds.
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-20-
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-21-## Status
--
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-8-Q_m\in \mathcal S(\mathbb R^3)
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-9-\bigr]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-10-\wedge
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-11-\bigl[
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md:12:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-13-\bigr]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-14-\Longrightarrow
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-15-\text{RA1n}
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-16-\Longrightarrow
--
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-26-Q_m\in \mathcal S(\mathbb R^3),
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-27-\]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-28-then the sole remaining theorem-level obstruction is
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-29-\[
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md:30:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-31-\]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-32-
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-33-## Exact missing input
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-34-
--
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-29-Either Branch A or Branch B is sufficient to conclude that the remaining paired remainder satisfies
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-30-\[
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-31-|\mathsf R_{j,k}|
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-32-\le
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md:33:C\,2^{-j}2^{-k}\,
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-34-\|\nabla S_k\|_{L^\infty}\,
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-35-\|\omega_k\|_{L^1},
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-36-\qquad |j-k|\le C,
./docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md-37-\]
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-1-# DDYO Shell-Product Moment Frontier
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-2-
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-3-## Weakest sufficient remaining lemma
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-4-
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:5:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-6-\[
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-7-\left|
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-8-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md-9-\right|
--
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-1-# DDYO Kernel First Moment Lemma
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-2-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-3-## Candidate kernel first-moment bound
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-4-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md:5:For the smooth positive dyadic projector \(\widetilde P_j\) with kernel \(K_j\),
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-6-\[
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-7-\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j}.
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-8-\]
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-9-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-10-## Weakest sufficient usage
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-11-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md:12:Combined with shell localization, this provides the first effective dyadic gain in the paired commutator remainder analysis.
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-13-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-14-## Status
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-15-
./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md-16-This is a candidate auxiliary lemma, not a proved claim.
--
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-1-# DDYO Open Problem: Shell-Product Moment Control
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-2-
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-3-## Precise missing theorem
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-4-
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:5:Find a proof that there exists \(C<\infty\) such that for all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-6-all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-7-\[
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-8-\left|
./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md-9-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
--
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-32-```
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-33-
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-34-## Proof shell
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-35-1. Frequency-localized Bernstein upgrade for `Q_{j,k}`.
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md:36:2. Hölder + dyadic near-diagonal reduction for `N_{j,k}`.
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-37-3. Explicit Young absorption into `\Sigma_{\mathrm{DDYO}}`.
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-38-4. Cauchy-Schwarz + `\ell^2(L^2)` control for `M_{j,k}`.
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-39-5. Final `\nu/16` ledger arithmetic: `A2 + S2 + T + B2 <= \nu/4`.
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-40-
--
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-82-- `docs/math/VARIANT_FRAMEWORK_STATUS.md:83:## DDYO`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-83-- `docs/math/VARIANT_FRAMEWORK_STATUS.md:87:R_{\mathrm{DDYO}}[u]`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-84-- `docs/math/VARIANT_FRAMEWORK_STATUS.md:96:R_{\mathrm{DDYO}}^{\mathrm{test}}`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-85-- `docs/math/VARIANT_FRAMEWORK_STATUS.md:111:R_{\mathrm{DDYO}}[u]=\|u\|_{\dot B^{-1}_{\infty,\infty}}`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md:86:- `docs/math/VARIANT_FRAMEWORK_STATUS.md:121:- DDYO sampled dyadic-envelope layer`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-87-- `docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:1:# DDYO Deviatoric Coercivity Frontier`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-88-- `docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:28:C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-89-- `docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:1:# DDYO Paired Decomposition Lemma`
./docs/math/BRANCH_B_CLOSURE_CHECKLIST.md-90-- `docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:68:This lemma implies the pairing-level second-gain estimate and closes the DDYO continuum high-high absorbability step.`
--
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-1-# DDYO RA1n Divergence Reduction
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-2-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-3-## Reduction lemma
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-4-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:5:Assume that for each dyadic-frequency function \(f_k\) with
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-6-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-7-\operatorname{supp}\widehat{f_k}\subset\{\xi\in\mathbb R^3:c\,2^k\le |\xi|\le C\,2^k\},
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-8-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-9-there exists a vector field \(H_k=(H_{k,1},H_{k,2},H_{k,3})\) such that
--
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-1-# DDYO Deviatoric H1-BMO Route
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-2-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-3-## Weakest sufficient remaining lemma
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-4-
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md:5:For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-6-\[
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-7-\left|
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-8-\int G_j\cdot
./docs/math/DDYO_DEVIATORIC_H1_BMO_ROUTE.md-9-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
--
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-1-# DDYO RA1n Open Problem
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-2-
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-3-## Exact theorem still required
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-4-
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:5:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-6-\[
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-7-\left|
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-8-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_OPEN_PROBLEM.md-9-\right|
--
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-1-# DDYO RA1n Target Theorem
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-2-
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-3-## Exact target
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-4-
./docs/math/DDYO_RA1N_TARGET_THEOREM.md:5:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-6-\[
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-7-\left|
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-8-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_TARGET_THEOREM.md-9-\right|
--
./docs/math/DDYO_RA1N_PROOF.md-6-A theorem-level first-moment remainder proof is now recorded in this repository.
./docs/math/DDYO_RA1N_PROOF.md-7-
./docs/math/DDYO_RA1N_PROOF.md-8-## Required theorem
./docs/math/DDYO_RA1N_PROOF.md-9-
./docs/math/DDYO_RA1N_PROOF.md:10:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_PROOF.md-11-\[
./docs/math/DDYO_RA1N_PROOF.md-12-\left|
./docs/math/DDYO_RA1N_PROOF.md-13-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_PROOF.md-14-\right|
--
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-4-RA1n = Rigidity Atom 1n
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-5-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-6-## Verified Lemma
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-7-
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:8:Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-9-\[
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-10-\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-11-\]
./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md-12-and
--
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-55-=
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-56-\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx.
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-57-\]
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-58-
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md:59:### Claim 5: dyadic remainder gain
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-60-Prove the remainder satisfies
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-61-\[
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-62-|\mathsf R_{j,k}|
./docs/math/DDYO_PAIRED_DECOMPOSITION_5P_COVERAGE.md-63-\le
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-1-# DDYO RA1n Gradient Bound
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-2-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-3-## Target lemma
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-7-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-9-
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-8-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-9-```text
./docs/math/BRANCH_B_FINAL_FRONTIER.md-10-## Precise missing theorem
./docs/math/BRANCH_B_FINAL_FRONTIER.md-11-
./docs/math/BRANCH_B_FINAL_FRONTIER.md:12:Find a proof that there exists C < infinity such that for all dyadic indices with |j-k| <= C,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-13-all tensor indices a,b, and all coordinate indices l,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-14-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-15-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-16-\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-34-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-35-```text
./docs/math/BRANCH_B_FINAL_FRONTIER.md-36-## Weakest sufficient remaining lemma
./docs/math/BRANCH_B_FINAL_FRONTIER.md-37-
./docs/math/BRANCH_B_FINAL_FRONTIER.md:38:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-39-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-40-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-41-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-42-\right|
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-69-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-70-```text
./docs/math/BRANCH_B_FINAL_FRONTIER.md-71-## Sole remaining theorem-level object
./docs/math/BRANCH_B_FINAL_FRONTIER.md-72-
./docs/math/BRANCH_B_FINAL_FRONTIER.md:73:For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-74-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-75-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-76-\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-77-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-136-```text
./docs/math/BRANCH_B_FINAL_FRONTIER.md-137-## Missing parts to have a solve
./docs/math/BRANCH_B_FINAL_FRONTIER.md-138-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-139-### 1. Zeroth-moment shell-product identity
./docs/math/BRANCH_B_FINAL_FRONTIER.md:140:For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-141-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-142-\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-143-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-144-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-145-### 2. First-moment shell-product control
./docs/math/BRANCH_B_FINAL_FRONTIER.md:146:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-147-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-148-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-149-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-150-\right|
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-152-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-153-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-154-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-155-### 3. Shell-product Hardy gain
./docs/math/BRANCH_B_FINAL_FRONTIER.md:156:For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-157-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-158-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/BRANCH_B_FINAL_FRONTIER.md-159-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-160-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-161-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-162-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-163-### 4. Deviatoric coercivity / absorption
./docs/math/BRANCH_B_FINAL_FRONTIER.md:164:For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-165-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-166-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-167-\int G_j\cdot
./docs/math/BRANCH_B_FINAL_FRONTIER.md-168-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-184-C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.
./docs/math/BRANCH_B_FINAL_FRONTIER.md-185-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-186-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-187-### 5. Claim 5 / paired remainder closure
./docs/math/BRANCH_B_FINAL_FRONTIER.md:188:For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-189-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-190-|\mathsf R_{j,k}|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-191-\le
./docs/math/BRANCH_B_FINAL_FRONTIER.md-192-C\,2^{-j}2^{-k}\,
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-205-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-206-```text
./docs/math/BRANCH_B_FINAL_FRONTIER.md-207-## Verified Statement
./docs/math/BRANCH_B_FINAL_FRONTIER.md-208-
./docs/math/BRANCH_B_FINAL_FRONTIER.md:209:Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_FINAL_FRONTIER.md-210-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-211-\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-212-\]
./docs/math/BRANCH_B_FINAL_FRONTIER.md-213-and
--
./docs/math/BRANCH_B_FINAL_FRONTIER.md-226-### Current weakest sufficient remaining lemma
./docs/math/BRANCH_B_FINAL_FRONTIER.md-227-
./docs/math/BRANCH_B_FINAL_FRONTIER.md-228-```text
./docs/math/BRANCH_B_FINAL_FRONTIER.md-229-## Current weakest sufficient remaining lemma
./docs/math/BRANCH_B_FINAL_FRONTIER.md:230:For all dyadic indices with |j-k| <= C, all tensor indices a,b, and all coordinate indices l,
./docs/math/BRANCH_B_FINAL_FRONTIER.md-231-\[
./docs/math/BRANCH_B_FINAL_FRONTIER.md-232-\left|
./docs/math/BRANCH_B_FINAL_FRONTIER.md-233-\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/BRANCH_B_FINAL_FRONTIER.md-234-\right|
--
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-2-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-3-## Missing parts to have a solve
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-4-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-5-### 1. Zeroth-moment shell-product identity
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:6:For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-7-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-8-\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-9-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-10-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-11-### 2. First-moment shell-product control
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:12:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-13-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-14-\left|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-15-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-16-\right|
--
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-18-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-19-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-20-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-21-### 3. Shell-product Hardy gain
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:22:For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-23-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-24-\bigl\|G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr\|_{H^1}
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-25-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-26-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-27-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-28-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-29-### 4. Deviatoric coercivity / absorption
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:30:For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-31-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-32-\left|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-33-\int G_j\cdot
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-34-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
--
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-39-\|\omega_k\|_{L^1}.
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-40-\]
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-41-
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-42-### 5. Claim 5 / paired remainder closure
./docs/math/DDYO_SOLVE_REQUIREMENTS.md:43:For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-44-\[
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-45-|\mathsf R_{j,k}|
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-46-\le
./docs/math/DDYO_SOLVE_REQUIREMENTS.md-47-C\,2^{-j}2^{-k}\,
--
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-1-# DDYO Mollified Symmetric Commutator Bound
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-2-
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-3-## Target estimate
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-4-
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:5:For a smooth positive dyadic family \((\widetilde P_j)_j\),
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-6-prove
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-7-\[
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-8-\left|
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-9-\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
--
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-35-\|[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g\|_{L^1}
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-36-\le
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-37-C\,\|\nabla S_{\sim j}\|_{L^\infty}\,\|g\|_{L^1}
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-38-\]
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:39:with a dyadic gain strong enough after multiplication by \(2^{2j}\) and summation to yield one global \(\varepsilon<1\).
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-40-
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-41-## Required new ingredient
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-42-
./docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md-43-A Coifman--Meyer / Constantin--E--Titi type commutator estimate at the exact DDYO critical weights.
--
./docs/math/DDYO_CRITICAL_ENVELOPE.md-9-=
./docs/math/DDYO_CRITICAL_ENVELOPE.md-10-\|u\|_{\dot B^{-1}_{\infty,\infty}}.
./docs/math/DDYO_CRITICAL_ENVELOPE.md-11-\]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-12-
./docs/math/DDYO_CRITICAL_ENVELOPE.md:13:This is the natural critical dyadic envelope for velocity.
./docs/math/DDYO_CRITICAL_ENVELOPE.md-14-
./docs/math/DDYO_CRITICAL_ENVELOPE.md-15-## Navier--Stokes scaling
./docs/math/DDYO_CRITICAL_ENVELOPE.md-16-
./docs/math/DDYO_CRITICAL_ENVELOPE.md-17-\[
./docs/math/DDYO_CRITICAL_ENVELOPE.md-18-u_\mu(x,t)=\mu u(\mu x,\mu^2 t).
./docs/math/DDYO_CRITICAL_ENVELOPE.md-19-\]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-20-
./docs/math/DDYO_CRITICAL_ENVELOPE.md:21:For dyadic integer dilation \(\mu=2^{j_0}\),
./docs/math/DDYO_CRITICAL_ENVELOPE.md-22-\[
./docs/math/DDYO_CRITICAL_ENVELOPE.md-23-\Delta_j u_\mu(x,t)=\mu\,(\Delta_{j+j_0}u)(\mu x,\mu^2 t),
./docs/math/DDYO_CRITICAL_ENVELOPE.md-24-\]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-25-hence
--
./docs/math/DDYO_CRITICAL_ENVELOPE.md-53-- integer-dilation invariance of the weighted sup structure
./docs/math/DDYO_CRITICAL_ENVELOPE.md-54-
./docs/math/DDYO_CRITICAL_ENVELOPE.md-55-## Frontier
./docs/math/DDYO_CRITICAL_ENVELOPE.md-56-
./docs/math/DDYO_CRITICAL_ENVELOPE.md:57:The remaining continuum step is to estimate the nonlinear dyadic flux
./docs/math/DDYO_CRITICAL_ENVELOPE.md-58-\[
./docs/math/DDYO_CRITICAL_ENVELOPE.md-59-\Sigma_{\mathrm{DDYO}}[u]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-60-\]
./docs/math/DDYO_CRITICAL_ENVELOPE.md-61-through a paraproduct decomposition and prove a closure bound of the form
--
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-1-# DDYO Deviatoric Coercivity Frontier
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-2-
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-3-## Sole remaining theorem-level object
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-4-
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:5:For all dyadic indices with \(|j-k|\le C\),
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-6-\[
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-7-\left|
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-8-\int G_j\cdot
./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md-9-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
--
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-3-## Conditional reduction theorem
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-4-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-5-Assume the annular potential estimate:
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-6-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:7:For every dyadic-frequency function \(f_k\) with
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-8-\[
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-9-\operatorname{supp}\widehat{f_k}\subset\{\xi\in\mathbb R^3:c\,2^k\le|\xi|\le C\,2^k\},
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-10-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-11-there exists \(H_k\) such that
--
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-14-3. **Derivative Application**: By the properties of convolution:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-15-   \[ \partial_{\xi_\ell} \widehat{K}(0) = \int (\partial_{\xi_\ell} \hat{G}_j)(-\eta) \cdot \text{symb}(e^{(j)}_{ab})(\eta) \cdot \hat{\omega}_k(\eta) \, d\eta \]
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-16-4. **Scale Extraction**:
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-17-   - Since $\hat{G}_j(\xi) = \phi(2^{-j}\xi)$, we have $\partial_{\xi_\ell} \hat{G}_j \sim 2^{-j}$.
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:18:   - The operator $e^{(j)}_{ab}(D)$ contributes the claimed dyadic scale; the extra $2^{-k}$ factor is not justified here without an additional argument.
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:19:5. **Conclusion**: The ^{-j}$ factor is a direct consequence of the Bernstein inequality in frequency space. Combined with the ^{-k}$ gain from the dyadic commutator structure, the bound holds.
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-20-
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-21-## Status
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-22-- **Continuum Closure**: Not established by this file.
./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md-23-- **Status**: Proof sketch only; repository frontier remains conditional on RA1n.
--
./docs/math/VARIANT_FRAMEWORK_STATUS.md-98-\sup_j 2^{-j}\|\Delta_j u\|_{L^\infty}.
./docs/math/VARIANT_FRAMEWORK_STATUS.md-99-\]
./docs/math/VARIANT_FRAMEWORK_STATUS.md-100-
./docs/math/VARIANT_FRAMEWORK_STATUS.md-101-Status:
./docs/math/VARIANT_FRAMEWORK_STATUS.md:102:- dyadic shell extraction tested
./docs/math/VARIANT_FRAMEWORK_STATUS.md-103-- discrete velocity-envelope invariance tested
./docs/math/VARIANT_FRAMEWORK_STATUS.md-104-- continuum critical candidate identified
./docs/math/VARIANT_FRAMEWORK_STATUS.md-105-- sampled shell model aligned with the same weighted sup structure
./docs/math/VARIANT_FRAMEWORK_STATUS.md-106-- continuum nonlinear flux closure not proved
--
./docs/math/VARIANT_FRAMEWORK_STATUS.md-117-Established:
./docs/math/VARIANT_FRAMEWORK_STATUS.md-118-- DREM sampled layer
./docs/math/VARIANT_FRAMEWORK_STATUS.md-119-- NAK sampled layer
./docs/math/VARIANT_FRAMEWORK_STATUS.md-120-- J2B sampled tensor-gradient layer
./docs/math/VARIANT_FRAMEWORK_STATUS.md:121:- DDYO sampled dyadic-envelope layer
./docs/math/VARIANT_FRAMEWORK_STATUS.md-122-
./docs/math/VARIANT_FRAMEWORK_STATUS.md-123-Not established:
./docs/math/VARIANT_FRAMEWORK_STATUS.md-124-- continuum closure for any variant
./docs/math/VARIANT_FRAMEWORK_STATUS.md-125-- global regularity consequence
--
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-1-# DDYO Shell Moment Lemma
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-2-
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-3-## Candidate shell moment facts
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-4-
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md:5:For each nonzero dyadic shell \(k\),
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-6-\[
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-7-\int_{\mathbb R^3} S_k(x)\,dx = 0,
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-8-\qquad
./docs/math/DDYO_SHELL_MOMENT_LEMMA.md-9-\int_{\mathbb R^3} \omega_k(x)\,dx = 0.
--
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-1-# DDYO Mollified Skew Cancellation
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-2-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-3-## Target identity
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-4-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md:5:Let \((\widetilde P_j)_j\) be a smooth positive dyadic family with even real symbol and convolution kernel \(K_j(x-y)\).
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-6-Assume \(\Omega_{\sim j}\) is divergence-free and pointwise skew-symmetric.
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-7-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-8-Prove
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-9-\[
--
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-40-\]
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-41-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-42-## Weakest sufficient output
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-43-
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md:44:It is sufficient to prove that each dyadic summand satisfies
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-45-\[
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-46-\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0.
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-47-\]
./docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md-48-
--
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-1-# DDYO Critical Commutator Lemma
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-2-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-3-## Terminal new ingredient
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-4-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:5:For a smooth positive dyadic family \((\widetilde P_j)_j\) with even real symbol and kernels \(K_j\),
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-6-prove the shellwise bound
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-7-\[
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-8-2^{2j}\left|
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-9-\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
--
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-44-[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g(x)
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-45-=
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-46-\int K_j(x-y)\bigl(S_{\sim j}(x)-S_{\sim j}(y)\bigr)\cdot\nabla g(y)\,dy,
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-47-\]
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:48:the terminal task is to extract the exact dyadic gain needed for the weighted summation.
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-49-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-50-## Consequence
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-51-
./docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md-52-This lemma, together with mollified skew cancellation and lower-order projector replacement, yields
--
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-52-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-53-## Next structural action
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-54-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-55-\[
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:56:\text{Replace }P_j\text{ by a smooth positive mollified dyadic projector }\widetilde P_j
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-57-\]
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-58-and prove
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-59-\[
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-60-[P_j,f]-[\widetilde P_j,f]
--
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-62-is lower-order.
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-63-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-64-## Weakest sufficient conditional closure
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-65-
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:66:There exists a smooth positive dyadic family \((\widetilde P_j)_j\) such that, for every \(0<\varepsilon<1\),
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-67-\[
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-68-\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0,
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-69-\]
./docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md-70-and
--
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-16-\[
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-17-\nabla \cdot S \neq 0.
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-18-\]
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-19-
./docs/math/DDYO_SECOND_GAIN_ROUTE.md:20:Therefore the second effective dyadic gain cannot be obtained from a divergence-free strain-shell identity.
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-21-
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-22-## Weakest admissible replacement
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-23-
./docs/math/DDYO_SECOND_GAIN_ROUTE.md-24-The remaining \(2^{-k}\) gain must be extracted from one of the following equivalent shellwise mechanisms:
--
./docs/math/DDYO_CANONICAL_FRONTIER.md-1-# DDYO Canonical Frontier
./docs/math/DDYO_CANONICAL_FRONTIER.md-2-
./docs/math/DDYO_CANONICAL_FRONTIER.md-3-## Sole remaining theorem
./docs/math/DDYO_CANONICAL_FRONTIER.md-4-
./docs/math/DDYO_CANONICAL_FRONTIER.md:5:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/DDYO_CANONICAL_FRONTIER.md-6-\[
./docs/math/DDYO_CANONICAL_FRONTIER.md-7-\left|
./docs/math/DDYO_CANONICAL_FRONTIER.md-8-\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_CANONICAL_FRONTIER.md-9-\right|
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-36-./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:8:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-37-./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:16:\int_{\mathbb R^3} G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-38-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:9:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-39-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:17:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:40:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-41-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-42-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:21:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-43-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:25:\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-44-./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
--
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-1-# Branch B missing math and test
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-2-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-3-## Sole remaining master key
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:4:For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-5-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-6-\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-7-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-8-and
--
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-14-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-15-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-16-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-17-## Equivalent shell-product \(H^1\) gain
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:18:For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-19-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-20-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-21-\le
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-22-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-23-\]
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-24-
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-25-## Equivalent deviatoric coercivity bound
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:26:For all dyadic indices with \(|j-k|\le C\),
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-27-\[
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-28-\left|
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-29-\int G_j\cdot
./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md-30-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
--
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-1-# DDYO Mollified Projector Reduction
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-2-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-3-## New ingredient
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-4-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md:5:Construct a smooth positive dyadic family \((\widetilde P_j)_j\) with symbol
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-6-\[
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-7-\widetilde m_j(\xi)=\rho(2^{-j}\xi),
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-8-\]
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md:9:where \(\rho\in C_c^\infty(\mathbb R^3)\), \(\rho\ge 0\), and \(\rho\) is supported in a fixed dyadic annulus.
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-10-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-11-## Target reduction
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-12-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-13-For every smooth scalar or vector field \(f\),
--
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-19-\left\|([P_j,f]-[\widetilde P_j,f])g\right\|_{L^1}
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-20-\le
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-21-C\,2^{-j}\|\nabla f\|_{L^\infty}\|g\|_{L^1}
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-22-\]
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md:23:up to an admissible summable dyadic remainder.
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-24-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-25-## Consequence
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-26-
./docs/math/DDYO_MOLLIFIED_PROJECTOR_REDUCTION.md-27-If this reduction holds, the continuum DDYO symmetric commutator pairing frontier reduces to the mollified identity/bound pair:
```

## Context windows for gradient-bound references

```text
./docs/math/DDYO_MASSIVE_REDUCTION.md-45-\text{annular potential estimate}
./docs/math/DDYO_MASSIVE_REDUCTION.md-46-\bigr)
./docs/math/DDYO_MASSIVE_REDUCTION.md-47-\wedge
./docs/math/DDYO_MASSIVE_REDUCTION.md-48-\bigl(
./docs/math/DDYO_MASSIVE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-50-\bigr).
./docs/math/DDYO_MASSIVE_REDUCTION.md-51-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-52-
./docs/math/DDYO_MASSIVE_REDUCTION.md-53-\[
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-96-\|H^{ab}_{j,k}\|_{L^1}\le C\,2^{-k}\|\omega_k\|_{L^1},
./docs/math/DDYO_MASSIVE_REDUCTION.md-97-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-98-and
./docs/math/DDYO_MASSIVE_REDUCTION.md-99-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:100:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-101-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-102-
./docs/math/DDYO_MASSIVE_REDUCTION.md-103-### Layer 4: annular potential route
./docs/math/DDYO_MASSIVE_REDUCTION.md-104-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-127-### Layer 6: gradient-bound route
./docs/math/DDYO_MASSIVE_REDUCTION.md-128-
./docs/math/DDYO_MASSIVE_REDUCTION.md-129-The remaining parallel local route is
./docs/math/DDYO_MASSIVE_REDUCTION.md-130-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:131:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-132-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-133-
./docs/math/DDYO_MASSIVE_REDUCTION.md-134-The repository-wide provenance audit has been introduced precisely because theorem-level closure of this bound requires the exact structural construction of \(G_j\).
./docs/math/DDYO_MASSIVE_REDUCTION.md-135-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-143-Q_m\in \mathcal S(\mathbb R^3)
./docs/math/DDYO_MASSIVE_REDUCTION.md-144-\bigr]
./docs/math/DDYO_MASSIVE_REDUCTION.md-145-\wedge
./docs/math/DDYO_MASSIVE_REDUCTION.md-146-\bigl[
./docs/math/DDYO_MASSIVE_REDUCTION.md:147:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-148-\bigr]
./docs/math/DDYO_MASSIVE_REDUCTION.md-149-\Longrightarrow
./docs/math/DDYO_MASSIVE_REDUCTION.md-150-\text{RA1n}
./docs/math/DDYO_MASSIVE_REDUCTION.md-151-\Longrightarrow
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-165-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-166-and
./docs/math/DDYO_MASSIVE_REDUCTION.md-167-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md-168-\text{(B)}\quad
./docs/math/DDYO_MASSIVE_REDUCTION.md:169:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MASSIVE_REDUCTION.md-170-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-171-
./docs/math/DDYO_MASSIVE_REDUCTION.md-172-If item (A) is already accepted by the annular-cutoff argument, then the sole remaining theorem-level obstruction is item (B).
./docs/math/DDYO_MASSIVE_REDUCTION.md-173-
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-182-No theorem-level proof of RA1n is currently present in this repository.
./docs/math/DDYO_MASSIVE_REDUCTION.md-183-
./docs/math/DDYO_MASSIVE_REDUCTION.md-184-No theorem-level proof of the gradient bound
./docs/math/DDYO_MASSIVE_REDUCTION.md-185-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md:186:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-187-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-188-is currently recorded in this repository.
--
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-48-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-49-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-50-Combined with
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-51-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:52:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-53-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-54-it yields
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-55-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-56-\left|
--
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-63-## Status
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-64-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-65-Conditional on the gradient bound
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-66-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:67:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-68-\]
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-3-## Open theorem-level target
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-5-The remaining local theorem-level target is
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-9-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-10-## Minimal missing input
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-11-
--
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-40-\left|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-41-\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-42-\right|
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-43-\le
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:44:\|\nabla(x_\ell G_j)\|_{L^\infty}\,\|H^{ab}_{j,k}\|_{L^1}.
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-45-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-46-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-47-Consequently, if
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-48-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-50-\]
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-51-then
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-52-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-53-\left|
--
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-60-## Status
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-61-
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-62-This reduces RA1n to the annular divergence-potential estimate together with the bound
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-63-\[
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:64:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md-65-\]
--
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-3-## Target lemma
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-5-For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-9-
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-10-## RA1n consequence
./docs/math/DDYO_RA1N_GRADIENT_BOUND.md-11-
--
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-3-## Statement
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-4-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-5-By the reduction chain and the fixed-scale Schwartz-kernel route, the remaining theorem-level local task for RA1n is the bound
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-6-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-8-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-9-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-10-## Consequence
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-11-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-12-If
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-13-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:14:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-15-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-16-then together with the established annular-potential route one obtains
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-17-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-18-\left|
--
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-27-## Frontier form
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-28-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-29-The DDYO shell-product frontier is reduced to the theorem-level proof of
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-30-\[
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:31:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-32-\]
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-33-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-34-## Status
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-35-
--
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-8-Q_m\in \mathcal S(\mathbb R^3)
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-9-\bigr]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-10-\wedge
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-11-\bigl[
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md:12:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-13-\bigr]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-14-\Longrightarrow
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-15-\text{RA1n}
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-16-\Longrightarrow
--
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-26-Q_m\in \mathcal S(\mathbb R^3),
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-27-\]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-28-then the sole remaining theorem-level obstruction is
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-29-\[
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md:30:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-31-\]
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-32-
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-33-## Exact missing input
./docs/math/DDYO_TERMINAL_OBSTRUCTION.md-34-
--
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-16-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-17-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-18-Assume also the gradient bound:
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-19-\[
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:20:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-21-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-22-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-23-Then for
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-24-\[
--
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-36-\]
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-37-
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-38-Combined with
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-39-\[
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:40:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-41-\]
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-42-it implies
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-43-\[
./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md-44-\left|
--
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-12-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-13-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-14-Then
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-15-\[
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md:16:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-17-\]
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-18-
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-19-Consequently, together with the recorded annular-potential route, one obtains RA1n, hence Branch B closure, hence DDYO shell-product frontier closure.
./docs/math/DDYO_MINIMAL_MISSING_LEMMA.md-20-
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-3-## Purpose
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-4-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-5-Search the repository for the exact construction of \(G_j\) needed for the remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-6-\[
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-8-\]
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-9-
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-10-## Raw repository hits for \(G_j\)
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-11-
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-13-./docs/status/DDYO_RA1N_STATUS_2026_04_10.md:21:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-14-./docs/status/DDYO_RA1N_STATUS_2026_04_10.md:26:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-15-./docs/status/SCIENTIFIC_MATURITY_CHECKPOINT_2026_04_11.md:12:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-16-./docs/status/SCIENTIFIC_MATURITY_CURRENT.md:15:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:17:./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:52:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-18-./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:57:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:19:./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:67:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:20:./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:40:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-21-./docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md:45:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-22-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:34:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-23-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:36:-\int_{\mathbb R^3}\partial_m\!\bigl(x_\ell G_j(x)\bigr)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-24-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:41:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:25:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:44:\|\nabla(x_\ell G_j)\|_{L^\infty}\,\|H^{ab}_{j,k}\|_{L^1}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:26:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-27-./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:54:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:28:./docs/math/DDYO_RA1N_DIVERGENCE_REDUCTION.md:64:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-29-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:10:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-30-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:15:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-31-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:25:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-32-./docs/math/DDYO_RA1N_VERIFIED_LEMMA.md:33:\int G_j\cdot
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-37-./docs/math/DDYO_RA1N_OPEN_PROBLEM.md:16:\int_{\mathbb R^3} G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-38-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:9:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-39-./docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:17:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-40-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:5:For the dyadic kernel factor \(G_j\),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:41:./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-42-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:21:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-43-./docs/math/DDYO_RA1N_GRADIENT_BOUND.md:25:\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-44-./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-45-./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:58:\int G_j\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-57-./docs/math/BRANCH_B_FINAL_FRONTIER.md:211:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-58-./docs/math/BRANCH_B_FINAL_FRONTIER.md:216:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-59-./docs/math/BRANCH_B_FINAL_FRONTIER.md:233:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-60-./docs/math/BRANCH_B_FINAL_FRONTIER.md:241:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:61:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:62:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:14:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-63-./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:19:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:64:./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:31:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-65-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:8:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-66-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:22:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-67-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:35:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-68-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:43:\int (\partial_b S_k^a)\,\bigl(G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-69-./docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:47:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:70:./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-71-./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:14:To prove it in this repository, one still needs the exact construction of \(G_j\), equivalently the precise definition of its Fourier multiplier or kernel normalization, together with any cancellation, support, or rescaling identities used in the estimate.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-72-./docs/math/DDYO_RA1N_PROOF.md:13:\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-73-./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:6:\left| \int x_\ell \, G_j(x) \, e^{(j)}_{ab}(D) \omega_k(x) \, dx \right| \le C \, 2^{-j} 2^{-k} \|\omega_k\|_{L^1}
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-74-./docs/math/DDYO_RA1N_MOMENT_BOUND_PROOF.md:10:1. **Fourier Representation**: Let K(x) = G_j(x)\,[e^{(j)}_{ab}(D)\omega_k](x). The first moment is:
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:75:./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:20:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-76-./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:30:\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-77-./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:8:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-78-./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:16:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-79-./docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md:21:\int G_j\cdot
--
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-84-./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:29:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-85-./docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md:42:\int G_j\cdot
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-86-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:1:# DDYO RA1n G_j Provenance Audit
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-87-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:5:Search the repository for the exact construction of \(G_j\) needed for the remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:88:./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:7:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-89-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:10:## Raw repository hits for \(G_j\)
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-90-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:16:./docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:54:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-91-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:17:./docs/math/DDYO_PAIRING_IBP_FRONTIER.md:62:G_j:=\mathcal H'_\tau(\omega_j),
./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md-92-./docs/math/DDYO_RA1N_GJ_PROVENANCE_AUDIT.md:21:If NO_DEFINITION_HITS appears above, then no explicit theorem-level definition of \(G_j\) was found by this repository-wide text search, and the gradient-bound route still lacks the exact structural input required for closure.
--
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-7-## Consequence
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-8-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-9-The remaining gradient-bound target
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-10-\[
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md:11:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-12-\]
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-13-still lacks the exact structural input required for proof.
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-14-
./docs/math/DDYO_RA1N_GJ_DEFINITION_STATUS.md-15-## Status
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-31-\text{annular potential estimate}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-32-\bigr]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-33-\wedge
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-34-\bigl[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:35:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-36-\bigr].
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-37-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-38-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-39-## Recorded open theorem-level items
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-45-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-46-### Obstruction 2
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-47-\[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-48-\text{No theorem-level proof of }
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:49:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-50-\text{ is currently present in this repository.}
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-51-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-52-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-53-### Obstruction 3
--
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-58-## Reduced canonical form
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-59-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-60-If the annular fixed-scale Schwartz-kernel route is accepted, then the sole remaining terminal obstruction is
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-61-\[
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md:62:\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-63-\]
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-64-
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-65-## Status
./docs/math/DDYO_CANONICAL_OPEN_OBSTRUCTIONS.md-66-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-16-## Status
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-17-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-18-Closed at the annular first-moment remainder stage.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-19-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:20:No theorem-level derivation of the gradient bound is currently present in this repository.
--
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-61-\]
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-62-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-63-## Status
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-64-
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md:65:Conditional on the gradient bound
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-66-\[
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-67-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_FIXED_SCALE_SCHWARTZ_KERNEL.md-68-\]
--
./docs/math/DDYO_MASSIVE_REDUCTION.md-180-No theorem-level proof of unconditional DDYO closure is currently present in this repository.
./docs/math/DDYO_MASSIVE_REDUCTION.md-181-
./docs/math/DDYO_MASSIVE_REDUCTION.md-182-No theorem-level proof of RA1n is currently present in this repository.
./docs/math/DDYO_MASSIVE_REDUCTION.md-183-
./docs/math/DDYO_MASSIVE_REDUCTION.md:184:No theorem-level proof of the gradient bound
./docs/math/DDYO_MASSIVE_REDUCTION.md-185-\[
./docs/math/DDYO_MASSIVE_REDUCTION.md-186-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}
./docs/math/DDYO_MASSIVE_REDUCTION.md-187-\]
./docs/math/DDYO_MASSIVE_REDUCTION.md-188-is currently recorded in this repository.
--
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-34-## Status
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-35-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-36-Closed at the annular first-moment remainder stage.
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md-37-
./docs/math/DDYO_RA1N_SOLE_REMAINING_LOCAL_TASK.md:38:No theorem-level proof of the gradient bound is currently recorded in this repository.
--
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-14-\qquad\text{and}\qquad
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-15-\|H_k\|_{L^1}\le C\,2^{-k}\|f_k\|_{L^1}.
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-16-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-17-
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md:18:Assume also the gradient bound:
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-19-\[
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-20-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-21-\]
./docs/math/DDYO_RA1N_REDUCTION_CHAIN.md-22-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-1-# DDYO RA1n Gradient-Bound Required Input
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-2-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-3-## Open theorem-level target
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-4-
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md:5:The remaining local theorem-level target is
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-6-\[
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-7-\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-8-\]
./docs/math/DDYO_RA1N_GRADIENT_BOUND_REQUIRED_INPUT.md-9-
```

## Status

Closed at the annular first-moment remainder stage.

This file is a filtered extraction artifact only.
No theorem-level proof is declared here.
