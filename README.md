## Status
Current repository work may be complete at the artifact, test, script, dashboard, and reproducibility-infrastructure level within the declared experimental scope.
No theorem-level completion claim is implied.

# Clay Problem Lab


<!-- PUBLIC-SURFACE:BEGIN -->
## Start Here
- [`QUICKSTART.md`](QUICKSTART.md)
- [`docs/public/START_HERE.md`](docs/public/START_HERE.md)

## Proof Status
- [`docs/public/PROOF_STATUS.md`](docs/public/PROOF_STATUS.md)

## Independent Verification
- [`docs/public/INDEPENDENT_VERIFICATION.md`](docs/public/INDEPENDENT_VERIFICATION.md)

## Why It Matters
- [`docs/public/WHY_IT_MATTERS.md`](docs/public/WHY_IT_MATTERS.md)

## Citation
- [`CITATION.cff`](CITATION.cff)
<!-- PUBLIC-SURFACE:END -->

Clay Problem Lab is a unified experimental framework for computational exploration of the Clay Millennium Problems.

Modules included:

- riemann — experiments related to the Riemann Hypothesis
- navier_stokes — numerical experiments for Navier–Stokes dynamics
- yang_mills — spectral gap and lattice experiments for Yang–Mills
- complexity — experiments related to P vs NP and locality barriers
- bsd — exploratory computations for Birch–Swinnerton–Dyer
- hodge — symbolic and numerical tools for Hodge theory

Framework components:

- experiments: executable research experiments
- data: datasets used by experiments
- scripts: automation tools
- tests: experiment verification pipeline
- dashboard: repository status utilities

Run all experiments:

scripts/run_pipeline.sh

Run tests:

scripts/test_pipeline.sh


## Conditional notes
- `docs/REPLAY_INTEGRITY_NOTE_2026_04.md` — conditional note specifying the weakest replay-audit extension compatible with the repository's experimental-framework scope.
- `docs/MODULE_ADAPTER_COMPLETENESS_NOTE_2026_04.md` — conditional note specifying the weakest adapter-coverage audit compatible with the repository's multi-module experimental scope.
- `docs/ENVIRONMENT_PIN_INTEGRITY_NOTE_2026_04.md` — conditional note specifying the weakest environment-hash audit compatible with the repository's reproducibility boundary.
- `docs/SUMMARY_TRACEABILITY_NOTE_2026_04.md` — conditional note specifying the weakest summary-to-artifact traceability audit compatible with the repository's result-reporting scope.
- `docs/PIPELINE_SCOPE_NOTE_2026_04.md` — conditional note specifying the weakest non-overreach audit compatible with the repository's exploration-only boundary.
- `docs/CROSS_MODULE_COMPARABILITY_NOTE_2026_04.md` — conditional note specifying the weakest cross-module normalization audit compatible with the repository's unified-framework scope.
- `docs/TEST_COVERAGE_BOUNDARY_NOTE_2026_04.md` — conditional note specifying the weakest test-boundary audit compatible with the repository's verification-pipeline scope.


## Conditional notes
- `docs/CURRENT_WORK_COMPLETION_NOTE_2026_04.md` — conditional note updating repository scope text to reflect completed current work without strengthening scientific claims.

Project goal:

Create a reproducible research infrastructure for experimentation,
verification, and exploration related to the Clay Millennium Problems.

## RA1n Exact Symbol Status

See `docs/status/DDYO_RA1N_RK_DEFINITION_STATUS.md`.

## Current DDYO / RA1n frontier

- RA1n remains Open.
- Canonical residual: `r_k = \widehat G_k - P_k\widehat G_k`.
- Next missing object: `terminal_high_high_resonance_curvature_gain`.
- Canonical route: `docs/math/TERMINAL_HIGH_HIGH_RESONANCE_GAIN_ROUTE.md`.
