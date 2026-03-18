# Mellin Bernstein Inequality

## Conditional Statement

Assume
F(t)=M_f\!\left(\tfrac12+it\right)

and
\operatorname{supp} F \subset [-B,B].

## Plancherel Form

Under Mellin Plancherel:
\[
\|x\partial_x f\|_{L^2(w)}
\sim
\|\, t\,F(t)\|_{L^2(\mathbb R)}.
\]

## Bernstein Bound

Since
|t| \le B
on \operatorname{supp} F,
\[
\|\, t\,F(t)\|_{L^2}
\le
B \|F\|_{L^2}.
\]

Hence
\[
\|x\partial_x f\|_{L^2(w)}
\le
C_w B \|f\|_{L^2(w)}.
\]

## Iterated Form

For every n \ge 1,
\[
\|(x\partial_x)^n f\|_{L^2(w)}
\le
C_w B^n \|f\|_{L^2(w)}.
\]

## Role

Derivative control in logarithmic scale
⇒ exponential type control in Mellin domain
⇒ upper-line bound candidate.
