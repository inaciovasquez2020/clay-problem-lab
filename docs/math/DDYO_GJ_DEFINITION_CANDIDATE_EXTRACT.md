# DDYO G_j Definition Candidate Extract

## Status

Open.

## Candidate definition lines from top nongenerated leads

## `docs/math/BRANCH_B_MISSING_MATH_AND_TEST.md`

### pattern `G_j(`

```text
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
```

### pattern `2^{-j}`

```text
12-\right|
13-\le
14:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
15-\]
16-
--
20-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
21-\le
22:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
23-\]
24-
--
31-\right|
32-\le
33:C\,2^{-j}2^{-k}\,
34-\|\nabla S_k\|_{L^\infty}\,
35-\|\omega_k\|_{L^1}.
--
53-|\mathsf R_{j,k}|
54-\le
55:C\,2^{-j}2^{-k}\,
56-\|\nabla S_k\|_{L^\infty}\,
57-\|\omega_k\|_{L^1},
```

### pattern `RA1n`

```text
79-
80-## Truthful frontier
81:- continuum DDYO high-high absorbability: OPEN; conditional on RA1n
82-- full continuum solve / global regularity closure: open
```

## `docs/math/BRANCH_B_FINAL_FRONTIER.md`

### pattern `G_j(`

```text
14-\[
15-\left|
16:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
17-\right|
18-\le
--
22-Together with
23-\[
24:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
25-\]
26-this implies the shell-product H^1 gain, the deviatoric coercivity estimate,
--
39-\[
40-\left|
41:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
42-\right|
43-\le
--
47-Together with the zeroth-moment identity
48-\[
49:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
50-\]
51-this is sufficient to recover the shell-product \(H^1\) gain and hence
--
140-For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
141-\[
142:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
143-\]
144-
--
147-\[
148-\left|
149:\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
150-\right|
151-\le
--
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
--
231-\[
232-\left|
233:\int x_l\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
234-\right|
235-\le
--
239-Together with the zeroth-moment identity
240-\[
241:\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
242-\]
243-this is sufficient to recover the shell-product H^1 gain and the target deviatoric coercivity bound.
```

### pattern `2^{-j}`

```text
17-\right|
18-\le
19:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
20-\]
21-
--
42-\right|
43-\le
44:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
45-\]
46-
--
56-\right|
57-\le
58:C\,2^{-j}2^{-k}\,
59-\|\nabla S_k\|_{L^\infty}\,
60-\|\omega_k\|_{L^1},
--
78-\right|
79-\le
80:C\,2^{-j}2^{-k}\,
81-\|\nabla S_k\|_{L^\infty}\,
82-\|\omega_k\|_{L^1}.
--
103-|\mathsf R_{j,k}|
104-\le
105:C\,2^{-j}2^{-k}\,
106-\|\nabla S_k\|_{L^\infty}\,
107-\|\omega_k\|_{L^1},
--
150-\right|
151-\le
152:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
153-\]
154-
--
158-\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
159-\le
160:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
161-\]
162-
--
169-\right|
170-\le
171:C\,2^{-j}2^{-k}\,
172-\|\nabla S_k\|_{L^\infty}\,
173-\|\omega_k\|_{L^1},
--
190-|\mathsf R_{j,k}|
191-\le
192:C\,2^{-j}2^{-k}\,
193-\|\nabla S_k\|_{L^\infty}\,
194-\|\omega_k\|_{L^1}.
--
217-\right|
218-\le
219:C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
220-\]
221-
--
234-\right|
235-\le
236:C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
237-\]
238-
```

### pattern `RA1n`

```text
207-## Verified Statement
208-
209:Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
210-\[
211-\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
--
217-\right|
218-\le
219:C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
220-\]
221-
--
255-L45: ## Symmetric commutator pairing frontier
256-L52: ## Truthful frontier
257:L54: - continuum DDYO high-high absorbability: OPEN; conditional on RA1n
258-L55: - continuum J2B exact residual closure: open
259-L56: - full continuum solve / global regularity closure: open
```

## `tests/test_ddyo_hybrid_proxy.py`

### pattern `kernel`

```text
8-
9-
10:def make_even_gaussian_kernel(n, sigma_pts):
11-    m = centered_offsets(n).astype(float)
12-    K = np.exp(-(m**2) / (2.0 * sigma_pts**2))
--
29-    wp = deriv(w, h)
30-
31:    K = make_even_gaussian_kernel(n, sigma_pts)
32-    m = centered_offsets(n).astype(float)
33-    y = np.arange(n)
--
51-
52-
53:def test_hybrid_proxy_even_kernel_has_zero_signed_first_moment():
54-    n = 513
55:    K = make_even_gaussian_kernel(n, sigma_pts=3.0)
56-    m = centered_offsets(n).astype(float)
57-    signed_first_moment = float(np.sum(K * m))
```

## `modules/rh/experiments/akcl_normalized_scan.py`

### pattern `kernel`

```text
6-
7-
8:def kernel(x, y):
9-    return (x - y) ** 2
10-
--
14-    for x in xs:
15-        for y in xs:
16:            E += kernel(x, y) * weight(x) * weight(y)
17-    return E
18-
--
23-        s = 0.0
24-        for y in xs:
25:            s += kernel(x, y) * weight(y)
26-        vals.append(s)
27-    return max(vals)
```

## `docs/math/BRANCH_B_CLOSURE_CHECKLIST.md`

### pattern `2^{2j}`

```text
117-- `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md:35:This is the minimal remaining object for hybrid DDYO Claim 5 after first-order post-symmetrization.`
118-- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:1:# DDYO Dyadic Gain Extraction`
119:- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:11:extract the exact shellwise gain needed to offset the DDYO weight \(2^{2j}\).`
120-- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:25:\varepsilon\,\lambda^{-1}\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)`
121-- `docs/math/DDYO_DYADIC_GAIN_EXTRACTION.md:27:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),`
```

### pattern `RA1n`

```text
40-
41-## Focused repository evidence
42:- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:1:# DDYO RA1n Status — 2026-04-10`
43-- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:13:- docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md`
44-- `docs/status/DDYO_RA1N_STATUS_2026_04_10.md:14:- docs/math/DDYO_RA1N_CONDITIONAL.md`
--
57-- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:26:## DDYO commutator frontier`
58-- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:32:## DDYO commutator absorbability frontier`
59:- `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md:54:- continuum DDYO high-high absorbability: OPEN; conditional on RA1n`
60-- `docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:1:# DDYO Post-Symmetrized First-Order Leakage`
61-- `docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:19:C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr)_{j,k}.`
```

