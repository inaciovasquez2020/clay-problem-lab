# Hardy–Mellin Embedding

## Minimal Missing Lemma

Let
w(x)=e^{-x}.

Assume
f \in L^2((0,\infty),w(x)\,dx)

and
M_f\!\left(\tfrac12+it\right)=0
for |t|>B.

The required upgrade is:

there exists a strip
\Sigma_\sigma=\{s\in\mathbb C: |\Re s-\tfrac12|<\sigma\}
and a constant C(B,\sigma) such that
M_f(s)
extends holomorphically to \Sigma_\sigma
and satisfies
\sup_{|\Re s-\tfrac12|<\sigma}
\int_{\mathbb R} |M_f(\Re s+it)|^2\,dt
\le
C(B,\sigma)\|f\|_{L^2(w)}^2.

## Consequence

M_f \in H^2(\Sigma_\sigma)

## Closure Chain

Hardy–Mellin embedding
⇒ contour shift
⇒ explicit tail decay
⇒ uniform tail domination
⇒ AKCL unconditional.
