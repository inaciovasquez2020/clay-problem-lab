# Coarse-Scale Gradient Bound for Block Projection

## Block Projection

Let \(P_L\) denote the conditional expectation onto functions that are constant on each block of side \(L\).

Define

\[
Q_L = I - P_L.
\]

Interpretation:

- \(P_L f\): coarse-scale component.
- \(Q_L f\): fluctuation component.

---

## Coarse Variation Structure

Since \(P_L f\) is constant inside each block, variation of \(P_L f\) occurs only across **block boundaries**.

Thus gradients appear only on links connecting adjacent blocks.

---

## Gradient Estimate

Let \(\ell\) be a link crossing the boundary between blocks \(B_i\) and \(B_j\).

Then

\[
\nabla_\ell (P_L f)
=
P_L f(B_j) - P_L f(B_i).
\]

---

## Discrete Gradient Scaling

Block averages vary over scale \(L\).

Thus

\[
|P_L f(B_j) - P_L f(B_i)|^2
\le
C L^{-2} \|P_L f\|^2 .
\]

---

## Global Bound

Summing over all boundary links yields

\[
\sum_{\ell}
\|\nabla_\ell (P_L f)\|^2
\le
C L^{-2}
\|P_L f\|^2 .
\]

---

## Interpretation

The coarse component behaves like a discrete field with spatial resolution \(L\), producing the \(L^{-2}\) scaling characteristic of diffusive operators.

---

## Role in Mass Gap Reduction

Combined with the fluctuation inequality

\[
\|Q_L f\|^2
\ge
c L^2
\sum_\ell
\|\nabla_\ell(Q_L f)\|^2
\]

this separates the two scales in the RG decomposition.

