# Exact DDYO Symbol to Lambda Transfer

## Status
OPEN

## Dependency
This file is a locked dependency note for the terminal frontier
`terminal_high_high_resonance_curvature_gain`.

## Transfer statement
Assume there exists a retained admissible witness class and a constant `c0 > 0`
such that for every retained witness `(xi, eta, k)` one has
`positive_lower_bound_candidate(xi, eta, k) >= c0`.

Then the search functional satisfies `lambda_search > 0`.

## Repository consequence
If this transfer statement and the Exact Symbol Curvature Lemma are both
instantiated, then the terminal frontier cannot remain in the zero-score state.

## Finish condition
Replace `OPEN` by `COMPLETE` only after the simulator computes the transfer
internally and the frontier artifact records `lambda_search > 0` without any run-script postprocess patching.
