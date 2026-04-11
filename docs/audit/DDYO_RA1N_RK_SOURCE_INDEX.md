# DDYO RA1n r_k Source Index

## `STATUS.md`
- L9: `- reduction framework`
- L23: `- framework: active`

## `README.md`
- L2: `Current repository work may be complete at the artifact, test, script, dashboard, and reproducibility-infrastructure level within the declared experimental scope.`
- L26: `Clay Problem Lab is a unified experimental framework for computational exploration of the Clay Millennium Problems.`
- L37: `Framework components:`
- L55: `- `docs/REPLAY_INTEGRITY_NOTE_2026_04.md` — conditional note specifying the weakest replay-audit extension compatible with the repository's experimental-framework scope.`
- L60: `- `docs/CROSS_MODULE_COMPARABILITY_NOTE_2026_04.md` — conditional note specifying the weakest cross-module normalization audit compatible with the repository's unified-framework scope.`
- L65: `- `docs/CURRENT_WORK_COMPLETION_NOTE_2026_04.md` — conditional note updating repository scope text to reflect completed current work without strengthening scientific claims.`

## `artifacts/max_fight/compileall.log`
- L204: `Listing './.github/workflows'...`
- L226: `Listing './framework'...`

## `artifacts/max_fight/retry_compileall.log`
- L169: `Listing './.github/workflows'...`
- L191: `Listing './framework'...`

## `artifacts/audit/ddyo_completion_truth_report.md`
- L40: `## Required markers`
- L44: `### theorem-level RA1n proof marker`
- L47: `## Forbidden markers`
- L49: `### open frontier markers in DDYO status layer`
- L70: `### simultaneous open and complete markers in DDYO frontier scope`

## `artifacts/audit/ddyo_open_truth_spec.json`
- L28: `      "label": "explicit theorem missing marker",`
- L35: `      "label": "open frontier markers present",`
- L52: `      "label": "false theorem-complete marker",`
- L61: `      "label": "simultaneous incomplete and complete markers in DDYO frontier scope",`

## `artifacts/audit/run_completion_truth_test_smoke.log`
- L41: `## Required markers`
- L45: `### theorem-level RA1n proof marker`
- L48: `## Forbidden markers`
- L50: `### open frontier markers in DDYO status layer`
- L75: `### simultaneous open and complete markers in DDYO frontier scope`

## `artifacts/audit/run_ddyo_source_truth_test.py`
- L26: `    ("explicit theorem missing marker", [`
- L30: `    ("open frontier markers present", [`
- L40: `    ("false theorem-complete marker", re.compile(r"Theorem-level proof complete")),`
- L75: `sections.append("\n## Required markers\n")`
- L90: `sections.append("\n## Forbidden markers\n")`
- L107: `        mixed.append((p.as_posix(), 0, "contains both open and closed state markers"))`
- L109: `sections.append("\n### simultaneous incomplete and complete markers in canonical source scope\n")`

## `artifacts/audit/generate_ddyo_terminal_frontier_core.py`
- L7: `    r"### open frontier markers present\nPASS\n(?P<body>(?:- `.*\n)+)",`
- L12: `markers = [line.strip() for line in body.splitlines() if line.strip().startswith("- `")]`
- L30: `for line in markers:`
- L45: `text += "## Priority terminal markers\n\n"`
- L47: `text += "\n## Residual open markers\n\n"`
- L49: `text += f"\n## Cardinalities\n\n- priority_markers: {len(priority)}\n- residual_markers: {len(other)}\n- total_markers: {len(priority) + len(other)}\n"`

## `artifacts/audit/ddyo_open_truth_report.md`
- L63: `## Required markers`
- L69: `### explicit theorem missing marker`
- L73: `### open frontier markers present`
- L96: `## Forbidden markers`
- L100: `### false theorem-complete marker`
- L105: `### simultaneous incomplete and complete markers in DDYO frontier scope`

## `artifacts/audit/ddyo_completion_truth_spec.json`
- L28: `      "label": "theorem-level RA1n proof marker",`
- L37: `      "label": "open frontier markers in DDYO status layer",`
- L57: `      "label": "simultaneous open and complete markers in DDYO frontier scope",`

## `artifacts/audit/ddyo_completion_truth_after_marker_sync.log`
- L40: `## Required markers`
- L44: `### theorem-level RA1n proof marker`
- L47: `## Forbidden markers`
- L49: `### open frontier markers in DDYO status layer`
- L70: `### simultaneous open and complete markers in DDYO frontier scope`

## `artifacts/audit/ddyo_completion_truth_post_readme.log`
- L40: `## Required markers`
- L44: `### theorem-level RA1n proof marker`
- L47: `## Forbidden markers`
- L49: `### open frontier markers in DDYO status layer`
- L70: `### simultaneous open and complete markers in DDYO frontier scope`

## `artifacts/audit/COMPLETION_TRUTH_TEST_README.md`
- L13: `  means at least one completion requirement is missing or at least one open-frontier marker remains.`
- L26: `required completion markers are present;`
- L27: `forbidden open-frontier markers are absent;`

## `artifacts/audit/ddyo_completion_truth_stdout.log`
- L41: `## Required markers`
- L45: `### theorem-level RA1n proof marker`
- L48: `## Forbidden markers`
- L50: `### open frontier markers in DDYO status layer`
- L69: `### simultaneous open and complete markers in DDYO frontier scope`

## `artifacts/audit/completion_truth_test.py`
- L111: `    report += section("Required markers")`
- L125: `    report += section("Forbidden markers")`

## `artifacts/audit/ddyo_source_truth_spec.json`
- L28: `      "label": "explicit theorem missing marker",`
- L35: `      "label": "open frontier markers present",`
- L52: `      "label": "false theorem-complete marker",`
- L61: `      "label": "simultaneous incomplete and complete markers in DDYO frontier scope",`

## `artifacts/audit/generate_ddyo_canonical_terminal_obstruction.py`
- L6: `marker_re = re.compile(r"- `([^`]+:\d+)`: (.+)")`
- L7: `markers = marker_re.findall(report)`
- L23: `for loc, text in markers:`
- L37: `s += "## Priority canonical markers\n\n"`
- L39: `s += "\n## Residual canonical markers\n\n"`

## `artifacts/audit/ddyo_source_frontier_scan.py`
- L45: `parts.append("\n## Source-only frontier markers\n")`
- L53: `parts.append(f"\n## Cardinality\n\n- total_markers: {len(hits)}\n")`

## `artifacts/audit/completion_truth_spec.template.json`
- L25: `      "label": "theorem-level proof marker",`
- L34: `      "label": "open frontier markers",`
- L52: `      "label": "simultaneous open and complete markers",`

## `artifacts/audit/ddyo_canonical_source_truth_report.md`
- L19: `## Required markers`
- L26: `### explicit theorem missing marker`
- L35: `### open frontier markers present`
- L51: `## Forbidden markers`
- L57: `### false theorem-complete marker`
- L63: `### simultaneous incomplete and complete markers in canonical source scope`

## `artifacts/audit/ddyo_source_truth_report.md`
- L63: `## Required markers`
- L69: `### explicit theorem missing marker`
- L73: `### open frontier markers present`
- L96: `## Forbidden markers`
- L100: `### false theorem-complete marker`
- L105: `### simultaneous incomplete and complete markers in DDYO frontier scope`

## `artifacts/branch_b/branch_b_relevant_hits.log`
- L240: `./.git/logs/HEAD:10:53824dc9a3a6326e73ea2be5e000159702fdd4b0 c8a83591b951d90e3949a23244cc0eee174dfb32 Inacio F. Vasquez <inaciovasquez2020@gmail.com> 1775858537 -0300	commit: Add honest framework status for DREM NAK J2B DDYO`
- L282: `./.git/logs/refs/heads/main:10:53824dc9a3a6326e73ea2be5e000159702fdd4b0 c8a83591b951d90e3949a23244cc0eee174dfb32 Inacio F. Vasquez <inaciovasquez2020@gmail.com> 1775858537 -0300	commit: Add honest framework status for DREM NAK J2B DDYO`

## `tools/max_fight.py`
- L45: `    "benchmark",`

## `.pytest_cache/v/cache/nodeids`
- L13: `  "tests/test_ddyo_commutator_frontier.py::test_ddyo_strain_commutator_kato_ponce_proxy_bound",`

## `framework/run_registry.py`
- L4: `with open("framework/problem_registry.json") as f:`

## `tests/test_ddyo_commutator_frontier.py`
- L351: `def test_ddyo_strain_commutator_kato_ponce_proxy_bound():`

## `docs/SUMMARY_TRACEABILITY_NOTE_2026_04.md`
- L43: `It preserves the repository's experimental-framework scope.`

## `docs/REPLAY_INTEGRITY_NOTE_2026_04.md`
- L7: `This repository is a unified experimental framework for reproducible computational exploration of the Clay Millennium Problems.`
- L11: `3. dashboard and framework infrastructure;`
- L58: `It preserves the repository's experimental-framework scope.`

## `docs/MODULE_ADAPTER_COMPLETENESS_NOTE_2026_04.md`
- L54: `It preserves the repository's experimental-framework scope.`

## `docs/framework_overview.md`
- L1: `# Clay Problem Lab Framework`
- L5: `framework/`

## `docs/PIPELINE_SCOPE_NOTE_2026_04.md`
- L38: `It preserves the repository's experimental-framework scope.`

## `docs/CURRENT_WORK_COMPLETION_NOTE_2026_04.md`
- L1: `# Current Work Completion Note (2026-04)`
- L7: `This repository is an experimental framework.`
- L8: `It may record completed implementation work, completed tests, completed scripts, completed dashboards, and completed reproducibility infrastructure.`
- L20: `be the set of completed repository work items presently materialized as committed artifacts, tests, scripts, dashboards, or pinned infrastructure states.`
- L22: `A work item`
- L42: `4. README status text inconsistent with the current committed work surface.`
- L46: `It updates repository scope text to reflect completed current work without strengthening scientific claims.`

## `docs/CROSS_MODULE_COMPARABILITY_NOTE_2026_04.md`
- L7: `This repository unifies multiple Clay-problem modules under a common framework.`
- L38: `It preserves the repository's unified-framework scope.`

## `docs/ENVIRONMENT_PIN_INTEGRITY_NOTE_2026_04.md`
- L42: `It preserves the repository's experimental-framework scope.`

## `docs/status/DDYO_CANONICAL_TERMINAL_OBSTRUCTION.md`
- L11: `## Priority canonical markers`
- L25: `## Residual canonical markers`

## `docs/status/DDYO_SOURCE_FRONTIER.md`
- L14: `## Source-only frontier markers`
- L36: `- total_markers: 14`

## `docs/status/COMPLETION_TRUTH_TEST_STATUS.md`
- L12: `## Open frontier markers still present`

## `docs/status/DDYO_FRONTIER_REGISTRY.md`
- L9: `## Canonical open-frontier markers`

## `docs/status/DDYO_TERMINAL_FRONTIER_CORE.md`
- L11: `## Priority terminal markers`
- L28: `## Residual open markers`
- L39: `- priority_markers: 14`
- L40: `- residual_markers: 6`
- L41: `- total_markers: 20`

## `docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md`
- L258: `./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`

## `docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md`
- L9: `denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`

## `docs/math/DDYO_REMAINDER_ROUTING_LEMMA.md`
- L5: `Let \(\mathsf R^{\mathrm{lo}}_{j,k}\) denote all lower-order paired commutator remainders.`

## `docs/math/DDYO_GJ_CONTEXT_EXTRACT.md`
- L933: `./docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md-258-./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`
- L1449: `./docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md-258-./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`
- L1799: `./docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md:258:./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`
- L1885: `./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`
- L1917: `./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-38-of the paired commutator remainder satisfies`
- L3983: `./docs/math/DDYO_GJ_STRUCTURAL_CANDIDATES.md-258-./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`
- L4016: `./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md:12:Combined with shell localization, this provides the first effective dyadic gain in the paired commutator remainder analysis.`

## `docs/math/DDYO_MASSIVE_REDUCTION.md`
- L23: `3. consistency of open-frontier audit markers.`

## `docs/math/VARIANT_FRAMEWORK_STATUS.md`
- L1: `# Variant framework status`

## `docs/math/DDYO_RA1N_EXACT_MISSING_LEMMA.md`
- L10: `\partial_\xi^\alpha r_k(\xi)`
- L14: `where \(r_k\) is the exact DDYO/RA1n remainder symbol defined in the repository.`
- L17: `\text{This estimate must be derived directly from the exact repository formula for }r_k,`
- L21: `r_k=\widehat G_k-P_k\widehat G_k`

## `docs/math/DDYO_GJ_CONTEXT_EXTRACT_CLEAN.md`
- L1178: `./docs/math/DDYO_POST_SYMMETRIZED_FIRST_ORDER_LEAKAGE.md:9:denote the first-order Taylor contribution to the paired commutator remainder after kernel symmetrization in the hybrid route.`
- L1340: `./docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md-38-of the paired commutator remainder satisfies`
- L2640: `./docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md:12:Combined with shell localization, this provides the first effective dyadic gain in the paired commutator remainder analysis.`

## `docs/math/DDYO_RA1N_SHELL_PRODUCT_KERNEL_ESTIMATE_CONDITIONAL.md`
- L15: `|\partial_\xi^\alpha r_k(\xi)|`
- L25: `m_{j,k}(\xi):=\varphi(2^{-j}\xi)\varphi(2^{-k}\xi)r_k(\xi),`
- L40: `=\varphi(2^{k-j}\eta)\varphi(\eta)\,r_k(2^k\eta).`
- L51: `2^{k|\delta|}\bigl(\partial^\delta r_k\bigr)(2^k\eta).`
- L61: `2^{k|\delta|}\left|(\partial^\delta r_k)(2^k\eta)\right|`
- L115: `This proves the shell-product kernel estimate only under the stated symbol-derivative hypothesis on \(r_k\).`

## `docs/math/DDYO_RA1N_SHELL_PRODUCT_MOMENT_TARGET.md`
- L10: `\mathcal F^{-1}\!\left[\varphi(2^{-j}\xi)\varphi(2^{-k}\xi)r_k(\xi)\right](x)`

## `docs/math/DDYO_CLAIM5_POST_COUNTEREXAMPLE_BRANCH.md`
- L47: `It is sufficient to prove that the first-order Taylor part of the paired remainder has zero shell average, so that the commutator remainder behaves as a dipole and gains the second factor`

## `docs/math/DDYO_GENUINE_DIPOLE_CANCELLATION_ROUTE.md`
- L38: `of the paired commutator remainder satisfies`

## `docs/math/DDYO_KERNEL_FIRST_MOMENT_LEMMA.md`
- L12: `Combined with shell localization, this provides the first effective dyadic gain in the paired commutator remainder analysis.`

## `docs/public/START_HERE.md`
- L4: `Experimental framework for computational exploration, artifact generation, dashboards, and reproducible problem-lab workflows.`

## `docs/public/PROOF_STATUS.md`
- L6: `| Status | Experimental and artifact-level framework. |`
- L7: `| Scope | Experimental framework for computational exploration, artifact generation, dashboards, and reproducible problem-lab workflows. |`

## `cli/clay.py`
- L6: `REGISTRY = Path("framework/problem_registry.json")`
