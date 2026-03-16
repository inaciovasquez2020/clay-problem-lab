# Clay Problem Lab

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

Project goal:

Create a reproducible research infrastructure for experimentation,
verification, and exploration related to the Clay Millennium Problems.
