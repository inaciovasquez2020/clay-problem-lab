# RA1n Conservation-Transfer Frontier

Status: TERMINAL FRONTIER

Full_RA1n_status: CONDITIONAL, not CLOSED.

## Weighted Affine-Transfer Cancellation Lemma

Let

\[
U_{k,\omega}
=
\{\xi\in\mathbb R^d:\ |\xi|\sim 2^k,\ \angle(\xi,e_\omega)\le C2^{-\sigma k}\}.
\]

Define the exact interaction surface

\[
\Sigma_{k,\omega}(\xi_{\mathrm{out}})
=
\{
(\xi_1,\xi_2):
\xi_1+\xi_2=\xi_{\mathrm{out}},
\ \xi_1\in U_{k,\omega},
\ \xi_2\in U_{k,\omega}
\}.
\]

The exact parametrization is

\[
\Phi_{\xi_{\mathrm{out}}}(\eta)
=
(\xi_{\mathrm{out}}-\eta,\eta).
\]

Equivalently,

\[
\xi_1=\xi_{\mathrm{out}}-\eta,
\qquad
\xi_2=\eta.
\]

Let

\[
d\mu_{k,\omega}^{\xi_{\mathrm{out}}}
=
J_{k,\omega}(\eta)\,d\eta.
\]

For every admissible RA1n packet input

\[
F=\widehat{P_{k,\omega}f},
\]

and every \(|\beta|=1\), the terminal transfer estimate required for full RA1n promotion is

\[
\left|
\int_{\Sigma_{k,\omega}(\xi_{\mathrm{out}})}
(\xi_2-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\xi_2)
F(\xi_2)
\,d\mu_{k,\omega}^{\xi_{\mathrm{out}}}
\right|
\le
C2^{-\delta k}
\|\sigma_{k,\omega}\|_{L^1}
\|P_{k,\omega}f\|_{L^2}.
\]

Using

\[
\xi_2-\xi_{k,\omega}
=
(\xi_{\mathrm{out}}-2\xi_{k,\omega})
-
(\xi_1-\xi_{k,\omega}),
\]

this is equivalent to

\[
\left|
\gamma_{k,\omega}^{\beta}I_0(F)-I_1^\beta(F)
\right|
\le
C2^{-\delta k}
\|\sigma_{k,\omega}\|_{L^1}
\|P_{k,\omega}f\|_{L^2},
\]

where

\[
\gamma_{k,\omega}^{\beta}
=
(\xi_{\mathrm{out}}-2\xi_{k,\omega})^\beta,
\]

\[
I_0(F)
=
\int
\sigma_{k,\omega}(\xi_2)
F(\xi_2)
\,d\mu_{k,\omega}^{\xi_{\mathrm{out}}},
\]

and

\[
I_1^\beta(F)
=
\int
(\xi_1-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\xi_2)
F(\xi_2)
\,d\mu_{k,\omega}^{\xi_{\mathrm{out}}}.
\]

## Counterexample Guard

Weighted FM-1 transfer is not derivable from unweighted FM-1 alone.

Let

\[
g(\eta)
=
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
J_{k,\omega}(\eta).
\]

If

\[
g\not\equiv0,
\]

then the admissible guard input

\[
F=\frac{\overline g}{\|g\|_2}
\]

gives

\[
I_1^\beta(F)=\|g\|_2\ne0.
\]

Thus conservation alone does not prove weighted FM-1 transfer.

## Conditional Promotion Consequence

If the Weighted Affine-Transfer Cancellation Lemma holds, then

\[
m_{k,\omega}
=
A_{k,\omega}(\xi_2,\ldots,\xi_N)r_{k,\omega}(\xi_1)
+
E_{k,\omega},
\]

with

\[
\|\operatorname{Op}(E_{k,\omega})\|_{H^1\times\cdots\to H^1}
\le
C2^{-\delta k}
\|\operatorname{Op}(A_{k,\omega}r_{k,\omega})\|_{H^1\times\cdots\to H^1}.
\]

The corrected cap-localized unary remainder estimate is

\[
\sup_{|\xi|\sim2^k}
|D_k^\alpha r_{k,\omega}(\xi)|
\le
C_\alpha 2^{-4k}2^{\sigma k|\alpha|}.
\]

The cap-summed estimate is

\[
\|T_k\|_{H^1\times H^1\to H^1}
\lesssim
2^{-4k}2^{\sigma dk}
=
2^{k(\sigma d-4)}.
\]

Hence, for

\[
0<\sigma<\frac4d,
\]

\[
\|T_k\|_{H^1\times H^1\to H^1}\to0.
\]

Therefore full RA1n promotion is CONDITIONAL on the Weighted Affine-Transfer Cancellation Lemma.
