# Hardy–Mellin Upgrade

## Minimal Assumption

Assume
M_f(s) ∈ H^2(\Sigma_B),

where
\Sigma_B = \{ s : |\Im s| < B \}.

## Consequence

By Hardy space theory:

1. M_f admits boundary limits.
2. M_f extends holomorphically to strip |\Im s| < B.
3. Growth bound:
   |M_f(\sigma+it)| ≤ C(B)

## Pullback

Using Mellin inversion:

f(x)
=
\frac{1}{2\pi i}
\int_{\Re s = 1/2} M_f(s) x^{-s} ds

Shift contour to
\Re s = 1/2 + \eta.

## Result

|f(x)| ≤ C(B) x^{-(1/2+\eta)}

## Implication

Provides required analytic continuation for:

g(u) = f(e^u)e^{u/2}

⇒ holomorphic strip |\Im u| < B

⇒ contour shift valid

⇒ exponential tail decay

⇒ uniform tail domination

⇒ AKCL unconditional.

## Status

Conditional on Hardy–Mellin admissibility.
