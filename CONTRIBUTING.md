# Contributing to Clay Problem Lab

## Contribution classes

### 1. Documentation improvements

- clarify repository scope
- improve onboarding text
- tighten quickstart commands
- improve public status navigation

### 2. Pipeline and test hardening

- strengthen test scripts
- add regression tests
- improve experiment verification surfaces

### 3. Experimental or semantic changes

These require explicit justification.

- changing status claims
- expanding theorem-level language
- altering experimental scope boundaries

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run tests before commit:

```bash
[ -x scripts/test_pipeline.sh ] && scripts/test_pipeline.sh
python3 -m pytest -q
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- overclaiming theorem-level completion
- changing declared non-claim boundaries without status updates
