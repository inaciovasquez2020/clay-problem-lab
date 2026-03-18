# Exact Mellin Paley–Wiener Transfer

## Input

Let
g(u)=e^{u/2}f(e^u)

and assume
\[
\widehat{g}(\xi)=0
\quad\text{for }|\xi|>B.
\]

## Fourier Paley–Wiener

Then g extends to an entire function on \(\mathbb C\) and satisfies
\[
|g(u+iv)| \le C_N (1+|u+iv|)^{-N} e^{B|v|}
\]
for every \(N\ge 0\).

## Pullback

Since
\[
f(e^u)=e^{-u/2}g(u),
\]
we obtain
\[
|f(e^{u+iv})|
\le
C_N e^{-u/2}(1+|u+iv|)^{-N} e^{B|v|}.
\]

## Mellin Form

Therefore
\[
M_f\!\left(\tfrac12+it\right)\ \text{bandlimited}
\quad\Longrightarrow\quad
g \text{ entire of exponential type } B.
\]

## Consequence

For every fixed \(\eta>0\),
\[
|f(e^u)| \le C_\eta e^{-(1/2+\eta)u}
\]
after contour shift.

## Role

Bandlimit
\(\Longrightarrow\)
entire extension
\(\Longrightarrow\)
Hardy-strip control
\(\Longrightarrow\)
tail decay
\(\Longrightarrow\)
uniform AKCL closure.
