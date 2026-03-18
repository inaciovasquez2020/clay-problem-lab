# Core Lower Bound

## Conditional Input

Assume
f \in \mathcal A_B,
\qquad
\|f\|_{L^2(w)} = 1.

Assume also
\int_{\mathrm{Core}(L)} |f(x)|^2 w(x)\,dx = 0.

## Consequence

Then
\int_{\mathrm{Tail}(L)} |f(x)|^2 w(x)\,dx = 1.

But tail domination gives
1
\le
\varepsilon_B(L)\int_{\mathrm{Core}(L)} |f(x)|^2 w(x)\,dx
=
0,

contradiction.

## Result

For every normalized admissible f,
\int_{\mathrm{Core}(L)} |f(x)|^2 w(x)\,dx > 0.

## Required Upgrade

Prove quantitative form:

\int_{\mathrm{Core}(L)} |f(x)|^2 w(x)\,dx \ge c(B) > 0

uniformly over normalized admissible f.
