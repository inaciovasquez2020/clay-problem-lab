# Branch B final frontier

## Canonical remaining objects

## docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md

### Precise missing theorem

```text
## Precise missing theorem

Find a proof that there exists C < infinity such that for all dyadic indices with |j-k| <= C,
all tensor indices a,b, and all coordinate indices l,
\[
\left|
\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

Together with
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
\]
this implies the shell-product H^1 gain, the deviatoric coercivity estimate,
Claim 5, and final DDYO continuum closure.

```

## docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md

### Weakest sufficient remaining lemma

```text
## Weakest sufficient remaining lemma

For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\left|
\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

Together with the zeroth-moment identity
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
\]
this is sufficient to recover the shell-product \(H^1\) gain and hence
\[
\left|
\int G_j\cdot
\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\qquad |j-k|\le C.
\]

```

## docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md

### Sole remaining theorem-level object

```text
## Sole remaining theorem-level object

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

```

## docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md

### Frontier object

```text
## Frontier object
Let \(\mathsf T^{(1)}_{j,k}\) denote the post-symmetrized first-order leakage term.

```

### Weakest sufficient consequence

```text
## Weakest sufficient consequence
Either branch implies that the remaining paired remainder satisfies
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\qquad |j-k|\le C,
\]
up to summable lower-order terms.

```

## docs/math/DDYO_PAIRING_IBP_FRONTIER.md

### Weakest sufficient IBP form

```text
## Weakest sufficient IBP form

It is sufficient to prove an identity of the form
\[
\int \mathcal H'_\tau(\omega_j)\cdot S_k\!\cdot\nabla(\widetilde P_j\omega_k)\,dx
=
-\int (\nabla \mathcal H'_\tau(\omega_j)) : (S_k\otimes \widetilde P_j\omega_k)\,dx
-\int \mathcal H'_\tau(\omega_j)\cdot ((\nabla\cdot S_k)\widetilde P_j\omega_k)\,dx,
\]
and then show that the antisymmetric contribution cancels in the full paired commutator, leaving only the symmetric-gradient contribution plus lower-order remainder.

```

## docs/math/DDYO_SOLVE_REQUIREMENTS.md

### Missing parts to have a solve

```text
## Missing parts to have a solve

### 1. Zeroth-moment shell-product identity
For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
\]

### 2. First-moment shell-product control
For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\left|
\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

### 3. Shell-product Hardy gain
For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
\[
\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

### 4. Deviatoric coercivity / absorption
For all dyadic indices with \(|j-k|\le C\),
\[
\left|
\int G_j\cdot
\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\]
or equivalently, for every \(\varepsilon\in(0,1)\),
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

### 5. Claim 5 / paired remainder closure
For all dyadic indices with \(|j-k|\le C\),
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}.
\]

### 6. Final DDYO continuum closure
High-high absorbability closes, hence the DDYO continuum argument closes.

```

## docs/math/DDYO_RA1N_CONDITIONAL.md

### Verified Statement

```text
## Verified Statement

Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
\]
and
\[
\left|
\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

```

## docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md

### Current weakest sufficient remaining lemma

```text
## Current weakest sufficient remaining lemma
For all dyadic indices with |j-k| <= C, all tensor indices a,b, and all coordinate indices l,
\[
\left|
\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

Together with the zeroth-moment identity
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
\]
this is sufficient to recover the shell-product H^1 gain and the target deviatoric coercivity bound.

```

### docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md

```text
L1: # Navier--Stokes Frontier Snapshot (2026-04-10)
L14: - J2B sampled frontier now includes:
L26: ## DDYO commutator frontier
L32: ## DDYO commutator absorbability frontier
L39: ## Exact skew-adjoint reduction frontier
L45: ## Symmetric commutator pairing frontier
L52: ## Truthful frontier
L54: - continuum DDYO high-high absorbability: VERIFIED
L55: - continuum J2B exact residual closure: open
L56: - full continuum solve / global regularity closure: open
```

