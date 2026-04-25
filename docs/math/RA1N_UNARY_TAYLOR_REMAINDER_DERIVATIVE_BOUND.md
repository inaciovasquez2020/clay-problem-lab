# RA1n Unary Taylor-Remainder Derivative Bound

Status: CONDITIONAL.

Canonical unary formula:

\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}.

P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k).

r_k(ξ)=\widehat G_k(ξ)−P_k\widehat G_k(ξ).

Let ξ=2^kη and ξ_k=2^kη_k. Then

\widehat G_k(2^kη)=2^{-4k} φ(η)|η|^{-4}.

Define

g(η):=φ(η)|η|^{-4}.

Then

r_k(2^kη)
=
2^{-4k}\Bigl[g(η)-g(η_k)-∇g(η_k)·(η−η_k)\Bigr].

Therefore, for every multi-index α,

(2^k∇_ξ)^α r_k(2^kη)
=
2^{-4k}∂_η^α
\Bigl[g(η)-g(η_k)-∇g(η_k)·(η−η_k)\Bigr].

Hence on any fixed annulus where φ is smooth and |η| is bounded away from 0,

sup_{|ξ|~2^k}|(2^k∇_ξ)^α r_k(ξ)|
≤ C_α 2^{-4k}
≤ C_α.

Thus the normalized derivative bound holds for the selected unary Taylor-remainder model.

Conditional boundary:

This closes only the selected unary Taylor-remainder RA1n surface. It does not close binary, ternary, transverse high-high, sampled surrogate, or noncanonical residual surfaces.
