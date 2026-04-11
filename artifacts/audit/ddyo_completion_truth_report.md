# DDYO Completion Truth Test

- UTC: 2026-04-11T23:40:01.159655+00:00
- Spec: `artifacts/audit/ddyo_completion_truth_spec.json`
- Scope files: 97


## Required files

PASS

## Required commands

### `./artifacts/audit/ddyo_status_consistency_2026_04_11.sh`
- rc: 0

```text
DDYO_STATUS_CONSISTENCY: PASS

EXPECTED_OPEN_FRONTIER_MARKERS:
docs/math/DDYO_GJ_CONTEXT_EXTRACT_CLEAN.md:2716:./docs/math/DDYO_RA1N_PROOF.md-6-No theorem-level proof is currently present in this repository.
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:2375:./artifacts/branch_b/branch_b_open_hits.log-24-docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:3870:./artifacts/branch_b/branch_b_open_hits.log-15-docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md:34:- Formally open at the shell-product moment frontier
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:3879:./artifacts/branch_b/branch_b_open_hits.log-24-docs/status/DDYO_RA1N_STATUS_2026_04_10.md:38:- Formally conditional on RA1n
docs/math/DDYO_GJ_CONTEXT_EXTRACT.md:4140:./docs/math/DDYO_RA1N_PROOF.md-6-No theorem-level proof is currently present in this repository.

```
### `python3 -m pytest -q`
- rc: 1

```text
...............................F.F...................................... [100%]
=================================== FAILURES ===================================
___________________ test_single_remaining_theorem_doc_exists ___________________

    def test_single_remaining_theorem_doc_exists():
        p = Path("docs/math/DDYO_RA1N_SINGLE_REMAINING_THEOREM.md")
        assert p.exists(), "missing single remaining theorem doc"
        s = p.read_text()
        assert r"r_k(\xi)=\widehat G_k(\xi)-P_k\widehat G_k(\xi)" in s
        assert "unconditional RA1n closure" in s
>       assert "Open." in s
E       AssertionError: assert 'Open.' in '# DDYO RA1n Single Remaining Theorem\n\n## Canonical statement\n\n\\[\n\\forall \\alpha\\in\\mathbb N^3,\\qquad\n\\su...tarrow\n\\text{unconditional RA1n closure}.\n\\]\n\n## Status\n\nClosed at the annular first-moment remainder stage.\n'

tests/test_ddyo_rk_definition_extracted.py:36: AssertionError
________________ test_quantitative_decay_closure_target_exists _________________

    def test_quantitative_decay_closure_target_exists():
        p = Path("docs/math/DDYO_RA1N_QUANTITATIVE_DECAY_CLOSURE_TARGET.md")
        assert p.exists(), "missing quantitative decay closure target doc"
        s = p.read_text()
        assert r"r_k(\xi)=\widehat G_k(\xi)-P_k\widehat G_k(\xi)" in s
        assert r"2^{-k(2+|\alpha|)}" in s
        assert "unconditional RA1n closure" in s
>       assert "Open." in s
E       AssertionError: assert 'Open.' in '# DDYO RA1n Quantitative Decay Closure Target\n\n## Canonical remainder\n\n\\[\nr_k(\\xi)=\\widehat G_k(\\xi)-P_k\\wi...tarrow\n\\text{unconditional RA1n closure}.\n\\]\n\n## Status\n\nClosed at the annular first-moment remainder stage.\n'

tests/test_ddyo_rk_definition_extracted.py:56: AssertionError
=========================== short test summary info ============================
FAILED tests/test_ddyo_rk_definition_extracted.py::test_single_remaining_theorem_doc_exists
FAILED tests/test_ddyo_rk_definition_extracted.py::test_quantitative_decay_closure_target_exists
2 failed, 70 passed in 25.65s

```

## Required markers

### explicit unconditional completion declaration
FAIL
### theorem-level RA1n proof marker
FAIL

## Forbidden markers

### open frontier markers in DDYO status layer
PASS
### conditional or premature completion claims
PASS

## Mixed-state contradictions

### simultaneous open and complete markers in DDYO frontier scope
PASS

## Verdict

COMPLETION_TRUTH_TEST: FAIL
