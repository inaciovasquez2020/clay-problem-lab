# DDYO G_j Multi-Lead Inspection

## Status

Open.

## Top inspected nongenerated leads

### Lead 1

`docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md`

#### Head

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

#### `G_j` matches

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

#### `Gamma` / kernel matches

```text
NO_GAMMA_KERNEL_MATCHES
```

#### dyadic / RA1n matches

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

### Lead 2

`docs/math/BRANCH_B_FINAL_FRONTIER.md`

#### Head

```text
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
```

#### `G_j` matches

```text
13-all tensor indices a,b, and all coordinate indices l,
14-\[
15-\left|
16:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
17-\right|
18-\le
19-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
--
21-
22-Together with
23-\[
24:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
25-\]
26-this implies the shell-product H^1 gain, the deviatoric coercivity estimate,
27-Claim 5, and final DDYO continuum closure.
--
38-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
39-\[
40-\left|
41:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
42-\right|
43-\le
44-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
--
46-
47-Together with the zeroth-moment identity
48-\[
49:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
50-\]
51-this is sufficient to recover the shell-product \(H^1\) gain and hence
52-\[
53-\left|
54:\int G_j\cdot
55-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
56-\right|
57-\le
--
73-For all dyadic indices with \(|j-k|\le C\),
74-\[
75-\left|
76:\int G_j\cdot
77-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
78-\right|
79-\le
--
139-### 1. Zeroth-moment shell-product identity
140-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
141-\[
142:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
143-\]
144-
145-### 2. First-moment shell-product control
146-For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
147-\[
148-\left|
149:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
150-\right|
151-\le
152-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
--
155-### 3. Shell-product Hardy gain
156-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
157-\[
158:\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
159-\le
160-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
161-\]
--
164-For all dyadic indices with \(|j-k|\le C\),
165-\[
166-\left|
167:\int G_j\cdot
168-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
169-\right|
170-\le
--
175-or equivalently, for every \(\varepsilon\in(0,1)\),
176-\[
177-\left|
178:\int G_j\cdot
179-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
180-\right|
181-\le
--
208-
209-Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
210-\[
211:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
212-\]
213-and
214-\[
215-\left|
216:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
217-\right|
218-\le
219-C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
--
230-For all dyadic indices with |j-k| <= C, all tensor indices a,b, and all coordinate indices l,
231-\[
232-\left|
233:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
234-\right|
235-\le
236-C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
--
238-
239-Together with the zeroth-moment identity
240-\[
241:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
242-\]
243-this is sufficient to recover the shell-product H^1 gain and the target deviatoric coercivity bound.
244-
```

#### `Gamma` / kernel matches

```text
NO_GAMMA_KERNEL_MATCHES
```

#### dyadic / RA1n matches

```text
16-\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
17-\right|
18-\le
19:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
20-\]
21-
22-Together with
--
41-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
42-\right|
43-\le
44:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
45-\]
46-
47-Together with the zeroth-moment identity
--
55-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
56-\right|
57-\le
58:C\,2^{-j}2^{-k}\,
59-\|\nabla S_k\|_{L^\infty}\,
60-\|\omega_k\|_{L^1},
61-\qquad |j-k|\le C.
--
77-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
78-\right|
79-\le
80:C\,2^{-j}2^{-k}\,
81-\|\nabla S_k\|_{L^\infty}\,
82-\|\omega_k\|_{L^1}.
83-\]
--
102-\[
103-|\mathsf R_{j,k}|
104-\le
105:C\,2^{-j}2^{-k}\,
106-\|\nabla S_k\|_{L^\infty}\,
107-\|\omega_k\|_{L^1},
108-\qquad |j-k|\le C,
--
149-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
150-\right|
151-\le
152:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
153-\]
154-
155-### 3. Shell-product Hardy gain
--
157-\[
158-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
159-\le
160:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
161-\]
162-
163-### 4. Deviatoric coercivity / absorption
--
168-\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
169-\right|
170-\le
171:C\,2^{-j}2^{-k}\,
172-\|\nabla S_k\|_{L^\infty}\,
173-\|\omega_k\|_{L^1},
174-\]
--
189-\[
190-|\mathsf R_{j,k}|
191-\le
192:C\,2^{-j}2^{-k}\,
193-\|\nabla S_k\|_{L^\infty}\,
194-\|\omega_k\|_{L^1}.
195-\]
--
216-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
217-\right|
218-\le
219:C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
220-\]
221-
222-```
--
233-\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
234-\right|
235-\le
236:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
237-\]
238-
239-Together with the zeroth-moment identity
206-```text
207-## Verified Statement
208-
209:Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
210-\[
211-\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
212-\]
--
216-\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
217-\right|
218-\le
219:C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
220-\]
221-
222-```
--
254-L39: ## Exact skew-adjoint reduction frontier
255-L45: ## Symmetric commutator pairing frontier
256-L52: ## Truthful frontier
257:L54: - continuum DDYO high-high absorbability: OPEN; conditional on RA1n
258-L55: - continuum J2B exact residual closure: open
259-L56: - full continuum solve / global regularity closure: open
260-```
```

### Lead 3

`tests/test_ddyo_hybrid_proxy.py`

#### Head

```text
import math
import numpy as np


def centered_offsets(n):
    idx = np.arange(n)
    return np.where(idx <= n // 2, idx, idx - n)


def make_even_gaussian_kernel(n, sigma_pts):
    m = centered_offsets(n).astype(float)
    K = np.exp(-(m**2) / (2.0 * sigma_pts**2))
    K /= np.sum(K)
    return K


def deriv(f, h):
    return (np.roll(f, -1) - np.roll(f, 1)) / (2.0 * h)


def scalar_hybrid_proxy_l1s(n=384, k=4, sigma_pts=2.0, phase=0.4, wphase=-0.3):
    x = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    h = float(x[1] - x[0])

    s = np.sin(k * x + phase)
    w = np.cos(k * x + wphase)

    sp = deriv(s, h)
    wp = deriv(w, h)

    K = make_even_gaussian_kernel(n, sigma_pts)
    m = centered_offsets(n).astype(float)
    y = np.arange(n)

    raw = np.zeros(n, dtype=float)
    first = np.zeros(n, dtype=float)

    for xi in range(n):
        off = (xi - y) % n
        dx = m[off] * h
        raw[xi] = np.sum(K[off] * (s[xi] - s[y]) * wp[y])
        first[xi] = np.sum(K[off] * (dx * sp[y]) * wp[y])

    raw *= h
    first *= h
    rem = raw - first

    l1_raw = np.sum(np.abs(raw)) * h
    l1_rem = np.sum(np.abs(rem)) * h
    return l1_raw, l1_rem


def test_hybrid_proxy_even_kernel_has_zero_signed_first_moment():
    n = 513
    K = make_even_gaussian_kernel(n, sigma_pts=3.0)
    m = centered_offsets(n).astype(float)
    signed_first_moment = float(np.sum(K * m))
    assert abs(signed_first_moment) < 1e-12


def test_hybrid_proxy_first_order_subtraction_reduces_commutator_l1():
    ratios = []
    for k in [2, 4, 8]:
        l1_raw, l1_rem = scalar_hybrid_proxy_l1s(n=384, k=k, sigma_pts=2.0)
        assert l1_raw > 1e-8
        assert l1_rem < 0.5 * l1_raw
        ratios.append(l1_rem / l1_raw)

    assert max(ratios) < 0.5
```

#### `G_j` matches

```text
NO_G_J_MATCHES
```

#### `Gamma` / kernel matches

```text
7-    return np.where(idx <= n // 2, idx, idx - n)
8-
9-
10:def make_even_gaussian_kernel(n, sigma_pts):
11-    m = centered_offsets(n).astype(float)
12-    K = np.exp(-(m**2) / (2.0 * sigma_pts**2))
13-    K /= np.sum(K)
--
28-    sp = deriv(s, h)
29-    wp = deriv(w, h)
30-
31:    K = make_even_gaussian_kernel(n, sigma_pts)
32-    m = centered_offsets(n).astype(float)
33-    y = np.arange(n)
34-
--
50-    return l1_raw, l1_rem
51-
52-
53:def test_hybrid_proxy_even_kernel_has_zero_signed_first_moment():
54-    n = 513
55:    K = make_even_gaussian_kernel(n, sigma_pts=3.0)
56-    m = centered_offsets(n).astype(float)
57-    signed_first_moment = float(np.sum(K * m))
58-    assert abs(signed_first_moment) < 1e-12
```

#### dyadic / RA1n matches

```text
NO_DYADIC_RA1N_MATCHES
```

### Lead 4

`modules/rh/experiments/akcl_normalized_scan.py`

#### Head

```text
import numpy as np


def weight(x):
    return np.exp(-x)


def kernel(x, y):
    return (x - y) ** 2


def energy(xs):
    E = 0.0
    for x in xs:
        for y in xs:
            E += kernel(x, y) * weight(x) * weight(y)
    return E


def D(xs):
    vals = []
    for x in xs:
        s = 0.0
        for y in xs:
            s += kernel(x, y) * weight(y)
        vals.append(s)
    return max(vals)


def f_sample(xs):
    return xs - np.mean(xs)


for L in [2, 3, 4, 5]:
    xs = np.linspace(0.5, L, 20)
    f = f_sample(xs)
    E = energy(xs)
    norm = np.sum(f**2 * weight(xs))
    d = D(xs)
    print("L =", L, "E_norm/norm =", (E / d) / norm)
```

#### `G_j` matches

```text
NO_G_J_MATCHES
```

#### `Gamma` / kernel matches

```text
5-    return np.exp(-x)
6-
7-
8:def kernel(x, y):
9-    return (x - y) ** 2
10-
11-
--
13-    E = 0.0
14-    for x in xs:
15-        for y in xs:
16:            E += kernel(x, y) * weight(x) * weight(y)
17-    return E
18-
19-
--
22-    for x in xs:
23-        s = 0.0
24-        for y in xs:
25:            s += kernel(x, y) * weight(y)
26-        vals.append(s)
27-    return max(vals)
28-
```

#### dyadic / RA1n matches

```text
NO_DYADIC_RA1N_MATCHES
```

### Lead 5

`docs/math/BRANCH_B_CLOSURE_CHECKLIST.md`

#### Head

```text
# Branch B closure checklist

## Machine status
- `derivative_commutator_bound`: **MISSING**
- `stress_transport_potential`: **MISSING**
- `s2_defect_budget`: **MISSING**
- `f2_flux_budget`: **MISSING**
- `final_branch_b_theorem`: **FOUND**
- `a2_term`: **MISSING**
- `t_term`: **MISSING**
- `b2_term`: **MISSING**

## Weakest sufficient closure target
```tex
\sum_{|j-k|\le C_0}2^{2sj}\|N_{j,k}\|_{L^1}
+
\left|
\sum_{|j-k|\le C_0}2^{2sj}\int_{\mathbb R^3}\nabla \mathbf S(u)\mathbin{\vdots}M_{j,k}\,dx
\right|
\le \frac{\nu}{8}\Sigma_{\mathrm{DDYO}} + C\Phi_{\mathrm{DDYO}}^2.
```

## Split targets
```tex
\sum_{|j-k|\le C_0}2^{2sj}\|N_{j,k}\|_{L^1}
\le \frac{\nu}{16}\Sigma_{\mathrm{DDYO}} + C\Phi_{\mathrm{DDYO}}^2,

\left|
\sum_{|j-k|\le C_0}2^{2sj}\int_{\mathbb R^3}\nabla \mathbf S(u)\mathbin{\vdots}M_{j,k}\,dx
\right|
\le \frac{\nu}{16}\Sigma_{\mathrm{DDYO}} + C\Phi_{\mathrm{DDYO}}^2.
```

## Proof shell
1. Frequency-localized Bernstein upgrade for `Q_{j,k}`.
2. Hölder + dyadic near-diagonal reduction for `N_{j,k}`.
3. Explicit Young absorption into `\Sigma_{\mathrm{DDYO}}`.
4. Cauchy-Schwarz + `\ell^2(L^2)` control for `M_{j,k}`.
5. Final `\nu/16` ledger arithmetic: `A2 + S2 + T + B2 <= \nu/4`.

## Focused repository evidence
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:1:# DDYO RA1n Status — 2026-04-10`
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:13:- docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md`
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:14:- docs/math/DDYO_RA1N_CONDITIONAL.md`
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:15:- docs/math/DDYO_SOLVE_REQUIREMENTS.md`
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:16:- docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md`
- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:34:Claim 5, high-high absorbability, and final DDYO continuum closure follow.`
- `docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:1:# DDYO Closure Status — 2026-04-10`
- `docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:13:- docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md`
- `docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:14:- docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md`
- `docs/status/DDYO_CHECKPOINT_a641031.md:1:# DDYO Checkpoint — a641031`
- `docs/status/DDYO_CHECKPOINT_a641031.md:13:- docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md`
- `docs/status/DDYO_CHECKPOINT_a641031.md:14:- docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md`
- `docs/status/DDYO_CHECKPOINT_a641031.md:15:- docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md`
- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:4:- DDYO wall sampled layer: 31/31 tests passing.`
- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:5:- Verified sampled DDYO components:`
- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:26:## DDYO commutator frontier`
- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:32:## DDYO commutator absorbability frontier`
- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:54:- continuum DDYO high-high absorbability: OPEN; conditional on RA1n`
- `docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:1:# DDYO Post-Symmetrized First-Order Leakage`
- `docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:19:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr)_{j,k}.`
- `docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md:1:# DDYO Remainder Routing Lemma`
- `docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md:10:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).`
- `docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md:25:\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u],`
- `docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:1:# DDYO Mollified Symmetric Commutator Bound`
- `docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:12:\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
- `docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:14:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),`
- `docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:43:A Coifman--Meyer / Constantin--E--Titi type commutator estimate at the exact DDYO critical weights.`
- `docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md:48:this closes continuum DDYO high-high absorbability.`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:1:# DDYO critical envelope`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:6:R_{\mathrm{DDYO}}[u]`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:37:R_{\mathrm{DDYO}}[u_\mu]=R_{\mathrm{DDYO}}[u].`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:44:R_{\mathrm{DDYO}}^{\mathrm{test}}`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:59:\Sigma_{\mathrm{DDYO}}[u]`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:63:\Sigma_{\mathrm{DDYO}}[u]`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:65:\eta(\mathcal D[u]+\lambda \mathcal C_{\mathrm{DDYO}}[u])`
- `docs/math/DDYO_CRITICAL_ENVELOPE.md:67:C(\Phi[u]+\lambda R_{\mathrm{DDYO}}[u]),`
- `docs/math/DDYO_PAIRED_PARACOMMUTATOR_H1_BMO.md:1:# DDYO Paired Paracommutator H1-BMO Candidate`
- `docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:1:# DDYO Hybrid Claim 5 Route`
- `docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:13:\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u].`
- `docs/math/DDYO_HYBRID_CLAIM5_ROUTE.md:64:without claiming the continuum DDYO lemma is proved.`
- `docs/math/VARIANT_FRAMEWORK_STATUS.md:83:## DDYO`
- `docs/math/VARIANT_FRAMEWORK_STATUS.md:87:R_{\mathrm{DDYO}}[u]`
- `docs/math/VARIANT_FRAMEWORK_STATUS.md:96:R_{\mathrm{DDYO}}^{\mathrm{test}}`
- `docs/math/VARIANT_FRAMEWORK_STATUS.md:111:R_{\mathrm{DDYO}}[u]=\|u\|_{\dot B^{-1}_{\infty,\infty}}`
- `docs/math/VARIANT_FRAMEWORK_STATUS.md:121:- DDYO sampled dyadic-envelope layer`
- `docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:1:# DDYO Deviatoric Coercivity Frontier`
- `docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md:28:C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.`
- `docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:1:# DDYO Paired Decomposition Lemma`
- `docs/math/DDYO_PAIRED_DECOMPOSITION_LEMMA.md:68:This lemma implies the pairing-level second-gain estimate and closes the DDYO continuum high-high absorbability step.`
- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:1:# DDYO Open Problem: Shell-Product Moment Control`
- `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md:20:Claim 5, and final DDYO continuum closure.`
- `docs/math/DDYO_CLAIM5_TARGET.md:1:# DDYO Claim 5 Target`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:1:# DDYO Symmetric Commutator Pairing Frontier`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:10:\text{Verified sampled DDYO/J2B chain now includes:}`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:13:\text{DDYO wall},\quad`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:15:\text{DDYO commutator frontier},\quad`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:16:\text{DDYO commutator-absorbability proxy},\quad`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:34:\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:36:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:48:\text{hence continuum DDYO high-high absorbability remains open;}`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:76:\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:78:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).`
- `docs/math/DDYO_SYMMETRIC_COMMUTATOR_PAIRING_FRONTIER.md:86:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).`
- `docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md:1:# DDYO Mollified Skew Cancellation`
- `docs/math/DDYO_MOLLIFIED_SKEW_CANCELLATION.md:51:This removes the skew part exactly, leaving only the symmetric commutator term for continuum DDYO absorbability.`
- `docs/math/DDYO_COUNTEREXAMPLE_ZERO_SHELL_MEAN_NOT_SUFFICIENT.md:1:# DDYO Counterexample: zero shell mean is not sufficient for cancellation`
- `docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:1:# DDYO Critical Commutator Lemma`
- `docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:22:\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u].`
- `docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:35:\sum_j \alpha_j \lesssim \varepsilon\,\lambda^{-1}\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
- `docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:37:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).`
- `docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:58:\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
- `docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md:60:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),`
- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:1:# DDYO Claim 5 Final Dichotomy`
- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:14:### Branch B: lower-order routing`
- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:18:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr)_{j,k}.`
- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:35:This is the minimal remaining object for hybrid DDYO Claim 5 after first-order post-symmetrization.`
- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:1:# DDYO Dyadic Gain Extraction`
- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:11:extract the exact shellwise gain needed to offset the DDYO weight \(2^{2j}\).`
- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:25:\varepsilon\,\lambda^{-1}\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:27:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),`

## Missing machine checks
- `derivative_commutator_bound`
- `stress_transport_potential`
- `s2_defect_budget`
- `f2_flux_budget`
- `a2_term`
- `t_term`
- `b2_term`
```

#### `G_j` matches

```text
NO_G_J_MATCHES
```

#### `Gamma` / kernel matches

```text
NO_GAMMA_KERNEL_MATCHES
```

#### dyadic / RA1n matches

```text
39-5. Final `\nu/16` ledger arithmetic: `A2 + S2 + T + B2 <= \nu/4`.
40-
41-## Focused repository evidence
42:- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:1:# DDYO RA1n Status — 2026-04-10`
43-- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:13:- docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md`
44-- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:14:- docs/math/DDYO_RA1N_CONDITIONAL.md`
45-- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:15:- docs/math/DDYO_SOLVE_REQUIREMENTS.md`
--
56-- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:5:- Verified sampled DDYO components:`
57-- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:26:## DDYO commutator frontier`
58-- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:32:## DDYO commutator absorbability frontier`
59:- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:54:- continuum DDYO high-high absorbability: OPEN; conditional on RA1n`
60-- `docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:1:# DDYO Post-Symmetrized First-Order Leakage`
61-- `docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:19:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr)_{j,k}.`
62-- `docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md:1:# DDYO Remainder Routing Lemma`
```

